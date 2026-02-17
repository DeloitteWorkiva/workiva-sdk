<div align="center">

# Workiva SDK

[![PyPI](https://img.shields.io/pypi/v/workiva?v=0.6.2)](https://pypi.org/project/workiva/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/workiva/)
[![Tests](https://img.shields.io/badge/tests-100%25-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)]()
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://deloitteworkiva.github.io/workiva-sdk/)

**3 APIs. 18 namespaces. 357 operaciones. Un solo cliente Python.**

[Documentación](https://deloitteworkiva.github.io/workiva-sdk/) · [Quick Start](https://deloitteworkiva.github.io/workiva-sdk/inicio-rapido/) · [API Reference](https://deloitteworkiva.github.io/workiva-sdk/referencia-api/)

</div>

---

## Instalación

```bash
uv add workiva
```

```bash
pip install workiva
```

## Uso

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    # Platform API — respuestas tipadas con modelos Pydantic
    result = client.files.get_files()
    for f in result.data:
        print(f.name)

    # Wdata API
    tables = client.wdata.get_tables()

    # Chains API
    chains = client.chains.get_chains()

    # Operaciones de larga duracion (202)
    response = client.files.copy_file(file_id="abc", body=params)
    operation = client.wait(response).result(timeout=300)
```

Respuestas tipadas, auto-paginacion transparente, reintentos, multi-region — todo documentado en las [guias](https://deloitteworkiva.github.io/workiva-sdk/).

## APIs

| | API | Namespaces | Operaciones |
|---|-----|-----------|:-----------:|
| :gear: | **Platform** | `files`, `documents`, `spreadsheets`, `admin`, `permissions`, `tasks`, `presentations`, `milestones`, `activities`, `content`, `graph`, `sustainability`, `test_forms`, `reports`, `operations`, `iam` | 280+ |
| :link: | **Chains** | `chains` | 29 |
| :bar_chart: | **Wdata** | `wdata` | 83 |

## Desarrollo

```bash
make test           # unit + integration tests
make force          # Regenerar SDK desde specs
make build          # Construir wheel
```

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para el setup completo y la guía de contribución.

---

<sub>Este software es propiedad de Deloitte. Todos los derechos reservados. El acceso público al repositorio no constituye una licencia de uso. Ver [LICENSE](LICENSE).</sub>
