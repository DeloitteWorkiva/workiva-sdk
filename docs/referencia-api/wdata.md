# Wdata

`client.wdata` — Gestión de datos en Wdata: tablas, queries, imports/exports, carpetas, parámetros y más.

Wdata es el motor de datos de Workiva. Este namespace es el más extenso del SDK con 56+ operaciones.

> Los endpoints de Wdata usan una URL base distinta a Platform. El SDK rutea automáticamente.

## Operaciones

### Tablas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_tables` | Listar tablas | Sí |
| `get_table` | Obtener tabla por ID | No |
| `create_table` | Crear tabla | No |
| `update_table` | Actualizar tabla | No |
| `delete_table` | Eliminar tabla | No |
| `validate_tables` | Validar tablas | No |

### Tablas compartidas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_shared_tables` | Listar tablas compartidas | Sí |
| `get_shared_table` | Obtener tabla compartida | No |
| `create_shared_table` | Crear tabla compartida | No |
| `delete_shared_table` | Eliminar tabla compartida | No |

### Queries

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_queries` | Listar queries | Sí |
| `get_query` | Obtener query por ID | No |
| `create_query` | Crear query | No |
| `update_query` | Actualizar query | No |
| `delete_query` | Eliminar query | No |
| `run_query` | Ejecutar query | No |
| `cancel_query` | Cancelar query | No |
| `describe_query` | Describir query | No |
| `is_query_valid` | Validar query | No |
| `get_query_result` | Obtener resultado de query | No |
| `get_query_column_data` | Obtener datos de columna | No |
| `list_query_results` | Listar resultados de query | Sí |
| `get_tables_dependent_on_query` | Tablas dependientes de query | Sí |
| `download_query_result` | Descargar resultado | No |
| `export_query_result_to_spreadsheets` | Exportar resultado a spreadsheet | No |
| `get_workspace_query_usage` | Uso de queries del workspace | No |

### Imports/Exports

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `import_data` | Importar datos | No |
| `import_file` | Importar archivo | No |
| `import_from_spreadsheets` | Importar desde spreadsheet | No |
| `get_import_info` | Info de importación | No |
| `unimport_file` | Des-importar archivo | No |
| `export_file_to_spreadsheets` | Exportar a spreadsheet | No |
| `export_workspace` | Exportar workspace | No |

### Archivos

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_files` | Listar archivos | Sí |
| `get_file` | Obtener archivo | No |
| `upload_file` | Subir archivo | No |
| `download_file` | Descargar archivo | No |
| `delete_file` | Eliminar archivo | No |
| `validate_filename` | Validar nombre de archivo | No |
| `validate_files` | Validar archivos | No |
| `find_workspace_files_by_size` | Archivos por tamaño | Sí |
| `get_workspace_upload_usage` | Uso de uploads | No |

### Carpetas

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_folders` | Listar carpetas | Sí |
| `get_folder` | Obtener carpeta | No |
| `create_folder` | Crear carpeta | No |
| `update_folder` | Actualizar carpeta | No |
| `delete_folder` | Eliminar carpeta | No |
| `list_children` | Listar hijos de carpeta | Sí |
| `set_children` | Establecer hijos | No |

### Parámetros

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_parameters` | Listar parámetros | Sí |
| `get_parameter` | Obtener parámetro | No |
| `create_parameter` | Crear parámetro | No |
| `update_parameter` | Actualizar parámetro | No |
| `delete_parameter` | Eliminar parámetro | No |

### Select Lists

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_select_lists` | Listar select lists | Sí |
| `get_select_list` | Obtener select list | No |
| `create_select_list` | Crear select list | No |
| `update_select_list` | Actualizar select list | No |

### Pivot Views

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_pivot_views` | Listar pivot views | Sí |
| `get_pivot_view` | Obtener pivot view | No |
| `create_pivot_view` | Crear pivot view | No |
| `update_pivot_view` | Actualizar pivot view | No |
| `delete_pivot_view` | Eliminar pivot view | No |

### Tags

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_tags` | Listar tags | Sí |
| `create_tag` | Crear tag | No |
| `update_tag` | Actualizar tag | No |
| `delete_tag` | Eliminar tag | No |

### Conexiones y dependencias

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `list_connections` | Listar conexiones | Sí |
| `get_connection` | Obtener conexión | No |
| `refresh_connection` | Refrescar conexión | No |
| `refresh_batch` | Refrescar batch | No |
| `get_refresh_status` | Estado de refresco | No |
| `get_refresh_batch_status` | Estado de refresco batch | No |
| `get_dependencies` | Listar dependencias | Sí |
| `get_dependents` | Listar dependientes | Sí |

### Otros

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `search` | Buscar en Wdata | Sí |
| `get_errors` | Listar errores | Sí |
| `create_token` | Crear token de Wdata | No |
| `parse_date` | Parsear fecha | No |
| `health_check` | Health check | No |
| `delete_workspace` | Eliminar workspace de Wdata | No |
| `delete` | Eliminar recurso | No |

## Ejemplos

### Listar tablas

```python
response = client.wdata.get_tables()

for table in response.result.data:
    print(f"Tabla: {table.name} (ID: {table.id})")

# Paginar
while response.next is not None:
    response = response.next()
```

### Crear y ejecutar una query

```python
# Crear query
response = client.wdata.create_query(
    query={"name": "Mi Query", "query_string": "SELECT * FROM mi_tabla"},
)
query_id = response.result.data.id

# Ejecutar
response = client.wdata.run_query(query_id=query_id)

# Obtener resultados
result = client.wdata.get_query_result(query_id=query_id)
```

### Importar datos

```python
response = client.wdata.import_data(
    table_id="tbl-123",
    import_data=data,
)
```

### Subir archivo

```python
response = client.wdata.upload_file(
    file_upload=file_data,
)
```

### Buscar en Wdata

```python
response = client.wdata.search(
    search_request={"query": "revenue"},
)

for result in response.result.data:
    print(result)

while response.next is not None:
    response = response.next()
```

### Gestión de carpetas

```python
# Crear carpeta
response = client.wdata.create_folder(
    folder={"name": "Datos Q4"},
)

# Listar carpetas
response = client.wdata.list_folders()

# Listar contenido de una carpeta
response = client.wdata.list_children(folder_id="folder-123")
```
