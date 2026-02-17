# Operations

`client.operations` -- Consultar el estado de operaciones asincronas y obtener resultados.

Este namespace es el complemento de las operaciones 202. Cuando una operacion (copy, import, export, etc.) se completa, puedes consultar sus resultados detallados aqui.

> Para polling automatico, usa `client.wait(response).result()`. Este namespace se usa para consultas manuales o para obtener resultados detallados despues de que el polling termine.

## Operaciones

### Estado general

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_operation_by_id` | Obtener estado de una operacion | No |

### Resultados de archivos

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_copy_file_results` | Resultados de copia de archivo | Si |
| `get_import_file_results` | Resultados de importacion | Si |
| `get_image_upload_creation_results` | Resultados de subida de imagen | Si |

### Resultados de contenido

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_rich_text_anchor_creation_results` | Resultados de creacion de anchor | Si |
| `get_rich_text_batch_edit_results` | Resultados de edicion batch de rich text | Si |
| `get_rich_text_duplication_edit_results` | Resultados de duplicacion | Si |
| `get_rich_text_links_batch_edit_results` | Resultados de links batch | Si |
| `get_table_anchor_creation_results` | Resultados de creacion de table anchor | Si |
| `get_table_cell_edit_results` | Resultados de edicion de celdas | No |
| `get_table_edit_results` | Resultados de edicion de tabla | No |
| `get_table_links_edit_results` | Resultados de links de tabla | Si |
| `get_table_reapply_filter_results` | Resultados de reaplicacion de filtros | No |
| `get_range_link_edit_results` | Resultados de edicion de range links | Si |
| `get_destination_link_source_conversion_results` | Resultados de conversion | Si |

### Resultados de documentos/presentaciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_patch_document_results` | Resultados de actualizacion de documento | No |
| `get_patch_section_results` | Resultados de actualizacion de seccion | No |
| `get_patch_presentation_results` | Resultados de actualizacion de presentacion | No |
| `get_patch_slide_results` | Resultados de actualizacion de slide | No |
| `get_patch_slide_layout_results` | Resultados de actualizacion de slide layout | No |
| `get_patch_sheet_results` | Resultados de actualizacion de sheet | No |
| `get_patch_spreadsheet_results` | Resultados de actualizacion de spreadsheet | No |
| `get_patch_table_properties_results` | Resultados de actualizacion de tabla | No |

### Resultados de milestones y metricas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_milestone_creation_results` | Resultados de creacion de milestone | Si |
| `get_batch_upsertion_metric_values_results` | Resultados de upsert de metricas | Si |

## Ejemplo

### Consultar estado de operacion

```python
operation = client.operations.get_operation_by_id(operation_id="op-123")
print(f"Estado: {operation.status}")
print(f"Recurso: {operation.resource_url}")
```

### Obtener resultados de copia (auto-paginacion)

```python
# Despues de completar un copy_file
results = client.operations.get_copy_file_results(operation_id="op-123")

for item in results.data:
    print(f"Archivo copiado: {item}")
```
