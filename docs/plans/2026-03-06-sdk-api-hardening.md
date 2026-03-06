# SDK API Hardening — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Eliminate every API design issue that causes bugs, traps, or unnecessary verbosity for end users.

**Architecture:** All changes are to hand-written modules (survive `make force`). Codegen template changes are separate tasks that require `make generate` after. Each task is independently testable and commitable.

**Tech Stack:** Python 3.10+, Pydantic v2, httpx, pytest, Jinja2 (templates only)

---

## Task 1: Simplify constructor — remove dual config path

The `config=SDKConfig(...)` parameter creates a second way to set `region` and `timeout`, leading to silent conflicts. Replace with direct `retry` parameter.

**Files:**
- Modify: `src/workiva/client.py` (constructor)
- Modify: `src/workiva/__init__.py` (remove SDKConfig from `__all__` — users no longer need it)
- Modify: `tests/unit/test_workiva_client.py`
- Modify: `tests/unit/test_audit_usability.py`
- Modify: `tests/unit/test_audit_exceptions.py`

**Step 1: Write the failing test**

```python
# In tests/unit/test_audit_usability.py, add to TestConfigSimplicity:

def test_retry_param_accepted(self):
    from workiva import Workiva, RetryConfig
    client = Workiva(
        client_id="id", client_secret="secret",
        retry=RetryConfig(max_retries=10),
    )
    assert client._config.retry.max_retries == 10
    client.close()

def test_config_param_removed(self):
    """SDKConfig should not be a constructor parameter."""
    import inspect
    from workiva.client import Workiva
    sig = inspect.signature(Workiva.__init__)
    assert "config" not in sig.parameters
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/unit/test_audit_usability.py::TestConfigSimplicity::test_retry_param_accepted -v`
Expected: FAIL (no `retry` param yet)

**Step 3: Implement**

In `src/workiva/client.py`, change `__init__`:

```python
def __init__(
    self,
    client_id: str,
    client_secret: str,
    *,
    region: Region = Region.EU,
    timeout: Optional[float] = None,
    retry: Optional[RetryConfig] = None,
    client: Optional[httpx.Client] = None,
    async_client: Optional[httpx.AsyncClient] = None,
) -> None:
    if not client_id or not isinstance(client_id, str):
        raise ValueError("client_id must be a non-empty string")
    if not client_secret or not isinstance(client_secret, str):
        raise ValueError("client_secret must be a non-empty string")

    config = SDKConfig(
        region=region,
        timeout_s=timeout,
        retry=retry or RetryConfig(),
    )
    # ... rest unchanged
```

Remove `SDKConfig` from `__init__.py`'s `__all__` (keep import for internal use).
Update all tests that use `config=SDKConfig(...)` to use direct params.
Remove the H7 validation check (no longer needed — single path).

**Step 4: Run tests, fix any that used `config=`**

Run: `uv run pytest tests/ -v`

**Step 5: Commit**

```
feat: simplify constructor — replace config param with retry

BREAKING CHANGE: `config=SDKConfig(...)` parameter removed.
Use `region=`, `timeout=`, and `retry=RetryConfig(...)` directly.
```

---

## Task 2: Clean up dead code in `wait()`

After adding the `TypeError` guard, the `else` branch of `isinstance(response, httpx.Response)` is unreachable. Remove it.

**Files:**
- Modify: `src/workiva/client.py` (wait method)

**Step 1: Write the failing test**

No new test needed — this is dead code removal. Existing tests cover `wait()`.

**Step 2: Implement**

Replace the `wait()` method body after the TypeError guard:

```python
def wait(self, response: httpx.Response) -> OperationPoller:
    # ... docstring ...
    if not isinstance(response, httpx.Response):
        actual_type = type(response).__name__
        raise TypeError(
            f"wait() expects an httpx.Response from a 202 operation, "
            f"but got {actual_type}. Only long-running operations "
            f"(copy_file, export_file, etc.) return pollable responses. "
            f"If you used wait=True, the operation already returns an "
            f"Operation directly — no need to call wait()."
        )

    headers = dict(response.headers)
    body = None
    try:
        body = response.json()
    except (ValueError, RuntimeError):
        pass

    operation_id = _extract_operation_id(headers)
    retry_after = _get_retry_after(headers)
    return OperationPoller(
        client=self,
        operation_id=operation_id,
        initial_retry_after=retry_after,
        response_body=body,
    )
```

**Step 3: Run tests**

Run: `uv run pytest tests/unit/test_workiva_client.py tests/unit/test_audit_exceptions.py -v`

**Step 4: Commit**

```
refactor: remove dead code branch in wait()
```

---

## Task 3: Add sync `copy_sheets` variant

