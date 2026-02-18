# Paginacion

El SDK pagina automaticamente. Una sola llamada devuelve TODOS los items de todas las paginas.

## Uso basico

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    # Esto devuelve TODOS los archivos, no solo la primera pagina
    result = client.files.get_files()

    for file in result.data:
        print(f"{file.name} ({file.kind})")

    print(f"Total: {len(result.data)} archivos")
```

El SDK itera internamente todas las paginas de la API y te devuelve un unico modelo Pydantic con todos los items agregados.

## Como funciona internamente

```
Tu codigo                         SDK                              API
    |                               |                                |
    |  get_files()                  |                                |
    | ----------------------------> |  GET /files                    |
    |                               | -----------------------------> |
    |                               |  {data: [...], @nextLink: X}  |
    |                               | <----------------------------- |
    |                               |  GET /files?$next=X            |
    |                               | -----------------------------> |
    |                               |  {data: [...], @nextLink: Y}  |
    |                               | <----------------------------- |
    |                               |  GET /files?$next=Y            |
    |                               | -----------------------------> |
    |                               |  {data: [...], @nextLink: null}|
    |                               | <----------------------------- |
    |  FilesListResult              |                                |
    |  (con TODOS los items)        |                                |
    | <---------------------------- |                                |
```

## Controlar el tamano de pagina

Para controlar cuantos items trae cada request individual al servidor, usa el parametro de la API correspondiente (normalmente `maxpagesize`):

```python
# Paginas de 100 items cada una (el SDK sigue iterando todas automaticamente)
result = client.files.get_files(maxpagesize=100)
```

El parametro no limita el resultado final -- solo el tamano de cada request HTTP. El SDK sigue iterando hasta que no haya mas paginas.

## Limite de seguridad

El SDK tiene un limite de seguridad de **1000 paginas** por operacion para prevenir bucles infinitos. Si se excede, lanza `RuntimeError`:

```python
try:
    result = client.files.get_files()
except RuntimeError as e:
    print(f"Demasiadas paginas: {e}")
```

Para la gran mayoria de casos, 1000 paginas es mas que suficiente. Si necesitas mas, usa los parametros de la API para filtrar los resultados.

## Los 5 patrones de paginacion

El SDK maneja 5 patrones distintos de paginacion, todos transparentes para ti:

| Patron | API | Mecanismo | Endpoints | Extractor |
|--------|-----|-----------|-----------|-----------|
| A | Platform | Cursor `$next` en query + `@nextLink` en body | ~60 | `extract_next_link` |
| B | Platform | URL en `links.next` (JSON:API) | 1 | `extract_jsonapi_next` |
| C | Chains | Cursor en `data.cursor` | 3 | `extract_chains_cursor` |
| D | Chains | Page offset/limit | 7 | (page-based) |
| E | Wdata | Cursor en `cursor` | ~18 | `extract_wdata_cursor` |

Todos se consumen de la misma forma: llamas al metodo y recibes el modelo completo.

### Patron A -- Platform cursor ($next)

```python
# El SDK inyecta $next automaticamente en cada pagina
result = client.files.get_files()
# result.data contiene TODOS los archivos
```

### Patron B -- JSON:API (Reports)

```python
result = client.reports.get_org_report_users(
    organization_id="org-123",
    report_type="users",
)
# result.data contiene TODOS los usuarios del reporte
```

### Patron C -- Chains cursor

```python
result = client.chains.chain_run_history(chain_id="chain-123")
# result.data.chain_executors contiene TODAS las ejecuciones
```

### Patron E -- Wdata cursor

```python
result = client.wdata.get_tables()
# result.body contiene TODAS las tablas
```

## Paginacion async

La paginacion transparente funciona igual en modo async:

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="...", client_secret="...") as client:
        result = await client.files.get_files_async()
        print(f"Total: {len(result.data)} archivos")

asyncio.run(main())
```

## Paginacion lazy (avanzado)

El SDK tambien ofrece generadores lazy que hacen `yield` item por item sin acumular todo en memoria. Utiles para datasets muy grandes:

```python
from workiva._pagination import paginate_lazy, paginate_lazy_async

# Sync — itera items uno a uno
for item in paginate_lazy(fetch_fn, extract_cursor, items_path="data"):
    process(item)

# Async
async for item in paginate_lazy_async(fetch_fn, extract_cursor, items_path="data"):
    await process(item)
```

> **Nota:** Los generadores lazy son funciones de infraestructura interna (`_pagination.py`). Los metodos generados del SDK usan `paginate_all()` que devuelve todos los items de golpe. Los lazy generators estan disponibles para uso avanzado cuando necesitas control sobre el consumo de memoria.

## Endpoints paginados por API

### Platform (~61 endpoints)

Incluye: `get_files`, `get_documents`, `get_workspaces`, `get_organization_users`, `get_sheets`, `get_spreadsheets`, `get_slides`, `get_tasks`, `get_permissions`, `get_organization_activities`, `get_activity_actions`, entre otros.

### Chains (~10 endpoints)

- `chain_filter_search`, `chain_inputs_search`, `chain_run_history`
- `get_authorizations_activity`, `get_login_activity`
- `get_permissions`, `get_users`, `get_user_groups`, `get_user_group_permissions`, `get_user_user_groups`

### Wdata (~18 endpoints)

- `get_tables`, `list_queries`, `list_folders`, `list_parameters`
- `list_pivot_views`, `list_select_lists`, `list_shared_tables`, `list_tags`
- `list_connections`, `list_children`, `list_query_results`
- `get_files`, `get_dependencies`, `get_dependents`, `get_errors`
- `find_workspace_files_by_size`, `get_tables_dependent_on_query`, `search`
