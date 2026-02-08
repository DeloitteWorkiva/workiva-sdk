# Spreadsheets

`client.spreadsheets` — Gestión de hojas de cálculo, sheets, datos y datasets.

## Operaciones

### Spreadsheets

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_spreadsheets` | Listar spreadsheets | Sí | No |
| `get_spreadsheet_by_id` | Obtener spreadsheet por ID | No | No |
| `partially_update_spreadsheet_by_id` | Actualizar spreadsheet | No | Sí |
| `spreadsheet_export` | Exportar spreadsheet | No | Sí |
| `spreadsheet_filters_reapplication` | Reaplicar filtros | No | Sí |
| `spreadsheet_links_publication` | Publicar links | No | Sí |
| `spreadsheet_permissions_modification` | Modificar permisos | No | Sí |
| `get_spreadsheet_permissions` | Listar permisos | Sí | No |
| `get_spreadsheet_milestones` | Listar milestones | Sí | No |

### Sheets

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_sheets` | Listar sheets | Sí | No |
| `get_sheet_by_id` | Obtener sheet por ID | No | No |
| `create_sheet` | Crear sheet | No | No |
| `copy_sheet` | Copiar sheet | No | Sí |
| `partially_update_sheet_by_id` | Actualizar sheet | No | Sí |
| `update_sheet` | Reemplazar sheet | No | No |
| `delete_sheet_by_id` | Eliminar sheet | No | No |
| `sheet_permissions_modification` | Modificar permisos | No | Sí |
| `get_sheet_permissions` | Listar permisos | Sí | No |

### Datos

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_sheet_data` | Obtener datos del sheet | Sí |
| `get_values_by_range` | Obtener valores por rango | Sí |
| `update_values_by_range` | Actualizar valores por rango | No |

### Datasets

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_datasets` | Listar datasets | No |
| `upsert_datasets` | Upsert de datasets | No |
| `delete_dataset_by_sheet_id` | Eliminar dataset | No |

## Ejemplos

### Listar spreadsheets

```python
response = client.spreadsheets.get_spreadsheets()

for ss in response.result.data:
    print(f"{ss.name} (ID: {ss.id})")
```

### Obtener datos de un sheet

```python
response = client.spreadsheets.get_sheet_data(
    spreadsheet_id="ss-123",
    sheet_id="sheet-456",
)

for row in response.result.data:
    print(row)

# Paginar si hay muchos datos
while response.next is not None:
    response = response.next()
```

### Obtener valores por rango

```python
response = client.spreadsheets.get_values_by_range(
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
    cell_range=values_data,
)
```

### Exportar spreadsheet (operación 202)

```python
response = client.spreadsheets.spreadsheet_export(
    spreadsheet_id="ss-123",
    spreadsheet_export={"format": "xlsx"},
)

operation = client.wait(response).result(timeout=120)
print(f"Exportado: {operation.resource_url}")
```
