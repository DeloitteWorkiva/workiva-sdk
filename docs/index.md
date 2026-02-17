# Workiva SDK

[![PyPI](https://img.shields.io/pypi/v/workiva)](https://pypi.org/project/workiva/)
[![Python](https://img.shields.io/pypi/pyversions/workiva)](https://pypi.org/project/workiva/)

SDK unificado para las APIs de Workiva: **Platform**, **Chains** y **Wdata**, en un solo paquete Python.

## Que es este SDK?

El SDK de Workiva proporciona un **unico cliente Python tipado** (`Workiva`) para interactuar con las tres APIs de la plataforma Workiva. Todas las respuestas son modelos Pydantic v2 con autocompletado y validacion de tipos. La paginacion es transparente, la autenticacion es automatica y el ruteo multi-API se resuelve internamente.

**Cifras clave:** 3 APIs, 18 namespaces, 357 operaciones.

## Requisitos

- **Python 3.10+**
- Credenciales OAuth2 (`client_id` y `client_secret`) de Workiva

## Ejemplo rapido

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # Listar archivos — la paginacion es transparente
    result = client.files.get_files()
    for file in result.data:
        print(f"{file.name} ({file.kind})")

    # Copiar un archivo (operacion de larga duracion)
    response = client.files.copy_file(file_id="abc123", destination_container="folder-456")
    operation = client.wait(response).result(timeout=300)
    print(f"Operacion completada: {operation.resource_url}")
```

> **Nota:** `result.data` contiene TODOS los items de todas las paginas. El SDK pagina automaticamente.

## Tabla de contenidos

### Guias principales

1. [Inicio rapido](inicio-rapido.md) -- Instalacion y primer request en 2 minutos
2. [Autenticacion](autenticacion.md) -- OAuth2 client_credentials, token caching, thread safety
3. [Configuracion](configuracion.md) -- Regiones, timeouts, reintentos, clientes HTTP custom
4. [Operaciones de larga duracion](operaciones-larga-duracion.md) -- Patron 202, polling, `wait()`
5. [Paginacion](paginacion.md) -- 5 patrones, auto-paginacion transparente
6. [Manejo de errores](manejo-errores.md) -- Jerarquia de excepciones, try/except
7. [Uso asincrono](uso-asincrono.md) -- Metodos `_async`, concurrencia con asyncio

### Referencia de API

8. [Referencia de API](referencia-api/index.md) -- Los 18 namespaces y sus operaciones

### Guias especializadas

9. [Workiva Scripting](workiva-scripting.md) -- Uso del SDK en el modulo de scripting
10. [Arquitectura del SDK](arquitectura-sdk.md) -- Como esta construido internamente

## Namespaces por API

### Platform (16 namespaces)

| Namespace | Atributo del cliente | Ejemplo |
|-----------|---------------------|---------|
| Activities | `client.activities` | `client.activities.get_activities(...)` |
| Admin | `client.admin` | `client.admin.get_workspaces(...)` |
| Content | `client.content` | `client.content.get_content(...)` |
| Documents | `client.documents` | `client.documents.get_document(...)` |
| Files | `client.files` | `client.files.get_files()` |
| Graph | `client.graph` | `client.graph.get_graph(...)` |
| IAM | `client.iam` | `client.iam.get_users(...)` |
| Milestones | `client.milestones` | `client.milestones.get_milestones(...)` |
| Operations | `client.operations` | `client.operations.get_operation_by_id(...)` |
| Permissions | `client.permissions` | `client.permissions.get_permissions(...)` |
| Presentations | `client.presentations` | `client.presentations.get_presentation(...)` |
| Reports | `client.reports` | `client.reports.get_reports(...)` |
| Spreadsheets | `client.spreadsheets` | `client.spreadsheets.get_spreadsheet(...)` |
| Sustainability | `client.sustainability` | `client.sustainability.get_metrics(...)` |
| Tasks | `client.tasks` | `client.tasks.get_tasks(...)` |
| Test Forms | `client.test_forms` | `client.test_forms.get_test_forms(...)` |

### Chains (1 namespace)

| Namespace | Atributo del cliente | Ejemplo |
|-----------|---------------------|---------|
| Chains | `client.chains` | `client.chains.get_chains(...)` |

### Wdata (1 namespace)

| Namespace | Atributo del cliente | Ejemplo |
|-----------|---------------------|---------|
| Wdata | `client.wdata` | `client.wdata.get_tables(...)` |

## Modelos tipados

Todas las operaciones devuelven modelos Pydantic v2. Importalos desde el submodulo correspondiente:

```python
from workiva.models.platform import File, FilesListResult, Operation
from workiva.models.chains import ChainResponse
from workiva.models.wdata import TableDto
```

Las operaciones que devuelven HTTP 202 (operaciones de larga duracion) o 204 (sin contenido) retornan `httpx.Response` directamente.

## Version actual

- **SDK**: 0.6.1
- **Python target**: 3.10+
- **Codegen**: datamodel-code-generator + Jinja2 (sin Speakeasy ni openapi-generator)
