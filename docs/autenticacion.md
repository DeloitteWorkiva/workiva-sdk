# Autenticación

El SDK utiliza OAuth2 **Client Credentials** para autenticarse con las APIs de Workiva. Todo el manejo de tokens es automático.

## Flujo OAuth2 Client Credentials

```
Tu aplicación                    Workiva IAM
     │                                │
     │  POST /iam/v1/oauth2/token     │
     │  client_id + client_secret     │
     │ ─────────────────────────────► │
     │                                │
     │  access_token + expires_in     │
     │ ◄───────────────────────────── │
     │                                │
     │  GET /files (Bearer token)     │
     │ ─────────────────────────────► │
     │                                │
```

El endpoint de tokens es: `https://api.app.wdesk.com/iam/v1/oauth2/token`

## Clase `Workiva` (recomendado)

La forma más sencilla de autenticarse:

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    response = client.files.get_files()
```

`Workiva` extiende `SDK` y simplifica la autenticación — internamente crea el modelo `Security` por ti.

## Clase `SDK` (avanzado)

Si necesitas más control, puedes usar `SDK` directamente con el modelo `Security`:

```python
from workiva import SDK
from workiva.models import Security

sdk = SDK(
    security=Security(
        client_id="tu_client_id",
        client_secret="tu_client_secret",
    ),
)
```

También puedes pasar `security` como un callable para credenciales dinámicas:

```python
def get_credentials():
    return Security(
        client_id=fetch_from_vault("client_id"),
        client_secret=fetch_from_vault("client_secret"),
    )

sdk = SDK(security=get_credentials)
```

## Token caching

El SDK cachea los tokens de acceso de forma **global** a nivel de proceso:

- La caché es un `ClassVar` en `ClientCredentialsHook` — compartida entre TODAS las instancias del SDK
- Si creas múltiples instancias de `Workiva` con las mismas credenciales, reutilizan el mismo token
- Los tokens se refrescan automáticamente antes de expirar (buffer de 60 segundos)
- Ante un error 401, el token se invalida y se obtiene uno nuevo

```python
# Ambos clientes comparten el mismo token cacheado
client1 = Workiva(client_id="abc", client_secret="xyz")
client2 = Workiva(client_id="abc", client_secret="xyz")
```

## Scopes

Los scopes se determinan automáticamente por operación. Cada endpoint del SDK tiene sus scopes OAuth2 definidos y se envían en la solicitud del token.

## Refresco automático ante 401

Si una llamada a la API devuelve HTTP 401:

1. El hook `AfterError` detecta el 401
2. Invalida el token cacheado para esas credenciales
3. La próxima solicitud obtiene un token nuevo automáticamente

No necesitas manejar la renovación de tokens manualmente.

## Token URL personalizado

Por defecto, el token URL es `/iam/v1/oauth2/token` (relativo al servidor base). Si necesitas cambiarlo:

```python
from workiva.models import Security

security = Security(
    client_id="abc",
    client_secret="xyz",
    token_url="https://custom-auth.example.com/oauth2/token",
)
```

## Thread safety

El sistema de tokens es thread-safe:

- Cada par de credenciales tiene su propio lock
- Las solicitudes de token se serializan por cliente (no hay race conditions)
- Las solicitudes de token siempre son síncronas (incluso en flujos async se ejecutan con `self.client.send()`)
