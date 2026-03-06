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
        # snake_case keys in nested dicts get converted to camelCase
        assert result["options"]["shallowCopy"] is True
        assert result["options"]["includeComments"] is False

    def test_pydantic_model_and_dict_produce_same_keys(self):
        """A Pydantic model and equivalent dict must serialize compatibly."""
        from workiva.models.platform import FileCopyOptions
        from workiva._client import _deep_serialize

        # Pydantic model
        model = FileCopyOptions(shallow_copy=True)
        model_json = model.model_dump(by_alias=True, exclude_none=True)

        # Equivalent dict (using snake_case, which _deep_serialize converts)
        dict_input = {"shallow_copy": True}
        dict_json = _deep_serialize(dict_input)

        assert model_json["shallowCopy"] == dict_json["shallowCopy"]

    def test_typeddict_type_checking(self):
        """TypedDict provides correct key information."""
        from workiva.models.platform_types import FileCopyOptionsParam

        opts: FileCopyOptionsParam = {
            "shallow_copy": True,
            "include_comments": False,
        }
        assert opts["shallow_copy"] is True

    def test_list_of_dicts_serialized(self):
        """List of dicts should also get camelCase conversion."""
        from workiva._client import _deep_serialize

        data = [
            {"principal_type": "user", "permission": "read"},
            {"principal_type": "group", "permission": "write"},
        ]
        result = _deep_serialize(data)
        assert result[0]["principalType"] == "user"
        assert result[1]["principalType"] == "group"

    def test_nested_body_structure(self):
        """Simulate full body dict as operations build it."""
        from workiva._client import _deep_serialize

        # This is what happens inside a generated operation:
        # _body["options"] = {"shallow_copy": True}
        _body = {}
        _body["options"] = {"shallow_copy": True, "include_comments": False}

        result = _deep_serialize(_body)
        # Top-level key "options" has no underscore, stays as-is
        assert "options" in result
        # Nested keys get converted
        assert result["options"]["shallowCopy"] is True
