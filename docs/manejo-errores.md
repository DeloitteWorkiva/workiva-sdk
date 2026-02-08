# Manejo de errores

El SDK define una jerarquía de excepciones que cubre errores de API, errores de validación y errores de polling.

## Jerarquía de excepciones

```
Exception
├── SDKBaseError                    # Base para errores HTTP
│   ├── ErrorResponse               # Platform API errors (4xx/5xx con body JSON)
│   ├── SingleError                 # Error simple con code + body + details
│   ├── MultiError                  # Múltiples mensajes en body
│   ├── ChainSingleError            # Error de Chains API (error + error_description)
│   ├── Failure                     # Error JSON:API
│   ├── IamError                    # Error de IAM/OAuth
│   ├── SDKError                    # Fallback genérico
│   ├── ResponseValidationError     # Pydantic no pudo parsear la respuesta
│   └── NoResponseError             # Sin respuesta del servidor
├── OperationFailed                 # Operación polling: status == "failed"
├── OperationCancelled              # Operación polling: status == "cancelled"
└── OperationTimeout                # Operación polling: timeout excedido
```

## `SDKBaseError` — La base

Todos los errores HTTP heredan de `SDKBaseError`:

```python
from workiva.errors import SDKBaseError

try:
    response = client.files.get_file_by_id(file_id="no-existe")
except SDKBaseError as e:
    print(f"Status: {e.status_code}")
    print(f"Mensaje: {e.message}")
    print(f"Body: {e.body}")
    print(f"Headers: {e.headers}")
    print(f"Response: {e.raw_response}")
```

### Propiedades

| Propiedad | Tipo | Descripción |
|-----------|------|-------------|
| `message` | `str` | Mensaje del error |
| `status_code` | `int` | Código HTTP |
| `body` | `str` | Body de la respuesta |
| `headers` | `httpx.Headers` | Headers de la respuesta |
| `raw_response` | `httpx.Response` | Respuesta HTTP completa |

## `ErrorResponse` — Error de Platform API

La mayoría de errores de Platform API (archivos, documentos, etc.):

```python
from workiva.errors import ErrorResponse

try:
    client.files.get_file_by_id(file_id="invalid")
except ErrorResponse as e:
    print(f"Code: {e.data.code}")
    print(f"Message: {e.data.message}")
    print(f"Target: {e.data.target}")
    print(f"Docs: {e.data.documentation_url}")

    if e.data.details:
        for detail in e.data.details:
            print(f"  Detail: {detail.code} - {detail.message}")
```

### `ErrorResponseData`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `code` | `str \| None` | Código de error del servidor |
| `message` | `str \| None` | Mensaje legible |
| `target` | `str \| None` | Objetivo del error |
| `documentation_url` | `str \| None` | URL de documentación |
| `details` | `list[ErrorDetails] \| None` | Detalles adicionales |
| `version` | `str \| None` | Versión de la API |

## `SingleError` — Error simple

Usado por algunos endpoints de Platform:

```python
from workiva.errors import SingleError

try:
    client.admin.create_workspace(workspace=data)
except SingleError as e:
    print(f"Code: {e.data.code}")      # int
    print(f"Body: {e.data.body}")      # str
    if e.data.details:
        for d in e.data.details:
            print(f"  {d.code}: {d.message} → {d.target}")
```

## `MultiError` — Error múltiple

Similar a `SingleError` pero `body` es una lista de strings:

```python
from workiva.errors import MultiError

try:
    client.admin.assign_organization_user_roles(
        organization_id="org-1",
        user_id="user-1",
        request_body=["invalid-role"],
    )
except MultiError as e:
    for msg in e.data.body:
        print(f"Error: {msg}")
```

## `ChainSingleError` — Error de Chains

Los endpoints de Chains devuelven un formato distinto:

```python
from workiva.errors import ChainSingleError

try:
    client.chains.get_chain(chain_id="invalid")
except ChainSingleError as e:
    print(f"Error: {e.data.error}")
    print(f"Descripción: {e.data.error_description}")
```

## `SDKError` — Fallback genérico

Cuando la respuesta no coincide con ningún error tipado:

```python
from workiva.errors import SDKError

try:
    client.files.get_files()
except SDKError as e:
    print(f"Status: {e.status_code}")
    print(f"Body: {e.body}")
```

## `ResponseValidationError` — Error de validación

Cuando Pydantic no puede parsear la respuesta del servidor:

```python
from workiva.errors import ResponseValidationError

try:
    response = client.files.get_files()
except ResponseValidationError as e:
    print(f"Error de validación: {e.message}")
    print(f"Causa: {e.cause}")  # ValidationError de Pydantic
```

## Excepciones de polling

Estas NO heredan de `SDKBaseError` — son `Exception` directas:

```python
from workiva import OperationFailed, OperationCancelled, OperationTimeout

try:
    operation = client.wait(response).result(timeout=120)
except OperationFailed as e:
    # e.operation: Operation
    # e.details: list[OperationDetail]
    print(f"Falló: {e}")
except OperationCancelled as e:
    # e.operation: Operation
    print(f"Cancelada: {e.operation.id}")
except OperationTimeout as e:
    # e.operation_id: str
    # e.timeout: float
    # e.last_status: str | None
    print(f"Timeout: {e}")
```

## Ejemplo completo: try/except multinivel

```python
from workiva import Workiva, OperationFailed, OperationTimeout
from workiva.errors import ErrorResponse, SingleError, SDKBaseError
from workiva.models import FileCopy

with Workiva(client_id="...", client_secret="...") as client:
    try:
        # Copiar archivo
        response = client.files.copy_file(
            file_id="abc",
            file_copy=FileCopy(workspace_id="ws-123"),
        )

        # Esperar resultado
        operation = client.wait(response).result(timeout=300)
        print(f"Completado: {operation.resource_url}")

    except ErrorResponse as e:
        # Error de API con detalles ricos
        print(f"API Error [{e.data.code}]: {e.data.message}")

    except SingleError as e:
        # Error simple
        print(f"Error {e.data.code}: {e.data.body}")

    except OperationFailed as e:
        # La operación se completó con error
        print(f"Operación fallida: {e.operation.id}")
        for detail in e.details:
            print(f"  {detail.message}")

    except OperationTimeout as e:
        # Timeout de polling
        print(f"Timeout después de {e.timeout}s")

    except SDKBaseError as e:
        # Cualquier otro error HTTP
        print(f"Error HTTP {e.status_code}: {e.message}")

    except Exception as e:
        # Errores de red, etc.
        print(f"Error inesperado: {e}")
```

## Errores de red

Los errores de red de `httpx` se propagan directamente:

```python
import httpx

try:
    response = client.files.get_files()
except httpx.ConnectError:
    print("No se pudo conectar al servidor")
except httpx.TimeoutException:
    print("Timeout de conexión")
```
