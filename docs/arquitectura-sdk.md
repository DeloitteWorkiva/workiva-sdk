# Arquitectura del SDK

Cómo está construido el SDK internamente. Para contribuidores y curiosos.

## Pipeline: Spec → SDK

```
platform.yaml ─┐
chains.yaml   ─┤→ prepare_specs.py → *_processed.yaml
wdata.yaml    ─┘         │
                          ▼
                  speakeasy merge → merged.yaml
                          │
                          ▼
                speakeasy generate → python-sdk/src/workiva/
                          │
                          ▼
                   patch_sdk.py → __init__.py exports + README cleanup
```

### Paso 1: Pre-procesamiento (`scripts/prepare_specs.py`)

Speakeasy necesita un solo OpenAPI spec, pero tenemos 3 APIs con conflictos de nombres. `prepare_specs.py` resuelve:

| Problema | Solución |
|----------|----------|
| Schemas duplicados (Activity, Permission, User, Workspace) | Renombrar con prefijo `Chain` |
| OperationIds duplicados (getWorkspaces, getFiles, importFile) | Prefijo per-API + `x-speakeasy-name-override` |
| Recursión de schemas (Section.parent, Slide.parent) | Reemplazar `allOf` con objetos inline |
| Multi-base-URL (3 APIs, 3 servidores) | Path-level `servers` injection |
| Namespaces de SDK | `x-speakeasy-group` por API |
| Paginación (89 endpoints, 5 patrones) | `x-speakeasy-pagination` extensions |

### Paso 2: Merge (`speakeasy merge`)

```bash
speakeasy merge \
  -s chains_processed.yaml \
  -s wdata_processed.yaml \
  -s platform_processed.yaml \  # ÚLTIMO: sus servers globales ganan
  -o merged.yaml
```

> El orden importa. El ÚLTIMO spec define los servers globales. Platform va último porque queremos US/EU/APAC como servers por defecto.

### Paso 3: Generación (`speakeasy generate`)

```bash
speakeasy generate sdk --lang python --schema merged.yaml --out python-sdk
```

Speakeasy genera:
- 17 namespace modules (`files.py`, `admin.py`, `wdata.py`, etc.)
- Modelos Pydantic para request/response
- Hooks de autenticación (OAuth2 client_credentials)
- Paginación automática con `.next()`
- Métodos sync + async para cada operación

### Paso 4: Patch (`scripts/patch_sdk.py`)

Post-generación idempotente:
1. **`__init__.py`** — agrega exports de `Workiva`, `OperationPoller`, `OperationFailed`, etc.
2. **`README.md`** — remueve scaffolding de Speakeasy, agrega instrucciones reales

## 3 APIs, 1 SDK

```python
client.files              # Platform API → https://api.app.wdesk.com
client.wdata              # Wdata API    → https://h.app.wdesk.com/s/wdata/...
client.chains             # Chains API   → https://h.app.wdesk.com/s/orchestration/...
```

Cada operación se enruta al servidor correcto gracias a path-level `servers` inyectados en el pre-procesamiento. El usuario no necesita saber qué API está detrás.

## Código generado vs custom

### Sobrevive `make force`

| Archivo | Descripción |
|---------|-------------|
| `_hooks/client.py` | Clase `Workiva(SDK)` con `wait()` |
| `_hooks/polling.py` | `OperationPoller` con sync/async polling |
| `_hooks/exceptions.py` | `OperationFailed`, `OperationCancelled`, `OperationTimeout` |
| `_hooks/registration.py` | Registro de hooks (generado una vez, luego libre) |
| `gen.yaml` | Configuración de Speakeasy |
| `scripts/` | Pipeline scripts |
| `tests/` | Tests (fuera de `src/`) |
| `Makefile` | Build system |

### Se regenera con `make force`

| Archivo | Notas |
|---------|-------|
| Todos los `.py` en `src/workiva/` (excepto `_hooks/`) | Modelos, namespaces, utils |
| `_hooks/clientcredentials.py` | Hook de OAuth2 |
| `_hooks/sdkhooks.py` | Orquestación de hooks |
| `_hooks/types.py` | Interfaces de hooks |
| `__init__.py` | Regenerado, luego patcheado |
| `pyproject.toml` | Regenerado desde `gen.yaml` |
| `README.md` | Regenerado, luego patcheado |

## Sistema de hooks

Speakeasy genera un sistema de hooks que permite interceptar el ciclo de vida HTTP:

```
SDKInit → BeforeRequest → [HTTP Request] → AfterSuccess / AfterError
```

### Hooks registrados

1. **`ClientCredentialsHook`** (generado) — obtiene y cachea tokens OAuth2
2. **`OAuth2Scopes`** (generado) — define scopes por operación

Los hooks se registran en `_hooks/registration.py`:

```python
def init_hooks(base_url, hooks):
    cc_hook = ClientCredentialsHook()
    hooks.register_sdk_init_hook(cc_hook)
    hooks.register_before_request_hook(cc_hook)
    hooks.register_after_error_hook(cc_hook)
```

## Autenticación interna

El flujo de autenticación:

1. SDK se inicializa con `Security(client_id=..., client_secret=...)`
2. `ClientCredentialsHook.before_request()` intercepta cada request
3. Busca un token cacheado para esas credenciales + scopes
4. Si no hay token válido, hace `POST /iam/v1/oauth2/token` (sync)
5. Cachea el token en `_sessions` (ClassVar global)
6. Agrega `Authorization: Bearer {token}` al request
7. Si el server devuelve 401, `after_error()` invalida el token

```
_sessions = {
    "md5(client_id:client_secret)": {
        "scope1 scope2": Session(token="...", expires_at=1234567890),
    }
}
```

## Configuración (`gen.yaml`)

Campos clave que controlan la generación:

```yaml
python:
  version: 0.4.0
  packageName: workiva
  asyncMode: both              # Genera sync + async
  asyncPaginationSep2025: true # Paginación async
  allOfMergeStrategy: shallowMerge  # Para el spec mergeado
  additionalDependencies:      # → pyproject.toml
    httpx: ">=0.28.1"
```

## Comandos útiles

```bash
# Pipeline completo
make all                  # Download → check → prepare → merge → generate → patch

# Forzar regeneración
make force                # prepare → merge → generate → patch (sin check)

# Solo un paso
make prepare              # Pre-procesar specs
make merge                # Speakeasy merge
make generate             # Speakeasy generate + patch

# Tests
make test                 # 58 tests (unit + integration)
make test-cov             # Coverage report

# Build
make build                # → dist/workiva-0.4.0-py3-none-any.whl
```

## Para contribuidores

### Modificar el SDK

1. **Código custom** → edita directamente en `_hooks/` (sobrevive regeneración)
2. **Cambios en API** → modifica `prepare_specs.py`, luego `make force`
3. **Nueva configuración** → edita `gen.yaml`, luego `make force`
4. **Tests** → `python-sdk/tests/` (fuera de `src/`, seguro)

### Agregar un nuevo endpoint

Si Workiva agrega un nuevo endpoint:

1. Descarga el spec actualizado
2. Ejecuta `make all` (detecta cambios y regenera)
3. Los nuevos métodos aparecen automáticamente en el SDK

### Agregar una nueva API

1. Agrega el spec a `prepare_specs.py` (resolución de conflictos)
2. Agrega la línea en el `Makefile` (merge command)
3. `make force`
