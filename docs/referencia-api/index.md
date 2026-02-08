# Referencia de API

El SDK organiza las operaciones en 17 namespaces, accesibles como propiedades del cliente.

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    client.activities       # Actividades de organización/workspace
    client.admin            # Usuarios, workspaces, grupos, roles
    client.chains           # Automatización de flujos
    client.content          # Tablas, imágenes, links, rich text
    client.documents        # Documentos y secciones
    client.files            # Archivos y carpetas
    client.graph            # Integrated Risk (registros, tipos)
    client.iam              # Tokens OAuth2
    client.milestones       # Hitos
    client.operations       # Estado de operaciones asíncronas
    client.permissions      # Permisos
    client.presentations    # Presentaciones y slides
    client.reports          # Reportes administrativos
    client.spreadsheets     # Hojas de cálculo y sheets
    client.sustainability   # Métricas ESG
    client.tasks            # Tareas
    client.test_forms       # Formularios de prueba
    client.wdata            # Wdata: queries, tablas, imports
```

## Resumen por namespace

| Namespace | API | Operaciones | Descripción |
|-----------|-----|-------------|-------------|
| [`activities`](activities.md) | Platform | 4 | Actividades de org y workspace |
| [`admin`](admin.md) | Platform | 33 | Usuarios, workspaces, grupos, roles |
| [`chains`](chains.md) | Chains | 24 | Automatización de cadenas |
| [`content`](content.md) | Platform | 30 | Tablas, imágenes, links, rich text |
| [`documents`](documents.md) | Platform | 16 | Documentos y secciones |
| [`files`](files.md) | Platform | 12 | Archivos y carpetas |
| [`graph`](graph.md) | Platform | 6 | Integrated Risk |
| [`iam`](iam.md) | Platform | 1 | Token OAuth2 |
| [`milestones`](milestones.md) | Platform | 4 | Hitos |
| [`operations`](operations.md) | Platform | 26+ | Resultados de operaciones |
| [`permissions`](permissions.md) | Platform | 2 | Permisos |
| [`presentations`](presentations.md) | Platform | 12 | Presentaciones y slides |
| [`reports`](reports.md) | Platform | 1 | Reportes administrativos |
| [`spreadsheets`](spreadsheets.md) | Platform | 22 | Hojas de cálculo |
| [`sustainability`](sustainability.md) | Platform | 24 | Métricas ESG |
| [`tasks`](tasks.md) | Platform | 6 | Gestión de tareas |
| [`test_forms`](test-forms.md) | Platform | 29 | Formularios de prueba |
| [`wdata`](wdata.md) | Wdata | 56 | Queries, tablas, imports/exports |

## Parámetros comunes

Todos los métodos aceptan estos parámetros opcionales:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `retries` | `RetryConfig` | Sobreescribir config de reintentos |
| `server_url` | `str` | Sobreescribir URL del servidor |
| `timeout_ms` | `int` | Timeout en milisegundos |
| `http_headers` | `dict[str, str]` | Headers HTTP adicionales |

## Variantes async

Cada método tiene su variante async con sufijo `_async`:

```python
# Sync
response = client.files.get_files()

# Async
response = await client.files.get_files_async()
```
