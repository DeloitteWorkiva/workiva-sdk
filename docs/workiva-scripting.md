# Workiva Scripting

Guia para usar el SDK de Workiva dentro del modulo de scripting de la plataforma.

## Que es Workiva Scripting?

El modulo de scripting de Workiva permite ejecutar scripts Python directamente en la plataforma. Estos scripts corren en un sandbox con restricciones de red, tiempo y paquetes.

## Instalacion en el sandbox

Agrega el SDK a tu `requirements.txt` con version pinneada:

```
workiva==0.6.1
```

> Siempre pinnea la version para evitar cambios inesperados entre ejecuciones.

## Ejemplo minimo funcional

```python
from workiva import Workiva

def main():
    with Workiva(client_id="...", client_secret="...") as client:
        # Listar archivos del workspace (auto-paginacion)
        result = client.files.get_files()
        for file in result.data:
            print(f"{file.name} ({file.kind})")

if __name__ == "__main__":
    main()
```

## Patrones comunes

### Listar y filtrar

```python
with Workiva(client_id="...", client_secret="...") as client:
    # La paginacion es transparente — devuelve TODOS los spreadsheets
    result = client.spreadsheets.get_spreadsheets()
    print(f"Total spreadsheets: {len(result.data)}")

    # Filtrar en Python
    large_ss = [ss for ss in result.data if hasattr(ss, 'sheet_count') and ss.sheet_count > 10]
```

### Exportar archivo

```python
from workiva import Workiva, OperationTimeout

with Workiva(client_id="...", client_secret="...") as client:
    response = client.files.export_file_by_id(
        file_id="file-123",
        body={"format": "xlsx"},
    )

    try:
        operation = client.wait(response).result(timeout=120)
        print(f"URL de descarga: {operation.resource_url}")
    except OperationTimeout:
        print("La exportacion tardo demasiado")
```

### Copiar archivos entre workspaces

```python
from workiva import Workiva, OperationFailed
from workiva.models.platform import FileCopy

with Workiva(client_id="...", client_secret="...") as client:
    response = client.files.copy_file(
        file_id="source-file-id",
        body=FileCopy(workspace_id="target-workspace-id"),
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
    result = client.spreadsheets.get_sheet_data(
        spreadsheet_id="ss-123",
        sheet_id="sheet-456",
    )

    for row in result.data:
        print(row)
```

## Consideraciones del sandbox

### Timeout

Los scripts en el sandbox tienen un tiempo maximo de ejecucion. Ajusta tus timeouts de polling para no excederlo:

```python
# Si tu script tiene 5 minutos de timeout total,
# usa menos para el polling individual
operation = client.wait(response).result(timeout=120)  # 2 min max por operacion
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

El sandbox de scripting puede no soportar `asyncio`. Usa los metodos sync del SDK:

```python
# Esto funciona en el sandbox
result = client.files.get_files()

# Esto puede NO funcionar en el sandbox
# result = await client.files.get_files_async()
```

## Depuracion

Para depurar en el sandbox, usa `print()` -- los logs se capturan en la salida del script:

```python
from workiva import Workiva, WorkivaAPIError

with Workiva(client_id="...", client_secret="...") as client:
    try:
        result = client.files.get_files()
        print(f"Archivos encontrados: {len(result.data)}")
    except WorkivaAPIError as e:
        print(f"Error API [{e.status_code}]: {e}")
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")
```
