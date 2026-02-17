# Content

`client.content` -- Lectura y escritura de contenido de Workiva: tablas, imagenes, links, rich text, drawing anchors y mas.

## Operaciones

### Links

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `destination_link_source_conversion` | Convertir origen de link de destino | No |
| `get_destination_link_by_id` | Obtener link de destino por ID | No |
| `get_range_link_by_id` | Obtener range link por ID | No |
| `get_range_link_destinations` | Destinos de un range link | Si |
| `get_range_links` | Listar range links | Si |

### Rich text

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_anchor_by_id` | Obtener anchor por ID | No |
| `get_rich_text_anchor_by_id` | Obtener rich text anchor por ID | No |
| `get_rich_text_anchor_extensions` | Extensiones de rich text anchor | Si |
| `get_rich_text_anchors` | Listar rich text anchors | Si |
| `get_rich_text_paragraphs` | Parrafos de rich text | Si |
| `rich_text_anchor_creation` | Crear rich text anchor | No |
| `rich_text_batch_edit` | Edicion batch de rich text | No |
| `rich_text_duplication_edit` | Duplicar rich text | No |
| `rich_text_links_batch_edit` | Edicion batch de links en rich text | No |

### Tablas (contenido)

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_table_anchor_by_id` | Obtener table anchor por ID | No |
| `get_table_anchor_extensions` | Extensiones de table anchor | Si |
| `get_table_anchors` | Listar table anchors | Si |
| `get_table_cells` | Celdas de una tabla | Si |
| `get_table_properties` | Propiedades de tabla | No |
| `table_anchor_creation` | Crear table anchor | No |
| `table_cells_batch_edit` | Edicion batch de celdas | No |
| `table_edit` | Editar tabla | No |
| `table_filters_reapplication` | Reaplicar filtros de tabla | No |
| `table_links_batch_edit` | Edicion batch de links en tabla | No |
| `table_range_links_edit` | Editar range links de tabla | No |
| `partially_update_table_properties` | Actualizar propiedades de tabla | No |

### Imagenes y dibujos

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_image_by_id` | Obtener imagen por ID | No |
| `image_upload` | Subir imagen | No |
| `get_drawing_anchor_by_id` | Drawing anchor por ID | No |
| `get_drawing_anchor_extensions` | Extensiones de drawing anchor | Si |
| `get_drawing_anchors` | Listar drawing anchors | Si |
| `get_drawing_elements_by_id` | Elementos de drawing | Si |

### Filas, columnas y estilo

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_column_properties` | Propiedades de columnas | Si |
| `get_row_properties` | Propiedades de filas | Si |
| `get_style_guide_by_id` | Style guide por ID | No |
| `style_guide_export` | Exportar style guide | No |
| `style_guide_import` | Importar style guide | No |

## Ejemplo

### Obtener celdas de una tabla (auto-paginacion)

```python
result = client.content.get_table_cells(
    document_id="doc-123",
    section_id="sec-456",
    table_id="tbl-789",
)

for cell in result.data:
    print(f"Celda: {cell.value}")
```

### Subir imagen

```python
response = client.content.image_upload(
    document_id="doc-123",
    section_id="sec-456",
    body=image_data,
)
# Operacion 202
operation = client.wait(response).result(timeout=60)
```
