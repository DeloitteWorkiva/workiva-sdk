# Presentations

`client.presentations` -- Gestion de presentaciones, slides y layouts.

## Operaciones

### Presentaciones

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_presentation_by_id` | Obtener presentacion por ID | No | No |
| `partially_update_presentation_by_id` | Actualizar presentacion | No | Si |
| `presentation_export` | Exportar presentacion | No | Si |
| `presentation_filters_reapplication` | Reaplicar filtros | No | Si |
| `presentation_links_publication` | Publicar links | No | Si |
| `get_presentation_milestones` | Milestones de presentacion | Si | No |

### Slides

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_slides` | Listar slides | Si | No |
| `get_slide_by_id` | Obtener slide por ID | No | No |
| `partially_update_slide_by_id` | Actualizar slide | No | Si |

### Slide Layouts

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_slide_layouts` | Listar layouts | Si | No |
| `get_slide_layout_by_id` | Obtener layout por ID | No | No |
| `partially_update_slide_layout_by_id` | Actualizar layout | No | Si |

## Ejemplos

### Obtener presentacion

```python
pres = client.presentations.get_presentation_by_id(
    presentation_id="pres-123",
)
print(f"Presentacion: {pres.name}")
```

### Listar slides (auto-paginacion)

```python
result = client.presentations.get_slides(presentation_id="pres-123")

for slide in result.data:
    print(f"Slide: {slide.id}")
```

### Exportar presentacion (operacion 202)

```python
response = client.presentations.presentation_export(
    presentation_id="pres-123",
    format_="pdf",
)

operation = client.wait(response).result(timeout=120)
print(f"Exportado: {operation.resource_url}")
```
