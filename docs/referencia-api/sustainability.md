# Sustainability

`client.sustainability` — Gestión de programas, métricas, dimensiones y temas ESG.

## Operaciones

### Programas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_programs` | Listar programas | Sí |
| `get_program_by_id` | Obtener programa por ID | No |
| `create_program` | Crear programa | No |
| `partially_update_program_by_id` | Actualizar programa | No |
| `get_program_permissions` | Permisos de programa | Sí |
| `program_permissions_modification` | Modificar permisos | No |

### Métricas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_metrics` | Listar métricas | Sí |
| `get_metric_by_id` | Obtener métrica por ID | No |
| `create_metric` | Crear métrica | No |
| `partially_update_metric_by_id` | Actualizar métrica | No |
| `delete_metric_by_id` | Eliminar métrica | No |

### Valores de métricas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_values` | Listar valores | Sí |
| `get_metric_value_by_id` | Obtener valor por ID | No |
| `create_value` | Crear valor | No |
| `partially_update_metric_value_by_id` | Actualizar valor | No |
| `delete_metric_value_by_id` | Eliminar valor | No |
| `batch_upsertion_metric_values` | Upsert batch de valores | No |
| `batch_deletion_metric_values` | Eliminación batch de valores | No |

### Dimensiones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_dimensions` | Listar dimensiones | Sí |
| `get_dimension_by_id` | Obtener dimensión por ID | No |
| `create_dimension` | Crear dimensión | No |
| `partially_update_dimension_by_id` | Actualizar dimensión | No |

### Temas (Topics)

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_topics` | Listar temas | Sí |
| `get_topic_by_id` | Obtener tema por ID | No |
| `create_topic` | Crear tema | No |
| `partially_update_topic_by_id` | Actualizar tema | No |
| `delete_topic_by_id` | Eliminar tema | No |

## Ejemplos

### Listar programas ESG

```python
response = client.sustainability.get_programs()

for program in response.result.data:
    print(f"{program.name} (ID: {program.id})")
```

### Crear métrica

```python
response = client.sustainability.create_metric(
    program_id="prog-123",
    metric={"name": "Emisiones CO2", "unit": "toneladas"},
)
print(f"Métrica creada: {response.result.id}")
```

### Upsert batch de valores

```python
response = client.sustainability.batch_upsertion_metric_values(
    program_id="prog-123",
    metric_value_batch_upsert=values_data,
)

# Operación 202
operation = client.wait(response).result(timeout=120)
```
