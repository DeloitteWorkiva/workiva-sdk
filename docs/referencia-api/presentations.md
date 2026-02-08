# Presentations

`client.presentations` — Gestión de presentaciones, slides y layouts.

## Operaciones

### Presentaciones

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_presentation_by_id` | Obtener presentación por ID | No | No |
| `partially_update_presentation_by_id` | Actualizar presentación | No | Sí |
| `presentation_export` | Exportar presentación | No | Sí |
| `presentation_filters_reapplication` | Reaplicar filtros | No | Sí |
| `presentation_links_publication` | Publicar links | No | Sí |
| `get_presentation_milestones` | Milestones de presentación | Sí | No |

### Slides

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_slides` | Listar slides | Sí | No |
| `get_slide_by_id` | Obtener slide por ID | No | No |
| `partially_update_slide_by_id` | Actualizar slide | No | Sí |

### Slide Layouts

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_slide_layouts` | Listar layouts | Sí | No |
| `get_slide_layout_by_id` | Obtener layout por ID | No | No |
| `partially_update_slide_layout_by_id` | Actualizar layout | No | Sí |

## Ejemplos

### Obtener presentación

```python
response = client.presentations.get_presentation_by_id(
    presentation_id="pres-123",
)
print(f"Presentación: {response.result.name}")
```

### Listar slides

```python
response = client.presentations.get_slides(
    presentation_id="pres-123",
)

for slide in response.result.data:
    print(f"Slide: {slide.id}")
```

### Exportar presentación (operación 202)

```python
response = client.presentations.presentation_export(
    presentation_id="pres-123",
    presentation_export={"format": "pdf"},
)

operation = client.wait(response).result(timeout=120)
print(f"Exportado: {operation.resource_url}")
```
