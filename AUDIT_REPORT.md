# Workiva SDK -- Deep Audit Report

5 agentes especializados, 87 hallazgos brutos, deduplicados a 42 unicos.

---

## CRITICAL (2)

### C1. Polling exceptions NO heredan de WorkivaError
- **Archivos:** `src/workiva/exceptions.py:29,52,61`
- **Agentes:** Architecture, DX (ambos lo encontraron independientemente)
- **Problema:** `OperationFailed`, `OperationCancelled` y `OperationTimeout` heredan de `Exception`, NO de `WorkivaError`. Un usuario que haga `except WorkivaError` para capturar "todos los errores del SDK" NO captura fallos de polling.
- **Impacto:** El contrato documentado de "WorkivaError es la raiz de todas las excepciones del SDK" esta ROTO.
- **Fix:** Una linea por clase: `class OperationFailed(WorkivaError): ...`

### C2. Ruta de retry por errores de conexion SIN TESTS
- **Archivo:** `src/workiva/_retry.py:101-112`
- **Agente:** Tests
- **Problema:** El `except (httpx.ConnectError, httpx.TimeoutException)` en `RetryTransport.handle_request()` tiene CERO cobertura. Es la ruta critica cuando el servidor no responde.
- **Impacto:** Un bug en la logica de retry de conexion pasa completamente desapercibido.
- **Fix:** Tests para: ConnectError con retry, ConnectError sin retry, max_retries alcanzado, max_elapsed_ms respetado. Lo mismo para AsyncRetryTransport.

---

## HIGH (14)

### H1. `_redact_response` MUTA el request original
- **Archivo:** `src/workiva/_errors.py:84-94`
- **Agentes:** Auth, Architecture
- **Problema:** `request.headers = httpx.Headers(headers)` modifica el request original in-place. Cualquier codigo que tenga referencia al request ve `[REDACTED]` en vez del header real.
- **Fix:** Crear copia del request, no mutar el original.

### H2. `close()` NO cierra el async client -- solo avisa
- **Archivo:** `src/workiva/_client.py:277-288`
- **Agente:** Auth
- **Problema:** Si un usuario usa sync y async, y sale con `with` (sync), el async client y su connection pool se filtran. Solo emite `ResourceWarning`.
- **Fix:** Best-effort close del async client en `close()`, o al menos `loop.create_task(self._async_client.aclose())`.

### H3. `_token_client` nunca se cierra si el auth object es GC'd sin `close()`
- **Archivo:** `src/workiva/_auth.py:70,134-141`
- **Agente:** Auth
- **Problema:** Sin `__del__` ni context manager obligatorio, el `httpx.Client` del token leak si el usuario no llama `close()`.
- **Fix:** Documentar que context manager es OBLIGATORIO, o anadir `__del__` con cleanup.

### H4. Estado global mutable en auth sin poda
- **Archivo:** `src/workiva/_auth.py:51-53`
- **Agente:** Architecture
- **Problema:** `_client_locks` crece una entrada por cada par `(client_id, secret)` y NUNCA se limpia. En procesos de larga duracion que rotan credenciales, crece indefinidamente.
- **Fix:** Limpiar entrada en `close()` cuando ningun otro instance la comparte.

### H5. Return type `httpx.Response | Operation` no se puede narrowear
- **Archivo:** Templates Jinja2, todos los generated operations con wait
- **Agente:** DX
- **Problema:** Type checkers no pueden deducir que `wait=True` devuelve `Operation`. El IDE no ayuda.
- **Fix:** `@overload` en templates con `Literal[True]` -> `Operation`, `Literal[False]` -> `httpx.Response`.

### H6. Error messages sin URL ni metodo HTTP
- **Archivo:** `src/workiva/_errors.py:133-149`
- **Agente:** DX
- **Problema:** `[404] NotFound: Resource not found` -- cual recurso? cual endpoint? El usuario no sabe que fallo.
- **Fix:** `f"[{status} {method} {path}] {msg}"` en `_build_message`.

### H7. `config` ignora silenciosamente `region` y `timeout`
- **Archivo:** `src/workiva/client.py:122-127`
- **Agentes:** DX, Architecture
- **Problema:** `Workiva(region=Region.US, config=SDKConfig(retry=...))` -- el `region=US` se ignora silenciosamente. El usuario recibe EU sin saberlo.
- **Fix:** `raise ValueError` si se pasan `config` junto con `region`/`timeout`.

### H8. Documentacion referencia metodos inexistentes
- **Archivo:** `docs/index.md:68,75,77`
- **Agente:** DX
- **Problema:** `get_document()` no existe, es `get_document_by_id()`. Copiar del doc da `AttributeError`.
- **Fix:** Corregir los nombres en la documentacion.

