# Manejo de errores

El SDK define una jerarquia de excepciones que cubre errores de API, errores de autenticacion y errores de polling.

## Jerarquia de excepciones

```
WorkivaError(Exception)             # Base para TODOS los errores del SDK
├── WorkivaAPIError                 # Base para errores HTTP de la API
│   ├── BadRequestError             # 400
│   ├── AuthenticationError         # 401
│   ├── ForbiddenError              # 403
│   ├── NotFoundError               # 404
│   ├── ConflictError               # 409
│   ├── RateLimitError              # 429
│   └── ServerError                 # 5xx
└── TokenAcquisitionError           # Error al obtener token OAuth2

Exception
├── OperationFailed                 # Polling: status == "failed"
├── OperationCancelled              # Polling: status == "cancelled"
└── OperationTimeout                # Polling: timeout excedido
```

> **`WorkivaError`** es la clase base comun para errores de API y errores de autenticacion. Puedes hacer `except WorkivaError` para atrapar ambos en un solo handler.

## `WorkivaError` -- La raiz

`WorkivaError` es la excepcion base de todo el SDK. Atrapa tanto errores HTTP como errores de token:

```python
from workiva import WorkivaError

try:
    result = client.files.get_file_by_id(file_id="no-existe")
except WorkivaError as e:
    # Atrapa WorkivaAPIError, TokenAcquisitionError, y todas sus subclases
    print(f"Error del SDK: {e}")
```

## `WorkivaAPIError` -- Errores HTTP

Todos los errores HTTP de la API heredan de `WorkivaAPIError` (que a su vez hereda de `WorkivaError`):

```python
from workiva import WorkivaAPIError

try:
    result = client.files.get_file_by_id(file_id="no-existe")
except WorkivaAPIError as e:
    print(f"Status: {e.status_code}")   # int (404, 400, etc.)
    print(f"Mensaje: {e}")              # Mensaje legible
    print(f"Body: {e.body}")            # dict JSON o texto
    print(f"Response: {e.response}")    # httpx.Response completo
```

### Atributos de `WorkivaAPIError`

| Atributo | Tipo | Descripcion |
|----------|------|-------------|
| `status_code` | `int` | Codigo HTTP (400, 401, 404, etc.) |
| `body` | `Any` | Body JSON parseado, o texto si no es JSON |
| `response` | `httpx.Response` | Respuesta HTTP completa (headers, etc.) |

## Excepciones por codigo HTTP

Cada codigo HTTP comun tiene su propia excepcion:

### `BadRequestError` (400)

```python
from workiva import BadRequestError

try:
    client.files.copy_file(file_id="abc")
except BadRequestError as e:
    print(f"Request invalido: {e}")
    print(f"Detalles: {e.body}")
```

### `AuthenticationError` (401)

```python
from workiva import AuthenticationError

try:
    client.files.get_files()
except AuthenticationError as e:
    print(f"Token invalido o expirado: {e}")
```

> Normalmente no veras esta excepcion porque el SDK reintenta automaticamente ante 401 con un token nuevo. Solo ocurre si el reintento tambien falla.

### `ForbiddenError` (403)

```python
from workiva import ForbiddenError

try:
    client.admin.get_workspaces()
except ForbiddenError as e:
    print(f"Sin permisos: {e}")
```

### `NotFoundError` (404)

```python
from workiva import NotFoundError

try:
    client.files.get_file_by_id(file_id="no-existe")
except NotFoundError as e:
    print(f"No encontrado: {e}")
```

### `ConflictError` (409)

```python
from workiva import ConflictError

try:
    client.files.copy_file(file_id="abc", destination_container="folder-456")
except ConflictError as e:
    print(f"Conflicto: {e}")
```

### `RateLimitError` (429)

```python
from workiva import RateLimitError

try:
    client.files.get_files()
except RateLimitError as e:
    print(f"Rate limit: {e}")
    # El SDK reintenta automaticamente con backoff,
    # solo llegas aqui si se agotan los reintentos
```

### `ServerError` (5xx)

```python
from workiva import ServerError

try:
    client.files.get_files()
except ServerError as e:
    print(f"Error del servidor ({e.status_code}): {e}")
```

## `TokenAcquisitionError`

