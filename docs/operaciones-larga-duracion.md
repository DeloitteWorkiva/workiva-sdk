# Operaciones de larga duración

Algunas operaciones de Workiva (copiar archivos, importar, exportar) no se completan inmediatamente. En su lugar, devuelven un HTTP **202 Accepted** con un header `Location` que apunta a una operación que puedes consultar.

## El patrón 202

```
POST /files/{fileId}/copy
  → 202 Accepted
  → Location: /operations/{operationId}
  → Retry-After: 2
```

El SDK simplifica este patrón con `client.wait()` y `OperationPoller`.

## Uso básico

```python
from workiva import Workiva
from workiva.models import FileCopy

with Workiva(client_id="...", client_secret="...") as client:
    # Iniciar la operación (devuelve 202)
    response = client.files.copy_file(
        file_id="abc123",
        file_copy=FileCopy(
            workspace_id="ws-456",
        ),
    )

    # Crear el poller y esperar el resultado
    operation = client.wait(response).result(timeout=300)

    print(f"Estado: {operation.status}")          # "completed"
    print(f"Recurso: {operation.resource_url}")   # URL del resultado
```

## `client.wait(response)` → `OperationPoller`

`wait()` extrae automáticamente:
- El **operation ID** del header `Location`
- El **intervalo de polling** del header `Retry-After` (default: 2 segundos)

Devuelve un `OperationPoller` listo para usar.

## `OperationPoller`

### `poller.result(timeout=300)` — Polling automático (sync)

Hace polling hasta que la operación llega a un estado terminal o se agota el timeout:

```python
poller = client.wait(response)
operation = poller.result(timeout=300)  # Máximo 5 minutos
```

- Devuelve el `Operation` completado
- Respeta `Retry-After` del servidor (máximo 60 segundos)
- Lanza `OperationTimeout` si se excede el timeout

### `poller.result_async(timeout=300)` — Polling automático (async)

```python
poller = client.wait(response)
operation = await poller.result_async(timeout=300)
```

### `poller.poll()` — Polling manual (sync)

Ejecuta una sola solicitud de polling:

```python
poller = client.wait(response)

# Polling manual con lógica custom
while not poller.done():
    operation = poller.poll()
    print(f"Estado: {operation.status}")
    # Tu lógica de espera aquí
```

### `poller.poll_async()` — Polling manual (async)

```python
operation = await poller.poll_async()
```

### `poller.done()` — Verificar estado

Verifica si la operación ha llegado a un estado terminal **sin hacer una llamada a la API**:

```python
if poller.done():
    print("La operación terminó")
```

### Propiedades

| Propiedad | Tipo | Descripción |
|-----------|------|-------------|
| `operation_id` | `str` | ID de la operación |
| `response_body` | `Any \| None` | Body original de la respuesta 202 |
| `last_operation` | `Operation \| None` | Último snapshot de la operación (o `None` si nunca se hizo polling) |

## Estados de una operación

```python
from workiva.models.operation import OperationStatus

# No terminales (el polling continúa)
OperationStatus.ACKNOWLEDGED   # Recibida
OperationStatus.QUEUED         # En cola
OperationStatus.STARTED        # En progreso

# Terminales (el polling se detiene)
OperationStatus.COMPLETED      # Éxito
OperationStatus.FAILED         # Error
OperationStatus.CANCELLED      # Cancelada
```

## Excepciones

### `OperationFailed`

Lanzada cuando `status == "failed"`:

```python
from workiva import Workiva, OperationFailed

try:
    operation = client.wait(response).result(timeout=300)
except OperationFailed as e:
    print(f"Operación falló: {e}")
    print(f"Operation ID: {e.operation.id}")
    for detail in e.details:
        print(f"  [{detail.code}] {detail.message} → {detail.target}")
```

### `OperationCancelled`

Lanzada cuando `status == "cancelled"`:

```python
from workiva import OperationCancelled

try:
    operation = client.wait(response).result()
except OperationCancelled as e:
    print(f"Operación cancelada: {e.operation.id}")
```

### `OperationTimeout`

Lanzada cuando se excede el timeout:

```python
from workiva import OperationTimeout

try:
    operation = client.wait(response).result(timeout=60)
except OperationTimeout as e:
    print(f"Timeout: operación {e.operation_id}")
    print(f"Duración: {e.timeout}s")
    print(f"Último estado: {e.last_status}")
```

## Header `Retry-After`

El SDK respeta automáticamente el header `Retry-After` del servidor:

- Si el servidor indica `Retry-After: 5`, el SDK espera 5 segundos entre polls
- El máximo es 60 segundos (protección contra valores absurdos)
- Si no hay header, el default es 2 segundos
- El intervalo se actualiza con cada respuesta de polling

## Modelo `Operation`

```python
class Operation:
    id: str                          # ID único
    status: OperationStatus          # Estado actual
    created: OperationCreated        # Fecha y usuario de creación
    updated: Updated                 # Última actualización
    resource_url: str | None         # URL del recurso resultante (solo en completed)
    original_request: str | None     # Request ID original
    details: list[OperationDetail]   # Detalles adicionales (errores, etc.)
```

## Ejemplo completo: copiar + consultar resultado

```python
from workiva import Workiva, OperationFailed, OperationTimeout
from workiva.models import FileCopy

with Workiva(client_id="...", client_secret="...") as client:
    # 1. Iniciar copia
    response = client.files.copy_file(
        file_id="original-file-id",
        file_copy=FileCopy(workspace_id="target-workspace-id"),
    )

    # 2. Esperar resultado
    try:
        operation = client.wait(response).result(timeout=300)
    except OperationFailed as e:
        print(f"Error en copia: {e}")
        raise
    except OperationTimeout as e:
        print(f"La copia tardó más de {e.timeout}s")
        raise

    # 3. Consultar resultados de la copia
    results = client.operations.get_copy_file_results(
        operation_id=operation.id,
    )
    print(f"Archivos copiados: {results.result}")
```
