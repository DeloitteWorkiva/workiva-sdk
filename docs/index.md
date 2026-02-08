# Workiva Python SDK

[![PyPI](https://img.shields.io/pypi/v/workiva)](https://pypi.org/project/workiva/)
[![Python](https://img.shields.io/pypi/pyversions/workiva)](https://pypi.org/project/workiva/)

SDK unificado para las APIs de Workiva: **Platform**, **Chains** y **Wdata**, en un solo paquete Python.

## ¿Qué es este SDK?

El SDK de Workiva proporciona un cliente Python tipado para interactuar con las tres APIs de la plataforma Workiva:

| API | Descripción | Namespace |
|-----|-------------|-----------|
| **Platform** | Gestión de archivos, documentos, hojas de cálculo, presentaciones, usuarios, permisos y más | `sdk.files`, `sdk.documents`, `sdk.spreadsheets`, `sdk.admin`, etc. |
| **Chains** | Automatización de flujos de trabajo (cadenas) | `sdk.chains` |
| **Wdata** | Gestión de datos: tablas, queries, imports/exports | `sdk.wdata` |

## Requisitos

- **Python 3.10+**
- Credenciales OAuth2 (client_id y client_secret) de Workiva

## Tabla de contenidos

### Guías principales

1. [Inicio rápido](inicio-rapido.md) — Instalación y primer request en 2 minutos
2. [Autenticación](autenticacion.md) — OAuth2 client_credentials, token caching
3. [Configuración](configuracion.md) — Servidores, timeouts, reintentos, logging
4. [Operaciones de larga duración](operaciones-larga-duracion.md) — Patrón 202, polling, `wait()`
5. [Paginación](paginacion.md) — 5 patrones, iteración con `.next()`
6. [Manejo de errores](manejo-errores.md) — Excepciones, códigos, try/except
7. [Uso asíncrono](uso-asincrono.md) — Métodos `_async`, concurrencia

### Referencia de API

8. [Referencia de API](referencia-api/index.md) — Los 17 namespaces y sus operaciones

### Guías especializadas

9. [Workiva Scripting](workiva-scripting.md) — Uso del SDK en el módulo de scripting
10. [Arquitectura del SDK](arquitectura-sdk.md) — Cómo está construido internamente

## Ejemplo rápido

```python
from workiva import Workiva

with Workiva(client_id="tu_client_id", client_secret="tu_client_secret") as client:
    # Listar workspaces
    response = client.admin.get_workspaces()
    for ws in response.result.data:
        print(ws.name)

    # Copiar un archivo (operación de larga duración)
    response = client.files.copy_file(file_id="abc123", file_copy=params)
    operation = client.wait(response).result(timeout=300)
    print(f"Operación completada: {operation.resource_url}")
```

## Versión actual

- **SDK**: 0.4.0
- **Python target**: 3.10+
- **Generado con**: [Speakeasy](https://speakeasy.com)
