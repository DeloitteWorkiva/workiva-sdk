# Contribuir al Workiva SDK

Gracias por tu interés en contribuir. Esta guía explica cómo configurar el entorno, hacer cambios y enviar tu contribución.

## Requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) para gestión de dependencias
- [Speakeasy CLI](https://www.speakeasy.com/) para regeneración del SDK

## Setup del entorno

```bash
# Clonar el repositorio
git clone https://github.com/DeloitteWorkiva/workiva-sdk.git
cd workiva-sdk

# Instalar dependencias del SDK
cd workiva-sdk && uv sync && cd ..

# Verificar que todo funciona
make test
```

## Estructura del proyecto

Antes de hacer cambios, entiende qué puedes y qué NO puedes modificar:

### Seguro de editar (sobrevive regeneración)

| Ubicación | Descripción |
|-----------|-------------|
| `workiva-sdk/src/workiva/_hooks/client.py` | Clase `Workiva` con `wait()` |
| `workiva-sdk/src/workiva/_hooks/polling.py` | `OperationPoller` |
| `workiva-sdk/src/workiva/_hooks/exceptions.py` | Excepciones custom |
| `workiva-sdk/tests/` | Tests unitarios e integración |
| `scripts/` | Pipeline de pre/post procesamiento |
| `docs/` | Documentación |
| `Makefile` | Build system |
| `gen.yaml` | Configuración de Speakeasy |

### NO editar (se regenera con `make force`)

Todo en `workiva-sdk/src/workiva/` excepto `_hooks/` se regenera automáticamente. Cualquier cambio manual se pierde.

Si necesitas modificar código generado, el cambio debe ir en:
- `scripts/prepare_specs.py` — para cambios en el OpenAPI spec antes de generar
- `scripts/patch_sdk.py` — para patches post-generación
- `gen.yaml` — para configuración del generador

## Flujo de contribución

### 1. Crea un branch

```bash
git checkout -b feat/mi-cambio
```

### 2. Haz tus cambios

- **Código custom** → edita en `_hooks/`
- **Cambios en API** → modifica `prepare_specs.py`, luego `make force`
- **Configuración** → edita `gen.yaml`, luego `make force`
- **Tests** → `workiva-sdk/tests/`
- **Docs** → `docs/`

### 3. Ejecuta los tests

```bash
make test          # Los 58 tests deben pasar
make test-cov      # Verifica cobertura de _hooks
```

### 4. Commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add support for batch operations
fix: handle 429 rate limit in polling
docs: add retry configuration examples
chore: update Speakeasy to v2.900
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
cd workiva-sdk && uv run pytest tests/unit/test_polling_helpers.py -v
```

### Escribir tests

- **Unit tests** → `workiva-sdk/tests/unit/` — mockean el SDK con `MagicMock`/`AsyncMock`
- **Integration tests** → `workiva-sdk/tests/integration/` — usan `httpx.MockTransport`

Consideraciones:

- `conftest.py` limpia `ClientCredentialsHook._sessions` entre tests (autouse fixture)
- Tests async necesitan AMBOS clientes: sync (para OAuth) y async (para API calls)
- Los defaults de `OperationDetail()` son instancias `Unset()`, no `None`

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
pip install mkdocs-material
mkdocs serve
```

Abre `http://127.0.0.1:8000` para ver los cambios en tiempo real.

## Preguntas

Si tienes dudas, abre un [issue](https://github.com/DeloitteWorkiva/workiva-sdk/issues).
