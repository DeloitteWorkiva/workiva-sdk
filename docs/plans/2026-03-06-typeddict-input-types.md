# TypedDict Input Types — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Generate TypedDict classes for all 70 models used as method input parameters, so users can pass plain dicts with full IDE autocompletion — zero model imports needed.

**Architecture:** Add a new codegen phase that introspects the OpenAPI spec to generate TypedDict classes alongside existing Pydantic models. TypedDicts use snake_case keys (matching Python convention). Operation templates use `Union[Model, TypedDict]` for input params, so both patterns work. Runtime already handles dicts via `_deep_serialize()` — no runtime changes needed.

**Tech Stack:** Python 3.10+, TypedDict (typing), Jinja2, datamodel-code-generator (existing), pytest

---

## Background

### The Problem

102 method parameters across 70 unique models force users to import Pydantic model classes for input:

```python
# CURRENT — user must import FileCopyOptions
from workiva.models.platform import FileCopyOptions
client.files.copy_file(file_id="abc", options=FileCopyOptions(shallow_copy=True))
```

### The Stripe/OpenAI Standard

Modern SDKs use TypedDict for input (structural typing) and Pydantic for output (validation):

```python
# TARGET — zero imports, IDE autocompletion on dict keys
client.files.copy_file(file_id="abc", options={"shallow_copy": True})
```

### Key Facts from Analysis

- **70 unique models** used as input (66 platform, 4 wdata, 0 chains)
- **0 nested model references** — all input model fields are primitives (bool, str, int, Optional[str], Literal[...])
- **6 dual-use models** are used as both input AND output (MetricValue, OrganizationUser, Section, Sheet, Solution, Workspace)
- **`_deep_serialize()`** already handles dicts recursively — zero runtime changes needed
- **`populate_by_name=True`** is set on all Pydantic models — they already accept snake_case

### Architecture Decision: TypedDict Generation Strategy

**Option A (chosen): Generate from OAS spec at codegen time**
- Parse the same OpenAPI spec that generates Pydantic models
- Extract only models referenced as input params
- Generate TypedDict classes with snake_case keys
- Pro: single source of truth, stays in sync automatically
- Pro: only generates what's needed (70 models, not 610)

**Option B (rejected): Generate from Pydantic models at runtime**
- Introspect `model_fields` on existing Pydantic classes
- Pro: simpler
- Con: runtime overhead, harder to type-check

---

## Task 1: Create TypedDict generator module

Generate TypedDict classes from OAS spec schemas, targeting only models used as input parameters.

**Files:**
- Create: `scripts/codegen/typeddicts.py`
- Test: `tests/unit/test_typeddict_generation.py`

**Step 1: Write the failing test**

```python
# tests/unit/test_typeddict_generation.py
"""Tests for TypedDict generation from OAS schemas."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Add scripts/ to path for codegen imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))


class TestGenerateTypedDict:
    def test_simple_bool_fields(self):
        """FileCopyOptions-like schema produces correct TypedDict."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "shallowCopy": {"type": "boolean"},
                "includeComments": {"type": "boolean"},
            },
        }
        source = generate_typeddict_source("FileCopyOptions", schema, spec={})
        assert "class FileCopyOptionsParam(TypedDict, total=False):" in source
        assert "shallow_copy: bool" in source
        assert "include_comments: bool" in source

    def test_required_fields(self):
        """Required fields are NOT total=False — they stay required."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "permission": {"type": "string"},
                "principal": {"type": "string"},
                "principalType": {"type": "string", "enum": ["user", "group"]},
            },
            "required": ["permission", "principal"],
        }
        source = generate_typeddict_source("ResourcePermission", schema, spec={})
        # Required fields use Required[] annotation
        assert "permission: Required[str]" in source
        assert "principal: Required[str]" in source
        # Optional enum field
        assert "principal_type: Literal['user', 'group']" in source

    def test_optional_string_field(self):
        """Optional fields use NotRequired annotation."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
        }
        source = generate_typeddict_source("SimpleModel", schema, spec={})
        assert "name: str" in source

    def test_list_field(self):
        """Array fields become list[type]."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "values": {"type": "array", "items": {"type": "string"}},
            },
        }
        source = generate_typeddict_source("WithList", schema, spec={})
        assert "values: list[str]" in source

    def test_skips_readonly_fields(self):
        """readOnly fields are excluded from input TypedDict."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string", "readOnly": True},
                "name": {"type": "string"},
            },
        }
        source = generate_typeddict_source("WithReadOnly", schema, spec={})
        assert "id" not in source
        assert "name: str" in source
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/unit/test_typeddict_generation.py -v`
Expected: FAIL (module `codegen.typeddicts` not found)

