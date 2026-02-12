#!/usr/bin/env python3
"""Post-generation patches for the Workiva SDK.

This script runs AFTER `speakeasy generate` and applies idempotent patches
to files that Speakeasy regenerates on every run:

  1. __init__.py — appends custom re-exports (Workiva, OperationPoller, etc.)
  2. README.md  — removes Speakeasy scaffolding, adds real install instructions
  3. clientcredentials.py — injects X-Version header into token requests
  4. security.py — updates token_url to /oauth2/token (2026-01-01 API)
  5. sdkconfiguration.py — sets default retry config (backoff 500ms-30s, 2min max)
  6. pyproject.toml — adds license, classifiers, project URLs, [dependency-groups],
     and fixes authors format (Speakeasy merges email into name field)

Usage:
    python scripts/patch_sdk.py workiva-sdk
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SENTINEL = "# --- Custom exports (added by scripts/patch_sdk.py) ---"

CUSTOM_EXPORTS = f"""\

{SENTINEL}
from workiva._hooks.client import Workiva as Workiva
from workiva._hooks.polling import OperationPoller as OperationPoller
from workiva._hooks.exceptions import OperationFailed as OperationFailed
from workiva._hooks.exceptions import OperationCancelled as OperationCancelled
from workiva._hooks.exceptions import OperationTimeout as OperationTimeout
"""

PYPI_README = """\
# Workiva SDK

