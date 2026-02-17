# Configuracion

El SDK ofrece opciones de configuracion para seleccion de region, timeouts, reintentos y clientes HTTP custom.

## Seleccion de region

Workiva tiene 3 regiones disponibles. Se seleccionan con el enum `Region`:

```python
from workiva import Workiva, Region

# EU (por defecto)
client = Workiva(client_id="...", client_secret="...")

# US
client = Workiva(client_id="...", client_secret="...", region=Region.US)

# APAC
client = Workiva(client_id="...", client_secret="...", region=Region.APAC)
```

| Region | Enum | Platform URL | Chains URL | Wdata URL |
|--------|------|-------------|------------|-----------|
| EU (default) | `Region.EU` | `api.eu.wdesk.com` | `h.eu.wdesk.com/s/wdata/oc/api` | `h.eu.wdesk.com/s/wdata/prep` |
| US | `Region.US` | `api.app.wdesk.com` | `h.app.wdesk.com/s/wdata/oc/api` | `h.app.wdesk.com/s/wdata/prep` |
| APAC | `Region.APAC` | `api.apac.wdesk.com` | `h.apac.wdesk.com/s/wdata/oc/api` | `h.apac.wdesk.com/s/wdata/prep` |

> **No existe** un parametro `server_url` ni `server_idx`. La region es la unica forma de seleccionar el servidor.

### Multi-base-URL automatico

Cada API (Platform, Chains, Wdata) tiene su propio servidor base. El SDK rutea automaticamente cada operacion al servidor correcto segun el namespace que uses. No necesitas configurar nada:

```python
with Workiva(client_id="...", client_secret="...", region=Region.US) as client:
    # Se envia a api.app.wdesk.com
    files = client.files.get_files()

    # Se envia a h.app.wdesk.com/s/wdata/oc/api
    chains = client.chains.get_chains(...)

    # Se envia a h.app.wdesk.com/s/wdata/prep
    tables = client.wdata.get_tables(...)
```

## Timeout

### Global

Timeout en **segundos** para todas las operaciones HTTP:

```python
client = Workiva(
    client_id="...",
    client_secret="...",
    timeout=30,  # 30 segundos
)
```

Si no se especifica, no hay timeout (las conexiones esperan indefinidamente).

> **Nota:** el timeout se especifica en **segundos** (float), no en milisegundos.

### Per-operation

Cada metodo acepta un parametro `timeout` que sobreescribe el timeout global para esa solicitud especifica:

```python
# Timeout de 60 segundos solo para esta operacion
result = client.files.get_files(timeout=60)

# Timeout de 5 minutos para una operacion pesada
result = client.spreadsheets.get_spreadsheet(
    spreadsheet_id="abc",
    timeout=300,
)
```

> **No existen** parametros `retries=`, `server_url=` ni `http_headers=` per-operation. El unico parametro extra que aceptan todos los metodos es `timeout`.

## Reintentos

El SDK incluye un sistema de reintentos con backoff exponencial implementado como transport de httpx. Se configura a traves de `SDKConfig` y `RetryConfig`:

```python
from workiva import Workiva, Region
from workiva._config import SDKConfig, RetryConfig

client = Workiva(
    client_id="...",
    client_secret="...",
    config=SDKConfig(
        region=Region.EU,
        timeout_s=30,
        retry=RetryConfig(
            initial_interval_ms=500,       # 500ms intervalo inicial
            max_interval_ms=30_000,        # 30 segundos maximo entre reintentos
            exponent=1.5,                  # Factor exponencial
            max_elapsed_ms=120_000,        # 2 minutos maximo total
            retry_connection_errors=True,  # Reintentar errores de conexion
            status_codes=(429, 500, 502, 503, 504),  # Codigos a reintentar
        ),
    ),
)
```

### Parametros de RetryConfig

| Parametro | Default | Descripcion |
|-----------|---------|-------------|
| `initial_interval_ms` | `500` | Intervalo inicial entre reintentos (ms) |
| `max_interval_ms` | `30_000` | Intervalo maximo entre reintentos (ms) |
| `exponent` | `1.5` | Factor de crecimiento exponencial |
| `max_elapsed_ms` | `120_000` | Tiempo maximo total para reintentos (ms) |
| `retry_connection_errors` | `True` | Reintentar ante `ConnectError` y `TimeoutException` |
| `status_codes` | `(429, 500, 502, 503, 504)` | Codigos HTTP que activan reintento |

### Calculo del intervalo

El intervalo entre reintentos se calcula asi:

```
intervalo = (initial_interval_ms / 1000) * (exponent ^ intento) + jitter_aleatorio(0, 1)
intervalo = min(intervalo, max_interval_ms / 1000)
```

