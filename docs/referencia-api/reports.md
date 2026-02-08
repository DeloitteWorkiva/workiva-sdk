# Reports

`client.reports` — Generación de reportes administrativos.

## Operaciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_org_report_users` | Listar usuarios en reporte de organización | Sí |

> Este endpoint usa paginación estilo JSON:API (Patrón B), diferente al resto de Platform.

## Ejemplo

```python
response = client.reports.get_org_report_users(
    organization_id="org-123",
    report_type="users",
)

for user in response.result.data:
    print(f"Usuario: {user}")

# Paginar (funciona igual que el resto)
while response.next is not None:
    response = response.next()
```
