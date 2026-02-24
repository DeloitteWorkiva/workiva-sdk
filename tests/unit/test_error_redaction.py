"""Tests for Authorization header redaction in error responses."""

from __future__ import annotations

import httpx
import pytest

from workiva._errors import (
    BadRequestError,
    NotFoundError,
    ServerError,
    WorkivaAPIError,
    raise_for_status,
)


class TestAuthorizationRedaction:
    def test_authorization_header_redacted(self):
        """Authorization header should be [REDACTED] in raised exceptions."""
        request = httpx.Request(
            "GET",
            "https://api.example.com/test",
            headers={"Authorization": "Bearer secret-token-123"},
        )
        response = httpx.Response(
            404,
            request=request,
            json={"error": "not found"},
        )

        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(response)

        exc = exc_info.value
        assert exc.response.request.headers["authorization"] == "[REDACTED]"
        assert "secret-token-123" not in str(exc.response.request.headers)

    def test_no_authorization_header_unchanged(self):
        """Responses without Authorization header should pass through."""
        request = httpx.Request(
            "GET",
            "https://api.example.com/test",
            headers={"Content-Type": "application/json"},
        )
        response = httpx.Response(
            500,
            request=request,
            json={"error": "internal"},
        )

        with pytest.raises(ServerError) as exc_info:
            raise_for_status(response)

        exc = exc_info.value
        assert "authorization" not in exc.response.request.headers

    def test_response_body_still_accessible(self):
        """Response body should still be accessible after redaction."""
        request = httpx.Request(
            "GET",
            "https://api.example.com/test",
            headers={"Authorization": "Bearer token"},
        )
        response = httpx.Response(
            400,
            request=request,
            json={"error": "bad request"},
        )

        with pytest.raises(BadRequestError) as exc_info:
            raise_for_status(response)

        exc = exc_info.value
        assert exc.body is not None

    def test_2xx_no_exception(self):
        """Successful responses should not raise."""
        request = httpx.Request(
            "GET",
            "https://api.example.com/test",
            headers={"Authorization": "Bearer token"},
        )
        response = httpx.Response(200, request=request)
        # Should not raise
        raise_for_status(response)