The async-only `copy_sheets` breaks the SDK's sync/async naming convention. Sync users get a coroutine object instead of results.

**Files:**
- Modify: `src/workiva/client.py`
- Modify: `tests/unit/test_copy_sheets_batch.py`

**Step 1: Write the failing test**

```python
# In tests/unit/test_copy_sheets_batch.py, add:

class TestCopySheetSync:
    def test_returns_operations_in_order(self):
        w = _mock_workiva()
        ops = [
            Operation.model_validate({"id": f"op-{i}", "status": "completed"})
            for i in range(3)
        ]
        # Mock sync copy_sheet (not async)
        w.spreadsheets.copy_sheet = MagicMock(side_effect=ops)

        results = w.copy_sheets_sync(
            spreadsheet_id="ss-1",
            copies=[
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "A"},
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "B"},
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "C"},
            ],
        )

        assert len(results) == 3
        assert results[0].id == "op-0"
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/unit/test_copy_sheets_batch.py::TestCopySheetSync -v`

**Step 3: Implement**

In `src/workiva/client.py`:

```python
def copy_sheets_sync(
    self,
    *,
    spreadsheet_id: str,
    copies: list[dict[str, Any]],
    wait_timeout: float = 300,
) -> list[Operation]:
    """Copy multiple sheets sequentially (sync version).

    For concurrent execution, use the async ``copy_sheets`` method.
    """
    results: list[Any] = []
    for params in copies:
        op = self.spreadsheets.copy_sheet(
            spreadsheet_id=spreadsheet_id,
            wait=True,
            wait_timeout=wait_timeout,
            **params,
        )
        results.append(op)
    return results
```

**Step 4: Run tests**

Run: `uv run pytest tests/unit/test_copy_sheets_batch.py -v`

**Step 5: Commit**

```
feat: add sync copy_sheets_sync variant
```

---

## Task 4: RateLimitError.retry_after property (Issue #18)

Users must dig into `e.response.headers.get("Retry-After")` manually. Add a property.

**Files:**
- Modify: `src/workiva/_errors.py`
- Modify: `tests/unit/test_errors.py`

**Step 1: Write the failing test**

```python
# In tests/unit/test_errors.py, add:

class TestRateLimitRetryAfter:
    def test_retry_after_from_header(self):
        response = httpx.Response(
            429,
            headers={"retry-after": "30"},
            json={"error": {"message": "rate limited"}},
            request=httpx.Request("GET", "https://api.example.com/files"),
        )
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.retry_after == 30

    def test_retry_after_missing_defaults_60(self):
        response = httpx.Response(
            429,
            json={"error": {"message": "rate limited"}},
            request=httpx.Request("GET", "https://api.example.com/files"),
        )
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.retry_after == 60

    def test_retry_after_non_numeric_defaults_60(self):
        response = httpx.Response(
            429,
            headers={"retry-after": "invalid"},
            json={"error": {"message": "rate limited"}},
            request=httpx.Request("GET", "https://api.example.com/files"),
        )
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.retry_after == 60
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/unit/test_errors.py::TestRateLimitRetryAfter -v`

**Step 3: Implement**

In `src/workiva/_errors.py`, add to `RateLimitError`:

```python
class RateLimitError(WorkivaAPIError):
    """429 Too Many Requests."""

    @property
    def retry_after(self) -> int:
        """Seconds to wait before retrying, from Retry-After header.

        Defaults to 60 if header is missing or unparseable.
        """
        value = self.response.headers.get("retry-after")
        if value is None:
            return 60
        try:
            return int(value)
        except (TypeError, ValueError):
            return 60
```

**Step 4: Run tests**

Run: `uv run pytest tests/unit/test_errors.py -v`

**Step 5: Commit**

```
feat: add retry_after property to RateLimitError
```

---

## Task 5: `@overload` for `wait` parameter on generated operations

112 methods return `httpx.Response | Operation` — type checkers can't narrow. Add `@overload` to templates so `wait=True` -> `Operation` and `wait=False` -> `httpx.Response`.

**Files:**
- Modify: `scripts/codegen/templates/operation_sync.py.j2`
- Modify: `scripts/codegen/templates/operation_async.py.j2`
- Modify: `scripts/codegen/templates/namespace.py.j2` (add `overload` import)
- Regenerate: `make generate-operations`
- Test: `tests/unit/test_sdk_usability.py`

**Step 1: Write the failing test**

```python
# In tests/unit/test_sdk_usability.py, add:

class TestOverloadSignatures:
    def test_long_running_op_has_overloads(self):
        """Operations with wait param should have @overload decorators."""
        import inspect
        from workiva._operations.files import Files

        # Get all attributes named copy_file (including overloads)
        source = inspect.getsource(Files.copy_file)
        assert "overload" not in source  # Will flip to 'in' after fix

        # Alternative: check that typing.get_overloads returns entries
        from typing import get_overloads
        overloads = get_overloads(Files.copy_file)
        assert len(overloads) >= 2
```

