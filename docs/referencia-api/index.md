# Referencia de API

El SDK organiza las 357 operaciones en **18 namespaces**, accesibles como atributos del cliente. Los namespaces se cargan de forma lazy -- solo se importan cuando los usas.

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    # Platform (16 namespaces)
    client.activities
    client.admin
    client.content
    client.documents
    client.files
    client.graph
    client.iam
    client.milestones
    client.operations
    client.permissions
    client.presentations
    client.reports
    client.spreadsheets
    client.sustainability
    client.tasks
    client.test_forms

    # Chains (1 namespace)
    client.chains

    # Wdata (1 namespace)
    client.wdata
```

## Platform (16 namespaces)

| Namespace | Atributo | Operaciones | Descripcion |
|-----------|----------|-------------|-------------|
| [`Activities`](activities.md) | `client.activities` | 4 | Actividades de org y workspace |
| [`Admin`](admin.md) | `client.admin` | 33 | Usuarios, workspaces, grupos, roles |
| [`Content`](content.md) | `client.content` | 30 | Tablas, imagenes, links, rich text |
| [`Documents`](documents.md) | `client.documents` | 16 | Documentos y secciones |
| [`Files`](files.md) | `client.files` | 12 | Archivos y carpetas |
| [`Graph`](graph.md) | `client.graph` | 6 | Integrated Risk |
| [`IAM`](iam.md) | `client.iam` | 1 | Token OAuth2 |
| [`Milestones`](milestones.md) | `client.milestones` | 4 | Hitos |
| [`Operations`](operations.md) | `client.operations` | 26+ | Resultados de operaciones |
| [`Permissions`](permissions.md) | `client.permissions` | 2 | Permisos |
| [`Presentations`](presentations.md) | `client.presentations` | 12 | Presentaciones y slides |
| [`Reports`](reports.md) | `client.reports` | 1 | Reportes administrativos |
| [`Spreadsheets`](spreadsheets.md) | `client.spreadsheets` | 22 | Hojas de calculo |
| [`Sustainability`](sustainability.md) | `client.sustainability` | 24 | Metricas ESG |
| [`Tasks`](tasks.md) | `client.tasks` | 6 | Gestion de tareas |
| [`Test Forms`](test-forms.md) | `client.test_forms` | 29 | Formularios de prueba |

## Chains (1 namespace)

| Namespace | Atributo | Operaciones | Descripcion |
|-----------|----------|-------------|-------------|
| [`Chains`](chains.md) | `client.chains` | 29 | Cadenas, ejecuciones, usuarios, permisos, entornos, workspaces |

## Wdata (1 namespace)

| Namespace | Atributo | Operaciones | Descripcion |
|-----------|----------|-------------|-------------|
| [`Wdata`](wdata.md) | `client.wdata` | 83 | Tablas, queries, archivos, carpetas, conexiones, parametros, tags |

## Parametro comun

Todos los metodos aceptan un parametro opcional:

| Parametro | Tipo | Descripcion |
|-----------|------|-------------|
| `timeout` | `float \| None` | Timeout en segundos (sobreescribe el global) |

## Variantes async

Cada metodo tiene su variante async con sufijo `_async`:

```python
# Sync
result = client.files.get_files()

# Async
result = await client.files.get_files_async()
```

## Respuestas tipadas

Todas las operaciones que devuelven JSON retornan modelos Pydantic v2:

```python
# Devuelve FilesListResult (modelo tipado)
result = client.files.get_files()
# result.data es list[File]

# Devuelve File (modelo tipado)
file = client.files.get_file_by_id(file_id="abc")
# file.name, file.kind, etc.
```

Las operaciones que devuelven HTTP 202 (larga duracion) o 204 (sin contenido) retornan `httpx.Response`:

```python
# Devuelve httpx.Response (HTTP 202)
response = client.files.copy_file(file_id="abc", destination_container="folder-456")
# Usa client.wait(response).result() para obtener el resultado
```
