"""Tests for typed responses in generated operations.

Verifies that generated operation methods correctly parse JSON responses
into Pydantic models (Code path B) and return raw httpx.Response for
non-JSON / 202 operations (Code path C).
"""

from __future__ import annotations

from unittest.mock import MagicMock

import httpx
import pytest

from workiva._constants import _API
from workiva.models.platform import File, FilesListResult


def _mock_client(json_body: dict, status: int = 200) -> MagicMock:
    """Create a MagicMock BaseClient that returns a canned JSON response."""
    response = httpx.Response(status, json=json_body)
    client = MagicMock()
    client.request.return_value = response
    return client


class TestTypedJsonResponse:
    """Code path B: JSON response → Pydantic model."""

    def test_create_file_returns_model(self):
        """create_file() should return a File model, not httpx.Response."""
        from workiva._operations.files import Files

        body = {"name": "test.xlsx", "kind": "Spreadsheet", "id": "abc123"}
        client = _mock_client(body)
        ns = Files(client)

        result = ns.create_file(body=body)

        assert isinstance(result, File)
        assert result.name == "test.xlsx"
        assert result.kind == "Spreadsheet"

    def test_get_file_by_id_returns_model(self):
        """get_file_by_id() should return a File model."""
        from workiva._operations.files import Files

        body = {"name": "report.docx", "kind": "Document", "id": "xyz789"}
        client = _mock_client(body)
        ns = Files(client)

        result = ns.get_file_by_id(file_id="xyz789")

        assert isinstance(result, File)
        assert result.name == "report.docx"


class TestRawResponse:
    """Code path C: 202 / binary → raw httpx.Response."""

    def test_copy_file_returns_httpx_response(self):
        """copy_file() (202) should return raw httpx.Response for polling."""
        from workiva._operations.files import Files

        response = httpx.Response(
            202,
            headers={"Location": "/operations/op-123"},
        )
        client = MagicMock()
        client.request.return_value = response
        ns = Files(client)

        result = ns.copy_file(file_id="abc", body={"destFolderId": "f1"})

        assert isinstance(result, httpx.Response)
        assert result.status_code == 202


class TestPydanticBodySerialization:
    """Verify Pydantic model instances serialize correctly as request body."""

    def test_pydantic_model_serialized_with_aliases(self):
        """When body is a Pydantic model, it should be serialized with by_alias=True."""
        from workiva._client import BaseClient
        from workiva._config import RetryConfig, SDKConfig
        from workiva._constants import Region

        config = SDKConfig(region=Region.EU, retry=RetryConfig())
        bc = BaseClient(client_id="id", client_secret="secret", config=config)

        file_model = File(name="test.xlsx", kind="Spreadsheet")
        _, kwargs = bc._prepare_request(
            _API.PLATFORM, "/files", json_body=file_model
        )

        # Should be a plain dict (serialized), not a Pydantic instance
        assert isinstance(kwargs["json"], dict)
        # Aliases should be used
        assert "name" in kwargs["json"]
