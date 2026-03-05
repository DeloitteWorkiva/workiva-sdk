# Content

`client.content` -- Lectura y escritura de contenido de Workiva: tablas, imagenes, links, rich text, drawing anchors y mas.

## Operaciones

### Links

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `destination_link_source_conversion` | Convertir origen de link de destino | No | Si |
| `get_destination_link_by_id` | Obtener link de destino por ID | No | No |
| `get_range_link_by_id` | Obtener range link por ID | No | No |
| `get_range_link_destinations` | Destinos de un range link | Si | No |
| `get_range_links` | Listar range links | Si | No |

### Rich text

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_anchor_by_id` | Obtener anchor por ID | No | No |
| `get_rich_text_anchor_by_id` | Obtener rich text anchor por ID | No | No |
| `get_rich_text_anchor_extensions` | Extensiones de rich text anchor | Si | No |
| `get_rich_text_anchors` | Listar rich text anchors | Si | No |
| `get_rich_text_paragraphs` | Parrafos de rich text | Si | No |
| `rich_text_anchor_creation` | Crear rich text anchor | No | Si |
| `rich_text_batch_edit` | Edicion batch de rich text | No | Si |
| `rich_text_duplication_edit` | Duplicar rich text | No | Si |
| `rich_text_links_batch_edit` | Edicion batch de links en rich text | No | Si |

### Tablas (contenido)

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_table_anchor_by_id` | Obtener table anchor por ID | No | No |
| `get_table_anchor_extensions` | Extensiones de table anchor | Si | No |
| `get_table_anchors` | Listar table anchors | Si | No |
| `get_table_cells` | Celdas de una tabla | Si | No |
| `get_table_properties` | Propiedades de tabla | No | No |
| `table_anchor_creation` | Crear table anchor | No | Si |
| `table_cells_batch_edit` | Edicion batch de celdas | No | Si |
| `table_edit` | Editar tabla | No | Si |
| `table_filters_reapplication` | Reaplicar filtros de tabla | No | Si |
| `table_links_batch_edit` | Edicion batch de links en tabla | No | Si |
| `table_range_links_edit` | Editar range links de tabla | No | Si |
| `partially_update_table_properties` | Actualizar propiedades de tabla | No | Si |

### Imagenes y dibujos

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_image_by_id` | Obtener imagen por ID | No | No |
| `image_upload` | Subir imagen | No | No |
| `get_drawing_anchor_by_id` | Drawing anchor por ID | No | No |
| `get_drawing_anchor_extensions` | Extensiones de drawing anchor | Si | No |
| `get_drawing_anchors` | Listar drawing anchors | Si | No |
| `get_drawing_elements_by_id` | Elementos de drawing | Si | No |

### Filas, columnas y estilo

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_column_properties` | Propiedades de columnas | Si | No |
| `get_row_properties` | Propiedades de filas | Si | No |
| `get_style_guide_by_id` | Style guide por ID | No | No |
| `style_guide_export` | Exportar style guide | No | Si |
| `style_guide_import` | Importar style guide | No | No |

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
# image_upload retorna ImageUploadResponse con upload_url y operation_id
upload_response = client.content.image_upload(
    file_name="chart.png",
)
print(f"URL de subida: {upload_response.upload_url}")
print(f"Operation ID: {upload_response.operation_id}")
```
