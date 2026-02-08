# Content

`client.content` — Lectura y escritura de contenido de Workiva: tablas, imágenes, links, rich text, drawing anchors y más.

## Operaciones

### Links

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `destination_link_source_conversion` | Convertir origen de link de destino | No |
| `get_destination_link_by_id` | Obtener link de destino por ID | No |
| `get_range_link_by_id` | Obtener range link por ID | No |
| `get_range_link_destinations` | Destinos de un range link | Sí |
| `get_range_links` | Listar range links | Sí |

### Rich text

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_anchor_by_id` | Obtener anchor por ID | No |
| `get_rich_text_anchor_by_id` | Obtener rich text anchor por ID | No |
| `get_rich_text_anchor_extensions` | Extensiones de rich text anchor | Sí |
| `get_rich_text_anchors` | Listar rich text anchors | Sí |
| `get_rich_text_paragraphs` | Párrafos de rich text | Sí |
| `rich_text_anchor_creation` | Crear rich text anchor | No |
| `rich_text_batch_edit` | Edición batch de rich text | No |
| `rich_text_duplication_edit` | Duplicar rich text | No |
| `rich_text_links_batch_edit` | Edición batch de links en rich text | No |

### Tablas (contenido)

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_table_anchor_by_id` | Obtener table anchor por ID | No |
| `get_table_anchor_extensions` | Extensiones de table anchor | Sí |
| `get_table_anchors` | Listar table anchors | Sí |
| `get_table_cells` | Celdas de una tabla | Sí |
| `get_table_properties` | Propiedades de tabla | No |
| `table_anchor_creation` | Crear table anchor | No |
| `table_cells_batch_edit` | Edición batch de celdas | No |
| `table_edit` | Editar tabla | No |
| `table_filters_reapplication` | Reaplicar filtros de tabla | No |
| `table_links_batch_edit` | Edición batch de links en tabla | No |
| `table_range_links_edit` | Editar range links de tabla | No |
| `partially_update_table_properties` | Actualizar propiedades de tabla | No |

### Imágenes y dibujos

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_image_by_id` | Obtener imagen por ID | No |
| `image_upload` | Subir imagen | No |
| `get_drawing_anchor_by_id` | Drawing anchor por ID | No |
| `get_drawing_anchor_extensions` | Extensiones de drawing anchor | Sí |
| `get_drawing_anchors` | Listar drawing anchors | Sí |
| `get_drawing_elements_by_id` | Elementos de drawing | Sí |

### Filas, columnas y estilo

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_column_properties` | Propiedades de columnas | Sí |
| `get_row_properties` | Propiedades de filas | Sí |
| `get_style_guide_by_id` | Style guide por ID | No |
| `style_guide_export` | Exportar style guide | No |
| `style_guide_import` | Importar style guide | No |

## Ejemplo

### Obtener celdas de una tabla

```python
response = client.content.get_table_cells(
    document_id="doc-123",
    section_id="sec-456",
    table_id="tbl-789",
)

for cell in response.result.data:
    print(f"Celda: {cell.value}")

while response.next is not None:
    response = response.next()
```

### Subir imagen

```python
response = client.content.image_upload(
    document_id="doc-123",
    section_id="sec-456",
    image_upload=image_data,
)
# Operación 202 — usar client.wait()
operation = client.wait(response).result(timeout=60)
```