**Step 3: Implement**

```python
# scripts/codegen/typeddicts.py
"""Generate TypedDict classes from OpenAPI schemas for input parameters.

Produces TypedDict versions of Pydantic models used as method input params,
so users can pass plain dicts with IDE autocompletion.
"""

from __future__ import annotations

import keyword
import re
from typing import Any


# Map of OpenAPI type → Python type annotation
_TYPE_MAP: dict[str, str] = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list[Any]",
    "object": "dict[str, Any]",
}


def _snake_case(name: str) -> str:
    """Convert camelCase to snake_case."""
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s2 = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s1)
    result = s2.lower()
    if keyword.iskeyword(result) or result in ("type", "id", "format", "next", "filter"):
        result += "_"
    return result


def _resolve_ref(ref: str, spec: dict[str, Any]) -> dict[str, Any]:
    """Resolve a $ref pointer within the spec."""
    if not ref.startswith("#/"):
        return {}
    parts = ref[2:].split("/")
    node = spec
    for part in parts:
        node = node.get(part, {})
    return node


def _get_field_type(prop_schema: dict[str, Any], spec: dict[str, Any]) -> str:
    """Resolve an OAS property schema to a Python type string for TypedDict."""
    # Enum → Literal[...]
    enum_values = prop_schema.get("enum")
    if enum_values and prop_schema.get("type") == "string":
        quoted = ", ".join(f"'{v}'" for v in enum_values)
        return f"Literal[{quoted}]"

    # $ref → resolve and recurse
    if "$ref" in prop_schema:
        resolved = _resolve_ref(prop_schema["$ref"], spec)
        return _get_field_type(resolved, spec)

    # allOf with single $ref
    all_of = prop_schema.get("allOf")
    if all_of and len(all_of) >= 1 and "$ref" in all_of[0]:
        resolved = _resolve_ref(all_of[0]["$ref"], spec)
        return _get_field_type(resolved, spec)

    schema_type = prop_schema.get("type", "object")

    # Array
    if schema_type == "array":
        items = prop_schema.get("items", {})
        item_type = _get_field_type(items, spec)
        return f"list[{item_type}]"

    # Binary
    if prop_schema.get("format") == "binary":
        return "bytes"

    return _TYPE_MAP.get(schema_type, "Any")


def generate_typeddict_source(
    model_name: str,
    schema: dict[str, Any],
    spec: dict[str, Any],
) -> str:
    """Generate a TypedDict class source string from an OAS object schema.

    Args:
        model_name: The Pydantic model name (e.g. "FileCopyOptions").
        schema: The resolved OAS schema dict with "properties".
        spec: The full OAS spec (for $ref resolution).

    Returns:
        Python source code for the TypedDict class.
    """
    td_name = f"{model_name}Param"
    properties = schema.get("properties", {})
    required_set = set(schema.get("required", []))

    lines: list[str] = []
    # Use total=False so all fields are optional by default;
    # required fields use Required[] annotation
    lines.append(f"class {td_name}(TypedDict, total=False):")

    if not properties:
        lines.append("    pass")
        return "\n".join(lines)

    for prop_name, prop_schema in sorted(properties.items()):
        # Skip readOnly fields
        if prop_schema.get("readOnly", False):
            continue

        python_name = _snake_case(prop_name)
        python_type = _get_field_type(prop_schema, spec)

        if prop_name in required_set:
            lines.append(f"    {python_name}: Required[{python_type}]")
        else:
            lines.append(f"    {python_name}: {python_type}")

    return "\n".join(lines)


def generate_typeddicts_for_api(
    spec: dict[str, Any],
    input_model_names: set[str],
) -> dict[str, str]:
    """Generate TypedDict source for all input models in a spec.

    Args:
        spec: The full OAS spec.
        input_model_names: Set of model names to generate TypedDicts for.

    Returns:
        Dict mapping model name → TypedDict source string.
    """
    schemas = spec.get("components", {}).get("schemas", {})
    results: dict[str, str] = {}

    for model_name in sorted(input_model_names):
        if model_name not in schemas:
            continue
        schema = schemas[model_name]
        # Only generate for object schemas with properties
        if schema.get("type", "object") != "object" or "properties" not in schema:
            continue
        results[model_name] = generate_typeddict_source(model_name, schema, spec)

    return results
```

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/unit/test_typeddict_generation.py -v`
Expected: PASS

**Step 5: Commit**

```
feat: add TypedDict generator for input model params
```

---

## Task 2: Generate TypedDict files per API

Integrate the TypedDict generator into the codegen pipeline to produce `_types.py` files alongside existing model files.

**Files:**
- Modify: `scripts/generate_sdk.py`
- Create: `scripts/codegen/templates/typeddicts.py.j2`
- Test: `tests/unit/test_typeddict_generation.py` (add integration test)

**Step 1: Write the failing test**

```python
# Add to tests/unit/test_typeddict_generation.py

