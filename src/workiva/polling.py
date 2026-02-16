"""Polling support for long-running operations (HTTP 202).

Usage::

    response = client.files.copy_file(file_id="abc", file_copy=params)
    operation = client.wait(response).result(timeout=300)
"""

from __future__ import annotations

import asyncio
import re
import time
from typing import TYPE_CHECKING, Any, Optional

from workiva._constants import _API
from workiva.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
)

if TYPE_CHECKING:
    from workiva.client import Workiva

_OPERATION_ID_RE = re.compile(r"/operations/([a-zA-Z0-9\-]+)")

_TERMINAL_STATUSES = frozenset({"completed", "cancelled", "failed"})

_MAX_RETRY_AFTER = 60.0


def _extract_operation_id(headers: dict[str, Any]) -> str:
    """Extract the operation ID from the ``location`` response header."""
    location = headers.get("location")
    if location is None:
        raise ValueError(
            "Response has no 'location' header — cannot extract operation ID"
        )
    if isinstance(location, list):
        location = location[0]
    match = _OPERATION_ID_RE.search(location)
    if match is None:
        raise ValueError(
            f"Could not extract operation ID from location header: {location}"
        )
    return match.group(1)


def _get_retry_after(headers: dict[str, Any], default: float = 2.0) -> float:
    """Parse ``retry-after`` header, capped to ``_MAX_RETRY_AFTER``."""
    value = headers.get("retry-after")
    if value is None:
        return default
    if isinstance(value, list):
        value = value[0]
    try:
        seconds = float(value)
    except (TypeError, ValueError):
        return default
    return min(max(seconds, 0), _MAX_RETRY_AFTER)


class OperationPoller:
    """Polls a long-running Workiva operation until it reaches a terminal state.

    Created via :meth:`Workiva.wait` — not intended for direct instantiation.
    """

    def __init__(
        self,
        client: Workiva,
        operation_id: str,
        initial_retry_after: float = 2.0,
        response_body: Any = None,
    ) -> None:
        self._client = client
        self._operation_id = operation_id
        self._retry_after = initial_retry_after
        self._response_body = response_body
        self._last_operation: Optional[dict[str, Any]] = None

    # -- Properties ----------------------------------------------------------

    @property
    def operation_id(self) -> str:
        """The ID of the operation being polled."""
        return self._operation_id

    @property
    def response_body(self) -> Any:
        """The original response body from the 202, or ``None``."""
        return self._response_body

    @property
    def last_operation(self) -> Optional[dict[str, Any]]:
        """The most recent operation snapshot, or ``None`` if never polled."""
        return self._last_operation

    # -- Helpers -------------------------------------------------------------

    def done(self) -> bool:
        """Whether the operation has reached a terminal status (no API call)."""
        if self._last_operation is None:
            return False
        return self._last_operation.get("status") in _TERMINAL_STATUSES

    def _check_terminal(self, operation: dict[str, Any]) -> None:
        """Raise if the operation reached a terminal failure/cancelled state."""
        status = operation.get("status")
        if status == "failed":
            raise OperationFailed(self._to_operation_model(operation))
        if status == "cancelled":
            raise OperationCancelled(self._to_operation_model(operation))

    @staticmethod
    def _to_operation_model(data: dict[str, Any]) -> Any:
        """Convert raw dict to a lightweight namespace for exception attributes.

        Uses SimpleNamespace instead of the Pydantic Operation model to avoid
        coupling the polling loop to model validation. The exceptions only
        access ``.id``, ``.details``, ``.code``, ``.target``, ``.message``.
        """
        from types import SimpleNamespace

        op = SimpleNamespace(**data)
        if hasattr(op, "details") and isinstance(op.details, list):
            op.details = [SimpleNamespace(**d) if isinstance(d, dict) else d for d in op.details]
        return op

    # -- Sync ----------------------------------------------------------------

    def poll(self) -> dict[str, Any]:
        """Execute a single poll request (sync).

        Updates internal state and returns the operation dict.
        Raises :class:`OperationFailed` or :class:`OperationCancelled` on
        terminal failure states.
        """
        response = self._client._base_client.request(
            "GET",
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": self._operation_id},
        )
        operation = response.json()
        self._last_operation = operation
        self._retry_after = _get_retry_after(
            dict(response.headers), self._retry_after
        )
        self._check_terminal(operation)
        return operation

    def result(self, timeout: float = 300) -> dict[str, Any]:
        """Poll until terminal state or timeout (sync).

        Returns the completed operation on success.
        Raises :class:`OperationTimeout` if ``timeout`` seconds elapse.
        Raises :class:`OperationFailed` / :class:`OperationCancelled` on failure.
        """
        deadline = time.monotonic() + timeout
        while True:
            operation = self.poll()
            if operation.get("status") == "completed":
                return operation
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise OperationTimeout(
                    self._operation_id,
                    timeout,
                    operation.get("status"),
                )
            time.sleep(min(self._retry_after, remaining))

    # -- Async ---------------------------------------------------------------

    async def poll_async(self) -> dict[str, Any]:
        """Execute a single poll request (async).

        Updates internal state and returns the operation dict.
        Raises :class:`OperationFailed` or :class:`OperationCancelled` on
        terminal failure states.
        """
        response = await self._client._base_client.request_async(
            "GET",
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": self._operation_id},
        )
        operation = response.json()
        self._last_operation = operation
        self._retry_after = _get_retry_after(
            dict(response.headers), self._retry_after
        )
        self._check_terminal(operation)
        return operation

    async def result_async(self, timeout: float = 300) -> dict[str, Any]:
        """Poll until terminal state or timeout (async).

        Returns the completed operation on success.
        Raises :class:`OperationTimeout` if ``timeout`` seconds elapse.
        Raises :class:`OperationFailed` / :class:`OperationCancelled` on failure.
        """
        deadline = time.monotonic() + timeout
        while True:
            operation = await self.poll_async()
            if operation.get("status") == "completed":
                return operation
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise OperationTimeout(
                    self._operation_id,
                    timeout,
                    operation.get("status"),
                )
            await asyncio.sleep(min(self._retry_after, remaining))