[![Python 3.10+](https://img.shields.io/pypi/pyversions/workiva)](https://pypi.org/project/workiva/)

**3 APIs. 17 namespaces. 350+ operaciones. Un solo cliente Python.**

[Documentación](https://deloitteworkiva.github.io/workiva-sdk/) · [Quick Start](https://deloitteworkiva.github.io/workiva-sdk/inicio-rapido/) · [API Reference](https://deloitteworkiva.github.io/workiva-sdk/referencia-api/) · [GitHub](https://github.com/DeloitteWorkiva/workiva-sdk)

---

## Instalación

```bash
pip install workiva
```

## Uso

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    # Platform API
    response = client.admin.get_workspaces()

    # Wdata API
    tables = client.wdata.get_tables()

    # Chains API
    chains = client.chains.list_chains()

    # Operaciones de larga duración
    response = client.files.copy_file(file_id="abc", file_copy=params)
    operation = client.wait(response).result(timeout=300)
```

## Características

- **Autenticación automática** — OAuth2 client_credentials con token caching
- **Operaciones de larga duración** — `client.wait(response).result(timeout=300)`
- **Paginación transparente** — `while response.next is not None: response = response.next()`
- **Sync + Async** — Cada método tiene su variante `_async`
- **Multi-región** — EU (default), US, APAC con `server_idx=0|1|2`
- **Reintentos con backoff** — `RetryConfig` global o per-operation
- **Tipado completo** — Modelos Pydantic

## APIs

| API | Namespace | Operaciones |
|-----|-----------|:-----------:|
| **Platform** | `files`, `documents`, `spreadsheets`, `admin`, `permissions`, `tasks`, `presentations`, `milestones`, `activities`, `content`, `graph`, `sustainability`, `test_forms`, `reports`, `operations`, `iam` | 280+ |
| **Chains** | `chains` | 20+ |
| **Wdata** | `wdata` | 56+ |

## Documentación

La documentación completa está en [GitHub Pages](https://deloitteworkiva.github.io/workiva-sdk/):
guías de autenticación, configuración, paginación, operaciones async, manejo de errores,
referencia de los 17 namespaces y guía para Workiva Scripting.

---

Este software es propiedad de Deloitte. Todos los derechos reservados.
"""


def patch_init(sdk_dir: Path) -> None:
    """Append custom re-exports to __init__.py (idempotent)."""
    init_path = sdk_dir / "src" / "workiva" / "__init__.py"
    if not init_path.exists():
        print(f"  SKIP __init__.py — not found at {init_path}")
        return

    content = init_path.read_text()
    if SENTINEL in content:
        print("  __init__.py — custom exports already present, skipping")
        return

    init_path.write_text(content.rstrip("\n") + "\n" + CUSTOM_EXPORTS)
    print("  __init__.py — appended custom exports")


def patch_readme(sdk_dir: Path) -> None:
    """Replace generated README.md with production version (idempotent)."""
    readme_path = sdk_dir / "README.md"
    if not readme_path.exists():
        print(f"  SKIP README.md — not found at {readme_path}")
        return

    content = readme_path.read_text()
    if content.strip() == PYPI_README.strip():
        print("  README.md — already patched, skipping")
        return

    readme_path.write_text(PYPI_README)
    print("  README.md — replaced with production version")


DEPENDENCY_GROUPS_SENTINEL = "[dependency-groups]"

DEPENDENCY_GROUPS = """\
[dependency-groups]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.24",
    "pytest-cov>=6.0",
    "respx>=0.22",
]
"""

PYPROJECT_URLS_SENTINEL = "[project.urls]"

PYPROJECT_URLS = """
[project.urls]
Homepage = "https://github.com/DeloitteWorkiva/workiva-sdk"
Documentation = "https://deloitteworkiva.github.io/workiva-sdk/"
Repository = "https://github.com/DeloitteWorkiva/workiva-sdk"
Issues = "https://github.com/DeloitteWorkiva/workiva-sdk/issues"
Changelog = "https://github.com/DeloitteWorkiva/workiva-sdk/releases"
"""


def patch_pyproject(sdk_dir: Path) -> None:
    """Add project URLs and license to pyproject.toml (idempotent)."""
    pyproject_path = sdk_dir / "pyproject.toml"
    if not pyproject_path.exists():
        print(f"  SKIP pyproject.toml — not found at {pyproject_path}")
        return

    content = pyproject_path.read_text()
    original = content

    # Fix authors format: Speakeasy merges email into name field
    content = re.sub(
        r'authors\s*=\s*\[\{\s*name\s*=\s*"([^<"]+)\s*<([^>]+)>"\s*},?\s*\]',
        r'authors = [{ name = "\1", email = "\2" },]',
        content,
    )

    # Restore [dependency-groups] for uv sync (Speakeasy drops it on regeneration)
    if DEPENDENCY_GROUPS_SENTINEL not in content and "[build-system]" in content:
        content = content.replace(
            "\n[build-system]",
            "\n" + DEPENDENCY_GROUPS.strip() + "\n\n[build-system]",
        )

    # Add proprietary license if missing
    if 'license = ' not in content and 'requires-python' in content:
        content = content.replace(
            'requires-python',
            'license = {text = "Proprietary"}\nrequires-python',
        )
    if '"License :: Other/Proprietary License"' not in content and 'dependencies' in content:
        content = content.replace(
            'dependencies',
            'classifiers = [\n'
            '    "License :: Other/Proprietary License",\n'
            '    "Programming Language :: Python :: 3",\n'
            ']\n'
            'dependencies',
            1,
        )

    # Add project URLs if missing (after dependencies, before [tool.poetry])
    if PYPROJECT_URLS_SENTINEL not in content:
        content = content.replace(
            "\n[tool.poetry]",
            "\n" + PYPROJECT_URLS.strip() + "\n\n[tool.poetry]",
        )

    if content != original:
        pyproject_path.write_text(content)
        print("  pyproject.toml — patched (license + URLs)")
    else:
        print("  pyproject.toml — already patched, skipping")


VERSION_HEADER_SENTINEL = '"X-Version"'

# The token request in clientcredentials.py uses self.client.send() directly,
# bypassing the hook pipeline. We patch it to include the X-Version header
# required by the 2026-01-01 API endpoint /oauth2/token.
CC_OLD = 'self.client.build_request(method="POST", url=token_url, data=payload)'
CC_NEW = (
    'self.client.build_request(\n'
    '                method="POST",\n'
    '                url=token_url,\n'
    '                data=payload,\n'
    '                headers={"X-Version": "2026-01-01"},\n'
    '            )'
)


def patch_clientcredentials(sdk_dir: Path) -> None:
    """Inject X-Version header into token request (idempotent)."""
    cc_path = sdk_dir / "src" / "workiva" / "_hooks" / "clientcredentials.py"
    if not cc_path.exists():
        print(f"  SKIP clientcredentials.py — not found at {cc_path}")
        return

    content = cc_path.read_text()
    if VERSION_HEADER_SENTINEL in content:
        print("  clientcredentials.py — X-Version header already present, skipping")
        return

    if CC_OLD not in content:
        print("  WARN clientcredentials.py — build_request pattern not found, skipping")
        return

    content = content.replace(CC_OLD, CC_NEW)
    cc_path.write_text(content)
    print("  clientcredentials.py — injected X-Version header into token request")


RETRY_SENTINEL = "BackoffStrategy"

# sdk.py: change constructor default from UNSET to a real RetryConfig
SDK_RETRY_IMPORT_OLD = 'from .utils.retries import RetryConfig'
SDK_RETRY_IMPORT_NEW = 'from .utils.retries import BackoffStrategy, RetryConfig'

SDK_RETRY_DEFAULT_OLD = 'retry_config: OptionalNullable[RetryConfig] = UNSET,'
SDK_RETRY_DEFAULT_NEW = (
    'retry_config: OptionalNullable[RetryConfig] = RetryConfig(\n'
    '            "backoff", BackoffStrategy(500, 30000, 1.5, 120000), True\n'
    '        ),'
)


def patch_retry_defaults(sdk_dir: Path) -> None:
    """Set default retry config in SDK constructor (idempotent).

    Speakeasy generates `retry_config: ... = UNSET` in the SDK constructor,
    which means consumers must explicitly opt-in to retries. This patch
    changes the default to a concrete RetryConfig so all consumers get
    automatic retry with backoff on 429/5xx out of the box.
    """
    sdk_path = sdk_dir / "src" / "workiva" / "sdk.py"
    if not sdk_path.exists():
        print(f"  SKIP sdk.py — not found at {sdk_path}")
        return

    content = sdk_path.read_text()
    if RETRY_SENTINEL in content:
        print("  sdk.py — retry defaults already patched, skipping")
        return

    if SDK_RETRY_DEFAULT_OLD not in content:
        print("  WARN sdk.py — retry_config default pattern not found, skipping")
        return

    content = content.replace(SDK_RETRY_IMPORT_OLD, SDK_RETRY_IMPORT_NEW)
    content = content.replace(SDK_RETRY_DEFAULT_OLD, SDK_RETRY_DEFAULT_NEW)
    sdk_path.write_text(content)
    print("  sdk.py — set default retry config (backoff 500ms-30s, 2min max)")


TOKEN_URL_SENTINEL = "hook_ctx.config.get_server_details()"

TOKEN_URL_OLD = "token_url = urljoin(hook_ctx.base_url, credentials.token_url)"
TOKEN_URL_NEW = (
    "global_base_url, _ = hook_ctx.config.get_server_details()\n"
    "            token_url = urljoin(global_base_url, credentials.token_url)"
)


def patch_token_url_resolution(sdk_dir: Path) -> None:
    """Fix token URL resolution to use global server, not operation server (idempotent).

    Speakeasy generates ``urljoin(hook_ctx.base_url, ...)`` which resolves the
    relative /oauth2/token against the operation-specific server (e.g.
    h.eu.wdesk.com).  The token endpoint only exists on the global API server
    (api.eu.wdesk.com), so we resolve against ``hook_ctx.config`` instead.
    """
    cc_path = sdk_dir / "src" / "workiva" / "_hooks" / "clientcredentials.py"
    if not cc_path.exists():
        print(f"  SKIP clientcredentials.py — not found at {cc_path}")
        return

    content = cc_path.read_text()
    if TOKEN_URL_SENTINEL in content:
        print("  clientcredentials.py — token URL resolution already patched, skipping")
        return

    if TOKEN_URL_OLD not in content:
        print("  WARN clientcredentials.py — token URL pattern not found, skipping")
        return

    content = content.replace(TOKEN_URL_OLD, TOKEN_URL_NEW)
    cc_path.write_text(content)
    print("  clientcredentials.py — fixed token URL resolution (use global server)")


REGION_ORDER = {".eu.": 0, ".app.": 1, ".apac.": 2}


def patch_operation_server_order(sdk_dir: Path) -> None:
    """Reorder ``*_OP_SERVERS`` lists: EU=0, US=1, APAC=2 (idempotent).

    Speakeasy reorders path-level servers during generation, placing US at
    index 0.  This must match the global ``SERVERS`` order (EU=0, US=1,
    APAC=2) because ``sdk.server_idx`` applies to both global and
    per-operation server lists.
    """
    models_dir = sdk_dir / "src" / "workiva" / "models"
    if not models_dir.is_dir():
        print(f"  SKIP models/ — not found at {models_dir}")
        return

    op_servers_re = re.compile(
        r"(\w+_OP_SERVERS)\s*=\s*\[(.*?)\]",
        re.DOTALL,
    )
    url_entry_re = re.compile(r"#\s*(\w+)\s*\n\s*\"([^\"]+)\"")

    patched_count = 0
    skipped_count = 0
    model_files = sorted(models_dir.glob("wdata_*.py")) + sorted(
        models_dir.glob("chains_*.py")
    )

    for model_file in model_files:
        content = model_file.read_text()

        match = op_servers_re.search(content)
        if not match:
            continue

        var_name = match.group(1)
        block = match.group(2)

        entries = url_entry_re.findall(block)
        if len(entries) != 3:
            continue

        # Classify each (comment, url) pair by region marker in the URL
        ordered: list[tuple[str, str] | None] = [None, None, None]
        for comment, url in entries:
            for marker, idx in REGION_ORDER.items():
                if marker in url:
                    ordered[idx] = (comment, url)
                    break

        if None in ordered:
            print(
                f"  WARN {model_file.name} — could not classify all server URLs, skipping"
            )
            continue

        # Already correct?
        current_urls = [url for _, url in entries]
        target_urls = [url for _, url in ordered]  # type: ignore[misc]
        if current_urls == target_urls:
            skipped_count += 1
            continue

        # Rebuild the list literal
        new_entries = []
        for comment, url in ordered:  # type: ignore[misc]
            new_entries.append(f'    # {comment}\n    "{url}",')
        new_block = f"{var_name} = [\n" + "\n".join(new_entries) + "\n]"

        content = content[: match.start()] + new_block + content[match.end() :]
        model_file.write_text(content)
        patched_count += 1

    if patched_count > 0:
        print(
            f"  models/ — reordered {patched_count} *_OP_SERVERS lists (EU=0, US=1, APAC=2)"
        )
    else:
        print("  models/ — all *_OP_SERVERS lists already in correct order")


SECURITY_OLD_TOKEN_URL = '/iam/v1/oauth2/token'
SECURITY_NEW_TOKEN_URL = '/oauth2/token'


def patch_security(sdk_dir: Path) -> None:
    """Update token_url default to 2026-01-01 endpoint (idempotent)."""
    security_path = sdk_dir / "src" / "workiva" / "models" / "security.py"
    if not security_path.exists():
        print(f"  SKIP security.py — not found at {security_path}")
        return

    content = security_path.read_text()
    if SECURITY_NEW_TOKEN_URL in content and SECURITY_OLD_TOKEN_URL not in content:
        print("  security.py — token_url already updated, skipping")
        return

    if SECURITY_OLD_TOKEN_URL not in content:
        print("  WARN security.py — old token_url pattern not found, skipping")
        return

    content = content.replace(SECURITY_OLD_TOKEN_URL, SECURITY_NEW_TOKEN_URL)
    security_path.write_text(content)
    print("  security.py — updated token_url to /oauth2/token")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <sdk-dir>")
        sys.exit(1)

    sdk_dir = Path(sys.argv[1])
    if not sdk_dir.is_dir():
        print(f"Error: {sdk_dir} is not a directory")
        sys.exit(1)

    print(f"Patching SDK in {sdk_dir} ...")
    patch_init(sdk_dir)
    patch_readme(sdk_dir)
    patch_clientcredentials(sdk_dir)
    patch_token_url_resolution(sdk_dir)
    patch_security(sdk_dir)
    patch_retry_defaults(sdk_dir)
    patch_operation_server_order(sdk_dir)
    patch_pyproject(sdk_dir)
    print("Done.")


if __name__ == "__main__":
    main()
