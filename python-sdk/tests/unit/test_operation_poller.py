"""Tests for OperationPoller (sync + async)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from workiva._hooks.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
)
from workiva._hooks.polling import OperationPoller
from workiva.models.operation import Operation, OperationStatus
from workiva.models.getoperationbyidop import GetOperationByIDResponse


def _make_response(
    status: OperationStatus,
    op_id: str = "op-123",
    retry_after: str = "1",
) -> GetOperationByIDResponse:
    return GetOperationByIDResponse(
        headers={"retry-after": [retry_after]},
        result=Operation(id=op_id, status=status),
    )


class TestDone:
    def test_before_any_poll(self):
        poller = OperationPoller(sdk=MagicMock(), operation_id="x")
        assert poller.done() is False

    def test_after_non_terminal(self, mock_sdk, make_poll_response):
        mock_sdk.operations.get_operation_by_id.return_value = make_poll_response(
            status=OperationStatus.STARTED,
        )
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")
        poller.poll()
        assert poller.done() is False

    def test_after_completed(self, mock_sdk, make_poll_response):
        mock_sdk.operations.get_operation_by_id.return_value = make_poll_response(
            status=OperationStatus.COMPLETED,
        )
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")
        poller.poll()
        assert poller.done() is True


class TestPollSync:
    def test_updates_last_operation(self, mock_sdk, make_poll_response):
        resp = make_poll_response(status=OperationStatus.STARTED)
        mock_sdk.operations.get_operation_by_id.return_value = resp
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")

        result = poller.poll()
        assert result is resp.result
        assert poller.last_operation is resp.result

    def test_raises_on_failed(self, mock_sdk, make_poll_response):
        mock_sdk.operations.get_operation_by_id.return_value = make_poll_response(
            status=OperationStatus.FAILED,
        )
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")
        with pytest.raises(OperationFailed):
            poller.poll()

    def test_raises_on_cancelled(self, mock_sdk, make_poll_response):
        mock_sdk.operations.get_operation_by_id.return_value = make_poll_response(
            status=OperationStatus.CANCELLED,
        )
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")
        with pytest.raises(OperationCancelled):
            poller.poll()


class TestResultSync:
    def test_completes_first_poll(self, mock_sdk, make_poll_response):
        mock_sdk.operations.get_operation_by_id.return_value = make_poll_response(
            status=OperationStatus.COMPLETED,
        )
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")
        op = poller.result(timeout=10)
        assert op.status == OperationStatus.COMPLETED

    def test_completes_after_n_polls(self, mock_sdk, make_poll_response):
        started = make_poll_response(status=OperationStatus.STARTED, retry_after="0")
        completed = make_poll_response(status=OperationStatus.COMPLETED)
        mock_sdk.operations.get_operation_by_id.side_effect = [started, started, completed]

        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")
        op = poller.result(timeout=10)
        assert op.status == OperationStatus.COMPLETED
        assert mock_sdk.operations.get_operation_by_id.call_count == 3

    def test_timeout_raises(self, mock_sdk, make_poll_response):
        mock_sdk.operations.get_operation_by_id.return_value = make_poll_response(
            status=OperationStatus.STARTED, retry_after="0",
        )
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123")
        with pytest.raises(OperationTimeout) as exc_info:
            poller.result(timeout=0)
        assert exc_info.value.operation_id == "op-123"

    def test_retry_after_updated_from_header(self, mock_sdk, make_poll_response):
        resp = make_poll_response(status=OperationStatus.STARTED, retry_after="7")
        mock_sdk.operations.get_operation_by_id.return_value = resp
        poller = OperationPoller(sdk=mock_sdk, operation_id="op-123", initial_retry_after=1.0)
        try:
            poller.result(timeout=0)
        except OperationTimeout:
            pass
        assert poller._retry_after == 7.0


class TestPollAsync:
    @pytest.mark.asyncio
    async def test_poll_async_updates_state(self, make_poll_response):
        resp = make_poll_response(status=OperationStatus.STARTED)
        sdk = MagicMock()
        sdk.operations.get_operation_by_id_async = AsyncMock(return_value=resp)
        poller = OperationPoller(sdk=sdk, operation_id="op-123")

        result = await poller.poll_async()
        assert result is resp.result
        assert poller.last_operation is resp.result

    @pytest.mark.asyncio
    async def test_result_async_completes(self, make_poll_response):
        completed = make_poll_response(status=OperationStatus.COMPLETED)
        sdk = MagicMock()
        sdk.operations.get_operation_by_id_async = AsyncMock(return_value=completed)
        poller = OperationPoller(sdk=sdk, operation_id="op-123")

        op = await poller.result_async(timeout=10)
        assert op.status == OperationStatus.COMPLETED

    @pytest.mark.asyncio
    async def test_result_async_timeout(self, make_poll_response):
        started = make_poll_response(status=OperationStatus.STARTED, retry_after="0")
        sdk = MagicMock()
        sdk.operations.get_operation_by_id_async = AsyncMock(return_value=started)
        poller = OperationPoller(sdk=sdk, operation_id="op-123")

        with pytest.raises(OperationTimeout):
            await poller.result_async(timeout=0)


class TestProperties:
    def test_operation_id(self):
        poller = OperationPoller(sdk=MagicMock(), operation_id="my-op")
        assert poller.operation_id == "my-op"

    def test_response_body(self):
        poller = OperationPoller(sdk=MagicMock(), operation_id="x", response_body={"url": "/upload"})
        assert poller.response_body == {"url": "/upload"}

    def test_last_operation_initially_none(self):
        poller = OperationPoller(sdk=MagicMock(), operation_id="x")
        assert poller.last_operation is None
