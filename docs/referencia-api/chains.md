# Chains

Todas las operaciones de la API de Chains estan disponibles en un **unico namespace**: `client.chains`.

| Namespace | Atributo |
|-----------|----------|
| Chains | `client.chains` |

> Los endpoints de Chains usan una URL base distinta a Platform. El SDK rutea automaticamente.

## `client.chains` -- Todas las operaciones

### Cadenas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_chains` | Listar cadenas disponibles | No |
| `get_chain` | Obtener cadena por ID | No |
| `search_chains` | Buscar cadenas | No |
| `get_commands` | Listar comandos | No |
| `export_chain` | Exportar cadena | No |
| `import_chain` | Importar cadena | No |
| `publish_chain` | Publicar cadena | No |

### Ejecuciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `start_chain` | Iniciar ejecucion de cadena | No |
| `stop_chain` | Detener ejecucion de cadena | No |
| `chain_run_history` | Historial de ejecuciones | Si |
| `get_chain_run` | Obtener ejecucion por ID | No |
| `get_chain_run_nodes` | Nodos de una ejecucion | No |
| `chain_filter_search` | Buscar con filtros | Si |
| `chain_inputs_search` | Buscar inputs de cadena | Si |

### Usuarios y permisos

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_users` | Listar usuarios | Si |
| `get_user` | Obtener usuario por ID | No |
| `get_user_groups` | Listar grupos de usuarios | Si |
| `get_user_group` | Obtener grupo por ID | No |
| `get_user_group_permissions` | Permisos de un grupo | Si |
| `get_user_user_groups` | Grupos de un usuario | Si |
| `get_permissions` | Listar permisos | Si |
| `get_authorizations_activity` | Actividad de autorizaciones | Si |
| `get_login_activity` | Actividad de login | Si |

### Entornos

| Metodo | Descripcion |
|--------|-------------|
| `get_environments` | Listar entornos |
| `get_environment` | Obtener entorno por ID |

### Workspaces

| Metodo | Descripcion |
|--------|-------------|
| `get_workspaces` | Listar workspaces de Chains |
| `get_workspace` | Obtener workspace por ID |

### Publicacion y reglas

| Metodo | Descripcion |
|--------|-------------|
| `publish` | Publicar |
| `update_rules` | Actualizar reglas |

## Ejemplos

### Listar cadenas

```python
result = client.chains.get_chains()
```

### Iniciar una cadena

```python
result = client.chains.start_chain(
    environment_id="env-456",
    chain_id="chain-123",
    body={"key": "value"},
)
```

### Historial de ejecuciones (auto-paginacion)

```python
result = client.chains.chain_run_history(chain_id="chain-123")

for run in result.data:
    print(f"Run: {run.id} - {run.status}")
```

### Listar usuarios

```python
result = client.chains.get_users()

for user in result.data:
    print(f"Usuario: {user.name}")
```
