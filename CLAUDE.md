# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Workiva Multi-API Python SDK — 3 independent OpenAPI specs (Platform, Chains, Wdata) generated into a single unified Python SDK using a custom codegen pipeline (datamodel-code-generator + Jinja2). No external SDK generators (Speakeasy, openapi-generator, etc.). SDK source lives in `src/workiva/`.

## Commands

```bash
# Full pipeline (download specs → check changes → generate)
make all

# Force regeneration (bypass change detection)
make force

# Individual pipeline steps
make download            # Download latest specs from developers.workiva.com
make check               # Check if specs changed since last generation
make generate            # Generate models + operations from OAS specs
make generate-models     # Generate Pydantic models only
make generate-operations # Generate operation namespaces only

# Testing
make test                # All tests (unit + integration) — 184 tests
make test-unit           # Unit tests only
make test-integration    # Integration tests only
make test-cov            # Coverage report for core modules

# Run a single test
uv run pytest tests/unit/test_polling_helpers.py::TestExtractOperationId::test_full_url -v

# Build wheel
make build               # → dist/workiva-X.Y.Z-py3-none-any.whl

# Dependency management
uv sync                # Install runtime + dev deps
uv sync --group codegen  # Install codegen deps (for generation)
```

## Architecture

### Pipeline: Spec → SDK

```
                  ┌─ codegen/models.py ─────→ models/{api}.py (Pydantic v2)
oas/platform.yaml ─┐  │
oas/chains.yaml   ─┼→ generate_sdk.py ─┤
oas/wdata.yaml    ─┘  │
                  └─ codegen/operations.py ─→ _operations/{namespace}.py (Jinja2)
                       codegen/pagination.py    (pagination config)
```

**`scripts/generate_sdk.py`** — Master codegen orchestrator:
- Phase 1: Invokes `datamodel-code-generator` per spec → Pydantic v2 models
- Phase 2: Parses OAS specs → groups operations by tag → renders Jinja2 templates
- Post-processing: `ast.parse()` validation + Black + isort formatting
- Supports `--models-only` and `--operations-only` for partial regeneration

**`scripts/codegen/models.py`** — Wraps `datamodel-code-generator` CLI:
- Targets Pydantic v2 with strict nullable, extra fields allowed, enum-as-literal
- Applies self-reference fix for Python 3.14 compatibility (PEP 749)
- One model file per API: `platform.py` (~10k lines), `chains.py`, `wdata.py`

**`scripts/codegen/operations.py`** — OAS parser + Jinja2 renderer:
- Parses each spec into `OperationSpec` dataclasses (params, body, response, pagination)
- Groups operations by OAS tag → one namespace file per tag
- Renders sync + async methods using `templates/operation_sync.py.j2` and `operation_async.py.j2`

**`scripts/codegen/pagination.py`** — Pagination pattern configuration:
- 5 patterns: `PLATFORM_NEXT`, `PLATFORM_JSONAPI`, `CHAINS_CURSOR`, `CHAINS_PAGE`, `WDATA_CURSOR`
- Maps operationId → pattern + cursor extractor function

**`scripts/detect_breaking_changes.py`** — AST-based comparison of old vs new model files:
- Parses all `.py` in models dir, extracts Enum classes (members + OpenEnumMeta) and BaseModel classes (fields + types + defaults)
- **Breaking** (exit 1): enum value removed, OpenEnumMeta lost, model/field removed, new required field, schema collision
- **Compatible** (exit 0): new model/enum/field/value added, type annotation changed
- Outputs markdown report for PR body; also writes `breaking_changes_report.md`
- Usage: `python scripts/detect_breaking_changes.py <old_models_dir> <new_models_dir> [oas_dir]`

**`scripts/bump_version.py`** — Atomic patch version bump across all 3 version files:
- Reads current version from `pyproject.toml`, increments patch (e.g. `0.6.0` → `0.6.1`)
- Validates all files contain the old version before writing any (fail-fast)
- Updates: `pyproject.toml`, `_version.py` (`__version__` + `__user_agent__`), `README.md` badge
- Usage: `python scripts/bump_version.py` (prints new version to stdout)

**`scripts/e2e_test.py`** — End-to-end test suite against live APIs:
- 7 sync + 4 async tests across all 3 APIs
- Tests token caching, X-Version header injection, asyncio.gather concurrency
- Usage: `uv run python scripts/e2e_test.py`

### SDK Source Structure

