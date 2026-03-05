# Documents

`client.documents` -- Gestion de documentos y sus secciones en la plataforma Workiva.

## Operaciones

### Documentos

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_documents` | Listar documentos | Si | No |
| `get_document_by_id` | Obtener documento por ID | No | No |
| `partially_update_document_by_id` | Actualizar documento parcialmente | No | No |
| `document_export` | Exportar documento | No | Si |
| `document_filters_reapplication` | Reaplicar filtros del documento | No | Si |
| `document_links_publication` | Publicar links del documento | No | Si |
| `document_permissions_modification` | Modificar permisos del documento | No | Si |
| `get_document_milestones` | Listar milestones del documento | Si | No |
| `get_document_permissions` | Listar permisos del documento | Si | No |

### Secciones

| Metodo | Descripcion | Paginado | 202 |
|--------|-------------|----------|-----|
| `get_sections` | Listar secciones | Si | No |
| `get_section_by_id` | Obtener seccion por ID | No | No |
| `create_section` | Crear seccion | No | No |
| `copy_section` | Copiar seccion | No | Si |
| `partially_update_section_by_id` | Actualizar seccion parcialmente | No | No |
| `delete_section_by_id` | Eliminar seccion | No | No |
| `edit_sections` | Editar secciones | No | Si |
| `section_permissions_modification` | Modificar permisos de seccion | No | Si |
| `get_section_permissions` | Listar permisos de seccion | Si | No |

## Ejemplos

### Listar documentos (auto-paginacion)

```python
result = client.documents.get_documents()

for doc in result.data:
    print(f"{doc.name} (ID: {doc.id})")
```

### Exportar documento

```python
response = client.documents.document_export(
    document_id="doc-123",
    format_="pdf",
)

# Operacion 202
operation = client.wait(response).result(timeout=120)
print(f"Exportado: {operation.resource_url}")
```

### Crear seccion

```python
section = client.documents.create_section(
    document_id="doc-123",
    name="Nueva Seccion",
)
print(f"Seccion creada: {section.id}")
```

### Copiar seccion (operacion 202)

```python
response = client.documents.copy_section(
    document_id="doc-123",
    section_id="sec-456",
    document="doc-789",
)

operation = client.wait(response).result(timeout=300)
```
