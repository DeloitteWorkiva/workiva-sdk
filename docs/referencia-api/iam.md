# IAM

`client.iam` -- Tokens de acceso OAuth2.

> Normalmente NO necesitas usar este namespace directamente. El SDK obtiene y renueva tokens automaticamente a traves de `OAuth2ClientCredentials`. Este endpoint existe para casos avanzados donde necesitas gestionar tokens manualmente.

## Operaciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `token_request` | Solicitar token de acceso | No |

## Ejemplo

### Obtener token manualmente

```python
token = client.iam.token_request(
    body={
        "grant_type": "client_credentials",
        "client_id": "tu_client_id",
        "client_secret": "tu_client_secret",
    },
)

print(f"Token: {token.access_token}")
print(f"Tipo: {token.token_type}")
print(f"Expira en: {token.expires_in}s")
```

> En la practica, usa `Workiva(client_id=..., client_secret=...)` y deja que el SDK maneje los tokens automaticamente. Ver [Autenticacion](../autenticacion.md).