Si la respuesta incluye un header `Retry-After`, el SDK respeta ese intervalo (con tope en `max_interval_ms`).

### Valores por defecto

Si no configuras nada, el SDK usa estos valores por defecto:

```python
RetryConfig(
    initial_interval_ms=500,
    max_interval_ms=30_000,
    exponent=1.5,
    max_elapsed_ms=120_000,
    retry_connection_errors=True,
    status_codes=(429, 500, 502, 503, 504),
)
```

> **No existen** las clases `BackoffStrategy` ni el modulo `workiva.utils.retries`. La configuracion de reintentos vive en `workiva._config.RetryConfig`.

### Desactivar reintentos

Para desactivar completamente los reintentos:

```python
from workiva._config import SDKConfig, RetryConfig

client = Workiva(
    client_id="...",
    client_secret="...",
    config=SDKConfig(
        retry=RetryConfig(
            max_elapsed_ms=0,
            retry_connection_errors=False,
            status_codes=(),
        ),
    ),
)
```

## Clientes HTTP custom

El SDK usa `httpx` internamente. Puedes pasar tu propio cliente para escenarios avanzados (proxies, certificados, configuracion de red):

### Cliente sync custom

```python
import httpx
from workiva import Workiva

custom_client = httpx.Client(
    follow_redirects=True,
    verify=False,  # Solo para desarrollo
    proxy="http://proxy:8080",
)

client = Workiva(
    client_id="...",
    client_secret="...",
    client=custom_client,
)
```

### Cliente async custom

```python
import httpx
from workiva import Workiva

custom_async = httpx.AsyncClient(
    follow_redirects=True,
    timeout=httpx.Timeout(60.0),
)

client = Workiva(
    client_id="...",
    client_secret="...",
    async_client=custom_async,
)
```

> **Importante:** Si proporcionas un cliente custom, el SDK **NO** lo cerrara automaticamente. Eres responsable de gestionarlo. Los clientes creados internamente por el SDK si se cierran automaticamente al salir del context manager.

### Clientes lazy

Si no proporcionas un cliente custom, el SDK crea los clientes HTTP de forma **lazy** (al primer uso):

- Si solo usas metodos sync, nunca se crea un `AsyncClient`
- Si solo usas metodos async, nunca se crea un `Client` sync
- Esto evita crear recursos innecesarios

## Context managers

Usa context managers para cerrar conexiones automaticamente:

```python
# Sync
with Workiva(client_id="...", client_secret="...") as client:
    result = client.files.get_files()
# Conexiones cerradas automaticamente

# Async
async with Workiva(client_id="...", client_secret="...") as client:
    result = await client.files.get_files_async()
# Conexiones cerradas automaticamente
```

Si prefieres no usar context managers, cierra manualmente:

```python
client = Workiva(client_id="...", client_secret="...")
try:
    result = client.files.get_files()
finally:
    client.close()      # Sync
    # await client.aclose()  # Async
```

## SDKConfig completo

`SDKConfig` agrupa toda la configuracion del SDK en un solo dataclass:

```python
from workiva._config import SDKConfig, RetryConfig
from workiva._constants import Region

config = SDKConfig(
    region=Region.US,        # Region del servidor
    timeout_s=30.0,          # Timeout global en segundos
    retry=RetryConfig(...),  # Configuracion de reintentos
)
```

| Campo | Tipo | Default | Descripcion |
|-------|------|---------|-------------|
| `region` | `Region` | `Region.EU` | Region del servidor |
| `timeout_s` | `Optional[float]` | `None` | Timeout global (segundos). `None` = sin limite |
| `retry` | `RetryConfig` | `RetryConfig()` | Configuracion de reintentos |
| `logger` | `logging.Logger` | `logging.getLogger("workiva")` | Logger para el SDK |

### Relacion entre `timeout` y `config`

Si pasas tanto `timeout=` como `config=` al constructor de `Workiva`, el `config` tiene prioridad:

```python
# El timeout del config prevalece (timeout=30 se ignora)
client = Workiva(
    client_id="...",
    client_secret="...",
    timeout=30,
    config=SDKConfig(timeout_s=60),  # Este gana
)
```

Si pasas `timeout=` sin `config=`, el SDK crea un `SDKConfig` internamente con ese timeout:

```python
# Internamente: SDKConfig(region=Region.EU, timeout_s=30)
client = Workiva(
    client_id="...",
    client_secret="...",
    timeout=30,
)
```

## Siguiente paso

- [Operaciones de larga duracion](operaciones-larga-duracion.md) -- Patron 202, polling, `wait()`
- [Manejo de errores](manejo-errores.md) -- Jerarquia de excepciones, try/except
