# Contribuir al Workiva SDK

Gracias por tu interés en contribuir. Esta guía explica cómo configurar el entorno, hacer cambios y enviar tu contribución.

## Requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) para gestión de dependencias

## Setup del entorno

```bash
# Clonar el repositorio
git clone https://github.com/DeloitteWorkiva/workiva-sdk.git
cd workiva-sdk

# Instalar dependencias del SDK
cd workiva-sdk && uv sync && cd ..

# Instalar dependencias de codegen (si vas a regenerar)
cd workiva-sdk && uv sync --group codegen && cd ..

# Verificar que todo funciona
make test
```

## Estructura del proyecto

Antes de hacer cambios, entiende qué puedes y qué NO puedes modificar:

### Seguro de editar

| Ubicación | Descripción |
|-----------|-------------|
| `workiva-sdk/src/workiva/client.py` | Clase `Workiva` con `wait()` |
| `workiva-sdk/src/workiva/polling.py` | `OperationPoller` |
| `workiva-sdk/src/workiva/exceptions.py` | Excepciones custom |
| `workiva-sdk/src/workiva/_auth.py` | OAuth2 client credentials |
| `workiva-sdk/src/workiva/_client.py` | BaseClient (httpx wrapper) |
| `workiva-sdk/src/workiva/_retry.py` | RetryTransport |
| `workiva-sdk/src/workiva/_errors.py` | WorkivaAPIError hierarchy |
| `workiva-sdk/src/workiva/_pagination.py` | Pagination generators |
| `workiva-sdk/src/workiva/_config.py` | SDKConfig |
| `workiva-sdk/src/workiva/_constants.py` | Regions, servers, API version |
| `workiva-sdk/tests/` | Tests unitarios e integración |
| `scripts/` | Pipeline de codegen |
| `Makefile` | Build system |

### NO editar (se regenera con `make generate`)

- `workiva-sdk/src/workiva/_operations/*.py` (excepto `_base.py`)
- `workiva-sdk/src/workiva/models/platform/`, `models/chains/`, `models/wdata/`

Si necesitas modificar código generado, el cambio debe ir en:
- `scripts/codegen/templates/*.j2` — para cambios en las templates Jinja2
- `scripts/codegen/operations.py` — para cambios en parsing de OAS specs
- `scripts/codegen/models.py` — para cambios en generación de modelos

## Flujo de contribución

### 1. Crea un branch

```bash
git checkout -b feat/mi-cambio
```

### 2. Haz tus cambios

- **Código de infraestructura** → edita `_auth.py`, `_client.py`, `_retry.py`, etc.
- **Código público** → edita `client.py`, `polling.py`, `exceptions.py`
- **Cambios en API generada** → modifica templates o codegen, luego `make generate`
- **Tests** → `workiva-sdk/tests/`

### 3. Ejecuta los tests

```bash
make test          # Todos los tests deben pasar
make test-cov      # Verifica cobertura
```

### 4. Commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add support for batch operations
fix: handle 429 rate limit in polling
docs: add retry configuration examples
chore: update codegen templates
```

### 5. Abre un Pull Request

- Describe QUÉ cambiaste y POR QUÉ
- Referencia issues relacionados
- Asegúrate de que CI pase (tests + build)

## Tests

### Ejecutar tests

```bash
make test               # Todos (unit + integration)
make test-unit          # Solo unit
make test-integration   # Solo integration
make test-cov           # Con cobertura

# Un test específico
cd workiva-sdk && uv run python -m pytest tests/unit/test_polling_helpers.py -v
```

### Escribir tests

- **Unit tests** → `workiva-sdk/tests/unit/` — mockean el SDK con `MagicMock`/`AsyncMock`
- **Integration tests** → `workiva-sdk/tests/integration/` — usan `httpx.MockTransport`

Consideraciones:

- `conftest.py` limpia `OAuth2ClientCredentials._cache` entre tests (autouse fixture)
- Tests async necesitan AMBOS clientes: sync (para OAuth) y async (para API calls)

## Regeneración del SDK

Si Workiva publica un spec actualizado:

```bash
# Pipeline completo (descarga → detecta cambios → genera)
make all

# O forzar regeneración
make force
```

Después de regenerar, siempre:

1. Ejecuta `make test` para verificar que nada se rompió
2. Revisa el diff de código generado
3. Actualiza tests si hay endpoints nuevos o cambios de firma

## Documentación

La documentación vive en `docs/` y se despliega automáticamente a [GitHub Pages](https://deloitteworkiva.github.io/workiva-sdk/) con MkDocs Material.

```bash
# Preview local
uv run mkdocs serve
```

Abre `http://127.0.0.1:8000` para ver los cambios en tiempo real.

## Preguntas

Si tienes dudas, abre un [issue](https://github.com/DeloitteWorkiva/workiva-sdk/issues).
