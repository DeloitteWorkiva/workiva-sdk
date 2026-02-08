# Chains

`client.chains` — Automatización de flujos de trabajo (cadenas).

La API de Chains permite gestionar cadenas de automatización, ejecutarlas, consultar historial y administrar usuarios y permisos del sistema de Chains.

> Los endpoints de Chains usan una URL base distinta a Platform. El SDK rutea automáticamente.

## Operaciones

### Cadenas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_chains` | Listar cadenas disponibles | No |
| `get_chain` | Obtener cadena por ID | No |
| `search_chains` | Buscar cadenas | No |
| `chain_filter_search` | Buscar con filtros | Sí |
| `chain_inputs_search` | Buscar inputs de cadena | Sí |
| `start_chain` | Iniciar ejecución de cadena | No |
| `stop_chain` | Detener ejecución de cadena | No |
| `export_chain` | Exportar cadena | No |
| `import_chain` | Importar cadena | No |
| `publish` | Publicar cadena | No |
| `publish_chain` | Publicar cadena (alternativa) | No |

### Ejecuciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `chain_run_history` | Historial de ejecuciones | Sí |
| `get_chain_run` | Obtener ejecución por ID | No |
| `get_chain_run_nodes` | Nodos de una ejecución | No |

### Usuarios y permisos

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_users` | Listar usuarios | Sí |
| `get_user` | Obtener usuario por ID | No |
| `get_user_groups` | Listar grupos de usuarios | Sí |
| `get_user_group` | Obtener grupo por ID | No |
| `get_user_group_permissions` | Permisos de un grupo | Sí |
| `get_user_user_groups` | Grupos de un usuario | Sí |
| `get_permissions` | Listar permisos | Sí |

### Entorno y actividad

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_environments` | Listar entornos | No |
| `get_environment` | Obtener entorno por ID | No |
| `get_commands` | Listar comandos | No |
| `get_workspaces` | Listar workspaces de Chains | No |
| `get_workspace` | Obtener workspace por ID | No |
| `get_authorizations_activity` | Actividad de autorizaciones | Sí |
| `get_login_activity` | Actividad de login | Sí |
| `update_rules` | Actualizar reglas | No |

## Ejemplos

### Listar cadenas

```python
response = client.chains.get_chains()
print(response.result)
```

### Iniciar una cadena

```python
response = client.chains.start_chain(
    chain_id="chain-123",
    chain_run_request={
        "environment_id": "env-456",
    },
)
print(f"Ejecución iniciada: {response.result}")
```

### Historial de ejecuciones

```python
response = client.chains.chain_run_history(
    chain_id="chain-123",
)

for run in response.result.data:
    print(f"Run {run.id}: {run.status}")

# Paginar
while response.next is not None:
    response = response.next()
```

### Obtener detalles de una ejecución

```python
response = client.chains.get_chain_run(
    chain_id="chain-123",
    chain_run_id="run-789",
)
print(f"Estado: {response.result.status}")
```
