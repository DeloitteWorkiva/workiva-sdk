# Configuración

El SDK ofrece múltiples opciones de configuración: selección de servidor, timeouts, reintentos, logging y clientes HTTP custom.

## Selección de servidor

Workiva tiene 3 regiones disponibles:

| Índice | Región | URL |
|--------|--------|-----|
| 0 (default) | US | `https://api.app.wdesk.com` |
| 1 | EU | `https://api.eu.wdesk.com` |
| 2 | APAC | `https://api.apac.wdesk.com` |

```python
from workiva import Workiva

# US (por defecto)
client = Workiva(client_id="...", client_secret="...")

# EU
client = Workiva(client_id="...", client_secret="...", server_idx=1)

# APAC
client = Workiva(client_id="...", client_secret="...", server_idx=2)
```

### URL personalizada

Puedes pasar un `server_url` directamente:

```python
client = Workiva(
    client_id="...",
    client_secret="...",
    server_url="https://api.custom.wdesk.com",
)
```

### Multi-base-URL

Las APIs de Chains y Wdata tienen sus propias URLs base, inyectadas automáticamente a nivel de path. No necesitas configurar nada especial — el SDK rutea cada operación al servidor correcto.

## Timeout

### Global

Timeout en milisegundos para todas las operaciones:

```python
client = Workiva(
    client_id="...",
    client_secret="...",
    timeout_ms=30000,  # 30 segundos
)
```

### Per-operation

Cada método acepta un parámetro `timeout_ms` que sobreescribe el timeout global:

```python
# Timeout de 60 segundos solo para esta operación
response = client.files.get_files(timeout_ms=60000)
```

## Reintentos

Configura una estrategia de reintentos con backoff exponencial:

```python
from workiva import Workiva
from workiva.utils.retries import RetryConfig, BackoffStrategy

client = Workiva(
    client_id="...",
    client_secret="...",
    retry_config=RetryConfig(
        strategy="backoff",
        backoff=BackoffStrategy(
            initial_interval=500,    # 500ms
            max_interval=60000,      # 60 segundos
            exponent=1.5,            # Factor exponencial
            max_elapsed_time=300000, # 5 minutos máximo
        ),
        retry_connection_errors=True,
    ),
)
```

### Per-operation

```python
from workiva.utils.retries import RetryConfig, BackoffStrategy

custom_retry = RetryConfig(
    strategy="backoff",
    backoff=BackoffStrategy(
        initial_interval=1000,
        max_interval=30000,
        exponent=2.0,
        max_elapsed_time=120000,
    ),
    retry_connection_errors=True,
)

response = client.files.get_files(retries=custom_retry)
```

### Códigos HTTP reintentados

El SDK reintenta automáticamente los siguientes status codes (según la operación):
- `408` — Request Timeout
- `429` — Too Many Requests
- `5XX` — Server Errors

Si la respuesta incluye un header `Retry-After`, el SDK respeta ese intervalo.

## Debug logging

Para habilitar logging de debug:

```python
import logging

# Logger estándar de Python
logger = logging.getLogger("workiva")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

client = Workiva(
    client_id="...",
    client_secret="...",
    debug_logger=logger,
)
```

## Clientes HTTP custom

El SDK usa `httpx` internamente. Puedes pasar tu propio cliente:

```python
import httpx
from workiva import Workiva

# Cliente sync custom
custom_client = httpx.Client(
    follow_redirects=True,
    verify=False,  # Solo para desarrollo
    proxies="http://proxy:8080",
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

> Si proporcionas un cliente custom, el SDK NO lo cerrará automáticamente. Eres responsable de cerrarlo cuando termines.

## Context managers

El SDK soporta context managers para cerrar conexiones automáticamente:

```python
# Sync
with Workiva(client_id="...", client_secret="...") as client:
    response = client.files.get_files()
# Conexión cerrada automáticamente

# Async
async with Workiva(client_id="...", client_secret="...") as client:
    response = await client.files.get_files_async()
# Conexión cerrada automáticamente
```

## Headers personalizados

Cada método acepta `http_headers` para agregar o sobreescribir headers:

```python
response = client.files.get_files(
    http_headers={"X-Request-Id": "abc123"},
)
```

## Server URL per-operation

Cada método acepta `server_url` para sobreescribir el servidor de esa operación específica:

```python
response = client.files.get_files(
    server_url="https://api.eu.wdesk.com",
)
```