```
src/workiva/
├── __init__.py         # Public exports (hand-written)
├── _version.py         # __version__ + __user_agent__
├── client.py           # Workiva class — namespace access + .wait() polling
├── polling.py          # OperationPoller — sync/async polling with retry-after
├── exceptions.py       # OperationFailed, OperationCancelled, OperationTimeout
├── _client.py          # BaseClient — httpx wrapper (lazy sync/async clients)
├── _auth.py            # OAuth2ClientCredentials(httpx.Auth) — ClassVar token cache
├── _config.py          # SDKConfig + RetryConfig dataclasses
├── _constants.py       # Region enum, SERVERS dict, API_VERSION, get_base_url()
├── _errors.py          # WorkivaAPIError hierarchy + raise_for_status()
├── _retry.py           # RetryTransport + AsyncRetryTransport (exponential backoff)
├── _pagination.py      # paginate() / paginate_async() generators
├── models/
│   ├── platform.py     # ~10k lines — Pydantic v2 models (GENERATED)
│   ├── chains.py       # ~760 lines — Pydantic v2 models (GENERATED)
│   └── wdata.py        # ~2.2k lines — Pydantic v2 models (GENERATED)
└── _operations/
    ├── _base.py        # BaseNamespace(client, api) — shared base class
    ├── files.py         # 18 namespace files (GENERATED)
    ├── chains.py        # Chains: all OAS tags merged into single flat namespace
    ├── wdata.py         # Wdata: all OAS tags merged into single flat namespace
    └── ...              # 357 operations total across all namespaces
```

### Generated vs Hand-Written Code

**Hand-written** (never overwritten by `make generate`):

| File | Purpose |
|------|---------|
| `client.py` | `Workiva` class — namespace lazy-loading, `.wait()` polling |
| `polling.py` | `OperationPoller` — sync/async poll with timeout, retry-after |
| `exceptions.py` | `OperationFailed`, `OperationCancelled`, `OperationTimeout` |
| `_client.py` | `BaseClient` — httpx wrapper, lazy client init, URL building |
| `_auth.py` | `OAuth2ClientCredentials(httpx.Auth)` — token cache + refresh |
| `_config.py` | `SDKConfig`, `RetryConfig` dataclasses |
| `_constants.py` | `Region`, `_API`, `SERVERS`, `API_VERSION` |
| `_errors.py` | `WorkivaAPIError` hierarchy + `raise_for_status()` |
| `_retry.py` | `RetryTransport` + `AsyncRetryTransport` |
| `_pagination.py` | `paginate()` / `paginate_async()` generators |
| `__init__.py` | Public API exports |
| `_version.py` | Version constants |

**Generated** (overwritten on every `make generate`):

| Directory | Content |
|-----------|---------|
| `models/*.py` | Pydantic v2 models from `datamodel-code-generator` |
| `_operations/*.py` (except `_base.py`) | Operation namespaces from Jinja2 templates |

### Auth

All 3 APIs share the same bearer token from `/oauth2/token` (API version 2026-01-01). The `OAuth2ClientCredentials(httpx.Auth)` class handles this automatically:

- **Token cache**: `ClassVar` dict keyed by `(client_id, token_url)` — global across all SDK instances in a process
- **Thread safety**: `threading.Lock` per cache key for concurrent token acquisition
- **Async safety**: `async_auth_flow` wraps token fetch with `asyncio.to_thread` to avoid blocking the event loop
- **401 retry**: Both `sync_auth_flow` and `async_auth_flow` invalidate + re-fetch on 401
- **X-Version header**: Injected via httpx `event_hooks["request"]` (sync `def` for sync client, `async def` for async client)

### Region Routing

`Region.EU` (default), `Region.US`, `Region.APAC`. Each API resolves to a different base URL via the `SERVERS` dict in `_constants.py`:

```python
# Platform: api.{region}.wdesk.com
# Chains:   h.{region}.wdesk.com/s/wdata/oc/api
# Wdata:    h.{region}.wdesk.com/s/wdata/prep
```

### SDK Usage Pattern

```python
from workiva import Workiva, Region

# Sync usage
with Workiva(client_id="...", client_secret="...") as client:
    response = client.files.copy_file(file_id="abc", destination_container="folder-123")
    operation = client.wait(response).result(timeout=300)

# Async usage
async with Workiva(client_id="...", client_secret="...", region=Region.US) as client:
    response = await client.files.copy_file_async(file_id="abc", destination_container="folder-123")
    operation = await client.wait(response).result_async(timeout=300)
```

