# Operations

`client.operations` — Consultar el estado de operaciones asíncronas y obtener resultados.

Este namespace es el complemento de las operaciones 202. Cuando una operación (copy, import, export, etc.) se completa, puedes consultar sus resultados detallados aquí.

> Para polling automático, usa `client.wait(response).result()`. Este namespace se usa para consultas manuales o para obtener resultados detallados después de que el polling termine.

## Operaciones

### Estado general

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_operation_by_id` | Obtener estado de una operación | No |

### Resultados de archivos

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_copy_file_results` | Resultados de copia de archivo | Sí |
| `get_import_file_results` | Resultados de importación | Sí |
| `get_image_upload_creation_results` | Resultados de subida de imagen | Sí |

### Resultados de contenido

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_rich_text_anchor_creation_results` | Resultados de creación de anchor | Sí |
| `get_rich_text_batch_edit_results` | Resultados de edición batch de rich text | Sí |
| `get_rich_text_duplication_edit_results` | Resultados de duplicación | Sí |
| `get_rich_text_links_batch_edit_results` | Resultados de links batch | Sí |
| `get_table_anchor_creation_results` | Resultados de creación de table anchor | Sí |
| `get_table_cell_edit_results` | Resultados de edición de celdas | No |
| `get_table_edit_results` | Resultados de edición de tabla | No |
| `get_table_links_edit_results` | Resultados de links de tabla | Sí |
| `get_table_reapply_filter_results` | Resultados de reaplicación de filtros | No |
| `get_range_link_edit_results` | Resultados de edición de range links | Sí |
| `get_destination_link_source_conversion_results` | Resultados de conversión | Sí |

### Resultados de documentos/presentaciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_patch_document_results` | Resultados de actualización de documento | No |
| `get_patch_section_results` | Resultados de actualización de sección | No |
| `get_patch_presentation_results` | Resultados de actualización de presentación | No |
| `get_patch_slide_results` | Resultados de actualización de slide | No |
| `get_patch_slide_layout_results` | Resultados de actualización de slide layout | No |
| `get_patch_sheet_results` | Resultados de actualización de sheet | No |
| `get_patch_spreadsheet_results` | Resultados de actualización de spreadsheet | No |
| `get_patch_table_properties_results` | Resultados de actualización de tabla | No |

### Resultados de milestones y métricas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_milestone_creation_results` | Resultados de creación de milestone | Sí |
| `get_batch_upsertion_metric_values_results` | Resultados de upsert de métricas | Sí |

## Ejemplo

### Consultar estado de operación

```python
response = client.operations.get_operation_by_id(
    operation_id="op-123",
)

operation = response.result
print(f"Estado: {operation.status}")
print(f"Recurso: {operation.resource_url}")
```

### Obtener resultados de copia

```python
# Después de completar un copy_file
results = client.operations.get_copy_file_results(
    operation_id="op-123",
)

for result in results.result.data:
    print(f"Archivo copiado: {result}")
```
