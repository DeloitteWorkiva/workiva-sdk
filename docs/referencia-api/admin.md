# Admin

`client.admin` — Gestión de organizaciones, workspaces, usuarios, grupos y roles.

## Operaciones

### Organizaciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_organizations` | Listar organizaciones | Sí |
| `get_organization_by_id` | Obtener organización por ID | No |
| `partially_update_organization_by_id` | Actualizar organización parcialmente | No |
| `get_organization_roles` | Listar roles de la organización | No |
| `get_organization_solutions` | Listar soluciones de la organización | No |

### Usuarios de organización

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_organization_users` | Listar usuarios de la organización | Sí |
| `get_organization_user_by_id` | Obtener usuario por ID | No |
| `create_organization_user` | Crear usuario en la organización | No |
| `partially_update_organization_user_by_id` | Actualizar usuario parcialmente | No |
| `delete_organization_user_by_id` | Eliminar usuario de la organización | No |
| `assign_user_to_organization` | Asignar usuario a organización | No |

### Roles de usuario

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_organization_user_role_list` | Listar roles de un usuario | No |
| `assign_organization_user_roles` | Asignar roles a usuario | No |
| `revoke_organization_user_roles` | Revocar roles de usuario | No |

### Workspaces

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_workspaces` | Listar workspaces | Sí |
| `get_workspace_by_id` | Obtener workspace por ID | No |
| `create_workspace` | Crear workspace | No |
| `partially_update_workspace_by_id` | Actualizar workspace parcialmente | No |
| `get_workspace_solutions` | Listar soluciones del workspace | No |
| `get_workspace_solutions_by_id` | Obtener solución por ID | No |

### Membresías de workspace

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_workspace_memberships` | Listar membresías | Sí |
| `get_workspace_membership_by_id` | Obtener membresía por ID | No |
| `create_workspace_membership` | Crear membresía | No |
| `delete_workspace_membership_by_id` | Eliminar membresía | No |
| `workspace_membership_creation_with_options` | Crear membresía con opciones | No |
| `get_organization_workspace_membership_roles` | Roles de membresía | No |
| `get_organization_workspace_roles` | Roles del workspace | No |
| `assign_workspace_membership_roles` | Asignar roles a membresía | No |
| `revoke_workspace_membership_roles` | Revocar roles de membresía | No |

### Grupos de workspace

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_workspace_groups` | Listar grupos | Sí |
| `get_workspace_group_by_id` | Obtener grupo por ID | No |
| `create_workspace_group` | Crear grupo | No |
| `partially_update_workspace_group_by_id` | Actualizar grupo | No |
| `delete_workspace_group_by_id` | Eliminar grupo | No |
| `get_workspace_group_members` | Listar miembros del grupo | Sí |
| `modify_workspace_group_members` | Modificar miembros del grupo | No |

## Ejemplos

### Listar workspaces

```python
response = client.admin.get_workspaces()

for ws in response.result.data:
    print(f"{ws.name} (ID: {ws.id})")
```

### Crear un usuario en la organización

```python
response = client.admin.create_organization_user(
    organization_id="org-123",
    user={
        "email": "dev@example.com",
        "first_name": "Dev",
        "last_name": "User",
    },
)
print(f"Usuario creado: {response.result.id}")
```

### Asignar roles a un usuario

```python
client.admin.assign_organization_user_roles(
    organization_id="org-123",
    user_id="user-456",
    request_body=["OrgUserAdmin", "OrgWorkspaceAdmin"],
)
```
