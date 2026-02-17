# Arquitectura del SDK

Como esta construido el SDK internamente. Para contribuidores y curiosos.

## Pipeline: Spec -> SDK

```
oas/platform.yaml -┐
oas/chains.yaml   -┤-> generate_sdk.py
oas/wdata.yaml    -┘         |
                    ┌---------┴----------┐
                    v                    v
        datamodel-code-generator    Jinja2 codegen
         (models/*.py per spec)   (_operations/ per tag)
```

### Paso 1: Modelos (`scripts/codegen/models.py`)

Cada spec se pasa individualmente a `datamodel-code-generator`. Genera un archivo por API:

- `models/platform.py` (~10k lineas)
- `models/chains.py` (~760 lineas)
- `models/wdata.py` (~2.2k lineas)

Genera modelos Pydantic v2 con soporte para:
- `Optional` fields con defaults
- Enums con `OpenEnumMeta` para forward-compatibility
- Self-referencing schemas (Section.parent, Slide.parent)

### Paso 2: Operaciones (`scripts/codegen/operations.py`)

Parsea cada spec, agrupa endpoints por tag OAS, y renderiza templates Jinja2:

```
platform.yaml -> parse_spec() -> {files: [get_files, copy_file, ...], admin: [...], ...}
                                    |
                            namespace.py.j2 -> files.py, admin.py, ...
```

Cada operacion genera un metodo sync + async con:
- Path params, query params, header params, request body tipados
- Auto-paginacion transparente via `paginate_all()` / `paginate_all_async()`
- Respuestas tipadas con `Model.model_validate(response.json())`
- Timeout override por operacion
- Docstrings completos (Args, Returns, Raises, Note)

### 3 code paths en los templates

| Tipo | Return type | Ejemplo |
|------|-------------|---------|
| JSON + paginacion | Modelo Pydantic | `get_files() -> FilesListResult` |
| JSON sin paginacion | Modelo Pydantic | `get_file_by_id() -> File` |
| 202/204 (sin body JSON) | `httpx.Response` | `copy_file() -> httpx.Response` |

### Paso 3: Validacion y formato

Todo codigo generado pasa por:
1. `ast.parse()` -- valida syntax Python
2. `black` -- formato consistente
3. `isort` -- imports ordenados

## 3 APIs, 18 namespaces

```python
# Platform (16 namespaces)
client.files              # -> https://api.{region}.wdesk.com
client.admin
client.documents
# ... 13 mas

# Chains (1 namespace)
client.chains             # -> https://h.{region}.wdesk.com/s/wdata/oc/api

# Wdata (1 namespace)
client.wdata              # -> https://h.{region}.wdesk.com/s/wdata/prep
```

Cada namespace tiene un `_api: _API` que se resuelve al base URL correcto segun la region configurada.

## Codigo generado vs custom

### Infraestructura (hand-written)

| Archivo | Descripcion |
|---------|-------------|
| `_auth.py` | OAuth2 client_credentials via `httpx.Auth` |
| `_client.py` | BaseClient (httpx wrapper con retry, auth, headers) |
| `_retry.py` | RetryTransport + AsyncRetryTransport |
| `_errors.py` | WorkivaAPIError hierarchy |
| `_pagination.py` | `paginate_all()` / `paginate_all_async()` con max_pages guard |
| `_config.py` | SDKConfig, RetryConfig |
| `_constants.py` | Region enum, SERVERS, API_VERSION |
| `client.py` | Clase `Workiva` con lazy-loading y `wait()` |
| `polling.py` | `OperationPoller` con sync/async polling, typed `Operation` |
| `exceptions.py` | `OperationFailed`, `OperationCancelled`, `OperationTimeout` |

### Generado (se regenera con `make generate`)

| Archivo | Notas |
|---------|-------|
| `_operations/*.py` (excepto `_base.py`) | 18 namespace classes, 357 operaciones sync+async |
| `models/platform.py` | Pydantic models de Platform API (~10k lineas) |
| `models/chains.py` | Pydantic models de Chains API |
| `models/wdata.py` | Pydantic models de Wdata API |

## Autenticacion

El flujo de autenticacion usa `httpx.Auth`:

1. SDK se inicializa con `client_id` + `client_secret`
2. `OAuth2ClientCredentials.sync_auth_flow()` / `async_auth_flow()` intercepta cada request
3. Busca un token cacheado (cache global por `md5(client_id:secret)`)
4. Si no hay token valido, hace `POST /oauth2/token` (siempre sync, en async via `asyncio.to_thread`)
5. Cachea el token con expiry buffer de 60s
6. Agrega `Authorization: Bearer {token}` al request
7. Si el server devuelve 401, invalida token y reintenta una vez

## Paginacion

5 patrones de paginacion manejados por `paginate_all()`:

1. **Platform `@nextLink`**: Cursor `$next` en query params
2. **Platform JSON:API**: URL completa en `links.next`
3. **Chains cursor**: Campo `data.cursor` en response body
4. **Chains page**: Page offset/limit
5. **Wdata cursor**: Campo `cursor` en response body

El paginator itera todas las paginas a nivel de dict, acumula items, y retorna el body final con todos los items mergeados. Un solo `Model.model_validate(body)` al final.

## Comandos utiles

```bash
# Pipeline completo
make all                  # Download -> check -> generate

# Forzar regeneracion
make force                # generate sin check

# Solo modelos o solo operaciones
make generate-models
make generate-operations

# Tests
make test                 # 184 tests (unit + integration)
make test-cov             # Coverage report

# Build
make build                # -> dist/workiva-X.Y.Z-py3-none-any.whl
```

## Para contribuidores

### Modificar el SDK

1. **Codigo de infraestructura** -> edita `_auth.py`, `_client.py`, `_retry.py`, etc.
2. **Codigo publico** -> edita `client.py`, `polling.py`, `exceptions.py`
3. **Cambios en API generada** -> modifica templates o codegen, luego `make generate`
4. **Tests** -> `tests/` (fuera de `src/`, seguro)

### Agregar un nuevo endpoint

Si Workiva agrega un nuevo endpoint:

1. Descarga el spec actualizado a `oas/`
2. Ejecuta `make generate` (regenera modelos + operaciones)
3. Los nuevos metodos aparecen automaticamente en el SDK

### Agregar una nueva API

1. Agrega el spec `.yaml` a `oas/`
2. Agrega la entrada en `API_SPECS` de `scripts/generate_sdk.py`
3. Agrega la entrada en `API_MODEL_TARGETS` de `scripts/codegen/models.py`
4. `make generate`
