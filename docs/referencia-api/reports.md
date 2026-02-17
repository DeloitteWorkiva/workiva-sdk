# Reports

`client.reports` -- Generacion de reportes administrativos.

## Operaciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_org_report_users` | Listar usuarios en reporte de organizacion | Si |

> Este endpoint usa paginacion estilo JSON:API (Patron B), pero la auto-paginacion funciona igual que el resto.

## Ejemplo

```python
# Auto-paginacion transparente
result = client.reports.get_org_report_users(
    organization_id="org-123",
    report_type="users",
)

for user in result.data:
    print(f"Usuario: {user}")
```
