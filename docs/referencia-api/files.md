# Files

`client.files` — Gestión de archivos y carpetas en Workiva.

## Operaciones

| Método | Descripción | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_files` | Listar archivos | Sí | No |
| `get_file_by_id` | Obtener archivo por ID | No | No |
| `create_file` | Crear archivo | No | No |
| `partially_update_file_by_id` | Actualizar archivo parcialmente | No | No |
| `copy_file` | Copiar archivo | No | Sí |
| `import_file` | Importar archivo | No | Sí |
| `export_file_by_id` | Exportar archivo | No | Sí |
| `file_permissions_modification` | Modificar permisos | No | Sí |
| `get_file_permissions` | Listar permisos del archivo | Sí | No |
| `get_trashed_files` | Listar archivos en papelera | Sí | No |
| `trash_file_by_id` | Mover archivo a papelera | No | No |
| `restore_file_by_id` | Restaurar archivo de papelera | No | No |

## Ejemplos

### Listar archivos

```python
response = client.files.get_files()

for file in response.result.data:
    print(f"{file.name} ({file.kind}) - ID: {file.id}")

# Paginar
while response.next is not None:
    response = response.next()
    for file in response.result.data:
        print(f"{file.name}")
```

### Obtener un archivo

```python
response = client.files.get_file_by_id(file_id="file-123")
file = response.result
print(f"Nombre: {file.name}")
print(f"Tipo: {file.kind}")
print(f"Creado: {file.created}")
```

### Copiar archivo (operación 202)

```python
from workiva.models import FileCopy

response = client.files.copy_file(
    file_id="file-123",
    file_copy=FileCopy(
        workspace_id="ws-456",
    ),
)

# Esperar resultado
operation = client.wait(response).result(timeout=300)
print(f"Copiado: {operation.resource_url}")

# Consultar resultados detallados
results = client.operations.get_copy_file_results(
    operation_id=operation.id,
)
```

### Importar archivo (operación 202)

```python
response = client.files.import_file(
    file_id="file-123",
    file_import=import_data,
)

operation = client.wait(response).result(timeout=120)
```

### Exportar archivo (operación 202)

```python
response = client.files.export_file_by_id(
    file_id="file-123",
    file_export_by_id={"format": "pdf"},
)

operation = client.wait(response).result(timeout=120)
print(f"URL de descarga: {operation.resource_url}")
```

### Papelera

```python
# Mover a papelera
client.files.trash_file_by_id(file_id="file-123")

# Listar archivos en papelera
response = client.files.get_trashed_files()

# Restaurar
client.files.restore_file_by_id(
    file_id="file-123",
    file_restore_options={"destination_folder_id": "folder-456"},
)
```
