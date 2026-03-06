"""Error hierarchy for the Workiva SDK.

Wraps httpx responses and provides structured error data with
status-code-specific exception classes.
"""

from __future__ import annotations

from typing import Any, Optional

import httpx


class WorkivaError(Exception):
    """Base exception for all Workiva SDK errors.

    Catch this to handle any error raised by the SDK,
    including both API errors and token acquisition failures.
    """


class WorkivaAPIError(WorkivaError):
    """Base exception for all Workiva API errors.

    Attributes:
        status_code: HTTP status code from the response.
        response: The raw httpx.Response (headers, body, etc.).
        body: Parsed JSON body if available, else raw text.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        response: httpx.Response,
        body: Any = None,
    ) -> None:
        self.status_code = status_code
        self.response = response
        self.body = body
        super().__init__(message)


class BadRequestError(WorkivaAPIError):
    """400 Bad Request."""


class AuthenticationError(WorkivaAPIError):
    """401 Unauthorized."""


class ForbiddenError(WorkivaAPIError):
    """403 Forbidden."""


class NotFoundError(WorkivaAPIError):
    """404 Not Found."""


class ConflictError(WorkivaAPIError):
    """409 Conflict."""


class RateLimitError(WorkivaAPIError):
    """429 Too Many Requests."""

    @property
    def retry_after(self) -> int:
        """Seconds to wait before retrying, from Retry-After header.

        Defaults to 60 if header is missing or unparseable.
        """
        value = self.response.headers.get("retry-after")
        if value is None:
            return 60
        try:
            return int(value)
        except (TypeError, ValueError):
            return 60


class ServerError(WorkivaAPIError):
    """5xx Server Error."""


# Status code → exception class mapping
_STATUS_MAP: dict[int, type[WorkivaAPIError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: ForbiddenError,
    404: NotFoundError,
    409: ConflictError,
    429: RateLimitError,
}


def _redact_response(response: httpx.Response) -> httpx.Response:
    """Return response with Authorization header redacted from the request.

    Creates a new request object to avoid mutating the original.
    """
    try:
        request = response.request
    except RuntimeError:
        return response
    if request and "authorization" in request.headers:
        headers = dict(request.headers)
        headers["authorization"] = "[REDACTED]"
        redacted_request = httpx.Request(
            method=request.method,
            url=request.url,
            headers=headers,
        )
        response._request = redacted_request
    return response


def raise_for_status(response: httpx.Response) -> None:
    """Raise the appropriate WorkivaAPIError for non-2xx responses.

    Attempts to parse JSON error body. Falls back to raw text.
    """
    if 200 <= response.status_code < 300:
        return

    status = response.status_code

    # Try to parse JSON body
    body: Any = None
    try:
        body = response.json()
    except ValueError:
        body = response.text[:2000] if response.text else None

    # Build a human-readable message with request context
    request_context = ""
    try:
        req = response.request
        path = req.url.raw_path.decode("ascii", errors="replace")
        request_context = f"{req.method} {path}"
    except (RuntimeError, AttributeError):
        pass
    message = _build_message(status, body, request_context)

    # Pick the right exception class
    if status in _STATUS_MAP:
        exc_cls = _STATUS_MAP[status]
    elif 500 <= status < 600:
        exc_cls = ServerError
    else:
        exc_cls = WorkivaAPIError

    raise exc_cls(
        message,
        status_code=status,
        response=_redact_response(response),
        body=body,
    )


def _build_message(status: int, body: Any, request_context: str = "") -> str:
    """Build a human-readable error message from the response body."""
    prefix = f"[{status} {request_context}]" if request_context else f"[{status}]"
    if isinstance(body, dict):
        # Workiva error format: {"error": {"code": "...", "message": "..."}}
        error = body.get("error", {})
        if isinstance(error, dict):
            code = error.get("code", "")
            msg = error.get("message", "")
            if msg:
                return f"{prefix} {code}: {msg}" if code else f"{prefix} {msg}"

        # Alternative format: {"message": "..."}
        msg = body.get("message", "")
        if msg:
            return f"{prefix} {msg}"

    return f"{prefix} API request failed"
