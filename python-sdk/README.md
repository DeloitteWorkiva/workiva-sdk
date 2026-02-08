# Workiva SDK

[![Python 3.10+](https://img.shields.io/pypi/pyversions/workiva)](https://pypi.org/project/workiva/)

**3 APIs. 17 namespaces. 350+ operaciones. Un solo cliente Python.**

[Documentación](https://deloitteworkiva.github.io/workiva-sdk/) · [Quick Start](https://deloitteworkiva.github.io/workiva-sdk/inicio-rapido/) · [API Reference](https://deloitteworkiva.github.io/workiva-sdk/referencia-api/) · [GitHub](https://github.com/DeloitteWorkiva/workiva-sdk)

---

## Instalación

```bash
pip install workiva
```

## Uso

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    # Platform API
    response = client.admin.get_workspaces()

    # Wdata API
    tables = client.wdata.get_tables()

    # Chains API
    chains = client.chains.list_chains()

    # Operaciones de larga duración
    response = client.files.copy_file(file_id="abc", file_copy=params)
    operation = client.wait(response).result(timeout=300)
```

## Características

- **Autenticación automática** — OAuth2 client_credentials con token caching
- **Operaciones de larga duración** — `client.wait(response).result(timeout=300)`
- **Paginación transparente** — `while response.next is not None: response = response.next()`
- **Sync + Async** — Cada método tiene su variante `_async`
- **Multi-región** — US, EU, APAC con `server_idx=0|1|2`
- **Reintentos con backoff** — `RetryConfig` global o per-operation
- **Tipado completo** — Modelos Pydantic

## APIs

| API | Namespace | Operaciones |
|-----|-----------|:-----------:|
| **Platform** | `files`, `documents`, `spreadsheets`, `admin`, `permissions`, `tasks`, `presentations`, `milestones`, `activities`, `content`, `graph`, `sustainability`, `test_forms`, `reports`, `operations`, `iam` | 280+ |
| **Chains** | `chains` | 20+ |
| **Wdata** | `wdata` | 56+ |

## Documentación

La documentación completa está en [GitHub Pages](https://deloitteworkiva.github.io/workiva-sdk/):
guías de autenticación, configuración, paginación, operaciones async, manejo de errores,
referencia de los 17 namespaces y guía para Workiva Scripting.

---

Este software es propiedad de Deloitte. Todos los derechos reservados.
