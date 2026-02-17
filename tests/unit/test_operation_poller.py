"""Tests for OperationPoller: _check_terminal, done(), poll(), result()."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from workiva.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
)
from workiva.models.platform import Operation
from workiva.polling import OperationPoller


def _make_poller(
    operation_id: str = "op-test-123",
    initial_retry_after: float = 0.01,
) -> OperationPoller:
    """Create an OperationPoller with a mocked Workiva client."""
    mock_client = MagicMock()
    return OperationPoller(
        client=mock_client,
        operation_id=operation_id,
        initial_retry_after=initial_retry_after,
    )


def _mock_response(body: dict, headers: dict | None = None) -> MagicMock:
    """Create a mock httpx.Response with .json() and .headers."""
    resp = MagicMock()
    resp.json.return_value = body
    resp.headers = headers or {}
    return resp


def _operation(**kwargs) -> Operation:
    """Build an Operation model instance for tests."""
    return Operation.model_validate(kwargs)


class TestCheckTerminal:
    """Tests for OperationPoller._check_terminal."""

    def test_raises_operation_failed_on_failed(self):
        poller = _make_poller()
        op = _operation(id="op-fail", status="failed")

        with pytest.raises(OperationFailed) as exc_info:
            poller._check_terminal(op)

        assert exc_info.value.operation.id == "op-fail"

    def test_raises_operation_cancelled_on_cancelled(self):
        poller = _make_poller()
        op = _operation(id="op-cancel", status="cancelled")

        with pytest.raises(OperationCancelled) as exc_info:
            poller._check_terminal(op)

        assert exc_info.value.operation.id == "op-cancel"

    def test_no_exception_on_completed(self):
        poller = _make_poller()
        op = _operation(id="op-ok", status="completed")
        poller._check_terminal(op)

    def test_no_exception_on_running(self):
        poller = _make_poller()
        op = _operation(id="op-run", status="started")
        poller._check_terminal(op)

    def test_no_exception_on_pending(self):
        poller = _make_poller()
        op = _operation(id="op-pend", status="queued")
        poller._check_terminal(op)

    def test_no_exception_on_missing_status(self):
        poller = _make_poller()
        op = _operation(id="op-no-status")
        poller._check_terminal(op)

    def test_failed_with_details_preserved(self):
        poller = _make_poller()
        op = _operation(
            id="op-fail-detail",
            status="failed",
            details=[{"code": "E001", "message": "disk full"}],
        )

        with pytest.raises(OperationFailed) as exc_info:
            poller._check_terminal(op)

        assert len(exc_info.value.details) == 1
        assert exc_info.value.details[0].code == "E001"


class TestDone:
    """Tests for OperationPoller.done()."""

    def test_false_before_any_polling(self):
        poller = _make_poller()
        assert poller.done() is False

    def test_false_when_last_operation_is_running(self):
        poller = _make_poller()
        poller._last_operation = _operation(status="started")
        assert poller.done() is False

    def test_true_after_completed(self):
        poller = _make_poller()
        poller._last_operation = _operation(status="completed")
        assert poller.done() is True

    def test_true_after_failed(self):
        poller = _make_poller()
        poller._last_operation = _operation(status="failed")
        assert poller.done() is True

    def test_true_after_cancelled(self):
        poller = _make_poller()
        poller._last_operation = _operation(status="cancelled")
        assert poller.done() is True


class TestPoll:
    """Tests for OperationPoller.poll() — single sync poll request."""

    def test_poll_returns_operation_model(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "started"}
        poller._client._base_client.request.return_value = _mock_response(body)

        result = poller.poll()

        assert isinstance(result, Operation)
        assert result.id == "op-test-123"
        assert result.status == "started"
        assert poller._last_operation is result

    def test_poll_calls_correct_endpoint(self):
        from workiva._constants import _API

        poller = _make_poller(operation_id="op-xyz")
        poller._client._base_client.request.return_value = _mock_response(
            {"id": "op-xyz", "status": "started"}
        )

        poller.poll()

        poller._client._base_client.request.assert_called_once_with(
            "GET",
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": "op-xyz"},
        )

    def test_poll_updates_retry_after_from_headers(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "started"}
        poller._client._base_client.request.return_value = _mock_response(
            body, headers={"retry-after": "7"}
        )

        poller.poll()

        assert poller._retry_after == 7.0

    def test_poll_raises_on_failed(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "failed"}
        poller._client._base_client.request.return_value = _mock_response(body)

        with pytest.raises(OperationFailed):
            poller.poll()

    def test_poll_raises_on_cancelled(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "cancelled"}
        poller._client._base_client.request.return_value = _mock_response(body)

        with pytest.raises(OperationCancelled):
            poller.poll()


class TestResult:
    """Tests for OperationPoller.result() — poll loop until terminal."""

    def test_result_returns_operation_model(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "completed"}
        poller._client._base_client.request.return_value = _mock_response(body)

        result = poller.result(timeout=5)

        assert isinstance(result, Operation)
        assert result.status == "completed"

    def test_result_polls_until_completed(self):
        poller = _make_poller()
        running = _mock_response(
            {"id": "op-test-123", "status": "started"},
            headers={"retry-after": "0"},
        )
        completed = _mock_response(
            {"id": "op-test-123", "status": "completed"},
        )
        poller._client._base_client.request.side_effect = [running, completed]

        with patch("workiva.polling.time.sleep"):
            result = poller.result(timeout=10)

        assert result.status == "completed"
        assert poller._client._base_client.request.call_count == 2

    def test_result_raises_timeout(self):
        poller = _make_poller()
        running = _mock_response(
            {"id": "op-test-123", "status": "started"},
            headers={"retry-after": "0"},
        )
        poller._client._base_client.request.return_value = running

        with patch("workiva.polling.time.sleep"):
            with pytest.raises(OperationTimeout) as exc_info:
                poller.result(timeout=0)

        assert exc_info.value.operation_id == "op-test-123"
        assert exc_info.value.last_status == "started"

    def test_result_propagates_failed(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "failed"}
        poller._client._base_client.request.return_value = _mock_response(body)

        with pytest.raises(OperationFailed):
            poller.result(timeout=5)

    def test_result_propagates_cancelled(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "cancelled"}
        poller._client._base_client.request.return_value = _mock_response(body)

        with pytest.raises(OperationCancelled):
            poller.result(timeout=5)


class TestPollAsync:
    """Tests for OperationPoller.poll_async()."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_poll_async_returns_operation_model(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "started"}
        poller._client._base_client.request_async = AsyncMock(
            return_value=_mock_response(body)
        )

        result = await poller.poll_async()

        assert isinstance(result, Operation)
        assert result.id == "op-test-123"
        assert result.status == "started"

    @pytest.mark.asyncio(loop_scope="function")
    async def test_poll_async_raises_on_failed(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "failed"}
        poller._client._base_client.request_async = AsyncMock(
            return_value=_mock_response(body)
        )

        with pytest.raises(OperationFailed):
            await poller.poll_async()


class TestResultAsync:
    """Tests for OperationPoller.result_async()."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_result_async_returns_on_completed(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "completed"}
        poller._client._base_client.request_async = AsyncMock(
            return_value=_mock_response(body)
        )

        result = await poller.result_async(timeout=5)

        assert isinstance(result, Operation)
        assert result.status == "completed"

    @pytest.mark.asyncio(loop_scope="function")
    async def test_result_async_raises_timeout(self):
        poller = _make_poller()
        body = {"id": "op-test-123", "status": "started"}
        poller._client._base_client.request_async = AsyncMock(
            return_value=_mock_response(body, headers={"retry-after": "0"})
        )

        with patch("workiva.polling.asyncio.sleep", new_callable=AsyncMock):
            with pytest.raises(OperationTimeout) as exc_info:
                await poller.result_async(timeout=0)

        assert exc_info.value.last_status == "started"
