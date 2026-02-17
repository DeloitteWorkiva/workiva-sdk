# Uso asincrono

Todos los metodos del SDK tienen una variante asincrona con el sufijo `_async`. El SDK genera metodos sync y async para cada una de las 357 operaciones.

## Uso basico

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="...", client_secret="...") as client:
        result = await client.files.get_files_async()
        for file in result.data:
            print(file.name)

asyncio.run(main())
```

## Convencion de nombres

| Sync | Async |
|------|-------|
| `client.files.get_files()` | `client.files.get_files_async()` |
| `client.admin.get_workspaces()` | `client.admin.get_workspaces_async()` |
| `client.wdata.get_tables()` | `client.wdata.get_tables_async()` |
| `client.chains.get_chains()` | `client.chains.get_chains_async()` |

TODOS los metodos de TODOS los 18 namespaces tienen su variante `_async`.

## Context manager async

```python
async with Workiva(client_id="...", client_secret="...") as client:
    result = await client.files.get_files_async()
# El cliente async se cierra automaticamente
```

## Concurrencia con `asyncio.gather`

Ejecuta multiples operaciones en paralelo:

```python
import asyncio
from workiva import Workiva

async def main():
    async with Workiva(client_id="...", client_secret="...") as client:
        # 3 llamadas en paralelo
        files, workspaces, tables = await asyncio.gather(
            client.files.get_files_async(),
            client.admin.get_workspaces_async(),
            client.wdata.get_tables_async(),
        )

        print(f"Archivos: {len(files.data)}")
        print(f"Workspaces: {len(workspaces.data)}")
        print(f"Tablas: {len(tables.body)}")

asyncio.run(main())
```

## Paginacion async

La paginacion transparente funciona igual en modo async:

```python
async with Workiva(client_id="...", client_secret="...") as client:
    # Esto devuelve TODOS los archivos de TODAS las paginas
    result = await client.files.get_files_async()
    print(f"Total: {len(result.data)} archivos")
```

## Polling async

`OperationPoller` tiene metodos async dedicados:

```python
async with Workiva(client_id="...", client_secret="...") as client:
    response = await client.files.copy_file_async(
        file_id="abc",
        destination_container="folder-456",
    )

    # Polling automatico async
    operation = await client.wait(response).result_async(timeout=300)
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

## Nota sobre el token OAuth

Las solicitudes de token OAuth2 en modo async se ejecutan con `asyncio.to_thread` para no bloquear el event loop:

- La obtencion del token es inherentemente sincrona (HTTP POST)
- `asyncio.to_thread` lo ejecuta en un thread del pool para evitar bloqueo
- Los tokens cacheados se reutilizan sin bloqueo
- No hay race conditions de tokens en flujos concurrentes

## Ejemplo completo: procesar archivos en paralelo

```python
import asyncio
from workiva import Workiva, OperationFailed

async def export_file(client, file_id: str):
    """Exportar un archivo y esperar el resultado."""
    response = await client.files.export_file_by_id_async(
        file_id=file_id,
        kind="Document",
        document_export={"format": "pdf"},
    )
    return await client.wait(response).result_async(timeout=120)

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
                print(f"  {file_id}: FALLO - {result}")
            elif isinstance(result, Exception):
                print(f"  {file_id}: ERROR - {result}")
            else:
                print(f"  {file_id}: OK - {result.resource_url}")

asyncio.run(main())
```