### H9. Body fields required se omiten silenciosamente
- **Archivo:** Templates `operation_sync.py.j2:118-123`
- **Agente:** Codegen
- **Problema:** Todos los body fields (incluyendo required) se guardan con `if field is not None`. Required fields deberian incluirse incondicionalmente.
- **Fix:** Condicional solo para campos Optional; required van directo al body.

### H10. Breaking change detector no detecta cambios de VALOR en enums
- **Archivo:** `scripts/detect_breaking_changes.py:215-233`
- **Agente:** Codegen
- **Problema:** Si un enum cambia de `FOO = "foo"` a `FOO = "bar"`, el detector no lo ve (la key `FOO` existe en ambos).
- **Fix:** Comparar valores ademas de keys.

### H11. Cambios de tipo annotation siempre clasificados como "compatible"
- **Archivo:** `scripts/detect_breaking_changes.py:286-298`
- **Agente:** Codegen
- **Problema:** `Optional[str]` -> `str` es un breaking change, pero el detector lo marca como compatible.
- **Fix:** Detectar narrowing (Optional removido, union reducido) como breaking.

### H12. `_CachedToken.is_expired()` sin tests directos
- **Archivo:** `src/workiva/_auth.py:29`
- **Agente:** Tests
- **Problema:** La funcion gatekeeper de todo el token refresh no tiene ni un test unitario directo.
- **Fix:** Tests con time.time() mockeado para boundary, buffer, None, expirado, y fresh.

### H13. `paginate_lazy()` y `paginate_lazy_async()` sin tests
- **Archivo:** `src/workiva/_pagination.py:174-248`
- **Agente:** Tests
- **Problema:** Dos funciones publicas completas sin cobertura alguna.
- **Fix:** Tests para single-page, multi-page, empty, y max_pages guard.

### H14. `AsyncRetryTransport` sin tests unitarios directos
- **Archivo:** `src/workiva/_retry.py`
- **Agente:** Tests
- **Problema:** 7 tests para sync, CERO para async. Tiene code paths propios (`await asyncio.sleep`, `await response.aclose()`).
- **Fix:** Mirror de todos los tests sync para async.

---

## MEDIUM (16)

### M1. No jitter en Retry-After -- thundering herd
- **Archivo:** `src/workiva/_retry.py:76-77`
- **Agente:** Auth
- **Problema:** 100 clientes con `Retry-After: 5` reintentan TODOS a t+5 exacto.
- **Fix:** `retry_after + random.uniform(0, 1)`.

### M2. Transient errors durante polling se propagan raw
- **Archivo:** `src/workiva/polling.py:115-135`
- **Agente:** Auth
- **Problema:** Un 5xx durante poll sube como `ServerError`, no como `OperationTimeout` con contexto.
- **Fix:** Catch transient errors en el loop de polling, reintentar hasta deadline.

### M3. Duplicacion de logica retry-after parsing
- **Archivos:** `polling.py:55-84` y `_retry.py:21-44`
- **Agente:** Architecture
- **Problema:** Misma logica implementada dos veces con variaciones. Bug fix en uno no se aplica al otro.
- **Fix:** Extraer `_parse_retry_after_value()` a modulo compartido.

### M4. Duplicacion de polling loops (functions vs class)
- **Archivo:** `src/workiva/polling.py:87-186 y 189-327`
- **Agente:** Architecture
- **Problema:** `_poll_until_done` y `OperationPoller.result` implementan loops identicos.
- **Fix:** Que `_poll_until_done` use `OperationPoller` internamente, o viceversa.

### M5. OperationPoller viola Law of Demeter
- **Archivo:** `src/workiva/polling.py:249,293`
- **Agente:** Architecture
- **Problema:** `self._client._base_client.request()` -- accede a atributo privado de otro objeto.
- **Fix:** Aceptar `BaseClient` directamente, no `Workiva`.

### M6. No validacion de `client_id`/`client_secret` en constructor
- **Archivo:** `src/workiva/client.py:112`
- **Agente:** Architecture
- **Problema:** String vacio pasa silenciosamente hasta el primer API call. Fail-fast seria mejor.
- **Fix:** `raise ValueError("client_id must be non-empty")` en `__init__`.

### M7. Dependencia httpx sin upper bound
- **Archivo:** `pyproject.toml:15`
- **Agente:** Architecture
- **Problema:** `httpx >=0.28.1` sin cota superior. httpx 0.x es conocido por breaking changes.
- **Fix:** `httpx >=0.28.1,<1.0`.

### M8. Pagination RuntimeError no es WorkivaError
- **Archivo:** `src/workiva/_pagination.py:126-130`
- **Agente:** DX
- **Problema:** Exceder 1000 paginas lanza `RuntimeError`, no capturado por `except WorkivaError`.
- **Fix:** Crear `PaginationError(WorkivaError)`.

