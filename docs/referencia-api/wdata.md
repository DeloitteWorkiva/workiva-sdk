# Wdata

Todas las operaciones de la API de Wdata estan disponibles en un **unico namespace**: `client.wdata`.

| Namespace | Atributo |
|-----------|----------|
| Wdata | `client.wdata` |

> Los endpoints de Wdata usan una URL base distinta a Platform. El SDK rutea automaticamente.

## `client.wdata` -- Todas las operaciones

### Tablas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_tables` | Listar tablas | Si |
| `get_table` | Obtener tabla por ID | No |
| `create_table` | Crear tabla | No |
| `update_table` | Actualizar tabla | No |
| `delete_table` | Eliminar tabla | No |
| `validate_tables` | Validar tablas | No |

### Tablas compartidas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_shared_tables` | Listar tablas compartidas | Si |
| `get_shared_table` | Obtener tabla compartida | No |
| `create_shared_table` | Crear tabla compartida | No |
| `delete_shared_table` | Eliminar tabla compartida | No |

### Queries

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_queries` | Listar queries | Si |
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
| `list_query_results` | Listar resultados de query | Si |
| `get_tables_dependent_on_query` | Tablas dependientes de query | Si |
| `download_query_result` | Descargar resultado | No |
| `export_query_result_to_spreadsheets` | Exportar resultado a spreadsheet | No |
| `get_workspace_query_usage` | Uso de queries del workspace | No |

### Archivos

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_files` | Listar archivos | Si |
| `get_file` | Obtener archivo | No |
| `upload_file` | Subir archivo | No |
| `download_file` | Descargar archivo | No |
| `delete_file` | Eliminar archivo | No |
| `validate_filename` | Validar nombre de archivo | No |
| `validate_files` | Validar archivos | No |
| `find_workspace_files_by_size` | Archivos por tamano | Si |
| `get_workspace_upload_usage` | Uso de uploads | No |

### Carpetas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_folders` | Listar carpetas | Si |
| `get_folder` | Obtener carpeta | No |
| `create_folder` | Crear carpeta | No |
| `update_folder` | Actualizar carpeta | No |
| `delete_folder` | Eliminar carpeta | No |
| `list_children` | Listar hijos de carpeta | Si |
| `set_children` | Establecer hijos | No |

### Conexiones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_connections` | Listar conexiones | Si |
| `get_connection` | Obtener conexion | No |
| `refresh_connection` | Refrescar conexion | No |
| `refresh_batch` | Refrescar batch | No |
| `get_refresh_status` | Estado de refresco | No |
| `get_refresh_batch_status` | Estado de refresco batch | No |
| `get_dependencies` | Listar dependencias | Si |
| `get_dependents` | Listar dependientes | Si |

### Parametros

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_parameters` | Listar parametros | Si |
| `get_parameter` | Obtener parametro | No |
| `create_parameter` | Crear parametro | No |
| `update_parameter` | Actualizar parametro | No |
| `delete_parameter` | Eliminar parametro | No |

### Vistas pivot

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_pivot_views` | Listar vistas pivot | Si |
| `get_pivot_view` | Obtener vista pivot por ID | No |
| `create_pivot_view` | Crear vista pivot | No |
| `update_pivot_view` | Actualizar vista pivot | No |
| `delete_pivot_view` | Eliminar vista pivot | No |

### Listas de seleccion

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_select_lists` | Listar listas de seleccion | Si |
| `get_select_list` | Obtener lista de seleccion por ID | No |
| `create_select_list` | Crear lista de seleccion | No |
| `update_select_list` | Actualizar lista de seleccion | No |
| `delete` | Eliminar lista de seleccion | No |

### Tags

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `list_tags` | Listar tags | Si |
| `create_tag` | Crear tag | No |
| `update_tag` | Actualizar tag | No |
| `delete_tag` | Eliminar tag | No |

### Import/Export de tablas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `import_file` | Importar archivo a tabla | No |
| `unimport_file` | Desimportar archivo de tabla | No |
| `get_import_info` | Informacion de importacion de tabla | No |
| `import_from_spreadsheets` | Importar desde spreadsheet a tabla | No |
| `export_file_to_spreadsheets` | Exportar archivo a spreadsheet | No |

### Tokens y descargas

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `create_token` | Crear token de descarga | No |
| `download_file` | Descargar archivo por token | No |

### Administracion de workspace

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `import_data` | Importar datos al workspace | No |
| `export_workspace` | Exportar workspace completo | No |
| `delete_workspace` | Eliminar workspace | No |

### Utilidades

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `search` | Buscar entidades | Si |
| `get_errors` | Listar errores de importacion | Si |
| `parse_date` | Parsear fecha | No |
| `health_check` | Estado del servicio | No |

## Ejemplos

### Listar tablas (auto-paginacion)

```python
# Devuelve TODAS las tablas, no solo la primera pagina
result = client.wdata.get_tables()

for table in result.body:
    print(f"Tabla: {table.name} (ID: {table.id})")
```

### Crear y ejecutar una query

```python
# Crear query
query = client.wdata.create_query(
    name="Mi Query",
    query_text="SELECT * FROM mi_tabla",
)

# Ejecutar
client.wdata.run_query(query_id=query.id)

# Obtener resultados
result = client.wdata.get_query_result(query_id=query.id)
```

### Importar datos

```python
client.wdata.import_data(
    table_id="tbl-123",
    body=data,
)
```

### Gestion de carpetas

```python
# Crear carpeta
folder = client.wdata.create_folder(
    name="Datos Q4",
)

# Listar carpetas (auto-paginacion)
result = client.wdata.list_folders()

# Listar contenido de una carpeta (auto-paginacion)
result = client.wdata.list_children(folder_id="folder-123")
```

### Buscar en Wdata (auto-paginacion)

```python
result = client.wdata.search(
    name="revenue",
)
```
