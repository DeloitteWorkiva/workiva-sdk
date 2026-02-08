# Graph

`client.graph` — Acceso a workspaces de Integrated Risk: registros, tipos y reportes.

## Operaciones

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_records` | Listar registros | No | No |
| `get_record_by_id` | Obtener registro por ID | No | No |
| `get_types` | Listar tipos de registro | No | No |
| `get_type_by_id` | Obtener tipo por ID | No | No |
| `create_edits` | Crear/editar registros | No | No |
| `graph_report_export` | Exportar reporte | No | Sí |

## Ejemplos

### Listar tipos de registro

```python
response = client.graph.get_types(
    workspace_id="ws-123",
)

for type_ in response.result.data:
    print(f"Tipo: {type_.name} (ID: {type_.id})")
```

### Obtener registros

```python
response = client.graph.get_records(
    workspace_id="ws-123",
    type_id="type-456",
)

for record in response.result.data:
    print(f"Registro: {record.id}")
```

### Exportar reporte (operación 202)

```python
response = client.graph.graph_report_export(
    workspace_id="ws-123",
    graph_report_export=export_config,
)

operation = client.wait(response).result(timeout=300)
```