### M9. `wait()` acepta `Any` y da error criptico en non-202 responses
- **Archivo:** `src/workiva/client.py:163`
- **Agente:** DX
- **Problema:** Pasar un modelo Pydantic (return de operacion normal) da `ValueError: no 'location' header`.
- **Fix:** Type check al inicio, error descriptivo, annotation `httpx.Response`.

### M10. Documentacion dice "MD5" pero codigo usa SHA-256
- **Archivo:** `docs/autenticacion.md:84`
- **Agente:** DX
- **Fix:** Corregir a "SHA-256".

### M11. Version hardcodeada "0.6.1" en docs/index.md (actual: 0.6.9)
- **Archivo:** `docs/index.md:108`
- **Agente:** DX
- **Fix:** Quitar version hardcoded o anadirlo a `bump_version.py`.

### M12. Template sync/async 96% duplicado
- **Archivos:** `operation_sync.py.j2` y `operation_async.py.j2`
- **Agente:** Codegen
- **Problema:** 235 lineas cada uno, solo 9 lineas distintas. Cada fix se hace 2 veces.
- **Fix:** Template unico con `is_async` boolean.

### M13. No deduplicacion de parametros path-level + operation-level
- **Archivo:** `scripts/codegen/operations.py:485-488`
- **Agente:** Codegen
- **Problema:** OAS permite override de parametros; el parser simplemente concatena.
- **Fix:** Dedup por `(name, location)`, precedencia a operation-level.

### M14. `oneOf`/`anyOf` no manejados en resolucion de tipos
- **Archivo:** `scripts/codegen/operations.py:177`
- **Agente:** Codegen
- **Problema:** Composicion OAS cae a `Any` silenciosamente.
- **Fix:** Warning o resolucion basica de unions.

### M15. `close()`/`aclose()` lifecycle sin tests unitarios
- **Archivos:** `src/workiva/_client.py:277-301`
- **Agente:** Tests
- **Problema:** ResourceWarning, sync close, async close, supplied client no-close -- todo sin tests.
- **Fix:** Tests especificos para cada path de lifecycle.

### M16. HTTP-date parsing nunca testeado con fecha valida
- **Archivos:** `_retry.py:36-43`, `polling.py:72-83`
- **Agente:** Tests
- **Problema:** Branch de HTTP-date existe pero ningun test lo ejercita con fecha valida.
- **Fix:** Test con `"Wed, 21 Oct 2099 07:28:00 GMT"` que confirme delay positivo.

---

## LOW (10)

### L1. `threading.Lock` en path async (pero sin I/O en seccion critica)
- `_client.py:131-148`

### L2. Double-checked locking potencialmente inseguro en free-threaded Python (PEP 703)
- `_client.py:112-129`

### L3. Namespace lazy-loading no es thread-safe (pero benigno)
- `client.py:144-154`

### L4. Client references no se nullifican tras `close()` -- use-after-close confuso
- `_client.py:277-301`

### L5. Import `__version__` no usado en `_client.py`
- `_client.py:28`

### L6. `copy_sheets` como metodo concreto de negocio en cliente generico (SRP)
- `client.py:201-252`

### L7. `_fix_non_optional_none_defaults` solo cubre tipos primitivos
- `scripts/codegen/models.py:282-309`

### L8. `_MERGE_TAGS` reconstruido en cada iteracion del loop
- `scripts/codegen/operations.py:545`

### L9. cookie parameters silenciosamente ignorados
- `scripts/codegen/operations.py`

### L10. `_sanitize_string_literal` no escapa newlines
- `scripts/codegen/sanitize.py:13-15`

---

## Estadisticas

| Severidad | Cantidad | Agentes que lo encontraron |
|-----------|----------|---------------------------|
| CRITICAL  | 2        | Architecture+DX, Tests |
| HIGH      | 14       | Todos los agentes |
| MEDIUM    | 16       | Todos los agentes |
| LOW       | 10       | Varios |
| **TOTAL** | **42**   | **5 agentes** |

### Hallazgos confirmados por multiples agentes (alta confianza)
- C1 (excepciones sin WorkivaError): Architecture + DX
- H1 (redact muta request): Auth + Architecture
- H7 (config ignora region): DX + Architecture

### Top 5 por impacto/esfuerzo
1. **C1** -- Excepciones de polling fuera de WorkivaError (1 linea por clase)
2. **H6** -- Error messages sin URL (cambio en `_build_message`)
3. **H8** -- Docs con metodos incorrectos (edicion de texto)
4. **M1** -- Jitter en Retry-After (1 linea)
5. **M6** -- Validacion de credenciales (3 lineas)
