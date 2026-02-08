# Inicio rápido

Instalación y primer request en menos de 2 minutos.

## Instalación

```bash
# Con pip
pip install workiva

# Con uv (recomendado)
uv add workiva
```

## Obtener credenciales

Necesitas un **client_id** y **client_secret** de OAuth2:

1. Ingresa a tu cuenta de Workiva
2. Ve a **Organization Admin** > **API Applications**
3. Crea una nueva aplicación o usa una existente
4. Copia el **Client ID** y **Client Secret**

> Las credenciales se intercambian automáticamente por un bearer token. El SDK maneja el ciclo de vida del token por ti.

## Primer request

```python
from workiva import Workiva

# Crear el cliente — el token se obtiene automáticamente
with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # Listar workspaces de la organización
    response = client.admin.get_workspaces()

    for workspace in response.result.data:
        print(f"Workspace: {workspace.name} (ID: {workspace.id})")
```

## Ejemplo completo: listar archivos de un workspace

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # Obtener archivos
    response = client.files.get_files()

    for file in response.result.data:
        print(f"  {file.name} ({file.kind})")

    # Si hay más páginas, iterar
    while response.next is not None:
        response = response.next()
        for file in response.result.data:
            print(f"  {file.name} ({file.kind})")
```

## Ejemplo con uso asíncrono

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
        response = await client.admin.get_workspaces_async()
        for ws in response.result.data:
            print(ws.name)

asyncio.run(main())
```

## Variables de entorno (recomendado)

No hardcodees las credenciales. Usa variables de entorno:

```python
import os
from workiva import Workiva

client = Workiva(
    client_id=os.environ["WORKIVA_CLIENT_ID"],
    client_secret=os.environ["WORKIVA_CLIENT_SECRET"],
)
```

## Siguiente paso

- [Autenticación](autenticacion.md) — Detalles del flujo OAuth2
- [Configuración](configuracion.md) — Servidores, timeouts, reintentos
