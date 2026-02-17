# Activities

`client.activities` -- Actividades de organizacion y workspace.

Permite consultar acciones realizadas en la organizacion o workspace: logins, cambios de roles, cambios de configuracion, etc. Requiere rol de admin.

## Operaciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_activity_action_by_id` | Obtener una accion de actividad por ID | No |
| `get_activity_actions` | Listar acciones de actividad | Si |
| `get_activity_by_id` | Obtener una actividad por ID | No |
| `get_organization_activities` | Listar actividades de la organizacion | Si |
| `get_organization_workspace_activities` | Listar actividades de un workspace | Si |

## Ejemplos

### Listar actividades de la organizacion (auto-paginacion)

```python
result = client.activities.get_organization_activities()

for activity in result.data:
    print(f"{activity.id}: {activity.action}")
```

### Obtener una actividad especifica

```python
activity = client.activities.get_activity_by_id(activity_id="act-123")
print(activity)
```

### Listar actividades de un workspace

```python
result = client.activities.get_organization_workspace_activities(
    workspace_id="ws-456",
)
```
