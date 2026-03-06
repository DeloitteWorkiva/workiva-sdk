"""Tests for the ``wait=True`` parameter on generated 202 operations.

Verifies that long-running operations can block until completion
and that the default (wait=False) preserves existing behavior.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest

from workiva.models.platform import Operation


def _mock_client_202(operation_id: str = "op-123") -> MagicMock:
    """Create a mock BaseClient that returns a 202 response."""
    response = httpx.Response(
        202,
        headers={
            "Location": f"/operations/{operation_id}",
            "Retry-After": "0",
        },
    )
    client = MagicMock()
    client.request.return_value = response
    return client


class TestWaitFalseDefault:
    """wait=False (default) returns httpx.Response as before."""

    def test_copy_file_returns_response_by_default(self):
        from workiva._operations.files import Files

        client = _mock_client_202()
        ns = Files(client)

        result = ns.copy_file(file_id="abc", destination_container="folder-1")

        assert isinstance(result, httpx.Response)
        assert result.status_code == 202

    def test_trash_file_returns_response_by_default(self):
        from workiva._operations.files import Files

        client = _mock_client_202()
        ns = Files(client)

        result = ns.trash_file_by_id(file_id="abc")

        assert isinstance(result, httpx.Response)
        assert result.status_code == 202


class TestWaitTrue:
    """wait=True polls and returns Operation."""

    @patch("workiva._operations.files._poll_until_done")
    def test_copy_file_wait_calls_poll(self, mock_poll):
        from workiva._operations.files import Files

        completed_op = Operation.model_validate({"id": "op-123", "status": "completed"})
        mock_poll.return_value = completed_op

        client = _mock_client_202()
        ns = Files(client)

        result = ns.copy_file(
            file_id="abc", destination_container="folder-1", wait=True
        )

        assert isinstance(result, Operation)
        assert result.status == "completed"
        mock_poll.assert_called_once()

    @patch("workiva._operations.files._poll_until_done")
    def test_wait_timeout_forwarded(self, mock_poll):
        from workiva._operations.files import Files

        mock_poll.return_value = Operation.model_validate(
            {"id": "op-1", "status": "completed"}
        )

        client = _mock_client_202()
        ns = Files(client)

        ns.copy_file(
            file_id="abc",
            destination_container="f1",
            wait=True,
            wait_timeout=60,
        )

        _, kwargs = mock_poll.call_args
        assert kwargs["timeout"] == 60


class TestBodyDefaultEmpty:
    """Operations with empty body schemas send {} when body=None."""

    def test_trash_file_sends_empty_body_when_none(self):
        from workiva._operations.files import Files

        client = _mock_client_202()
        ns = Files(client)

        ns.trash_file_by_id(file_id="abc")

        _, kwargs = client.request.call_args
        assert kwargs["json_body"] == {}

    def test_trash_file_sends_model_when_provided(self):
        from workiva._operations.files import Files
        from workiva.models.platform import FileTrashOptions

        client = _mock_client_202()
        ns = Files(client)
        body = FileTrashOptions()

        ns.trash_file_by_id(file_id="abc", body=body)

        _, kwargs = client.request.call_args
        # When a model is provided, it should be passed as-is (not replaced with {})
        assert kwargs["json_body"] is body
