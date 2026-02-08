<div align="center">

# Workiva SDK

[![PyPI](https://img.shields.io/pypi/v/workiva?v=0.4.5)](https://pypi.org/project/workiva/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/workiva/)
[![Tests](https://img.shields.io/badge/tests-100%25-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)]()
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://deloitteworkiva.github.io/workiva-sdk/)

**3 APIs. 17 namespaces. 350+ operaciones. Un solo cliente Python.**

[Documentación](https://deloitteworkiva.github.io/workiva-sdk/) · [Quick Start](https://deloitteworkiva.github.io/workiva-sdk/inicio-rapido/) · [API Reference](https://deloitteworkiva.github.io/workiva-sdk/referencia-api/)

</div>

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

Async, paginación, reintentos, multi-región — todo documentado en las [guías](https://deloitteworkiva.github.io/workiva-sdk/).

## APIs

| | API | Namespace | Operaciones |
|---|-----|-----------|:-----------:|
| :gear: | **Platform** | `files`, `documents`, `spreadsheets`, `admin`, `permissions`, `tasks`, `presentations`, `milestones`, `activities`, `content`, `graph`, `sustainability`, `test_forms`, `reports`, `operations`, `iam` | 280+ |
| :link: | **Chains** | `chains` | 20+ |
| :bar_chart: | **Wdata** | `wdata` | 56+ |

## Desarrollo

```bash
make test           # 58 tests (unit + integration)
make force          # Regenerar SDK desde specs
make build          # Construir wheel
```

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para el setup completo y la guía de contribución.

---

<sub>Este software es propiedad de Deloitte. Todos los derechos reservados. El acceso público al repositorio no constituye una licencia de uso. Ver [LICENSE](LICENSE).</sub>
