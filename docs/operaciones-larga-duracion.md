# Operaciones de larga duracion

Algunas operaciones de Workiva (copiar archivos, importar, exportar) no se completan inmediatamente. En su lugar, devuelven un HTTP **202 Accepted** con un header `Location` que apunta a una operacion que puedes consultar.

## El patron 202

```
POST /files/{fileId}/copy
  -> 202 Accepted
  -> Location: /operations/{operationId}
  -> Retry-After: 2
```

El SDK simplifica este patron con `client.wait()` y `OperationPoller`.

## Uso basico

```python
from workiva import Workiva
from workiva.models.platform import FileCopy

with Workiva(client_id="...", client_secret="...") as client:
    # Iniciar la operacion (devuelve httpx.Response con 202)
    response = client.files.copy_file(
        file_id="abc123",
        body=FileCopy(workspace_id="ws-456"),
    )

    # Crear el poller y esperar el resultado
    operation = client.wait(response).result(timeout=300)

    print(f"Estado: {operation.status}")          # "completed"
    print(f"Recurso: {operation.resource_url}")   # URL del resultado
```

## `client.wait(response)` -> `OperationPoller`

`wait()` extrae automaticamente:
- El **operation ID** del header `Location`
- El **intervalo de polling** del header `Retry-After` (default: 2 segundos)

Devuelve un `OperationPoller` listo para usar.

## `OperationPoller`

### `poller.result(timeout=300)` -- Polling automatico (sync)

Hace polling hasta que la operacion llega a un estado terminal o se agota el timeout:

```python
poller = client.wait(response)
operation = poller.result(timeout=300)  # Maximo 5 minutos
```

- Devuelve un `Operation` tipado (modelo Pydantic)
- Respeta `Retry-After` del servidor (maximo 60 segundos)
- Lanza `OperationTimeout` si se excede el timeout
- Lanza `OperationFailed` si la operacion falla
- Lanza `OperationCancelled` si la operacion se cancela

### `poller.result_async(timeout=300)` -- Polling automatico (async)

```python
poller = client.wait(response)
operation = await poller.result_async(timeout=300)
```

### `poller.poll()` -- Polling manual (sync)

Ejecuta una sola solicitud de polling y devuelve el `Operation` actual:

```python
poller = client.wait(response)

# Polling manual con logica custom
while not poller.done():
    operation = poller.poll()
    print(f"Estado: {operation.status}")
    # Tu logica de espera aqui
```

### `poller.poll_async()` -- Polling manual (async)

```python
operation = await poller.poll_async()
```

### `poller.done()` -- Verificar estado

Verifica si la operacion ha llegado a un estado terminal **sin hacer una llamada a la API**:

```python
if poller.done():
    print("La operacion termino")
```

### Propiedades

| Propiedad | Tipo | Descripcion |
|-----------|------|-------------|
| `operation_id` | `str` | ID de la operacion |
| `response_body` | `Any \| None` | Body original de la respuesta 202 |
| `last_operation` | `Operation \| None` | Ultimo snapshot de la operacion (o `None` si nunca se hizo polling) |

## Estados de una operacion

Los valores posibles de `operation.status` son strings:

```python
# No terminales (el polling continua)
"acknowledged"   # Recibida
"queued"         # En cola
"started"        # En progreso

# Terminales (el polling se detiene)
"completed"      # Exito
"failed"         # Error -> lanza OperationFailed
"cancelled"      # Cancelada -> lanza OperationCancelled
```

## Excepciones

### `OperationFailed`

Lanzada cuando `status == "failed"`:

```python
from workiva import OperationFailed

try:
    operation = client.wait(response).result(timeout=300)
except OperationFailed as e:
    print(f"Operacion fallo: {e}")
    print(f"Operation ID: {e.operation.id}")
    for detail in e.details:
        print(f"  [{detail.code}] {detail.message}")
```

### `OperationCancelled`

Lanzada cuando `status == "cancelled"`:

```python
from workiva import OperationCancelled

try:
    operation = client.wait(response).result()
except OperationCancelled as e:
    print(f"Operacion cancelada: {e.operation.id}")
```

### `OperationTimeout`

Lanzada cuando se excede el timeout:

```python
from workiva import OperationTimeout

try:
    operation = client.wait(response).result(timeout=60)
except OperationTimeout as e:
    print(f"Timeout: operacion {e.operation_id}")
    print(f"Duracion maxima: {e.timeout}s")
    print(f"Ultimo estado: {e.last_status}")
```

## Header `Retry-After`

El SDK respeta automaticamente el header `Retry-After` del servidor:

- Si el servidor indica `Retry-After: 5`, el SDK espera 5 segundos entre polls
- El maximo es 60 segundos (proteccion contra valores absurdos)
- Si no hay header, el default es 2 segundos
- El intervalo se actualiza con cada respuesta de polling
- Soporta formato numerico y HTTP-date

## Modelo `Operation`

El modelo `Operation` es un modelo Pydantic v2 con estos campos principales:

```python
from workiva.models.platform import Operation

# Campos principales:
operation.id              # str -- ID unico
operation.status          # str -- "completed", "failed", etc.
operation.resource_url    # str | None -- URL del recurso (solo en completed)
operation.details         # list[OperationDetail] -- Detalles (errores, etc.)
operation.created         # OperationCreated -- Fecha y usuario de creacion
operation.updated         # Updated -- Ultima actualizacion
```

## Ejemplo completo

```python
from workiva import Workiva, OperationFailed, OperationTimeout
from workiva.models.platform import FileCopy

with Workiva(client_id="...", client_secret="...") as client:
    # 1. Iniciar copia
    response = client.files.copy_file(
        file_id="original-file-id",
        body=FileCopy(workspace_id="target-workspace-id"),
    )

    # 2. Esperar resultado
    try:
        operation = client.wait(response).result(timeout=300)
    except OperationFailed as e:
        print(f"Error en copia: {e}")
        raise
    except OperationTimeout as e:
        print(f"La copia tardo mas de {e.timeout}s")
        raise

    # 3. Consultar resultados de la copia
    results = client.operations.get_copy_file_results(
        operation_id=operation.id,
    )
    print(f"Copia completada")
```