Error al obtener el token OAuth2 (credenciales invalidas, servidor no disponible):

```python
from workiva import Workiva, TokenAcquisitionError

try:
    with Workiva(client_id="invalido", client_secret="invalido") as client:
        client.files.get_files()
except TokenAcquisitionError as e:
    print(f"No se pudo obtener el token: {e}")
```

## Excepciones de polling

Estas NO heredan de `WorkivaError` -- son `Exception` directas, relacionadas con operaciones de larga duracion:

### `OperationFailed`

Lanzada cuando una operacion llega a `status == "failed"`:

```python
from workiva import OperationFailed

try:
    operation = client.wait(response).result(timeout=300)
except OperationFailed as e:
    print(f"Operacion fallida: {e}")
    print(f"Operation ID: {e.operation.id}")          # str
    print(f"Status: {e.operation.status}")             # "failed"
    for detail in e.details:                           # list[OperationDetail]
        print(f"  [{detail.code}] {detail.message}")
```

### `OperationCancelled`

Lanzada cuando una operacion llega a `status == "cancelled"`:

```python
from workiva import OperationCancelled

try:
    operation = client.wait(response).result()
except OperationCancelled as e:
    print(f"Cancelada: {e.operation.id}")
```

### `OperationTimeout`

Lanzada cuando el polling excede el timeout solicitado:

```python
from workiva import OperationTimeout

try:
    operation = client.wait(response).result(timeout=60)
except OperationTimeout as e:
    print(f"Timeout: operacion {e.operation_id}")
    print(f"Duracion maxima: {e.timeout}s")
    print(f"Ultimo estado conocido: {e.last_status}")
```

## Formato de mensajes de error

El SDK parsea automaticamente el body de error de la API y construye mensajes legibles:

```
# Formato Workiva: {"error": {"code": "...", "message": "..."}}
[404] NotFound: The requested resource was not found

# Formato alternativo: {"message": "..."}
[400] Invalid file ID format

# Sin body JSON
[500] API request failed
```

## Errores de red

Los errores de red de `httpx` se propagan directamente (no son `WorkivaAPIError`):

```python
import httpx

try:
    result = client.files.get_files()
except httpx.ConnectError:
    print("No se pudo conectar al servidor")
except httpx.TimeoutException:
    print("Timeout de conexion")
```

> El SDK reintenta automaticamente `ConnectError` y `TimeoutException` segun la configuracion de `RetryConfig`. Solo llegas al `except` si se agotan todos los reintentos.

## Ejemplo completo: try/except multinivel

```python
from workiva import (
    Workiva,
    WorkivaError,
    WorkivaAPIError,
    NotFoundError,
    BadRequestError,
    OperationFailed,
    OperationTimeout,
    TokenAcquisitionError,
)

with Workiva(client_id="...", client_secret="...") as client:
    try:
        # Copiar archivo (operacion de larga duracion)
        response = client.files.copy_file(
            file_id="abc",
            destination_container="ws-123",
        )

        # Esperar resultado
        operation = client.wait(response).result(timeout=300)
        print(f"Completado: {operation.resource_url}")

    except NotFoundError as e:
        # Archivo no encontrado
        print(f"Archivo no existe: {e}")

    except BadRequestError as e:
        # Parametros invalidos
        print(f"Request invalido: {e}")

    except OperationFailed as e:
        # La operacion se completo con error
        print(f"Operacion fallida: {e}")
        for detail in e.details:
            print(f"  {detail.message}")

    except OperationTimeout as e:
        # Timeout de polling
        print(f"Timeout despues de {e.timeout}s")

    except WorkivaError as e:
        # Cualquier error del SDK (API + token)
        print(f"Error SDK: {e}")
```

## Imports

Todas las excepciones se exportan desde el paquete raiz:

```python
from workiva import (
    # Base del SDK
    WorkivaError,
    # Errores de API
    WorkivaAPIError,
    BadRequestError,
    AuthenticationError,
    ForbiddenError,
    NotFoundError,
    ConflictError,
    RateLimitError,
    ServerError,
    # Errores de autenticacion
    TokenAcquisitionError,
    # Errores de polling
    OperationFailed,
    OperationCancelled,
    OperationTimeout,
)
```
