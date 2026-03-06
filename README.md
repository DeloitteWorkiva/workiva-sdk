<div align="center">

# Workiva SDK

[![PyPI](https://img.shields.io/pypi/v/workiva?v=0.6.9)](https://pypi.org/project/workiva/)
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

    # Operaciones de larga duracion (202) — modo simple
    operation = client.files.copy_file(
        file_id="abc", destination_container="folder-123", wait=True
    )

    # O con polling manual
    response = client.files.copy_file(file_id="abc", destination_container="folder-123")
    operation = client.wait(response).result(timeout=300)
```

Respuestas tipadas, auto-paginacion transparente, reintentos, multi-region — todo documentado en las [guias](https://deloitteworkiva.github.io/workiva-sdk/).

## Reintentos y Rate Limiting

El SDK incluye reintentos automaticos con backoff exponencial. Funciona sin configuracion adicional:

```python
from workiva import Workiva, RetryConfig

# Configuracion por defecto (sin cambios necesarios)
# 5 reintentos, backoff exponencial, 429/5xx automaticos
with Workiva(client_id="...", client_secret="...") as client:
    client.sustainability.create_metric(...)  # reintentos automaticos en 429

# Configuracion personalizada para operaciones pesadas
with Workiva(
    client_id="...",
    client_secret="...",
    retry=RetryConfig(
        max_retries=10,
        max_interval_ms=60_000,
        max_elapsed_ms=300_000,
    ),
) as client:
    ...
```

### RetryConfig por defecto

| Parametro | Default | Descripcion |
|-----------|---------|-------------|
| `max_retries` | 5 | Numero maximo de reintentos |
| `initial_interval_ms` | 500 | Intervalo inicial entre reintentos (ms) |
| `max_interval_ms` | 30,000 | Intervalo maximo entre reintentos (ms) |
| `exponent` | 1.5 | Factor de backoff exponencial |
| `max_elapsed_ms` | 120,000 | Tiempo maximo total de reintentos (ms) |
| `status_codes` | 429, 500, 502, 503, 504 | Codigos HTTP que disparan reintento |

### Excepciones tipadas

```python
from workiva import RateLimitError, WorkivaAPIError

try:
    client.sustainability.create_metric(...)
except RateLimitError as e:
    # 429 — solo se lanza si se agotan TODOS los reintentos
    print(f"Rate limited. Retry after {e.retry_after}s")
except WorkivaAPIError as e:
    print(f"API error {e.status_code}: {e}")
```

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
