# Workiva Scripting

Guía para usar el SDK de Workiva dentro del módulo de scripting de la plataforma.

## ¿Qué es Workiva Scripting?

El módulo de scripting de Workiva permite ejecutar scripts Python directamente en la plataforma. Estos scripts corren en un sandbox con restricciones de red, tiempo y paquetes.

## Instalación en el sandbox

Agrega el SDK a tu `requirements.txt` con versión pinneada:

```
workiva==0.4.0
```

> Siempre pinnea la versión para evitar cambios inesperados entre ejecuciones.

## Ejemplo mínimo funcional

```python
from workiva import Workiva

def main():
    with Workiva(client_id="...", client_secret="...") as client:
        # Listar archivos del workspace
        response = client.files.get_files()
        for file in response.result.data:
            print(f"{file.name} ({file.kind})")

if __name__ == "__main__":
    main()
```

## Patrones comunes

### Listar y filtrar

```python
def get_all_spreadsheets(client):
    """Obtener todos los spreadsheets paginando automáticamente."""
    response = client.spreadsheets.get_spreadsheets()
    spreadsheets = list(response.result.data)

    while response.next is not None:
        response = response.next()
        spreadsheets.extend(response.result.data)

    return spreadsheets

with Workiva(client_id="...", client_secret="...") as client:
    all_ss = get_all_spreadsheets(client)
    print(f"Total spreadsheets: {len(all_ss)}")
```

### Exportar archivo

```python
from workiva import Workiva, OperationTimeout

with Workiva(client_id="...", client_secret="...") as client:
    response = client.files.export_file_by_id(
        file_id="file-123",
        file_export_by_id={"format": "xlsx"},
    )

    try:
        operation = client.wait(response).result(timeout=120)
        print(f"URL de descarga: {operation.resource_url}")
    except OperationTimeout:
        print("La exportación tardó demasiado")
```

### Copiar archivos entre workspaces

```python
from workiva import Workiva, OperationFailed
from workiva.models import FileCopy

with Workiva(client_id="...", client_secret="...") as client:
    response = client.files.copy_file(
        file_id="source-file-id",
        file_copy=FileCopy(
            workspace_id="target-workspace-id",
        ),
    )

    try:
        operation = client.wait(response).result(timeout=300)
        print(f"Copia completada: {operation.resource_url}")
    except OperationFailed as e:
        print(f"Error en copia: {e}")
```

### Leer datos de un spreadsheet

```python
with Workiva(client_id="...", client_secret="...") as client:
    response = client.spreadsheets.get_sheet_data(
        spreadsheet_id="ss-123",
        sheet_id="sheet-456",
    )

    for row in response.result.data:
        print(row)
```

## Consideraciones del sandbox

### Timeout

Los scripts en el sandbox tienen un tiempo máximo de ejecución. Ajusta tus timeouts de polling para no excederlo:

```python
# Si tu script tiene 5 minutos de timeout total,
# usa menos para el polling individual
operation = client.wait(response).result(timeout=120)  # 2 min máx por operación
```

### Credenciales

No hardcodees credenciales en el script. Usa los mecanismos de secrets de Workiva o variables de entorno del sandbox:

```python
import os

client = Workiva(
    client_id=os.environ["WK_CLIENT_ID"],
    client_secret=os.environ["WK_CLIENT_SECRET"],
)
```

### Sin acceso a filesystem local

El sandbox no tiene acceso a disco persistente. Si necesitas procesar archivos, usa las APIs de import/export en memoria.

### Solo sync

El sandbox de scripting puede no soportar `asyncio`. Usa los métodos sync del SDK:

```python
# Esto funciona en el sandbox
response = client.files.get_files()

# Esto puede NO funcionar en el sandbox
# response = await client.files.get_files_async()
```

## Depuración

Para depurar en el sandbox, usa `print()` — los logs se capturan en la salida del script:

```python
from workiva import Workiva
from workiva.errors import SDKBaseError

with Workiva(client_id="...", client_secret="...") as client:
    try:
        response = client.files.get_files()
        print(f"Archivos encontrados: {len(response.result.data)}")
    except SDKBaseError as e:
        print(f"Error API: {e.status_code} - {e.message}")
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")
```