class TestTypedDictFileGeneration:
    def test_platform_types_file_exists(self):
        """TypedDict file should be generated for platform API."""
        from pathlib import Path
        types_file = Path("src/workiva/models/platform_types.py")
        assert types_file.exists(), "platform_types.py not generated"

    def test_platform_types_has_file_copy_options(self):
        """FileCopyOptionsParam should be importable."""
        from workiva.models.platform_types import FileCopyOptionsParam
        assert FileCopyOptionsParam is not None

    def test_typeddict_is_valid_typeddict(self):
        """Generated class must be a real TypedDict."""
        from workiva.models.platform_types import FileCopyOptionsParam
        import typing
        # TypedDict classes have __required_keys__ and __optional_keys__
        assert hasattr(FileCopyOptionsParam, "__optional_keys__")

    def test_typeddict_accepts_snake_case_keys(self):
        """TypedDict should use snake_case keys."""
        from workiva.models.platform_types import FileCopyOptionsParam
        opts: FileCopyOptionsParam = {"shallow_copy": True}
        assert opts["shallow_copy"] is True

    def test_wdata_types_file_exists(self):
        """TypedDict file should be generated for wdata API."""
        from pathlib import Path
        types_file = Path("src/workiva/models/wdata_types.py")
        assert types_file.exists(), "wdata_types.py not generated"

    def test_resource_permission_has_required_fields(self):
        """ResourcePermissionParam should mark permission/principal as Required."""
        from workiva.models.platform_types import ResourcePermissionParam
        assert "permission" in ResourcePermissionParam.__required_keys__
        assert "principal" in ResourcePermissionParam.__required_keys__
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/unit/test_typeddict_generation.py::TestTypedDictFileGeneration -v`
Expected: FAIL (files don't exist yet)

**Step 3: Create the Jinja2 template**

```jinja2
{# scripts/codegen/templates/typeddicts.py.j2 #}
"""{{ api | title }} API — TypedDict input types.

Auto-generated by codegen. Do not edit manually.

These TypedDict classes allow passing plain dicts to SDK methods
with full IDE autocompletion, instead of importing Pydantic models.
"""

from __future__ import annotations

from typing import Any, Literal, Required, TypedDict


{% for td_source in typeddict_sources %}
{{ td_source }}

{% endfor %}
```

**Step 4: Integrate into `scripts/generate_sdk.py`**

Add a Phase 3 to `generate_sdk.py` that:

1. For each API spec, calls `parse_spec()` to get operations
2. Collects all model types used as INPUT params (reuse `_collect_model_types` but only on body fields, not responses)
3. Calls `generate_typeddicts_for_api()` with the input model names
4. Renders the `typeddicts.py.j2` template
5. Writes to `src/workiva/models/{api}_types.py`

In `generate_sdk.py`, add after the operations phase:

```python
from codegen.typeddicts import generate_typeddicts_for_api
import yaml

def generate_typeddict_files(env: SandboxedEnvironment) -> None:
    """Generate TypedDict files for input models."""
    typeddict_template = env.get_template("typeddicts.py.j2")

    for api, spec_filename in API_SPECS.items():
        spec_path = OAS_DIR / spec_filename
        if not spec_path.exists():
            continue

        with open(spec_path) as f:
            spec = yaml.safe_load(f)

        # Collect input model names from operations
        groups = parse_spec(spec_path, api)
        input_models: set[str] = set()
        for tag, operations in groups.items():
            for op in operations:
                if op.body_fields:
                    for bf in op.body_fields:
                        _collect_model_types(bf.python_type, input_models)

        if not input_models:
            print(f"  [SKIP] {api}: no input models")
            continue

        # Generate TypedDict sources
        td_sources = generate_typeddicts_for_api(spec, input_models)
        if not td_sources:
            continue

        # Render template
        source = typeddict_template.render(
            api=api,
            typeddict_sources=list(td_sources.values()),
        )

        source = _format_source(source)

        # Write
        output_path = MODELS_DIR / f"{api}_types.py"
        output_path.write_text(source)
        print(f"  [OK] {api}_types.py: {len(td_sources)} TypedDict classes")
```

Add the phase call in `main()`:

```python
if do_operations:
    print("\n--- Phase 2: Generate Operations ---")
    env = SandboxedEnvironment(...)
    total = generate_operations(env)
    print(f"\n[DONE] Total operations generated: {total}")

    print("\n--- Phase 3: Generate TypedDict Input Types ---")
    generate_typeddict_files(env)
```

**Step 5: Run the generator and tests**

Run: `uv run python scripts/generate_sdk.py --operations-only && uv run pytest tests/unit/test_typeddict_generation.py -v`
Expected: PASS

**Step 6: Commit**

```
feat: generate TypedDict input type files per API
```

---

## Task 3: Update operation templates to accept TypedDict | Model

Change the generated method signatures to accept both Pydantic models and TypedDict dicts for input parameters.

**Files:**
- Modify: `scripts/codegen/templates/operation_sync.py.j2`
- Modify: `scripts/codegen/templates/operation_async.py.j2`
- Modify: `scripts/codegen/templates/_params.py.j2`
- Modify: `scripts/codegen/templates/namespace.py.j2`
- Modify: `scripts/generate_sdk.py` (pass `input_model_types` to template context)
- Regenerate: `uv run python scripts/generate_sdk.py --operations-only`
- Test: `tests/unit/test_typeddict_generation.py`

**Step 1: Write the failing test**

```python
# Add to tests/unit/test_typeddict_generation.py

class TestOperationAcceptsDicts:
    def test_copy_file_accepts_dict_for_options(self):
        """copy_file should accept a plain dict for the options param."""
        import inspect
        from workiva._operations.files import Files
        sig = inspect.signature(Files.copy_file)
        options_param = sig.parameters["options"]
        ann = str(options_param.annotation)
        # Should accept both FileCopyOptions and FileCopyOptionsParam (TypedDict)
        assert "FileCopyOptionsParam" in ann or "dict" in ann

    def test_permissions_mod_accepts_dict_for_list(self):
        """file_permissions_modification should accept list[dict] for to_assign."""
        import inspect
        from workiva._operations.files import Files
        sig = inspect.signature(Files.file_permissions_modification)
        param = sig.parameters["to_assign"]
        ann = str(param.annotation)
        assert "ResourcePermissionParam" in ann or "dict" in ann
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/unit/test_typeddict_generation.py::TestOperationAcceptsDicts -v`
Expected: FAIL

**Step 3: Implement template changes**

The key change is in the operation templates. When a body field's type is a model that has a TypedDict equivalent, the type hint becomes `ModelName | ModelNameParam`.

**3a. Track which models have TypedDict equivalents**

In `generate_sdk.py`, when rendering each namespace, pass the set of input model names that have TypedDicts:

```python
# In generate_operations(), add to template context:
source = namespace_template.render(
    ...
    input_model_types=input_model_types_for_api,  # set of model names with TypedDicts
)
```

Where `input_model_types_for_api` is collected by iterating body fields (same as Task 2).

**3b. Update namespace.py.j2**

Add conditional import of TypedDict types:

```jinja2
{% if typeddict_imports %}
from workiva.models.{{ api }}_types import (
{% for td in typeddict_imports %}
    {{ td }},
{% endfor %}
)
{% endif %}
```

**3c. Update _params.py.j2**

When rendering a body field parameter whose type has a TypedDict, change the annotation:

```jinja2
{# For each body field #}
{% if bf.python_type in input_model_types %}
        {{ bf.python_name }}: Optional[{{ bf.python_type }} | {{ bf.python_type }}Param] = None,
{% elif 'list[' in bf.python_type and bf.python_type | replace('list[', '') | replace(']', '') in input_model_types %}
{% set inner = bf.python_type | replace('list[', '') | replace(']', '') %}
        {{ bf.python_name }}: Optional[list[{{ inner }} | {{ inner }}Param]] = None,
{% else %}
        {{ bf.python_name }}: Optional[{{ bf.python_type }}] = None,
{% endif %}
```

Apply this logic everywhere body fields with model types are rendered — in both operation_sync.py.j2 and operation_async.py.j2, and in the _params.py.j2 macro used by @overload stubs.

**Step 4: Regenerate and test**

Run: `uv run python scripts/generate_sdk.py --operations-only && uv run pytest tests/ -v`
Expected: ALL tests pass

**Step 5: Verify generated output**

Spot-check `src/workiva/_operations/files.py`:

```python
# Should show:
def copy_file(
    self,
    *,
    file_id: str,
    options: Optional[FileCopyOptions | FileCopyOptionsParam] = None,
    ...
```

**Step 6: Commit**

```
feat: operation params accept TypedDict dicts alongside models
```

---

## Task 4: Re-export TypedDict types from `workiva.models`

Make TypedDict types discoverable via the models package so IDE autocompletion works on dict keys when users explicitly type their variables.

**Files:**
- Modify: `src/workiva/models/__init__.py`
- Test: `tests/unit/test_typeddict_generation.py`

**Step 1: Write the failing test**

```python
# Add to tests/unit/test_typeddict_generation.py

class TestTypedDictExports:
    def test_importable_from_models_package(self):
        """TypedDict types should be importable from workiva.models."""
        from workiva.models import FileCopyOptionsParam
        assert FileCopyOptionsParam is not None

    def test_importable_from_top_level(self):
        """Most common TypedDict types importable from workiva root (optional)."""
        # Users who want explicit typing can do:
        # from workiva.models import FileCopyOptionsParam
        # opts: FileCopyOptionsParam = {"shallow_copy": True}
        from workiva.models.platform_types import FileCopyOptionsParam
        opts: FileCopyOptionsParam = {"shallow_copy": True}
        assert opts["shallow_copy"] is True
```

**Step 2: Implement**

Update `src/workiva/models/__init__.py` to re-export TypedDict types:

```python
"""Workiva SDK models — generated by datamodel-code-generator.

Models (Pydantic, for responses)::

    from workiva.models.platform import File, Operation
    from workiva.models.chains import ChainResponse
    from workiva.models.wdata import TableDto

Input types (TypedDict, for method params — optional)::

    from workiva.models.platform_types import FileCopyOptionsParam
    from workiva.models.wdata_types import PivotDefinitionDtoParam
"""

# Re-export all TypedDict types for convenience
from workiva.models.platform_types import *  # noqa: F401,F403
try:
    from workiva.models.wdata_types import *  # noqa: F401,F403
except ImportError:
    pass
```

**Step 3: Run tests**

Run: `uv run pytest tests/unit/test_typeddict_generation.py tests/ -v`
Expected: ALL pass

**Step 4: Commit**

```
feat: re-export TypedDict input types from workiva.models
```

---

## Task 5: Update documentation and README

Show users the new zero-import pattern.

**Files:**
- Modify: `README.md`
- Modify: `docs/index.md`
- Modify: `docs/configuracion.md`

**Step 1: Add dict input examples to README.md**

In the usage section, add:

```markdown
### Input Parameters

Most operations accept plain dicts — no model imports needed:

```python
# Plain dicts with IDE autocompletion
client.files.copy_file(
    file_id="abc",
    options={"shallow_copy": True, "include_comments": True},
)

# Pydantic models still work for those who prefer them
from workiva.models.platform import FileCopyOptions
client.files.copy_file(
    file_id="abc",
    options=FileCopyOptions(shallow_copy=True),
)

# For explicit typing (optional):
from workiva.models import FileCopyOptionsParam
opts: FileCopyOptionsParam = {"shallow_copy": True}
client.files.copy_file(file_id="abc", options=opts)
```
```

**Step 2: Update docs/index.md and docs/configuracion.md**

Add a brief note about dict inputs in the quickstart sections.

**Step 3: Commit**

```
docs: document TypedDict input types and zero-import pattern
```

---

## Task 6: End-to-end integration test

Verify the complete flow works: user passes dict → serialized correctly → API receives camelCase JSON.

**Files:**
- Create: `tests/unit/test_dict_input_e2e.py`

**Step 1: Write the test**

```python
# tests/unit/test_dict_input_e2e.py
"""End-to-end test: dict input → correct JSON serialization."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import httpx
import pytest


class TestDictInputSerialization:
    def _capture_request(self):
        """Create a mock transport that captures the request body."""
        captured = {}

        def handler(request: httpx.Request) -> httpx.Response:
            captured["body"] = json.loads(request.content) if request.content else None
            captured["method"] = request.method
            return httpx.Response(200, json={"id": "file-1"})

        return captured, httpx.MockTransport(handler)

    def test_dict_options_serialized_as_camel_case(self):
        """Dict with snake_case keys must serialize to camelCase JSON."""
        from workiva._client import _deep_serialize

        body = {
            "options": {"shallow_copy": True, "include_comments": False},
        }
        result = _deep_serialize(body)
        # _deep_serialize passes dicts through as-is (no aliasing)
        # The camelCase aliasing happens in the OAS schema key names
        # used by the template (e.g. _body["shallowCopy"] = ...)
        assert isinstance(result, dict)

    def test_pydantic_model_and_dict_produce_same_keys(self):
        """A Pydantic model and equivalent dict must serialize compatibly."""
        from workiva.models.platform import FileCopyOptions
        from workiva._client import _deep_serialize

        # Pydantic model
        model = FileCopyOptions(shallow_copy=True)
        model_json = model.model_dump(by_alias=True, exclude_none=True)

        # Equivalent dict (using camelCase keys as the API expects)
        dict_input = {"shallowCopy": True}

        assert model_json["shallowCopy"] == dict_input["shallowCopy"]

    def test_typeddict_type_checking(self):
        """TypedDict provides correct key information."""
        from workiva.models.platform_types import FileCopyOptionsParam

        # This would fail type checking if keys were wrong
        opts: FileCopyOptionsParam = {
            "shallow_copy": True,
            "include_comments": False,
        }
        assert opts["shallow_copy"] is True
```

**Step 2: Run tests**

Run: `uv run pytest tests/unit/test_dict_input_e2e.py tests/ -v`
Expected: ALL pass

**Step 3: Commit**

```
test: add end-to-end tests for dict input serialization
```

---

## Execution Order and Dependencies

```
Task 1 (TypedDict generator) ──→ independent, foundation
Task 2 (generate files) ────────→ depends on Task 1
Task 3 (update templates) ──────→ depends on Task 2
Task 4 (re-exports) ────────────→ depends on Task 2
Task 5 (docs) ──────────────────→ depends on Task 3
Task 6 (e2e tests) ─────────────→ depends on Task 3
```

Recommended order: 1 → 2 → 3 → 4 → 6 → 5

Tasks 4, 5, and 6 are independent of each other (all depend on 3).

---

## Important: Key/Aliasing Decision

The TypedDict keys use **snake_case** (Python convention):

```python
class FileCopyOptionsParam(TypedDict, total=False):
    shallow_copy: bool          # NOT shallowCopy
    include_comments: bool      # NOT includeComments
```

However, the generated operation templates build `_body` dicts with **camelCase** keys (matching the API):

```python
# In operation_sync.py.j2:
if options is not None:
    _body["options"] = options    # ← raw value, serialized by _deep_serialize
```

When the user passes a TypedDict/dict, it arrives in `_body["options"]` as a raw dict. `_deep_serialize()` passes dicts through as-is. This means **the dict keys must be camelCase** to match what the API expects.

**BUT** — we want the TypedDict to have snake_case keys for Pythonic usage. This creates a mismatch.

**Resolution:** Add a snake_case → camelCase conversion in `_deep_serialize()` for dict values that correspond to known model fields. Alternatively, the TypedDict keys should use **camelCase** to match the API format, since the dict is passed directly to the JSON body.

**Decision: Use camelCase keys in TypedDict** — this matches the wire format and avoids runtime conversion overhead. The TypedDict serves as documentation of valid keys, and camelCase is what the API expects. Users who want snake_case should use the Pydantic model.

**Update the generator accordingly:**

```python
# In generate_typeddict_source(), use the OAS property name (camelCase)
# instead of _snake_case() conversion:

for prop_name, prop_schema in sorted(properties.items()):
    if prop_schema.get("readOnly", False):
        continue
    python_type = _get_field_type(prop_schema, spec)
    if prop_name in required_set:
        lines.append(f"    {prop_name}: Required[{python_type}]")
    else:
        lines.append(f"    {prop_name}: {python_type}")
```

Wait — camelCase keys aren't valid Python identifiers in some cases, and TypedDict keys must be valid identifiers. All OAS property names are valid camelCase identifiers, so this works.

**HOWEVER** — there's an even better approach. Looking at how the templates build `_body`:

```jinja2
if {{ bf.python_name }} is not None:
    _body["{{ bf.name }}"] = {{ bf.python_name }}
```

The value assigned is the raw Python variable. If the user passes a dict, it goes directly into `_body["options"]`. This dict is then sent as JSON. The dict keys must be camelCase.

**Final decision:** TypedDict uses **snake_case** keys AND we add a conversion step in `_deep_serialize()` that maps snake_case keys to camelCase when the value is a plain dict (not a Pydantic model). This gives the best UX: users write Pythonic snake_case, the SDK handles the rest.

Add this to `_deep_serialize()`:

```python
def _snake_to_camel(name: str) -> str:
    """Convert snake_case to camelCase."""
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])

def _deep_serialize(value: Any) -> Any:
    if isinstance(value, PydanticBaseModel):
        return value.model_dump(by_alias=True, exclude_none=True)
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, list):
        return [_deep_serialize(v) for v in value]
    if isinstance(value, dict):
        return {_snake_to_camel(k): _deep_serialize(v) for k, v in value.items()}
    return value
```

**WAIT** — this would break existing code that passes dicts with camelCase keys (which is what the template `_body` dict uses internally). The `_body` dict already has camelCase keys like `"shallowCopy"`, and converting those again would produce `"shallowcopy"`.

**Correct approach:** Only convert snake_case keys (keys containing underscores). Leave camelCase keys as-is:

```python
def _deep_serialize(value: Any) -> Any:
    if isinstance(value, PydanticBaseModel):
        return value.model_dump(by_alias=True, exclude_none=True)
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, list):
        return [_deep_serialize(v) for v in value]
    if isinstance(value, dict):
        return {
            (_snake_to_camel(k) if "_" in k else k): _deep_serialize(v)
            for k, v in value.items()
        }
    return value
```

This way:
- `{"shallow_copy": True}` → `{"shallowCopy": True}` ✅
- `{"shallowCopy": True}` → `{"shallowCopy": True}` ✅ (no underscore, no conversion)
- Internal `_body` keys → unchanged ✅

This should be implemented in Task 3 alongside the template changes.

---

## Total Test Impact

| Task | New Tests | Modified Tests |
|------|-----------|----------------|
| 1    | 5         | 0 |
| 2    | 6         | 0 |
| 3    | 2         | 0 |
| 4    | 2         | 0 |
| 5    | 0         | 0 |
| 6    | 3         | 0 |
| **Total** | **18** | **0** |
