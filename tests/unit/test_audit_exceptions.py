"""Audit tests for exception hierarchy, error messages, config validation, and safety fixes."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest

from workiva._errors import WorkivaError, _redact_response, raise_for_status
from workiva._pagination import paginate_all
from workiva.client import Workiva
from workiva.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
    PaginationError,
)


# ---------------------------------------------------------------------------
# C1 — Exception hierarchy: all polling exceptions are catchable via WorkivaError
# ---------------------------------------------------------------------------


class TestExceptionHierarchy:
    def test_operation_failed_caught_by_workiva_error(self):
        op = MagicMock()
        op.id = "op-1"
        op.details = None
        with pytest.raises(WorkivaError):
            raise OperationFailed(op)

    def test_operation_cancelled_caught_by_workiva_error(self):
        op = MagicMock()
        op.id = "op-2"
        with pytest.raises(WorkivaError):
            raise OperationCancelled(op)

    def test_operation_timeout_caught_by_workiva_error(self):
        with pytest.raises(WorkivaError):
            raise OperationTimeout("op-3", timeout=60.0, last_status="running")

    def test_pagination_error_caught_by_workiva_error(self):
        with pytest.raises(WorkivaError):
            raise PaginationError("too many pages")


# ---------------------------------------------------------------------------
# M8 — paginate_all raises PaginationError (not RuntimeError) on max_pages
# ---------------------------------------------------------------------------


class TestPaginationErrorOnMaxPages:
    def test_paginate_all_raises_pagination_error(self):
        def fake_fetch(cursor):
            return httpx.Response(
                200,
                json={"data": [{"id": 1}], "cursor": "next-page"},
                request=httpx.Request("GET", "https://api.example.com/items"),
            )

        def always_has_next(body):
            return body.get("cursor")

        with pytest.raises(PaginationError, match="exceeded 1 pages"):
            paginate_all(
                fetch=fake_fetch,
                extract_cursor=always_has_next,
                items_path="data",
                max_pages=1,
            )


# ---------------------------------------------------------------------------
# H6 — Error messages include HTTP method and URL path
# ---------------------------------------------------------------------------


class TestErrorMessageIncludesUrl:
    def test_raise_for_status_includes_method_and_path(self):
        request = httpx.Request("GET", "https://api.example.com/files/abc123")
        response = httpx.Response(
            404,
            json={"error": {"message": "Not found"}},
            request=request,
        )

        with pytest.raises(WorkivaError) as exc_info:
            raise_for_status(response)

        message = str(exc_info.value)
        assert "GET" in message
        assert "/files/abc123" in message


# ---------------------------------------------------------------------------
# H1 — _redact_response does NOT mutate the original request
# ---------------------------------------------------------------------------


class TestRedactResponseNoMutation:
    def test_original_request_preserves_authorization(self):
        request = httpx.Request(
            "GET",
            "https://api.example.com/test",
            headers={"Authorization": "Bearer real-token-123"},
        )
        response = httpx.Response(200, request=request)

        original_auth = request.headers["authorization"]

        _redact_response(response)

        assert request.headers["authorization"] == original_auth

    def test_redacted_response_has_redacted_header(self):
        request = httpx.Request(
            "GET",
            "https://api.example.com/test",
            headers={"Authorization": "Bearer real-token-123"},
        )
        response = httpx.Response(200, request=request)

        redacted = _redact_response(response)

        assert redacted.request.headers["authorization"] == "[REDACTED]"


# ---------------------------------------------------------------------------
# M6 — Credential validation: empty client_id raises ValueError
# ---------------------------------------------------------------------------


class TestCredentialValidation:
    def test_empty_client_id_raises_value_error(self):
        with pytest.raises(ValueError, match="client_id"):
            Workiva(client_id="", client_secret="secret")

    def test_empty_client_secret_raises_value_error(self):
        with pytest.raises(ValueError, match="client_secret"):
            Workiva(client_id="valid-id", client_secret="")


# ---------------------------------------------------------------------------
# M9 — wait() type safety: non-Response raises TypeError
# ---------------------------------------------------------------------------


class TestWaitTypeSafety:
    def test_wait_with_pydantic_model_raises_type_error(self):
        with patch.object(Workiva, "__init__", lambda self, **kw: None):
            w = Workiva.__new__(Workiva)

        fake_model = MagicMock()
        fake_model.__class__.__name__ = "Operation"

        with pytest.raises(TypeError, match="wait.*expects.*httpx.Response"):
            w.wait(fake_model)

    def test_wait_with_string_raises_type_error(self):
        with patch.object(Workiva, "__init__", lambda self, **kw: None):
            w = Workiva.__new__(Workiva)

        with pytest.raises(TypeError, match="got str"):
            w.wait("not-a-response")
