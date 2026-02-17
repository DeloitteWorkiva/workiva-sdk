# Sustainability

`client.sustainability` -- Gestion de programas, metricas, dimensiones y temas ESG.

## Operaciones

### Programas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_programs` | Listar programas | Si |
| `get_program_by_id` | Obtener programa por ID | No |
| `create_program` | Crear programa | No |
| `partially_update_program_by_id` | Actualizar programa | No |
| `get_program_permissions` | Permisos de programa | Si |
| `program_permissions_modification` | Modificar permisos | No |

### Metricas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_metrics` | Listar metricas | Si |
| `get_metric_by_id` | Obtener metrica por ID | No |
| `create_metric` | Crear metrica | No |
| `partially_update_metric_by_id` | Actualizar metrica | No |
| `delete_metric_by_id` | Eliminar metrica | No |

### Valores de metricas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_values` | Listar valores | Si |
| `get_metric_value_by_id` | Obtener valor por ID | No |
| `create_value` | Crear valor | No |
| `partially_update_metric_value_by_id` | Actualizar valor | No |
| `delete_metric_value_by_id` | Eliminar valor | No |
| `batch_upsertion_metric_values` | Upsert batch de valores | No |
| `batch_deletion_metric_values` | Eliminacion batch de valores | No |

### Dimensiones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_dimensions` | Listar dimensiones | Si |
| `get_dimension_by_id` | Obtener dimension por ID | No |
| `create_dimension` | Crear dimension | No |
| `partially_update_dimension_by_id` | Actualizar dimension | No |

### Temas (Topics)

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_topics` | Listar temas | Si |
| `get_topic_by_id` | Obtener tema por ID | No |
| `create_topic` | Crear tema | No |
| `partially_update_topic_by_id` | Actualizar tema | No |
| `delete_topic_by_id` | Eliminar tema | No |

## Ejemplos

### Listar programas ESG (auto-paginacion)

```python
result = client.sustainability.get_programs()

for program in result.data:
    print(f"{program.name} (ID: {program.id})")
```

### Crear metrica

```python
metric = client.sustainability.create_metric(
    program_id="prog-123",
    body={"name": "Emisiones CO2", "unit": "toneladas"},
)
print(f"Metrica creada: {metric.id}")
```

### Upsert batch de valores

```python
response = client.sustainability.batch_upsertion_metric_values(
    program_id="prog-123",
    body=values_data,
)

# Operacion 202
operation = client.wait(response).result(timeout=120)
```
