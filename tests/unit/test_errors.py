"""Tests for workiva._errors — raise_for_status and _build_message."""

from __future__ import annotations

import pytest

import httpx

from workiva._errors import (
    AuthenticationError,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    ServerError,
    WorkivaAPIError,
    _build_message,
    raise_for_status,
)


def _json_response(status_code: int, payload: dict) -> httpx.Response:
    """Build an httpx.Response with a JSON body."""
    return httpx.Response(status_code, json=payload)


def _text_response(status_code: int, body: str) -> httpx.Response:
    """Build an httpx.Response with a plain-text body."""
    return httpx.Response(status_code, text=body)


# ---------------------------------------------------------------------------
# raise_for_status — success (2xx)
# ---------------------------------------------------------------------------


class TestRaiseForStatusSuccess:
    @pytest.mark.parametrize("code", [200, 201, 204, 299])
    def test_returns_none_for_2xx(self, code: int):
        resp = httpx.Response(code)
        assert raise_for_status(resp) is None


# ---------------------------------------------------------------------------
# raise_for_status — mapped client errors
# ---------------------------------------------------------------------------


class TestRaiseForStatusMappedErrors:
    def test_400_raises_bad_request(self):
        resp = _json_response(400, {"message": "invalid field"})
        with pytest.raises(BadRequestError):
            raise_for_status(resp)

    def test_401_raises_authentication_error(self):
        resp = _json_response(401, {"message": "token expired"})
        with pytest.raises(AuthenticationError):
            raise_for_status(resp)

    def test_403_raises_forbidden(self):
        resp = _json_response(403, {"message": "not allowed"})
        with pytest.raises(ForbiddenError):
            raise_for_status(resp)

    def test_404_raises_not_found(self):
        resp = _json_response(404, {"message": "resource missing"})
        with pytest.raises(NotFoundError):
            raise_for_status(resp)

    def test_409_raises_conflict(self):
        resp = _json_response(409, {"message": "version conflict"})
        with pytest.raises(ConflictError):
            raise_for_status(resp)

    def test_429_raises_rate_limit(self):
        resp = _json_response(429, {"message": "slow down"})
        with pytest.raises(RateLimitError):
            raise_for_status(resp)


# ---------------------------------------------------------------------------
# raise_for_status — server errors (5xx)
# ---------------------------------------------------------------------------


class TestRaiseForStatusServerErrors:
    @pytest.mark.parametrize("code", [500, 502, 503])
    def test_5xx_raises_server_error(self, code: int):
        resp = _json_response(code, {"message": "internal"})
        with pytest.raises(ServerError):
            raise_for_status(resp)


# ---------------------------------------------------------------------------
# raise_for_status — unmapped codes
# ---------------------------------------------------------------------------


class TestRaiseForStatusUnmapped:
    def test_418_raises_base_workiva_api_error(self):
        resp = _json_response(418, {"message": "I'm a teapot"})
        with pytest.raises(WorkivaAPIError) as exc_info:
            raise_for_status(resp)
        # Must not be a more specific subclass
        assert type(exc_info.value) is WorkivaAPIError


# ---------------------------------------------------------------------------
# Exception attributes
# ---------------------------------------------------------------------------


class TestExceptionAttributes:
    def test_status_code_on_exception(self):
        resp = _json_response(404, {"message": "gone"})
        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(resp)
        assert exc_info.value.status_code == 404

    def test_response_on_exception(self):
        resp = _json_response(400, {"message": "bad"})
        with pytest.raises(BadRequestError) as exc_info:
            raise_for_status(resp)
        assert exc_info.value.response is resp

    def test_body_is_parsed_json(self):
        payload = {"error": {"code": "ERR_01", "message": "boom"}}
        resp = _json_response(500, payload)
        with pytest.raises(ServerError) as exc_info:
            raise_for_status(resp)
        assert exc_info.value.body == payload

    def test_body_falls_back_to_text(self):
        resp = _text_response(502, "gateway timeout")
        with pytest.raises(ServerError) as exc_info:
            raise_for_status(resp)
        assert exc_info.value.body == "gateway timeout"


# ---------------------------------------------------------------------------
# _build_message — Workiva nested error format
# ---------------------------------------------------------------------------


class TestBuildMessageWorkivaFormat:
    def test_full_error_object(self):
        body = {"error": {"code": "VALIDATION", "message": "field X is required"}}
        assert _build_message(400, body) == "[400] VALIDATION: field X is required"

    def test_error_object_without_code(self):
        body = {"error": {"message": "something broke"}}
        assert _build_message(500, body) == "[500] something broke"

    def test_error_object_without_message_falls_through(self):
        body = {"error": {"code": "UNKNOWN"}}
        # No `message` in error dict and no top-level `message` either
        assert _build_message(500, body) == "[500] API request failed"


# ---------------------------------------------------------------------------
# _build_message — simple {"message": "..."} format
# ---------------------------------------------------------------------------


class TestBuildMessageSimpleFormat:
    def test_top_level_message(self):
        body = {"message": "rate limit exceeded"}
        assert _build_message(429, body) == "[429] rate limit exceeded"


# ---------------------------------------------------------------------------
# _build_message — fallback
# ---------------------------------------------------------------------------


class TestBuildMessageFallback:
    def test_non_dict_body(self):
        assert _build_message(502, "not json at all") == "[502] API request failed"

    def test_none_body(self):
        assert _build_message(503, None) == "[503] API request failed"

    def test_empty_dict(self):
        assert _build_message(400, {}) == "[400] API request failed"
