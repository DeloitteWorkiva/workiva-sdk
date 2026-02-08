# Activities

`client.activities` — Actividades de organización y workspace.

Permite consultar acciones realizadas en la organización o workspace: logins, cambios de roles, cambios de configuración, etc. Requiere rol de admin (Org User Admin, Org Workspace Admin, Org Security Admin, o Workspace Owner).

## Operaciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_activity_action_by_id` | Obtener una acción de actividad por ID | No |
| `get_activity_actions` | Listar acciones de actividad | Sí |
| `get_activity_by_id` | Obtener una actividad por ID | No |
| `get_organization_activities` | Listar actividades de la organización | Sí |
| `get_organization_workspace_activities` | Listar actividades de un workspace | Sí |

## Ejemplos

### Listar actividades de la organización

```python
response = client.activities.get_organization_activities()

for activity in response.result.data:
    print(f"{activity.id}: {activity.action}")

# Paginar
while response.next is not None:
    response = response.next()
    for activity in response.result.data:
        print(f"{activity.id}: {activity.action}")
```

### Obtener una actividad específica

```python
response = client.activities.get_activity_by_id(
    activity_id="act-123",
)
print(response.result)
```

### Listar actividades de un workspace

```python
response = client.activities.get_organization_workspace_activities(
    workspace_id="ws-456",
)
```
