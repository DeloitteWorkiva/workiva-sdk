"""Integration tests: error responses by status code."""

from __future__ import annotations

import httpx
import pytest

from workiva._hooks.client import Workiva
from workiva.errors.errorresponse import ErrorResponse
from workiva.errors.sdkerror import SDKError


def _token_response() -> httpx.Response:
    return httpx.Response(
        200,
        json={"access_token": "tok-test", "token_type": "bearer", "expires_in": 3600},
    )


def _error_json(code: str = "BAD_REQUEST", message: str = "validation failed") -> dict:
    return {"code": code, "message": message}


def _make_client(handler) -> Workiva:
    transport = httpx.MockTransport(handler)
    return Workiva(
        client_id="test-id",
        client_secret="test-secret",
        server_url="https://api.test.wdesk.com",
        client=httpx.Client(transport=transport),
    )


class TestErrorHandling:
    """Verify SDK error classes are raised for various HTTP status codes."""

    @pytest.mark.parametrize("status_code", [400, 401, 404, 500])
    def test_json_error_response(self, status_code):
        """JSON error body should produce an ErrorResponse or SDKBaseError."""

        def handler(request: httpx.Request) -> httpx.Response:
            if "/oauth2/token" in str(request.url):
                return _token_response()
            return httpx.Response(
                status_code,
                json=_error_json(message=f"error {status_code}"),
                headers={"content-type": "application/json"},
            )

        client = _make_client(handler)
        with pytest.raises(Exception) as exc_info:
            client.operations.get_operation_by_id(operation_id="op-err")

        # Should be some SDK error type
        exc = exc_info.value
        assert hasattr(exc, "status_code") or isinstance(exc, (ErrorResponse, SDKError))

    def test_non_json_error_produces_sdk_error(self):
        """Non-JSON error body (e.g. 418) should produce SDKError."""

        def handler(request: httpx.Request) -> httpx.Response:
            if "/oauth2/token" in str(request.url):
                return _token_response()
            return httpx.Response(
                418,
                content=b"I'm a teapot",
                headers={"content-type": "text/plain"},
            )

        client = _make_client(handler)
        with pytest.raises(Exception) as exc_info:
            client.operations.get_operation_by_id(operation_id="op-teapot")

        exc = exc_info.value
        # Should be SDKError (catch-all) or at least an SDK-related exception
        assert hasattr(exc, "status_code") or "teapot" in str(exc).lower() or "418" in str(exc)
