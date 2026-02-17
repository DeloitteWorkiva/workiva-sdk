# Inicio rapido

Instalacion y primer request en menos de 2 minutos.

## Instalacion

```bash
# Con uv (recomendado)
uv add workiva

# Con pip
pip install workiva
```

## Obtener credenciales

Necesitas un **client_id** y **client_secret** de OAuth2:

1. Ingresa a tu cuenta de Workiva
2. Ve a **Organization Admin** > **API Applications**
3. Crea una nueva aplicacion o usa una existente
4. Copia el **Client ID** y **Client Secret**

> Las credenciales se intercambian automaticamente por un bearer token. El SDK maneja todo el ciclo de vida del token por ti: obtencion, cache, refresco antes de expirar y reintento ante 401.

## Primer request

```python
from workiva import Workiva

# Crear el cliente -- el token se obtiene automaticamente al primer request
with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # Listar archivos del workspace
    result = client.files.get_files()

    for file in result.data:
        print(f"Archivo: {file.name} (Tipo: {file.kind})")
```

Puntos clave:

- `client.files.get_files()` devuelve un modelo tipado `FilesListResult`
- `result.data` es una lista de objetos `File` con autocompletado
- **No hay `.result.data`**, no hay objetos intermedios -- accedes a `.data` directamente

## Auto-paginacion transparente

El SDK pagina automaticamente. Una sola llamada devuelve TODOS los items de todas las paginas:

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # Esto devuelve TODOS los archivos, no solo la primera pagina
    result = client.files.get_files()
    print(f"Total de archivos: {len(result.data)}")

    for file in result.data:
        print(f"  {file.name} ({file.kind})")
```

> El SDK itera internamente todas las paginas (hasta un maximo de seguridad de 1000 paginas) y te devuelve el resultado completo.

Para controlar el tamano de pagina de cada request al servidor, usa el parametro `maxpagesize`:

```python
# Paginas de 100 items cada una (el SDK sigue iterando todas automaticamente)
result = client.files.get_files(maxpagesize=100)
```

## Ejemplo asincrono

Todos los metodos tienen una variante asincrona con el sufijo `_async`:

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
        # Nota el sufijo _async y el await
        result = await client.files.get_files_async()

        for file in result.data:
            print(f"{file.name} ({file.kind})")

asyncio.run(main())
```

Puntos clave del modo asincrono:

- Usa `async with` en lugar de `with` para el context manager
- Todos los metodos tienen su version `_async`: `get_files_async()`, `copy_file_async()`, etc.
- La autenticacion en modo async usa `asyncio.to_thread` para no bloquear el event loop

## Operaciones de larga duracion

Algunas operaciones (copiar archivos, exportar, etc.) devuelven HTTP 202. Usa `client.wait()` para hacer polling:

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # copy_file devuelve httpx.Response (HTTP 202)
    response = client.files.copy_file(file_id="abc123", destination_container="folder-456")

    # wait() extrae el operation ID del header Location
    # result() hace polling hasta que la operacion termine o pase el timeout
    operation = client.wait(response).result(timeout=300)

    print(f"Estado: {operation.status}")          # "completed"
    print(f"Recurso: {operation.resource_url}")   # URL del resultado
```

## Variables de entorno (recomendado)

Nunca hardcodees las credenciales en tu codigo. Usa variables de entorno:

```bash
export WORKIVA_CLIENT_ID="tu_client_id"
export WORKIVA_CLIENT_SECRET="tu_client_secret"
```

```python
import os
from workiva import Workiva

with Workiva(
    client_id=os.environ["WORKIVA_CLIENT_ID"],
    client_secret=os.environ["WORKIVA_CLIENT_SECRET"],
) as client:
    result = client.files.get_files()
```

## Seleccion de region

Por defecto el SDK se conecta a la region EU. Para cambiarla:

```python
from workiva import Workiva, Region

# Region US
with Workiva(
    client_id="...",
    client_secret="...",
    region=Region.US,
) as client:
    result = client.files.get_files()
```

Regiones disponibles: `Region.EU` (default), `Region.US`, `Region.APAC`.

## Siguiente paso

- [Autenticacion](autenticacion.md) -- Detalles del flujo OAuth2, token caching, thread safety
- [Configuracion](configuracion.md) -- Regiones, timeouts, reintentos, clientes HTTP custom
