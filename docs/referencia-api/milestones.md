# Milestones

`client.milestones` — Gestión de hitos (milestones) en Workiva.

## Operaciones

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_milestone_by_id` | Obtener milestone por ID | No | No |
| `milestone_creation` | Crear milestone | No | Sí |
| `partially_update_milestone_by_id` | Actualizar milestone parcialmente | No | No |
| `delete_milestone_by_id` | Eliminar milestone | No | No |

## Ejemplos

### Crear milestone (operación 202)

```python
response = client.milestones.milestone_creation(
    file_id="file-123",
    milestone={"name": "Q4 Review"},
)

operation = client.wait(response).result(timeout=60)
```

### Obtener milestone

```python
response = client.milestones.get_milestone_by_id(
    file_id="file-123",
    milestone_id="ms-456",
)
print(f"Milestone: {response.result.name}")
```

### Eliminar milestone

```python
client.milestones.delete_milestone_by_id(
    file_id="file-123",
    milestone_id="ms-456",
)
```
