<div align="center">

# Workiva SDK

[![PyPI](https://img.shields.io/pypi/v/workiva)](https://pypi.org/project/workiva/)
[![Python 3.10+](https://img.shields.io/pypi/pyversions/workiva)](https://pypi.org/project/workiva/)
[![Tests](https://img.shields.io/badge/tests-58%20passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/hooks%20coverage-90%25-brightgreen)]()
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://deloitteworkiva.github.io/workiva-sdk/)

SDK unificado de Python para las APIs de Workiva: **Platform**, **Chains** y **Wdata**.

Tres OpenAPI specs, un solo paquete tipado con autenticación automática, polling de operaciones, paginación y soporte sync/async.

[Documentación](https://deloitteworkiva.github.io/workiva-sdk/) · [Inicio rápido](https://deloitteworkiva.github.io/workiva-sdk/inicio-rapido/) · [Referencia de API](https://deloitteworkiva.github.io/workiva-sdk/referencia-api/)

</div>

> **Aviso legal:** Este software es propiedad de Deloitte. Todos los derechos reservados. El acceso público al repositorio no constituye una licencia de uso. Consulta el archivo [LICENSE](LICENSE) para más información.

---

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
- **Operaciones de larga duración** — `client.wait(response).result(timeout=300)` para polling automático
- **Paginación transparente** — `while response.next is not None: response = response.next()`
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

La documentación completa está disponible en **[GitHub Pages](https://deloitteworkiva.github.io/workiva-sdk/)**.

| Guía | Descripción |
|------|-------------|
| [Inicio rápido](https://deloitteworkiva.github.io/workiva-sdk/inicio-rapido/) | Instalación y primer request en 2 minutos |
| [Autenticación](https://deloitteworkiva.github.io/workiva-sdk/autenticacion/) | OAuth2 client_credentials, token caching |
| [Configuración](https://deloitteworkiva.github.io/workiva-sdk/configuracion/) | Servidores, timeouts, reintentos, logging |
| [Operaciones de larga duración](https://deloitteworkiva.github.io/workiva-sdk/operaciones-larga-duracion/) | Patrón 202, polling con `wait()` |
| [Paginación](https://deloitteworkiva.github.io/workiva-sdk/paginacion/) | 5 patrones, iteración con `.next()` |
| [Manejo de errores](https://deloitteworkiva.github.io/workiva-sdk/manejo-errores/) | Jerarquía de excepciones, try/except |
| [Uso asíncrono](https://deloitteworkiva.github.io/workiva-sdk/uso-asincrono/) | Métodos `_async`, `asyncio.gather` |
| [Referencia de API](https://deloitteworkiva.github.io/workiva-sdk/referencia-api/) | Los 17 namespaces y sus operaciones |
| [Workiva Scripting](https://deloitteworkiva.github.io/workiva-sdk/workiva-scripting/) | Uso en el módulo de scripting |
| [Arquitectura](https://deloitteworkiva.github.io/workiva-sdk/arquitectura-sdk/) | Pipeline, hooks, regeneración |

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
make all                # Pipeline completo (descarga → detecta cambios → genera)
make force              # Forzar regeneración
make prepare            # Pre-procesar specs
make merge              # Speakeasy merge → merged.yaml
make generate           # Speakeasy generate + patch
```

### Tests

```bash
make test               # 58 tests (unit + integration)
make test-unit          # Solo unit tests
make test-integration   # Solo integration tests
make test-cov           # Coverage de _hooks (90%)
```

### Build

```bash
make build              # → python-sdk/dist/workiva-0.4.0-py3-none-any.whl
```

### Estructura del proyecto

```
.
├── Makefile                    # Build system
├── mkdocs.yml                  # Documentación (MkDocs Material)
├── scripts/
│   ├── prepare_specs.py        # Pre-procesamiento de specs
│   └── patch_sdk.py            # Patches post-generación
├── platform.yaml               # OpenAPI spec: Platform API
├── chains.yaml                 # OpenAPI spec: Chains API
├── wdata.yaml                  # OpenAPI spec: Wdata API
├── docs/                       # Documentación en español
└── python-sdk/                 # SDK generado
    ├── src/workiva/
    │   ├── _hooks/             # Código custom (sobrevive regeneración)
    │   ├── sdk.py              # Clase SDK base
    │   └── ...                 # 17 namespaces total
    └── tests/
        ├── unit/               # 38 unit tests
        └── integration/        # 20 integration tests
```

## Versión

- **SDK**: 0.4.0
- **Generador**: Speakeasy 2.803.3
- **Python**: 3.10+
