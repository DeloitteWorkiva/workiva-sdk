# Workiva Python SDK

[![PyPI](https://img.shields.io/pypi/v/workiva)](https://pypi.org/project/workiva/)
[![Python 3.10+](https://img.shields.io/pypi/pyversions/workiva)](https://pypi.org/project/workiva/)
[![Tests](https://img.shields.io/badge/tests-58%20passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/hooks%20coverage-90%25-brightgreen)]()

SDK unificado de Python para las APIs de Workiva: **Platform**, **Chains** y **Wdata**.

Tres OpenAPI specs, un solo paquete tipado con autenticación automática, polling de operaciones, paginación y soporte sync/async.

## Instalación

```bash
pip install workiva
```

```bash
uv add workiva
```

## Quick Start

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # Listar workspaces
    response = client.admin.get_workspaces()
    for ws in response.result.data:
        print(ws.name)

    # Copiar archivo (operación de larga duración)
    response = client.files.copy_file(file_id="abc123", file_copy=params)
    operation = client.wait(response).result(timeout=300)
    print(f"Completado: {operation.resource_url}")
```

## APIs cubiertas

| API | Namespace | Descripción |
|-----|-----------|-------------|
| **Platform** | `client.files`, `client.documents`, `client.spreadsheets`, `client.admin`, `client.presentations`, `client.tasks`, `client.permissions`, `client.milestones`, `client.activities`, `client.content`, `client.graph`, `client.sustainability`, `client.test_forms`, `client.reports`, `client.operations`, `client.iam` | Archivos, documentos, hojas de cálculo, usuarios, permisos, tareas |
| **Chains** | `client.chains` | Automatización de flujos de trabajo |
| **Wdata** | `client.wdata` | Motor de datos: tablas, queries, imports/exports |

**17 namespaces, 350+ operaciones** con métodos sync y async.

## Características

- **Autenticación automática** — OAuth2 client_credentials con token caching global y refresco ante 401
- **Operaciones de larga duración** — `client.wait(response).result(timeout=300)` para polling automático de operaciones 202
- **Paginación transparente** — `while response.next is not None: response = response.next()` para todos los patrones
- **Sync + Async** — Cada método tiene su variante `_async`: `client.files.get_files_async()`
- **Multi-región** — US (default), EU, APAC con `server_idx=0|1|2`
- **Reintentos con backoff** — `RetryConfig` global o per-operation
- **Tipado completo** — Modelos Pydantic para requests y responses

## Uso asíncrono

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="...", client_secret="...") as client:
        files, workspaces = await asyncio.gather(
            client.files.get_files_async(),
            client.admin.get_workspaces_async(),
        )
        print(f"Archivos: {len(files.result.data)}")
        print(f"Workspaces: {len(workspaces.result.data)}")

asyncio.run(main())
```

## Manejo de errores

```python
from workiva import Workiva, OperationFailed, OperationTimeout
from workiva.errors import ErrorResponse, SDKBaseError

with Workiva(client_id="...", client_secret="...") as client:
    try:
        response = client.files.copy_file(file_id="abc", file_copy=params)
        operation = client.wait(response).result(timeout=300)
    except ErrorResponse as e:
        print(f"API Error [{e.data.code}]: {e.data.message}")
    except OperationFailed as e:
        print(f"Operación falló: {e.operation.id}")
    except OperationTimeout as e:
        print(f"Timeout: {e.timeout}s")
    except SDKBaseError as e:
        print(f"HTTP {e.status_code}: {e.message}")
```

## Documentación

| Guía | Descripción |
|------|-------------|
| [Inicio rápido](docs/inicio-rapido.md) | Instalación y primer request en 2 minutos |
| [Autenticación](docs/autenticacion.md) | OAuth2 client_credentials, token caching |
| [Configuración](docs/configuracion.md) | Servidores, timeouts, reintentos, logging |
| [Operaciones de larga duración](docs/operaciones-larga-duracion.md) | Patrón 202, polling con `wait()` |
| [Paginación](docs/paginacion.md) | 5 patrones, iteración con `.next()` |
| [Manejo de errores](docs/manejo-errores.md) | Jerarquía de excepciones, try/except |
| [Uso asíncrono](docs/uso-asincrono.md) | Métodos `_async`, `asyncio.gather` |
| [Referencia de API](docs/referencia-api/index.md) | Los 17 namespaces y sus operaciones |
| [Workiva Scripting](docs/workiva-scripting.md) | Uso en el módulo de scripting |
| [Arquitectura](docs/arquitectura-sdk.md) | Pipeline, hooks, regeneración |

## Desarrollo

### Requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) para gestión de dependencias
- [Speakeasy CLI](https://www.speakeasy.com/) para regeneración del SDK

### Pipeline de generación

```
platform.yaml ─┐
chains.yaml   ─┤→ prepare_specs.py → speakeasy merge → speakeasy generate → patch_sdk.py
wdata.yaml    ─┘
```

```bash
# Pipeline completo (descarga → detecta cambios → genera)
make all

# Forzar regeneración
make force

# Pasos individuales
make prepare        # Pre-procesar specs (conflictos, paginación, recursión)
make merge          # Speakeasy merge → merged.yaml
make generate       # Speakeasy generate + patch
```

### Tests

```bash
make test               # 58 tests (unit + integration)
make test-unit          # Solo unit tests
make test-integration   # Solo integration tests
make test-cov           # Coverage de _hooks (90%)

# Un test específico
cd python-sdk && uv run pytest tests/unit/test_polling_helpers.py -v
```

### Build

```bash
make build              # → python-sdk/dist/workiva-0.4.0-py3-none-any.whl
```

### Estructura del proyecto

```
.
├── Makefile                    # Build system
├── scripts/
│   ├── prepare_specs.py        # Pre-procesamiento de specs
│   └── patch_sdk.py            # Patches post-generación
├── platform.yaml               # OpenAPI spec: Platform API
├── chains.yaml                 # OpenAPI spec: Chains API
├── wdata.yaml                  # OpenAPI spec: Wdata API
├── docs/                       # Documentación en español
│   ├── index.md
│   ├── referencia-api/
│   └── ...
└── python-sdk/                 # SDK generado
    ├── src/workiva/
    │   ├── _hooks/             # Código custom (sobrevive regeneración)
    │   │   ├── client.py       # Clase Workiva con wait()
    │   │   ├── polling.py      # OperationPoller
    │   │   └── exceptions.py   # OperationFailed, Cancelled, Timeout
    │   ├── sdk.py              # Clase SDK base
    │   ├── files.py            # Namespace: archivos
    │   ├── wdata.py            # Namespace: Wdata
    │   ├── chains.py           # Namespace: Chains
    │   └── ...                 # 17 namespaces total
    └── tests/
        ├── unit/               # 38 unit tests
        └── integration/        # 20 integration tests
```

## Versión

- **SDK**: 0.4.0
- **Generador**: Speakeasy 2.803.3
- **Python**: 3.10+
