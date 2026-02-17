# Admin

`client.admin` -- Gestion de organizaciones, workspaces, usuarios, grupos y roles.

## Operaciones

### Organizaciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_organizations` | Listar organizaciones | Si |
| `get_organization_by_id` | Obtener organizacion por ID | No |
| `partially_update_organization_by_id` | Actualizar organizacion parcialmente | No |
| `get_organization_roles` | Listar roles de la organizacion | No |
| `get_organization_solutions` | Listar soluciones de la organizacion | No |

### Usuarios de organizacion

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_organization_users` | Listar usuarios de la organizacion | Si |
| `get_organization_user_by_id` | Obtener usuario por ID | No |
| `create_organization_user` | Crear usuario en la organizacion | No |
| `partially_update_organization_user_by_id` | Actualizar usuario parcialmente | No |
| `delete_organization_user_by_id` | Eliminar usuario de la organizacion | No |
| `assign_user_to_organization` | Asignar usuario a organizacion | No |

### Roles de usuario

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_organization_user_role_list` | Listar roles de un usuario | No |
| `assign_organization_user_roles` | Asignar roles a usuario | No |
| `revoke_organization_user_roles` | Revocar roles de usuario | No |

### Workspaces

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_workspaces` | Listar workspaces | Si |
| `get_workspace_by_id` | Obtener workspace por ID | No |
| `create_workspace` | Crear workspace | No |
| `partially_update_workspace_by_id` | Actualizar workspace parcialmente | No |
| `get_workspace_solutions` | Listar soluciones del workspace | No |
| `get_workspace_solutions_by_id` | Obtener solucion por ID | No |

### Membresias de workspace

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_workspace_memberships` | Listar membresias | Si |
| `get_workspace_membership_by_id` | Obtener membresia por ID | No |
| `create_workspace_membership` | Crear membresia | No |
| `delete_workspace_membership_by_id` | Eliminar membresia | No |
| `workspace_membership_creation_with_options` | Crear membresia con opciones | No |
| `get_organization_workspace_membership_roles` | Roles de membresia | No |
| `get_organization_workspace_roles` | Roles del workspace | No |
| `assign_workspace_membership_roles` | Asignar roles a membresia | No |
| `revoke_workspace_membership_roles` | Revocar roles de membresia | No |

### Grupos de workspace

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_workspace_groups` | Listar grupos | Si |
| `get_workspace_group_by_id` | Obtener grupo por ID | No |
| `create_workspace_group` | Crear grupo | No |
| `partially_update_workspace_group_by_id` | Actualizar grupo | No |
| `delete_workspace_group_by_id` | Eliminar grupo | No |
| `get_workspace_group_members` | Listar miembros del grupo | Si |
| `modify_workspace_group_members` | Modificar miembros del grupo | No |

## Ejemplos

### Listar workspaces (auto-paginacion)

```python
result = client.admin.get_workspaces()

for ws in result.data:
    print(f"{ws.name} (ID: {ws.id})")
```

### Crear un usuario en la organizacion

```python
user = client.admin.create_organization_user(
    organization_id="org-123",
    body={
        "email": "dev@example.com",
        "first_name": "Dev",
        "last_name": "User",
    },
)
print(f"Usuario creado: {user.id}")
```

### Asignar roles a un usuario

```python
client.admin.assign_organization_user_roles(
    organization_id="org-123",
    user_id="user-456",
    body=["OrgUserAdmin", "OrgWorkspaceAdmin"],
)
```