**Step 2: Implement in templates**

In `namespace.py.j2`, add to imports:
```jinja2
{% if has_long_running %}
from typing import Literal, overload
{% endif %}
```

In `operation_sync.py.j2`, before the main method, add overload declarations:
```jinja2
{% if op.is_long_running %}
    @overload
    def {{ op.method_name }}(
        self,
        *,
        {{ params_without_wait }},
        wait: Literal[False] = ...,
        wait_timeout: float = ...,
    ) -> httpx.Response: ...

    @overload
    def {{ op.method_name }}(
        self,
        *,
        {{ params_without_wait }},
        wait: Literal[True],
        wait_timeout: float = ...,
    ) -> Operation: ...
{% endif %}
```

Same for async template.

**Step 3: Regenerate and test**

Run: `uv run python scripts/generate_sdk.py --operations-only && uv run pytest tests/ -v`

**Step 4: Commit**

```
feat: add @overload for wait parameter on long-running operations
```

---

## Task 6: Void operations return `None` instead of `httpx.Response`

44 DELETE/void operations leak raw `httpx.Response` to users. Since `raise_for_status` already runs, a successful void operation should return `None`.

**Files:**
- Modify: `scripts/codegen/templates/operation_sync.py.j2`
- Modify: `scripts/codegen/templates/operation_async.py.j2`
- Modify: `scripts/generate_sdk.py` (pass `is_void` flag to template context)
- Regenerate: `make generate-operations`
- Test: `tests/unit/test_sdk_usability.py`

**Step 1: Write the failing test**

```python
class TestVoidOperations:
    def test_delete_returns_none(self):
        from workiva._operations.files import Files
        import inspect
        sig = inspect.signature(Files.trash_file_by_id)
        # Return annotation should be None for void operations
        assert sig.return_annotation is None or sig.return_annotation == "None"
```

**Step 2: Implement**

In `scripts/codegen/operations.py`, detect void operations:
- Status 204 with no response body schema
- Status 202 with no JSON response body (already has `is_long_running`, these are different)

In template, when `op.is_void`:
```jinja2
{% if op.is_void %}
    ) -> None:
        ...
        self._client.request(...)
        return None
{% endif %}
```

**Step 3: Regenerate and test**

Run: `uv run python scripts/generate_sdk.py --operations-only && uv run pytest tests/ -v`

**Step 4: Commit**

```
feat: void operations return None instead of httpx.Response
```

---

## Task 7: Fix documentation errors

**Files:**
- Modify: `docs/index.md` (wrong method names, stale version)
- Modify: `docs/autenticacion.md` (MD5 → SHA-256)
- Modify: `docs/manejo-errores.md` (add retry_after docs)

**Step 1: Fix method names in docs/index.md**

Replace:
- `get_document(...)` → `get_document_by_id(...)`
- `get_presentation(...)` → `get_presentation_by_id(...)`
- `get_spreadsheet(...)` → `get_spreadsheet_by_id(...)`

Remove or automate the hardcoded version "0.6.1".

**Step 2: Fix hash algorithm in docs/autenticacion.md**

Replace "MD5" with "SHA-256".

**Step 3: Add retry_after to docs/manejo-errores.md**

Add example:
```python
except RateLimitError as e:
    print(f"Reintentar en {e.retry_after} segundos")
```

**Step 4: Commit**

```
docs: fix 5 documentation errors found in audit
```

---

## Execution Order and Dependencies

```
Task 1 (SDKConfig) ─────→ independent, do first (breaking change)
Task 2 (dead code) ─────→ independent, trivial
Task 3 (copy_sheets sync) → independent
Task 4 (RateLimitError) ──→ independent
Task 5 (@overload) ────────→ requires regeneration
Task 6 (void returns) ────→ requires regeneration, do after Task 5
Task 7 (docs) ────────────→ do last, references Task 4
```

Recommended order: 1 → 2 → 4 → 3 → 7 → 5 → 6

Tasks 5 and 6 are codegen changes that require `make generate-operations` — batch them together at the end to only regenerate once.

---

## Total Test Impact

| Task | New Tests | Modified Tests |
|------|-----------|----------------|
| 1    | 2         | ~6 (update config= usage) |
| 2    | 0         | 0 |
| 3    | 1         | 0 |
| 4    | 3         | 0 |
| 5    | 1         | 0 |
| 6    | 1         | ~2 (update return type assertions) |
| 7    | 0         | 0 |
| **Total** | **8** | **~8** |
