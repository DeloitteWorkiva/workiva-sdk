"""Tests for codegen sanitization helpers."""

import sys
from pathlib import Path

import pytest

# Add scripts/ to path so codegen package is importable (same as generate_sdk.py)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))

from codegen.sanitize import (
    _sanitize_string_literal,
    _sanitize_docstring,
    _validate_identifier,
    _validate_enum_value,
)


class TestSanitizeStringLiteral:
    def test_normal_string(self):
        assert _sanitize_string_literal("hello") == "hello"

    def test_escapes_double_quotes(self):
        assert _sanitize_string_literal('say "hi"') == 'say \\"hi\\"'

    def test_escapes_backslashes(self):
        assert _sanitize_string_literal("path\\to") == "path\\\\to"

    def test_escapes_both(self):
        assert _sanitize_string_literal('a\\"b') == 'a\\\\\\"b'


class TestSanitizeDocstring:
    def test_normal_string(self):
        assert _sanitize_docstring("normal docs") == "normal docs"

    def test_escapes_triple_quotes(self):
        result = _sanitize_docstring('contains """ inside')
        assert '"""' not in result

    def test_no_triple_quotes_unchanged(self):
        assert _sanitize_docstring("no quotes here") == "no quotes here"


class TestValidateIdentifier:
    def test_valid_identifier(self):
        assert _validate_identifier("MyModel", "test") == "MyModel"

    def test_valid_underscore(self):
        assert _validate_identifier("_private", "test") == "_private"

    def test_rejects_hyphenated(self):
        with pytest.raises(ValueError, match="Invalid Python identifier"):
            _validate_identifier("bad-name", "test")

    def test_rejects_injection(self):
        with pytest.raises(ValueError, match="Invalid Python identifier"):
            _validate_identifier("foo; import os", "test")

    def test_rejects_empty(self):
        with pytest.raises(ValueError, match="Invalid Python identifier"):
            _validate_identifier("", "test")

    def test_rejects_starts_with_number(self):
        with pytest.raises(ValueError, match="Invalid Python identifier"):
            _validate_identifier("1bad", "test")


class TestValidateEnumValue:
    def test_simple_value(self):
        assert _validate_enum_value("ACTIVE") == "ACTIVE"

    def test_hyphenated_value(self):
        assert _validate_enum_value("in-progress") == "in-progress"

    def test_spaced_value(self):
        assert _validate_enum_value("some value") == "some value"

    def test_rejects_injection(self):
        with pytest.raises(ValueError, match="Unsafe enum value"):
            _validate_enum_value('foo"]; import os')

    def test_rejects_newline(self):
        with pytest.raises(ValueError, match="Unsafe enum value"):
            _validate_enum_value("foo\nbar")

    def test_rejects_backtick(self):
        with pytest.raises(ValueError, match="Unsafe enum value"):
            _validate_enum_value("foo`bar")

    def test_escapes_quotes_in_valid_value(self):
        # Values with quotes should be rejected by the regex, not escaped
        with pytest.raises(ValueError, match="Unsafe enum value"):
            _validate_enum_value('contains"quote')
