# Milestones

`client.milestones` -- Gestion de hitos (milestones) en Workiva.

## Operaciones

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_milestone_by_id` | Obtener milestone por ID | No | No |
| `milestone_creation` | Crear milestone | No | Si |
| `partially_update_milestone_by_id` | Actualizar milestone parcialmente | No | No |
| `delete_milestone_by_id` | Eliminar milestone | No | No |

## Ejemplos

### Crear milestone (operacion 202)

```python
response = client.milestones.milestone_creation(
    title="Q4 Review",
    type_="review",
)

operation = client.wait(response).result(timeout=60)
```

### Obtener milestone

```python
milestone = client.milestones.get_milestone_by_id(
    milestone_id="ms-456",
)
print(f"Milestone: {milestone.title}")
```

### Actualizar milestone

```python
milestone = client.milestones.partially_update_milestone_by_id(
    milestone_id="ms-456",
    body=[{"op": "replace", "path": "/title", "value": "Q4 Final Review"}],
)
```

### Eliminar milestone

```python
client.milestones.delete_milestone_by_id(
    milestone_id="ms-456",
)
```
