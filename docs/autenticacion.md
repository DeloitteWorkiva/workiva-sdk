# Autenticacion

El SDK utiliza OAuth2 **Client Credentials** para autenticarse con las APIs de Workiva. Todo el manejo de tokens es automatico y transparente.

## Flujo OAuth2 Client Credentials

```
Tu aplicacion                    Workiva IAM
     |                                |
     |  POST /oauth2/token            |
     |  client_id + client_secret     |
     |  X-Version: 2026-01-01         |
     | ─────────────────────────────> |
     |                                |
     |  access_token + expires_in     |
     | <───────────────────────────── |
     |                                |
     |  GET /files                    |
     |  Authorization: Bearer <token> |
     |  X-Version: 2026-01-01         |
     | ─────────────────────────────> |
     |                                |
```

El endpoint de tokens se resuelve automaticamente segun la region:

| Region | Token URL |
|--------|-----------|
| EU (default) | `https://api.eu.wdesk.com/oauth2/token` |
| US | `https://api.app.wdesk.com/oauth2/token` |
| APAC | `https://api.apac.wdesk.com/oauth2/token` |

## Clase `Workiva` -- la unica forma de autenticarse

La clase `Workiva` es el unico punto de entrada del SDK. No existe una clase `SDK`, ni un modelo `Security`, ni ningun otro mecanismo de autenticacion:

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    result = client.files.get_files()
```

Internamente, `Workiva` crea una instancia de `OAuth2ClientCredentials(httpx.Auth)` que se inyecta como autenticador en los clientes httpx. El flujo OAuth2 se maneja de forma nativa por la interfaz `httpx.Auth`, no por hooks personalizados.

### Constructor completo

```python
from workiva import Workiva, Region
from workiva._config import SDKConfig

client = Workiva(
    client_id="tu_client_id",
    client_secret="tu_client_secret",
    region=Region.EU,          # Region.EU | Region.US | Region.APAC
    timeout=30,                # Timeout global en segundos (opcional)
    config=SDKConfig(...),     # Configuracion avanzada (opcional)
    client=httpx.Client(...),  # Cliente sync custom (opcional)
    async_client=httpx.AsyncClient(...),  # Cliente async custom (opcional)
)
```

## Token caching

El SDK cachea los tokens de acceso de forma **global** a nivel de proceso:

- La cache es un `ClassVar` en `OAuth2ClientCredentials` -- compartida entre TODAS las instancias del SDK
- La clave de cache es un hash MD5 de `client_id:client_secret` (no se almacenan credenciales en texto plano)
- Si creas multiples instancias de `Workiva` con las mismas credenciales, reutilizan el mismo token
- Los tokens se refrescan automaticamente 60 segundos antes de expirar

```python
# Ambos clientes comparten el mismo token cacheado
client1 = Workiva(client_id="abc", client_secret="xyz")
client2 = Workiva(client_id="abc", client_secret="xyz")
# Solo se hace UNA solicitud de token al servidor
```

### Como funciona el cache internamente

```
_cache: ClassVar[dict[str, _CachedToken]]

Clave:   MD5("client_id:client_secret")
Valor:   _CachedToken(access_token="...", expires_at=epoch_float)

Flujo:
1. Verificar si existe token en cache
2. Si existe y NO esta expirado (buffer de 60s) -> usar directamente
3. Si no existe o esta expirado -> adquirir lock, fetch nuevo token, guardar en cache
```

## Refresco automatico de tokens

El token se refresca automaticamente en dos escenarios:

### 1. Token proximo a expirar

Antes de cada request, el SDK verifica si el token expira en los proximos 60 segundos. Si es asi, obtiene uno nuevo antes de enviar la solicitud:

```python
def is_expired(self, buffer_s: float = 60.0) -> bool:
    if self.expires_at is None:
        return False
    return time.time() + buffer_s >= self.expires_at
```

### 2. Respuesta 401 (token invalido)

Si una llamada a la API devuelve HTTP 401:

1. El flujo `sync_auth_flow` / `async_auth_flow` de `httpx.Auth` detecta el 401
2. Invalida el token cacheado para esas credenciales
3. Obtiene un token nuevo
4. **Reintenta la solicitud original** automaticamente con el nuevo token

Este mecanismo es nativo de `httpx.Auth` -- no usa hooks como `AfterError` ni interceptores personalizados. Es el protocolo estandar de auth de httpx basado en generadores.

```python
# Flujo simplificado (sync)
def sync_auth_flow(self, request):
    token = self._get_or_refresh_token()
    request.headers["Authorization"] = f"Bearer {token}"
    response = yield request              # Enviar solicitud

    if response.status_code == 401:       # Token invalido?
        self._invalidate()                # Borrar cache
        token = self._get_or_refresh_token()  # Nuevo token
        request.headers["Authorization"] = f"Bearer {token}"
        yield request                     # Reintentar
```

## Thread safety

El sistema de tokens es completamente thread-safe con una estrategia de locks por cliente:

| Componente | Mecanismo | Proposito |
|-----------|-----------|-----------|
| `_global_lock` | `threading.Lock` (ClassVar) | Protege la creacion de locks por cliente |
| `_client_locks` | `dict[str, threading.Lock]` (ClassVar) | Un lock por clave de cache (por par de credenciales) |

```python
# Ejemplo: 3 threads con las mismas credenciales
# Solo 1 thread hace el fetch del token, los otros 2 esperan y reusan
Thread-1: lock.acquire() -> fetch token -> cache -> lock.release()
Thread-2: lock.acquire() -> cache hit! -> lock.release()
Thread-3: lock.acquire() -> cache hit! -> lock.release()
```

No existe un lock global que bloquee todos los clientes. Cada par de credenciales tiene su propio lock, asi que clientes con credenciales diferentes nunca se bloquean entre si.

## Async safety

En contextos asincronos, la obtencion de tokens siempre se ejecuta en un thread separado para no bloquear el event loop:

```python
async def async_auth_flow(self, request):
    # El fetch del token se hace en un thread aparte
    token = await asyncio.to_thread(self._get_or_refresh_token)
    request.headers["Authorization"] = f"Bearer {token}"
    response = yield request

    if response.status_code == 401:
        await asyncio.to_thread(self._invalidate)
        token = await asyncio.to_thread(self._get_or_refresh_token)
        request.headers["Authorization"] = f"Bearer {token}"
        yield request
```

Esto significa que:

- El event loop de asyncio **nunca se bloquea** esperando un token
- Los `threading.Lock` se adquieren dentro del thread, no en el event loop
- Multiples coroutines pueden esperar tokens concurrentemente sin deadlocks

## Header X-Version

El SDK inyecta automaticamente el header `X-Version: 2026-01-01` en cada solicitud a traves de un event hook de httpx. Esto aplica tanto al request de token como a todas las solicitudes de la API. No necesitas configurar nada.

## Errores de autenticacion

Si las credenciales son invalidas o el servidor de tokens no responde:

```python
from workiva import Workiva
from workiva._auth import TokenAcquisitionError

try:
    with Workiva(client_id="invalido", client_secret="invalido") as client:
        client.files.get_files()  # Aqui se intenta obtener el token
except TokenAcquisitionError as e:
    print(f"Error de autenticacion: {e}")
```

`TokenAcquisitionError` se lanza cuando:

- El servidor de tokens responde con un status no-2xx
- El `token_type` no es `"bearer"`
- La respuesta no contiene el campo `access_token`

## Siguiente paso

- [Configuracion](configuracion.md) -- Regiones, timeouts, reintentos, clientes HTTP custom
- [Manejo de errores](manejo-errores.md) -- Jerarquia completa de excepciones
