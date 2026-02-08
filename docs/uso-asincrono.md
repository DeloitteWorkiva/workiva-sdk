# Uso asíncrono

Todos los métodos del SDK tienen una variante asíncrona con el sufijo `_async`. El SDK genera métodos sync y async para cada operación.

## Uso básico

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="...", client_secret="...") as client:
        response = await client.files.get_files_async()
        for file in response.result.data:
            print(file.name)

asyncio.run(main())
```

## Convención de nombres

| Sync | Async |
|------|-------|
| `client.files.get_files()` | `client.files.get_files_async()` |
| `client.admin.get_workspaces()` | `client.admin.get_workspaces_async()` |
| `client.wdata.get_tables()` | `client.wdata.get_tables_async()` |
| `client.chains.get_chains()` | `client.chains.get_chains_async()` |

TODOS los métodos de TODOS los namespaces tienen su variante `_async`.

## Context manager async

```python
async with Workiva(client_id="...", client_secret="...") as client:
    # Todas las operaciones async aquí
    response = await client.files.get_files_async()
# El cliente async se cierra automáticamente
```

> Si creas el cliente sin context manager, el async client se cierra cuando el objeto es garbage collected.

## Concurrencia con `asyncio.gather`

Ejecuta múltiples operaciones en paralelo:

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="...", client_secret="...") as client:
        # 3 llamadas en paralelo
        files, workspaces, documents = await asyncio.gather(
            client.files.get_files_async(),
            client.admin.get_workspaces_async(),
            client.documents.get_documents_async(),
        )

        print(f"Archivos: {len(files.result.data)}")
        print(f"Workspaces: {len(workspaces.result.data)}")
        print(f"Documentos: {len(documents.result.data)}")

asyncio.run(main())
```

## Polling async

`OperationPoller` tiene métodos async dedicados:

```python
async with Workiva(client_id="...", client_secret="...") as client:
    response = await client.files.copy_file_async(
        file_id="abc",
        file_copy=params,
    )

    # Polling automático async
    poller = client.wait(response)
    operation = await poller.result_async(timeout=300)
    print(f"Completado: {operation.resource_url}")
```

### Polling manual async

```python
poller = client.wait(response)

while not poller.done():
    operation = await poller.poll_async()
    print(f"Estado: {operation.status}")
    await asyncio.sleep(2)
```

## Paginación async

La paginación funciona igual en modo async:

```python
async with Workiva(client_id="...", client_secret="...") as client:
    response = await client.files.get_files_async()

    all_files = list(response.result.data)

    while response.next is not None:
        response = await response.next()
        all_files.extend(response.result.data)

    print(f"Total: {len(all_files)} archivos")
```

## Nota sobre el token OAuth

Las solicitudes de token OAuth2 siempre son **síncronas**, incluso en flujos async. El hook `ClientCredentialsHook` usa `self.client.send()` (sync) para obtener tokens. Esto significa que:

- No hay race conditions de tokens en flujos concurrentes
- El primer request async puede tener una latencia ligeramente mayor (sincronía del token)
- Los tokens cacheados se reutilizan sin bloqueo

## Ejemplo completo: procesar archivos en paralelo

```python
import asyncio
from workiva import Workiva, OperationFailed

async def export_file(client, file_id: str):
    """Exportar un archivo y esperar el resultado."""
    response = await client.files.export_file_by_id_async(
        file_id=file_id,
        file_export_by_id={"format": "pdf"},
    )
    poller = client.wait(response)
    return await poller.result_async(timeout=120)

async def main():
    file_ids = ["file-1", "file-2", "file-3", "file-4"]

    async with Workiva(client_id="...", client_secret="...") as client:
        # Exportar 4 archivos en paralelo
        results = await asyncio.gather(
            *[export_file(client, fid) for fid in file_ids],
            return_exceptions=True,
        )

        for file_id, result in zip(file_ids, results):
            if isinstance(result, OperationFailed):
                print(f"  {file_id}: FALLÓ - {result}")
            elif isinstance(result, Exception):
                print(f"  {file_id}: ERROR - {result}")
            else:
                print(f"  {file_id}: OK - {result.resource_url}")

asyncio.run(main())
```
