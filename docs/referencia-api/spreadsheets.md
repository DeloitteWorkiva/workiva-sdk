# Spreadsheets

`client.spreadsheets` -- Gestion de hojas de calculo, sheets, datos y datasets.

## Operaciones

### Spreadsheets

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_spreadsheets` | Listar spreadsheets | Si | No |
| `get_spreadsheet_by_id` | Obtener spreadsheet por ID | No | No |
| `partially_update_spreadsheet_by_id` | Actualizar spreadsheet | No | Si |
| `spreadsheet_export` | Exportar spreadsheet | No | Si |
| `spreadsheet_filters_reapplication` | Reaplicar filtros | No | Si |
| `spreadsheet_links_publication` | Publicar links | No | Si |
| `spreadsheet_permissions_modification` | Modificar permisos | No | Si |
| `get_spreadsheet_permissions` | Listar permisos | Si | No |
| `get_spreadsheet_milestones` | Listar milestones | Si | No |

### Sheets

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_sheets` | Listar sheets | Si | No |
| `get_sheet_by_id` | Obtener sheet por ID | No | No |
| `create_sheet` | Crear sheet | No | No |
| `copy_sheet` | Copiar sheet | No | Si |
| `partially_update_sheet_by_id` | Actualizar sheet | No | Si |
| `update_sheet` | Reemplazar sheet | No | No |
| `delete_sheet_by_id` | Eliminar sheet | No | No |
| `sheet_permissions_modification` | Modificar permisos | No | Si |
| `get_sheet_permissions` | Listar permisos | Si | No |

### Datos

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_sheet_data` | Obtener datos del sheet | Si |
| `get_values_by_range` | Obtener valores por rango | Si |
| `update_values_by_range` | Actualizar valores por rango | No |

### Datasets

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_datasets` | Listar datasets | No |
| `upsert_datasets` | Upsert de datasets | No |
| `delete_dataset_by_sheet_id` | Eliminar dataset | No |

## Ejemplos

### Listar spreadsheets (auto-paginacion)

```python
result = client.spreadsheets.get_spreadsheets()

for ss in result.data:
    print(f"{ss.name} (ID: {ss.id})")
```

### Obtener datos de un sheet (auto-paginacion)

```python
result = client.spreadsheets.get_sheet_data(
    spreadsheet_id="ss-123",
    sheet_id="sheet-456",
)

for row in result.data:
    print(row)
```

### Obtener valores por rango

```python
result = client.spreadsheets.get_values_by_range(
    spreadsheet_id="ss-123",
    sheet_id="sheet-456",
    range_="A1:D10",
)
```

### Actualizar valores

```python
client.spreadsheets.update_values_by_range(
    spreadsheet_id="ss-123",
    sheet_id="sheet-456",
    range_="A1:B2",
    body=values_data,
)
```

### Exportar spreadsheet (operacion 202)

```python
response = client.spreadsheets.spreadsheet_export(
    spreadsheet_id="ss-123",
    body={"format": "xlsx"},
)

operation = client.wait(response).result(timeout=120)
print(f"Exportado: {operation.resource_url}")
```
