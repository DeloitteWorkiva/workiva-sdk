# Test Forms

`client.test_forms` -- Gestion de formularios de prueba, fases, matrices y muestras.

## Operaciones

### Formularios de prueba

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_test_forms` | Listar formularios | No |
| `get_test_form_by_id` | Obtener formulario por ID | No |
| `test_form_export` | Exportar formulario | No |

### Fases de prueba

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_test_phases` | Listar fases | No |
| `get_test_phase_by_id` | Obtener fase por ID | No |
| `get_test_phase_attachments` | Listar adjuntos de fase | No |
| `get_test_phase_attachment_by_id` | Obtener adjunto por ID | No |
| `test_phase_attachment_upload` | Subir adjunto a fase | No |
| `test_phase_attachment_download_by_id` | Descargar adjunto | No |
| `test_phase_attachment_export_by_id` | Exportar adjunto | No |

### Matrices

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_matrices` | Listar matrices | No |
| `get_matrix_by_id` | Obtener matriz por ID | No |
| `create_matrix` | Crear matriz | No |
| `get_matrix_attachments` | Listar adjuntos de matriz | No |
| `get_matrix_attachment_by_id` | Obtener adjunto por ID | No |
| `matrix_attachment_upload` | Subir adjunto a matriz | No |
| `matrix_attachment_download_by_id` | Descargar adjunto | No |
| `matrix_attachment_export_by_id` | Exportar adjunto | No |

### Muestras

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_samples` | Listar muestras | No |
| `get_sample_by_id` | Obtener muestra por ID | No |
| `create_sample` | Crear muestra | No |
| `partially_update_sample_by_id` | Actualizar muestra | No |
| `sample_insertion` | Insertar muestra | No |
| `sample_update` | Actualizar muestra (completa) | No |
| `get_sample_attachments` | Listar adjuntos de muestra | No |
| `get_sample_attachment_by_id` | Obtener adjunto por ID | No |
| `sample_attachment_upload` | Subir adjunto | No |
| `sample_attachment_download_by_id` | Descargar adjunto | No |
| `sample_attachment_export_by_id` | Exportar adjunto | No |

## Ejemplo

### Listar formularios de prueba

```python
result = client.test_forms.get_test_forms(workspace_id="ws-123")

for form in result.data:
    print(f"Formulario: {form.name} (ID: {form.id})")
```

### Obtener fases de un formulario

```python
result = client.test_forms.get_test_phases(test_form_id="tf-123")

for phase in result.data:
    print(f"Fase: {phase.name}")
```

### Crear una muestra

```python
client.test_forms.create_sample(
    test_form_id="tf-123",
    test_phase_id="tp-456",
    matrix_id="mx-789",
    body=sample_data,
)
```

### Subir adjunto a una fase

```python
client.test_forms.test_phase_attachment_upload(
    test_form_id="tf-123",
    test_phase_id="tp-456",
    body=attachment_data,
)
```
