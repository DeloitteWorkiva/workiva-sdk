# Paginación

El SDK de Workiva maneja 5 patrones de paginación distintos a lo largo de sus 89 endpoints paginados. Todos se consumen de la misma forma desde tu código.

## Uso básico

Todos los endpoints paginados devuelven un objeto con un método `.next()`:

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    response = client.files.get_files()

    # Primera página
    for file in response.result.data:
        print(file.name)

    # Iterar todas las páginas
    while response.next is not None:
        response = response.next()
        for file in response.result.data:
            print(file.name)
```

## Iterar TODAS las páginas

Patrón completo para recorrer todos los resultados:

```python
def get_all_items(initial_response):
    """Recorre todas las páginas de un endpoint paginado."""
    items = list(initial_response.result.data)
    response = initial_response

    while response.next is not None:
        response = response.next()
        items.extend(response.result.data)

    return items

# Uso
response = client.admin.get_workspaces()
all_workspaces = get_all_items(response)
print(f"Total: {len(all_workspaces)} workspaces")
```

## Los 5 patrones

| Patrón | API | Mecanismo | Endpoints | Ejemplo |
|--------|-----|-----------|-----------|---------|
| A | Platform | Cursor via `$next` | 60 | `get_files`, `get_workspaces` |
| B | Platform | URL en JSON:API | 1 | `get_org_report_users` |
| C | Chains | Cursor | 3 | `chain_run_history` |
| D | Chains | Page offset/limit | 7 | `get_users`, `get_permissions` |
| E | Wdata | Cursor | 18 | `get_tables`, `list_queries` |

### Patrón A — Platform cursor ($next)

La mayoría de endpoints de Platform usan un parámetro `$next` como cursor:

```python
# El SDK maneja $next automáticamente via .next()
response = client.activities.get_organization_activities()

while response.next is not None:
    response = response.next()
```

Puedes controlar el tamaño de página con `maxpagesize`:

```python
response = client.files.get_files(maxpagesize=50)
```

### Patrón B — JSON:API (Reports)

Un solo endpoint usa paginación estilo JSON:API con URLs completas:

```python
response = client.reports.get_org_report_users(
    organization_id="org-123",
    report_type="users",
)

while response.next is not None:
    response = response.next()
```

### Patrón C — Chains cursor

Algunos endpoints de Chains usan un campo `cursor` en la respuesta:

```python
response = client.chains.chain_run_history(
    chain_id="chain-123",
)

while response.next is not None:
    response = response.next()
```

### Patrón D — Chains page offset

Endpoints de Chains que usan paginación por número de página:

```python
response = client.chains.get_users()

while response.next is not None:
    response = response.next()
```

Puedes controlar el tamaño con `page_size`:

```python
response = client.chains.get_users(page_size=25)
```

### Patrón E — Wdata cursor

Los endpoints de Wdata usan un parámetro `cursor`:

```python
response = client.wdata.get_tables()

while response.next is not None:
    response = response.next()
```

## Todos los endpoints paginados

### Platform (61 endpoints)

Incluye: `get_files`, `get_documents`, `get_workspaces`, `get_organization_users`, `get_sheets`, `get_spreadsheets`, `get_slides`, `get_tasks`, `get_permissions`, `get_organization_activities`, `get_activity_actions`, y muchos más.

### Chains (10 endpoints)

- `chain_filter_search`, `chain_inputs_search`, `chain_run_history`
- `get_authorizations_activity`, `get_login_activity`
- `get_permissions`, `get_users`, `get_user_groups`, `get_user_group_permissions`, `get_user_user_groups`

### Wdata (18 endpoints)

- `get_tables`, `list_queries`, `list_folders`, `list_parameters`
- `list_pivot_views`, `list_select_lists`, `list_shared_tables`, `list_tags`
- `list_connections`, `list_children`, `list_query_results`
- `get_files`, `get_dependencies`, `get_dependents`, `get_errors`
- `find_workspace_files_by_size`, `get_tables_dependent_on_query`, `search`

## Notas importantes

- `.next` es `None` cuando no hay más páginas — siempre verifica antes de llamar
- El SDK parsea automáticamente los tokens de paginación de la respuesta
- Cada llamada a `.next()` ejecuta una nueva solicitud HTTP
- Los patrones son transparentes — todos se consumen con el mismo `while response.next is not None`
