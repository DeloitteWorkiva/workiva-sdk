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


class TestTypedDictFileGeneration:
    """Tests for the generated TypedDict files (Phase 3 output)."""

    def test_platform_types_file_exists(self):
        """TypedDict file should be generated for platform API."""
        types_file = Path("src/workiva/models/platform_types.py")
        assert types_file.exists(), "platform_types.py not generated"

    def test_platform_types_has_file_copy_options(self):
        """FileCopyOptionsParam should be importable."""
        from workiva.models.platform_types import FileCopyOptionsParam

        assert FileCopyOptionsParam is not None

    def test_typeddict_is_valid_typeddict(self):
        """Generated class must be a real TypedDict."""
        from workiva.models.platform_types import FileCopyOptionsParam

        assert hasattr(FileCopyOptionsParam, "__optional_keys__")

    def test_typeddict_accepts_snake_case_keys(self):
        """TypedDict should use snake_case keys."""
        from workiva.models.platform_types import FileCopyOptionsParam

        opts: FileCopyOptionsParam = {"shallow_copy": True}
        assert opts["shallow_copy"] is True

    def test_wdata_types_file_exists(self):
        """TypedDict file should be generated for wdata API."""
        types_file = Path("src/workiva/models/wdata_types.py")
        assert types_file.exists(), "wdata_types.py not generated"

    def test_resource_permission_has_required_fields(self):
        """ResourcePermissionParam should mark permission/principal as Required."""
        from workiva.models.platform_types import ResourcePermissionParam

        assert "permission" in ResourcePermissionParam.__required_keys__
        assert "principal" in ResourcePermissionParam.__required_keys__


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


class TestOperationAcceptsDicts:
    """Tests that generated operations accept TypedDict dicts in their signatures."""

    def test_copy_file_accepts_dict_for_options(self):
        """copy_file should accept FileCopyOptionsParam in its type hints."""
        import inspect

        from workiva._operations.files import Files

        sig = inspect.signature(Files.copy_file)
        options_param = sig.parameters["options"]
        ann = str(options_param.annotation)
        assert "FileCopyOptionsParam" in ann

    def test_permissions_mod_accepts_dict_for_list(self):
        """file_permissions_modification should accept TypedDict for list params."""
        import inspect

        from workiva._operations.files import Files

        sig = inspect.signature(Files.file_permissions_modification)
        param = sig.parameters["to_assign"]
        ann = str(param.annotation)
        assert "ResourcePermissionParam" in ann

    def test_restore_file_body_accepts_dict(self):
        """restore_file_by_id non-flat body should accept FileRestoreOptionsParam."""
        import inspect

        from workiva._operations.files import Files

        sig = inspect.signature(Files.restore_file_by_id)
        param = sig.parameters["body"]
        ann = str(param.annotation)
        assert "FileRestoreOptionsParam" in ann

    def test_async_variant_also_has_union(self):
        """Async methods should also accept TypedDict params."""
        import inspect

        from workiva._operations.files import Files

        sig = inspect.signature(Files.copy_file_async)
        options_param = sig.parameters["options"]
        ann = str(options_param.annotation)
        assert "FileCopyOptionsParam" in ann

    def test_namespace_without_body_has_no_typeddict_imports(self):
        """Namespaces with no body fields should not import TypedDict types."""
        import inspect

        source = inspect.getsource(
            __import__("workiva._operations.activities", fromlist=["Activities"])
        )
        assert "_types import" not in source


class TestTypedDictExports:
    """Tests for TypedDict re-exports from workiva.models package."""

    def test_importable_from_models_package(self):
        """TypedDict types should be importable from workiva.models."""
        from workiva.models import FileCopyOptionsParam

        assert FileCopyOptionsParam is not None

    def test_importable_from_top_level(self):
        """TypedDict types directly usable for typing."""
        from workiva.models.platform_types import FileCopyOptionsParam

        opts: FileCopyOptionsParam = {"shallow_copy": True}
        assert opts["shallow_copy"] is True


class TestSnakeToCamel:
    """Tests for the _snake_to_camel helper."""

    def test_converts_snake_to_camel(self):
        from workiva._client import _snake_to_camel

        assert _snake_to_camel("shallow_copy") == "shallowCopy"
        assert _snake_to_camel("include_comments") == "includeComments"

    def test_single_word(self):
        from workiva._client import _snake_to_camel

        assert _snake_to_camel("name") == "name"

    def test_multiple_underscores(self):
        from workiva._client import _snake_to_camel

        assert _snake_to_camel("a_b_c") == "aBC"

    def test_trailing_underscore(self):
        """Trailing underscore (keyword suffix) produces empty-string part."""
        from workiva._client import _snake_to_camel

        # "type_" -> parts = ["type", ""] -> "type" + "" = "type"
        assert _snake_to_camel("type_") == "type"


class TestDeepSerializeSnakeConversion:
    """Tests for snake_case → camelCase key conversion in _deep_serialize."""

    def test_dict_snake_keys_converted(self):
        from workiva._client import _deep_serialize

        result = _deep_serialize({"shallow_copy": True, "include_comments": False})
        assert result == {"shallowCopy": True, "includeComments": False}

    def test_dict_camel_keys_unchanged(self):
        from workiva._client import _deep_serialize

        result = _deep_serialize({"shallowCopy": True})
        assert result == {"shallowCopy": True}

    def test_nested_dict_converted(self):
        from workiva._client import _deep_serialize

        result = _deep_serialize({"outer_key": {"inner_key": "value"}})
        assert result == {"outerKey": {"innerKey": "value"}}

    def test_list_of_dicts_converted(self):
        from workiva._client import _deep_serialize

        result = _deep_serialize([{"snake_key": 1}, {"another_key": 2}])
        assert result == [{"snakeKey": 1}, {"anotherKey": 2}]

    def test_mixed_keys(self):
        """Keys with underscores are converted; keys without are not."""
        from workiva._client import _deep_serialize

        result = _deep_serialize({"camelCase": 1, "snake_case": 2})
        assert result == {"camelCase": 1, "snakeCase": 2}

    def test_pydantic_model_still_works(self):
        """Pydantic models are still serialized via model_dump."""
        from pydantic import BaseModel as PydanticBaseModel

        from workiva._client import _deep_serialize

        class TestModel(PydanticBaseModel):
            my_field: str = "hello"

        result = _deep_serialize(TestModel())
        # model_dump(by_alias=True) — field name depends on alias config
        assert isinstance(result, dict)
        assert "hello" in result.values()