## Testing

Tests live in `tests/` (outside `src/`, safe from regeneration). 184 tests total.

```
tests/
├── conftest.py                   # Autouse fixture: clears OAuth token cache between tests
├── unit/
│   ├── test_base_client.py       # URL building, request prep, lazy init, multipart
│   ├── test_errors.py            # raise_for_status, exception hierarchy, message parsing
│   ├── test_exceptions.py        # OperationFailed/Cancelled/Timeout with edge cases
│   ├── test_operation_poller.py  # poll, result, terminal states, timeout
│   ├── test_pagination.py        # Cursor extraction, page iteration
│   ├── test_polling_helpers.py   # _extract_operation_id, _get_retry_after
│   ├── test_retry_transport.py   # Backoff, status codes, connection errors
│   └── test_workiva_client.py    # Workiva class, namespace loading, .wait()
└── integration/
    ├── test_auth_flow.py         # Full OAuth flow with MockTransport
    └── test_async_flow.py        # Async auth, retry, 401 refresh, X-Version
```

### Key testing patterns

- **Unit tests** mock `BaseClient` with `MagicMock`/`AsyncMock`
- **Integration tests** use `httpx.MockTransport` with stateful handlers for end-to-end HTTP simulation
- **conftest.py** has an autouse fixture that calls `OAuth2ClientCredentials._clear_cache()` between tests — without this, cached tokens leak between tests
- **Async tests** use `@pytest.mark.asyncio(loop_scope="function")` decorator (pytest-asyncio strict mode)
- `[dependency-groups]` in pyproject.toml is what `uv sync` reads. `[tool.poetry.group.dev.dependencies]` is ignored by uv.

## Publishing to PyPI

When changes affect the SDK source code, a new version must be published to PyPI.

### Automated publish (OAS spec updates)

`check-specs.yml` runs every Monday and handles the full lifecycle:

```
download → changed? → snapshot models → regenerate → test
    → detect_breaking_changes.py
        ├─ exit 0 → bump_version.py → create PR → auto-merge → create release → publish.yml → PyPI
        └─ exit 1 → create PR with "breaking-change" label + report → STOP (manual review)
```

Auto-merge uses `AUTO_MERGE_TOKEN` (PAT with admin access) for `gh pr merge --admin`.

### Manual publish flow

For changes outside OAS updates (core modules, scripts):

```bash
# 1. Bump version atomically across all 3 files
python scripts/bump_version.py  # prints new version

# 2. Run tests
make test

# 3. Commit and push
git add ... && git commit && git push

# 4. Create GitHub release (triggers CI publish)
gh release create vX.Y.Z --title "vX.Y.Z" --notes "Release notes here"
```

**CI handles the rest**: `.github/workflows/publish.yml` triggers on `release: [published]`,
runs tests, builds the wheel, and publishes to PyPI via `gh-action-pypi-publish` using
the `PYPI_API_TOKEN` secret in the `pypi` environment.

### What triggers a new version

- Changes to hand-written core modules (`client.py`, `polling.py`, `exceptions.py`, `_client.py`, `_auth.py`, `_retry.py`, `_errors.py`, `_pagination.py`, `_config.py`, `_constants.py`)
- Changes to codegen scripts or templates that affect the generated SDK
- SDK regeneration after OAS spec updates (`make force`)

### Version files that must stay in sync

| File | Field | Role |
|------|-------|------|
| `pyproject.toml` | `[project].version` | What `uv build` / `pip` reads |
| `src/workiva/_version.py` | `__version__` + `__user_agent__` | Runtime version constant |
| `README.md` | Badge `?v=X.Y.Z` | Cache-buster for shields.io |

All 3 are updated atomically by `scripts/bump_version.py`.

### PyPI credentials

- **CI**: `PYPI_API_TOKEN` as GitHub secret in the `pypi` environment
- **API token**: generate at https://pypi.org/manage/account/token/

## File Survival Matrix

| Location | Survives `make force`? |
|----------|:---------------------:|
| `oas/`, `scripts/`, `Makefile`, `tests/` | Yes (never touched) |
| All hand-written modules (see table above) | Yes (never touched) |
| `pyproject.toml`, `README.md` | Yes (never touched) |
| `models/*.py` | No (regenerated by datamodel-code-generator) |
| `_operations/*.py` (except `_base.py`) | No (regenerated by Jinja2 templates) |
