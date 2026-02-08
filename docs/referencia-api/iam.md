# IAM

`client.iam` — Tokens de acceso OAuth2.

> Normalmente NO necesitas usar este namespace directamente. El SDK obtiene y renueva tokens automáticamente a través del hook `ClientCredentialsHook`. Este endpoint existe para casos avanzados donde necesitas gestionar tokens manualmente.

## Operaciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `token_request` | Solicitar token de acceso | No |

## Ejemplo

### Obtener token manualmente

```python
response = client.iam.token_request(
    grant_type="client_credentials",
    client_id="tu_client_id",
    client_secret="tu_client_secret",
)

print(f"Token: {response.result.access_token}")
print(f"Tipo: {response.result.token_type}")
print(f"Expira en: {response.result.expires_in}s")
```

> En la práctica, usa `Workiva(client_id=..., client_secret=...)` y deja que el SDK maneje los tokens automáticamente. Ver [Autenticación](../autenticacion.md).
