"""Polling support for long-running operations (HTTP 202).

This file lives in _hooks/ which Speakeasy preserves across regenerations.

Usage::

    response = client.files.copy_file(file_id="abc", file_copy=params)
    operation = client.wait(response).result(timeout=300)
"""

from __future__ import annotations

import asyncio
import re
import time
from typing import TYPE_CHECKING, Any, Optional

from workiva._hooks.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
)
from workiva.models.operation import Operation, OperationStatus

if TYPE_CHECKING:
    from workiva.sdk import SDK

_OPERATION_ID_RE = re.compile(r"/operations/([a-zA-Z0-9\-]+)")

_TERMINAL_STATUSES = frozenset(
    {OperationStatus.COMPLETED, OperationStatus.CANCELLED, OperationStatus.FAILED}
)

_MAX_RETRY_AFTER = 60.0


def _extract_operation_id(headers: dict[str, Any]) -> str:
    """Extract the operation ID from the ``location`` response header."""
    location = headers.get("location")
    if location is None:
        raise ValueError(
            "Response has no 'location' header — cannot extract operation ID"
        )
    # httpx lowercases header names; headers may be str or List[str]
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
        sdk: SDK,
        operation_id: str,
        initial_retry_after: float = 2.0,
        response_body: Any = None,
    ) -> None:
        self._sdk = sdk
        self._operation_id = operation_id
        self._retry_after = initial_retry_after
        self._response_body = response_body
        self._last_operation: Optional[Operation] = None

    # -- Properties ----------------------------------------------------------

    @property
    def operation_id(self) -> str:
        """The ID of the operation being polled."""
        return self._operation_id

    @property
    def response_body(self) -> Any:
        """The original response body from the 202 (e.g. an upload URL), or ``None``."""
        return self._response_body

    @property
    def last_operation(self) -> Optional[Operation]:
        """The most recent ``Operation`` snapshot, or ``None`` if never polled."""
        return self._last_operation

    # -- Helpers -------------------------------------------------------------

    def done(self) -> bool:
        """Whether the operation has reached a terminal status (no API call)."""
        if self._last_operation is None:
            return False
        return self._last_operation.status in _TERMINAL_STATUSES

    def _check_terminal(self, operation: Operation) -> None:
        """Raise if the operation reached a terminal failure/cancelled state."""
        if operation.status == OperationStatus.FAILED:
            raise OperationFailed(operation)
        if operation.status == OperationStatus.CANCELLED:
            raise OperationCancelled(operation)

    # -- Sync ----------------------------------------------------------------

    def poll(self) -> Operation:
        """Execute a single poll request (sync).

        Updates internal state and returns the ``Operation``.
        Raises :class:`OperationFailed` or :class:`OperationCancelled` on
        terminal failure states.
        """
        response = self._sdk.operations.get_operation_by_id(
            operation_id=self._operation_id
        )
        self._last_operation = response.result
        self._retry_after = _get_retry_after(response.headers, self._retry_after)
        self._check_terminal(response.result)
        return response.result

    def result(self, timeout: float = 300) -> Operation:
        """Poll until terminal state or timeout (sync).

        Returns the completed ``Operation`` on success.
        Raises :class:`OperationTimeout` if ``timeout`` seconds elapse.
        Raises :class:`OperationFailed` / :class:`OperationCancelled` on failure.
        """
        deadline = time.monotonic() + timeout
        while True:
            operation = self.poll()
            if operation.status == OperationStatus.COMPLETED:
                return operation
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise OperationTimeout(
                    self._operation_id,
                    timeout,
                    operation.status.value if operation.status else None,
                )
            time.sleep(min(self._retry_after, remaining))

    # -- Async ---------------------------------------------------------------

    async def poll_async(self) -> Operation:
        """Execute a single poll request (async).

        Updates internal state and returns the ``Operation``.
        Raises :class:`OperationFailed` or :class:`OperationCancelled` on
        terminal failure states.
        """
        response = await self._sdk.operations.get_operation_by_id_async(
            operation_id=self._operation_id
        )
        self._last_operation = response.result
        self._retry_after = _get_retry_after(response.headers, self._retry_after)
        self._check_terminal(response.result)
        return response.result

    async def result_async(self, timeout: float = 300) -> Operation:
        """Poll until terminal state or timeout (async).

        Returns the completed ``Operation`` on success.
        Raises :class:`OperationTimeout` if ``timeout`` seconds elapse.
        Raises :class:`OperationFailed` / :class:`OperationCancelled` on failure.
        """
        loop = asyncio.get_event_loop()
        deadline = loop.time() + timeout
        while True:
            operation = await self.poll_async()
            if operation.status == OperationStatus.COMPLETED:
                return operation
            remaining = deadline - loop.time()
            if remaining <= 0:
                raise OperationTimeout(
                    self._operation_id,
                    timeout,
                    operation.status.value if operation.status else None,
                )
            await asyncio.sleep(min(self._retry_after, remaining))
