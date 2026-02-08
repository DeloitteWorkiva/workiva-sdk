# Permissions

`client.permissions` — Consulta de permisos en Workiva.

## Operaciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_permissions` | Listar permisos | No |
| `get_permission_by_id` | Obtener permiso por ID | No |

## Ejemplo

```python
response = client.permissions.get_permissions()
print(response.result)
```

```python
response = client.permissions.get_permission_by_id(
    permission_id="perm-123",
)
print(f"Permiso: {response.result}")
```
