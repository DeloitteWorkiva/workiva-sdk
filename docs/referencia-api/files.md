# Files

`client.files` -- Gestion de archivos y carpetas en Workiva.

## Operaciones

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_files` | Listar archivos | Si | No |
| `get_file_by_id` | Obtener archivo por ID | No | No |
| `create_file` | Crear archivo | No | No |
| `partially_update_file_by_id` | Actualizar archivo parcialmente | No | No |
| `copy_file` | Copiar archivo | No | Si |
| `import_file` | Importar archivo | No | Si |
| `export_file_by_id` | Exportar archivo | No | Si |
| `file_permissions_modification` | Modificar permisos | No | Si |
| `get_file_permissions` | Listar permisos del archivo | Si | No |
| `get_trashed_files` | Listar archivos en papelera | Si | No |
| `trash_file_by_id` | Mover archivo a papelera | No | Si |
| `restore_file_by_id` | Restaurar archivo de papelera | No | Si |

## Ejemplos

### Listar archivos

```python
# Auto-paginacion transparente: devuelve TODOS los archivos
result = client.files.get_files()

for file in result.data:
    print(f"{file.name} ({file.kind}) - ID: {file.id}")

print(f"Total: {len(result.data)} archivos")
```

### Obtener un archivo

```python
file = client.files.get_file_by_id(file_id="file-123")
print(f"Nombre: {file.name}")
print(f"Tipo: {file.kind}")
print(f"Creado: {file.created}")
```

### Copiar archivo (operacion 202)

```python
response = client.files.copy_file(
    file_id="file-123",
    destination_container="ws-456",
)

# Esperar resultado
operation = client.wait(response).result(timeout=300)
print(f"Copiado: {operation.resource_url}")

# Consultar resultados detallados
results = client.operations.get_copy_file_results(
    operation_id=operation.id,
)
```

### Importar archivo (operacion 202)

```python
response = client.files.import_file(
    file_name="report.xlsx",
    kind="Spreadsheet",
)

operation = client.wait(response).result(timeout=120)
```

### Exportar archivo (operacion 202)

```python
response = client.files.export_file_by_id(
    file_id="file-123",
    kind="Document",
    document_export={"format": "pdf"},
)

operation = client.wait(response).result(timeout=120)
print(f"URL de descarga: {operation.resource_url}")
```

### Papelera (operaciones 202)

```python
from workiva.models.platform import FileTrashOptions, FileRestoreOptions

# Mover a papelera
response = client.files.trash_file_by_id(
    file_id="file-123",
    body=FileTrashOptions(),
)
client.wait(response).result(timeout=120)

# Listar archivos en papelera (auto-paginacion)
result = client.files.get_trashed_files()

# Restaurar
response = client.files.restore_file_by_id(
    file_id="file-123",
    body=FileRestoreOptions(destination_folder_id="folder-456"),
)
client.wait(response).result(timeout=120)
```
