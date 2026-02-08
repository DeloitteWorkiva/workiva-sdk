# Documents

`client.documents` — Gestión de documentos y sus secciones en la plataforma Workiva.

Los documentos permiten organizar y revisar datos con texto enlazado, documentos e imágenes de forma colaborativa.

## Operaciones

### Documentos

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_documents` | Listar documentos | Sí |
| `get_document_by_id` | Obtener documento por ID | No |
| `partially_update_document_by_id` | Actualizar documento parcialmente | No |
| `document_export` | Exportar documento | No |
| `document_filters_reapplication` | Reaplicar filtros del documento | No |
| `document_links_publication` | Publicar links del documento | No |
| `document_permissions_modification` | Modificar permisos del documento | No |
| `get_document_milestones` | Listar milestones del documento | Sí |
| `get_document_permissions` | Listar permisos del documento | Sí |

### Secciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_sections` | Listar secciones | Sí |
| `get_section_by_id` | Obtener sección por ID | No |
| `create_section` | Crear sección | No |
| `copy_section` | Copiar sección | No |
| `partially_update_section_by_id` | Actualizar sección parcialmente | No |
| `delete_section_by_id` | Eliminar sección | No |
| `edit_sections` | Editar secciones | No |
| `section_permissions_modification` | Modificar permisos de sección | No |
| `get_section_permissions` | Listar permisos de sección | Sí |

## Ejemplos

### Listar documentos

```python
response = client.documents.get_documents()

for doc in response.result.data:
    print(f"{doc.name} (ID: {doc.id})")
```

### Exportar documento

```python
response = client.documents.document_export(
    document_id="doc-123",
    document_export={
        "format": "pdf",
    },
)

# Operación 202
operation = client.wait(response).result(timeout=120)
print(f"Exportado: {operation.resource_url}")
```

### Crear sección

```python
response = client.documents.create_section(
    document_id="doc-123",
    section={
        "name": "Nueva Sección",
    },
)
print(f"Sección creada: {response.result.id}")
```

### Copiar sección (operación 202)

```python
response = client.documents.copy_section(
    document_id="doc-123",
    section_id="sec-456",
    section_copy={"destination_document_id": "doc-789"},
)

operation = client.wait(response).result(timeout=300)
```
