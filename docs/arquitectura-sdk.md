# Arquitectura del SDK

Como esta construido el SDK internamente. Para contribuidores y curiosos.

## Pipeline: Spec → SDK

```
oas/platform.yaml ─┐
oas/chains.yaml   ─┤→ generate_sdk.py
oas/wdata.yaml    ─┘         │
                    ┌─────────┴──────────┐
                    ▼                    ▼
        datamodel-code-generator    Jinja2 codegen
          (models/ per spec)      (_operations/ per tag)
```

### Paso 1: Modelos (`scripts/codegen/models.py`)

Cada spec se pasa individualmente a `datamodel-code-generator`:

```bash
datamodel-codegen --input oas/platform.yaml --output models/platform/
datamodel-codegen --input oas/chains.yaml   --output models/chains/
datamodel-codegen --input oas/wdata.yaml    --output models/wdata/
```

Genera modelos Pydantic v2 con soporte para:
- `Optional` fields con defaults
- Enums con `OpenEnumMeta` para forward-compatibility
- Self-referencing schemas (Section.parent, Slide.parent)

### Paso 2: Operaciones (`scripts/codegen/operations.py`)

Parsea cada spec, agrupa endpoints por tag OAS, y renderiza templates Jinja2:

```
platform.yaml → parse_spec() → {files: [get_files, copy_file, ...], admin: [...], ...}
                                    ↓
                            namespace.py.j2 → files.py, admin.py, ...
```

Cada operación genera un metodo sync + async con:
- Path params, query params, request body tipados
- Pagination helpers (`get_files_all()` con generators)
- Timeout override por operacion

### Paso 3: Validacion y formato

Todo codigo generado pasa por:
1. `ast.parse()` — valida syntax Python
2. `black` — formato consistente
3. `isort` — imports ordenados

## 3 APIs, 1 SDK

```python
client.files              # Platform API → https://api.app.wdesk.com
client.wdata              # Wdata API    → https://h.app.wdesk.com/s/wdata/...
client.chains             # Chains API   → https://h.app.wdesk.com/s/orchestration/...
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
| `_pagination.py` | `paginate()` / `paginate_async()` generators |
| `_config.py` | SDKConfig, RetryConfig |
| `_constants.py` | Region enum, SERVERS, API_VERSION |
| `client.py` | Clase `Workiva` con lazy-loading y `wait()` |
| `polling.py` | `OperationPoller` con sync/async polling |
| `exceptions.py` | `OperationFailed`, `OperationCancelled`, `OperationTimeout` |

### Generado (se regenera con `make generate`)

| Archivo | Notas |
|---------|-------|
| `_operations/*.py` (excepto `_base.py`) | Namespace classes con metodos sync+async |
| `models/platform/` | Pydantic models de Platform API |
| `models/chains/` | Pydantic models de Chains API |
| `models/wdata/` | Pydantic models de Wdata API |

## Autenticacion

El flujo de autenticacion usa `httpx.Auth`:

1. SDK se inicializa con `client_id` + `client_secret`
2. `OAuth2ClientCredentials.auth_flow()` intercepta cada request
3. Busca un token cacheado (cache global por `md5(client_id:secret)`)
4. Si no hay token valido, hace `POST /iam/v1/oauth2/token` (siempre sync)
5. Cachea el token con expiry buffer de 60s
6. Agrega `Authorization: Bearer {token}` al request
7. Si el server devuelve 401, invalida token y reintenta una vez

## Comandos utiles

```bash
# Pipeline completo
make all                  # Download → check → generate

# Forzar regeneracion
make force                # generate sin check

# Solo modelos o solo operaciones
make generate-models
make generate-operations

# Tests
make test                 # 70 tests (unit + integration)
make test-cov             # Coverage report

# Build
make build                # → dist/workiva-X.Y.Z-py3-none-any.whl
```

## Para contribuidores

### Modificar el SDK

1. **Codigo de infraestructura** → edita `_auth.py`, `_client.py`, `_retry.py`, etc.
2. **Codigo publico** → edita `client.py`, `polling.py`, `exceptions.py`
3. **Cambios en API generada** → modifica templates o codegen, luego `make generate`
4. **Tests** → `workiva-sdk/tests/` (fuera de `src/`, seguro)

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
