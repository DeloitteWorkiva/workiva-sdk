"""Sanitization helpers — guard against OAS-spec injection into generated code.

These are pure functions with no external dependencies, so they can be
imported safely from test environments that don't have the codegen group
(pyyaml, jinja2, etc.) installed.
"""

from __future__ import annotations

import re


def _sanitize_string_literal(value: str) -> str:
    """Escape characters that would break a Python string literal."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _sanitize_docstring(value: str) -> str:
    """Escape triple-quote sequences in docstrings."""
    return value.replace('"""', r'\"\"\"')


def _validate_identifier(name: str, context: str) -> str:
    """Validate that a name is a valid Python identifier. Raise on failure."""
    if not name.isidentifier():
        raise ValueError(f"Invalid Python identifier from OAS spec ({context}): {name!r}")
    return name


_SAFE_ENUM_RE = re.compile(r'^[a-zA-Z0-9_\-. /,:;()+@#&=*!?]+$')


def _validate_enum_value(value: str) -> str:
    """Validate enum value contains only safe characters."""
    if not _SAFE_ENUM_RE.match(value):
        raise ValueError(f"Unsafe enum value in OAS spec: {value!r}")
    return _sanitize_string_literal(value)
