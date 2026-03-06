"""Tests for standalone _poll_until_done / _poll_until_done_async functions.

These are used by generated operations when ``wait=True``.
"""

from __future__ import annotations

from unittest.mock import MagicMock, AsyncMock

import httpx
import pytest

from workiva.exceptions import OperationCancelled, OperationFailed, OperationTimeout
from workiva.polling import _poll_until_done, _poll_until_done_async


def _make_202_response(operation_id: str = "op-abc", retry_after: str = "0") -> httpx.Response:
    """Create a fake 202 response with Location and Retry-After headers."""
    return httpx.Response(
        202,
        headers={
            "Location": f"https://api.app.wdesk.com/platform/v1/operations/{operation_id}",
            "Retry-After": retry_after,
        },
    )


def _make_poll_response(status: str, retry_after: str = "0") -> httpx.Response:
    # Valid Operation statuses: acknowledged, queued, started, completed, cancelled, failed
    return httpx.Response(
        200,
        json={"id": "op-abc", "status": status},
        headers={"Retry-After": retry_after},
    )


class TestPollUntilDoneSync:
    """Sync standalone polling function."""

    def test_completes_on_first_poll(self):
        client = MagicMock()
        client.request.return_value = _make_poll_response("completed")
        response = _make_202_response()

        result = _poll_until_done(client, response, timeout=10)

        assert result.status == "completed"
        assert client.request.call_count == 1

    def test_polls_until_completed(self, monkeypatch):
        monkeypatch.setattr("workiva.polling.time.sleep", lambda _: None)
        client = MagicMock()
        client.request.side_effect = [
            _make_poll_response("started"),
            _make_poll_response("started"),
            _make_poll_response("completed"),
        ]
        response = _make_202_response()

        result = _poll_until_done(client, response, timeout=300)

        assert result.status == "completed"
        assert client.request.call_count == 3

    def test_raises_on_failed(self, monkeypatch):
        monkeypatch.setattr("workiva.polling.time.sleep", lambda _: None)
        client = MagicMock()
        client.request.return_value = _make_poll_response("failed")
        response = _make_202_response()

        with pytest.raises(OperationFailed):
            _poll_until_done(client, response, timeout=10)

    def test_raises_on_cancelled(self, monkeypatch):
        monkeypatch.setattr("workiva.polling.time.sleep", lambda _: None)
        client = MagicMock()
        client.request.return_value = _make_poll_response("cancelled")
        response = _make_202_response()

        with pytest.raises(OperationCancelled):
            _poll_until_done(client, response, timeout=10)

    def test_raises_on_timeout(self, monkeypatch):
        monkeypatch.setattr("workiva.polling.time.sleep", lambda _: None)
        client = MagicMock()
        client.request.return_value = _make_poll_response("started", retry_after="0")
        response = _make_202_response()

        with pytest.raises(OperationTimeout):
            _poll_until_done(client, response, timeout=0)

    def test_extracts_operation_id_from_location(self):
        client = MagicMock()
        client.request.return_value = _make_poll_response("completed")
        response = _make_202_response(operation_id="my-op-id")

        _poll_until_done(client, response, timeout=10)

        call_kwargs = client.request.call_args
        assert call_kwargs[1]["path_params"]["operationId"] == "my-op-id"


class TestPollUntilDoneAsync:
    """Async standalone polling function."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_completes_on_first_poll(self):
        client = MagicMock()
        client.request_async = AsyncMock(return_value=_make_poll_response("completed"))
        response = _make_202_response()

        result = await _poll_until_done_async(client, response, timeout=10)

        assert result.status == "completed"

    @pytest.mark.asyncio(loop_scope="function")
    async def test_raises_on_failed(self):
        client = MagicMock()
        client.request_async = AsyncMock(return_value=_make_poll_response("failed"))
        response = _make_202_response()

        with pytest.raises(OperationFailed):
            await _poll_until_done_async(client, response, timeout=10)

    @pytest.mark.asyncio(loop_scope="function")
    async def test_raises_on_timeout(self):
        client = MagicMock()
        client.request_async = AsyncMock(
            return_value=_make_poll_response("started", retry_after="0")
        )
        response = _make_202_response()

        with pytest.raises(OperationTimeout):
            await _poll_until_done_async(client, response, timeout=0)
