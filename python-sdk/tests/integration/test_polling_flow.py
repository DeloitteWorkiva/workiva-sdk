"""Integration tests: poll-to-completion flow with mock HTTP transport."""

from __future__ import annotations

import json
from typing import Iterator

import httpx
import pytest

from workiva._hooks.client import Workiva
from workiva._hooks.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
)
from workiva.models.operation import OperationStatus


def _operation_json(
    status: str,
    op_id: str = "op-integ-1",
    details: list | None = None,
) -> dict:
    body = {"id": op_id, "status": status}
    if details is not None:
        body["details"] = details
    return body


def _token_response() -> httpx.Response:
    return httpx.Response(
        200,
        json={"access_token": "tok-test", "token_type": "bearer", "expires_in": 3600},
    )


class TestPollingFlow:
    """Full Workiva -> wait() -> result() flows using httpx.MockTransport."""

    def _make_client(self, handler) -> Workiva:
        transport = httpx.MockTransport(handler)
        mock_client = httpx.Client(transport=transport)
        return Workiva(
            client_id="test-id",
            client_secret="test-secret",
            server_url="https://api.test.wdesk.com",
            client=mock_client,
        )

    def test_full_success_flow(self):
        """202 -> wait().result() -> completed Operation."""
        call_count = 0

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            if "/oauth2/token" in str(request.url):
                return _token_response()
            if "/operations/" in str(request.url):
                call_count += 1
                status = "completed" if call_count >= 2 else "started"
                return httpx.Response(
                    200,
                    json=_operation_json(status),
                    headers={"retry-after": "0"},
                )
            return httpx.Response(404)

        client = self._make_client(handler)
        # Simulate a 202 response that .wait() would receive
        fake_response = type("R", (), {
            "headers": {
                "location": "/platform/v1/operations/op-integ-1",
                "retry-after": "0",
            },
            "result": None,
        })()

        poller = client.wait(fake_response)
        op = poller.result(timeout=5)
        assert op.status == OperationStatus.COMPLETED
        assert op.id == "op-integ-1"

    def test_failure_raises(self):
        def handler(request: httpx.Request) -> httpx.Response:
            if "/oauth2/token" in str(request.url):
                return _token_response()
            if "/operations/" in str(request.url):
                return httpx.Response(
                    200,
                    json=_operation_json(
                        "failed",
                        details=[{"code": "ERR", "message": "file corrupt"}],
                    ),
                    headers={"retry-after": "0"},
                )
            return httpx.Response(404)

        client = self._make_client(handler)
        fake_response = type("R", (), {
            "headers": {"location": "/operations/op-fail", "retry-after": "0"},
            "result": None,
        })()

        poller = client.wait(fake_response)
        with pytest.raises(OperationFailed) as exc_info:
            poller.result(timeout=5)
        assert "file corrupt" in str(exc_info.value)

    def test_cancelled_raises(self):
        def handler(request: httpx.Request) -> httpx.Response:
            if "/oauth2/token" in str(request.url):
                return _token_response()
            if "/operations/" in str(request.url):
                return httpx.Response(
                    200,
                    json=_operation_json("cancelled"),
                    headers={"retry-after": "0"},
                )
            return httpx.Response(404)

        client = self._make_client(handler)
        fake_response = type("R", (), {
            "headers": {"location": "/operations/op-cancel", "retry-after": "0"},
            "result": None,
        })()

        poller = client.wait(fake_response)
        with pytest.raises(OperationCancelled):
            poller.result(timeout=5)

    def test_timeout_raises(self):
        def handler(request: httpx.Request) -> httpx.Response:
            if "/oauth2/token" in str(request.url):
                return _token_response()
            if "/operations/" in str(request.url):
                return httpx.Response(
                    200,
                    json=_operation_json("started"),
                    headers={"retry-after": "0"},
                )
            return httpx.Response(404)

        client = self._make_client(handler)
        fake_response = type("R", (), {
            "headers": {"location": "/operations/op-slow", "retry-after": "0"},
            "result": None,
        })()

        poller = client.wait(fake_response)
        with pytest.raises(OperationTimeout):
            poller.result(timeout=0)

    @pytest.mark.asyncio
    async def test_async_success_flow(self):
        """Async poll-to-completion.

        Note: The SDK's OAuth hook always uses a sync HTTP client for token
        requests (even in async flows), so we must provide BOTH sync and async
        mock transports.
        """
        call_count = 0

        def sync_handler(request: httpx.Request) -> httpx.Response:
            """Sync handler for token requests."""
            if "/oauth2/token" in str(request.url):
                return _token_response()
            return httpx.Response(404)

        async def async_handler(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            if "/operations/" in str(request.url):
                call_count += 1
                status = "completed" if call_count >= 2 else "started"
                return httpx.Response(
                    200,
                    json=_operation_json(status),
                    headers={"retry-after": "0"},
                )
            return httpx.Response(404)

        sync_transport = httpx.MockTransport(sync_handler)
        async_transport = httpx.MockTransport(async_handler)
        client = Workiva(
            client_id="test-id",
            client_secret="test-secret",
            server_url="https://api.test.wdesk.com",
            client=httpx.Client(transport=sync_transport),
            async_client=httpx.AsyncClient(transport=async_transport),
        )
        fake_response = type("R", (), {
            "headers": {
                "location": "/operations/op-async",
                "retry-after": "0",
            },
            "result": None,
        })()

        poller = client.wait(fake_response)
        op = await poller.result_async(timeout=5)
        assert op.status == OperationStatus.COMPLETED
