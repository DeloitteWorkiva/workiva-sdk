# Permissions

`client.permissions` -- Consulta de permisos en Workiva.

## Operaciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_permissions` | Listar permisos | No |
| `get_permission_by_id` | Obtener permiso por ID | No |

## Ejemplos

### Listar permisos

```python
result = client.permissions.get_permissions()

for perm in result.data:
    print(f"Permiso: {perm.id} - {perm.name}")
```

### Obtener permiso por ID

```python
perm = client.permissions.get_permission_by_id(
    permission_id="perm-123",
)
print(f"Permiso: {perm.name}")
```
