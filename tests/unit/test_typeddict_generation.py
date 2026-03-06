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
        """Required fields use Required[] annotation."""
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
        assert "permission: Required[str]" in source
        assert "principal: Required[str]" in source
        assert "principal_type: Literal['user', 'group']" in source

    def test_optional_string_field(self):
        """Optional fields use just the type."""
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

    def test_ref_resolution(self):
        """$ref fields resolve to the referenced schema type."""
        from codegen.typeddicts import generate_typeddict_source

        spec = {
            "components": {
                "schemas": {
                    "Status": {
                        "type": "string",
                        "enum": ["active", "inactive"],
                    }
                }
            }
        }
        schema = {
            "type": "object",
            "properties": {
                "status": {"$ref": "#/components/schemas/Status"},
            },
        }
        source = generate_typeddict_source("WithRef", schema, spec=spec)
        assert "status: Literal['active', 'inactive']" in source

    def test_allof_single_ref(self):
        """allOf with a single $ref resolves correctly."""
        from codegen.typeddicts import generate_typeddict_source

        spec = {
            "components": {
                "schemas": {
                    "Priority": {
                        "type": "string",
                        "enum": ["low", "high"],
                    }
                }
            }
        }
        schema = {
            "type": "object",
            "properties": {
                "priority": {"allOf": [{"$ref": "#/components/schemas/Priority"}]},
            },
        }
        source = generate_typeddict_source("WithAllOf", schema, spec=spec)
        assert "priority: Literal['low', 'high']" in source

    def test_binary_format(self):
        """format: binary maps to bytes."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "content": {"type": "string", "format": "binary"},
            },
        }
        source = generate_typeddict_source("WithBinary", schema, spec={})
        assert "content: bytes" in source

    def test_empty_properties(self):
        """Schema with no properties produces pass body."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {"type": "object", "properties": {}}
        source = generate_typeddict_source("EmptyModel", schema, spec={})
        assert "class EmptyModelParam(TypedDict, total=False):" in source
        assert "    pass" in source

    def test_snake_case_conversion(self):
        """camelCase property names become snake_case."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "XMLParser": {"type": "string"},
            },
        }
        source = generate_typeddict_source("Person", schema, spec={})
        assert "first_name: str" in source
        assert "last_name: str" in source
        assert "xml_parser: str" in source

    def test_keyword_suffix(self):
        """Python keywords get underscore suffix."""
        from codegen.typeddicts import generate_typeddict_source

        schema = {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "filter": {"type": "string"},
            },
        }
        source = generate_typeddict_source("WithKeywords", schema, spec={})
        assert "type_: str" in source
        assert "filter_: str" in source


class TestGenerateTypedDictsForApi:
    def test_generates_only_input_models(self):
        """Only models in input_model_names are generated."""
        from codegen.typeddicts import generate_typeddicts_for_api

        spec = {
            "components": {
                "schemas": {
                    "InputModel": {
                        "type": "object",
                        "properties": {"name": {"type": "string"}},
                    },
                    "OutputModel": {
                        "type": "object",
                        "properties": {"id": {"type": "string"}},
                    },
                }
            }
        }
        results = generate_typeddicts_for_api(spec, {"InputModel"})
        assert "InputModel" in results
        assert "OutputModel" not in results

    def test_skips_missing_schemas(self):
        """Models not found in schemas are silently skipped."""
        from codegen.typeddicts import generate_typeddicts_for_api

        spec = {"components": {"schemas": {}}}
        results = generate_typeddicts_for_api(spec, {"NonExistent"})
        assert results == {}

    def test_skips_non_object_schemas(self):
        """Non-object schemas (e.g., enums) are skipped."""
        from codegen.typeddicts import generate_typeddicts_for_api

        spec = {
            "components": {
                "schemas": {
                    "StatusEnum": {
                        "type": "string",
                        "enum": ["active", "inactive"],
                    }
                }
            }
        }
        results = generate_typeddicts_for_api(spec, {"StatusEnum"})
        assert results == {}
