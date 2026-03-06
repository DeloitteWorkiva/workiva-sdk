"""Polling support for long-running operations (HTTP 202).

Usage::

    response = client.files.copy_file(file_id="abc", destination_container="folder-123")
    operation = client.wait(response).result(timeout=300)
    print(operation.status)       # "completed"
    print(operation.resource_url)  # link to the result
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
from workiva.models.platform import Operation

if TYPE_CHECKING:
    from workiva.client import Workiva

_OPERATION_ID_RE = re.compile(r"/operations/([^/\s]+)")

_TERMINAL_STATUSES = frozenset({"completed", "cancelled", "failed"})

_MAX_RETRY_AFTER = 60.0

_MIN_RETRY_AFTER = 1.0  # Prevent tight polling loops


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
    """Parse ``retry-after`` header, capped to ``_MAX_RETRY_AFTER``.

    Supports both numeric seconds and HTTP-date formats.
    """
    value = headers.get("retry-after")
    if value is None:
        return default
    if isinstance(value, list):
        value = value[0]

    # Try numeric seconds first
    try:
        seconds = float(value)
        return min(max(seconds, _MIN_RETRY_AFTER), _MAX_RETRY_AFTER)
    except (TypeError, ValueError):
        pass

    # Try HTTP-date format
    try:
        from datetime import datetime
        from email.utils import parsedate_to_datetime

        retry_date = parsedate_to_datetime(str(value))
        delta = (retry_date - datetime.now(retry_date.tzinfo)).total_seconds()
        return min(max(delta, _MIN_RETRY_AFTER), _MAX_RETRY_AFTER)
    except (ValueError, TypeError):
        pass

    return default


def _poll_until_done(
    client: Any,
    response: Any,
    timeout: float = 300,
) -> Operation:
    """Poll a 202 response until the operation completes (sync).

    Standalone function that works with ``BaseClient`` directly — used by
    generated operations when ``wait=True``.

    Args:
        client: A ``BaseClient`` instance.
        response: The raw ``httpx.Response`` from the 202 request.
        timeout: Maximum seconds to wait for completion.

    Returns:
        The completed ``Operation``.

    Raises:
        OperationFailed: If the operation fails.
        OperationCancelled: If the operation is cancelled.
        OperationTimeout: If the timeout is exceeded.
    """
    headers = dict(response.headers)
    operation_id = _extract_operation_id(headers)
    retry_after = _get_retry_after(headers)
    deadline = time.monotonic() + timeout

    while True:
        poll_response = client.request(
            "GET",
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": operation_id},
        )
        operation = Operation.model_validate(poll_response.json())
        retry_after = _get_retry_after(dict(poll_response.headers), retry_after)

        if operation.status == "completed":
            return operation
        if operation.status == "failed":
            raise OperationFailed(operation)
        if operation.status == "cancelled":
            raise OperationCancelled(operation)

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise OperationTimeout(operation_id, timeout, operation.status)
        time.sleep(min(retry_after, remaining))


async def _poll_until_done_async(
    client: Any,
    response: Any,
    timeout: float = 300,
) -> Operation:
    """Poll a 202 response until the operation completes (async).

    Standalone function that works with ``BaseClient`` directly — used by
    generated operations when ``wait=True``.

    Args:
        client: A ``BaseClient`` instance.
        response: The raw ``httpx.Response`` from the 202 request.
        timeout: Maximum seconds to wait for completion.

    Returns:
        The completed ``Operation``.

    Raises:
        OperationFailed: If the operation fails.
        OperationCancelled: If the operation is cancelled.
        OperationTimeout: If the timeout is exceeded.
    """
    headers = dict(response.headers)
    operation_id = _extract_operation_id(headers)
    retry_after = _get_retry_after(headers)
    deadline = time.monotonic() + timeout

    while True:
        poll_response = await client.request_async(
            "GET",
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": operation_id},
        )
        operation = Operation.model_validate(poll_response.json())
        retry_after = _get_retry_after(dict(poll_response.headers), retry_after)

        if operation.status == "completed":
            return operation
        if operation.status == "failed":
            raise OperationFailed(operation)
        if operation.status == "cancelled":
            raise OperationCancelled(operation)

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise OperationTimeout(operation_id, timeout, operation.status)
        await asyncio.sleep(min(retry_after, remaining))


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
        self._last_operation: Optional[Operation] = None

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
    def last_operation(self) -> Optional[Operation]:
        """The most recent operation snapshot, or ``None`` if never polled."""
        return self._last_operation

    # -- Helpers -------------------------------------------------------------

    def done(self) -> bool:
        """Whether the operation has reached a terminal status (no API call)."""
        if self._last_operation is None:
            return False
        return self._last_operation.status in _TERMINAL_STATUSES

    def _check_terminal(self, operation: Operation) -> None:
        """Raise if the operation reached a terminal failure/cancelled state."""
        if operation.status == "failed":
            raise OperationFailed(operation)
        if operation.status == "cancelled":
            raise OperationCancelled(operation)

    # -- Sync ----------------------------------------------------------------

    def poll(self) -> Operation:
        """Execute a single poll request (sync).

        Updates internal state and returns the typed :class:`Operation`.
        Raises :class:`OperationFailed` or :class:`OperationCancelled` on
        terminal failure states.
        """
        response = self._client._base_client.request(
            "GET",
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": self._operation_id},
        )
        operation = Operation.model_validate(response.json())
        self._last_operation = operation
        self._retry_after = _get_retry_after(
            dict(response.headers), self._retry_after
        )
        self._check_terminal(operation)
        return operation

    def result(self, timeout: float = 300) -> Operation:
        """Poll until terminal state or timeout (sync).

        Returns the completed :class:`Operation` on success.
        Raises :class:`OperationTimeout` if ``timeout`` seconds elapse.
        Raises :class:`OperationFailed` / :class:`OperationCancelled` on failure.
        """
        deadline = time.monotonic() + timeout
        while True:
            operation = self.poll()
            if operation.status == "completed":
                return operation
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise OperationTimeout(
                    self._operation_id,
                    timeout,
                    operation.status,
                )
            time.sleep(min(self._retry_after, remaining))

    # -- Async ---------------------------------------------------------------

    async def poll_async(self) -> Operation:
        """Execute a single poll request (async).

        Updates internal state and returns the typed :class:`Operation`.
        Raises :class:`OperationFailed` or :class:`OperationCancelled` on
        terminal failure states.
        """
        response = await self._client._base_client.request_async(
            "GET",
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": self._operation_id},
        )
        operation = Operation.model_validate(response.json())
        self._last_operation = operation
        self._retry_after = _get_retry_after(
            dict(response.headers), self._retry_after
        )
        self._check_terminal(operation)
        return operation

    async def result_async(self, timeout: float = 300) -> Operation:
        """Poll until terminal state or timeout (async).

        Returns the completed :class:`Operation` on success.
        Raises :class:`OperationTimeout` if ``timeout`` seconds elapse.
        Raises :class:`OperationFailed` / :class:`OperationCancelled` on failure.
        """
        deadline = time.monotonic() + timeout
        while True:
            operation = await self.poll_async()
            if operation.status == "completed":
                return operation
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise OperationTimeout(
                    self._operation_id,
                    timeout,
                    operation.status,
                )
            await asyncio.sleep(min(self._retry_after, remaining))
