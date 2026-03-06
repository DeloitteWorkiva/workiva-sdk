"""Tests for Workiva.copy_sheets() batch helper."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from workiva.models.platform import Operation


def _mock_workiva():
    """Create a minimal mock Workiva client for copy_sheets testing."""
    from workiva.client import Workiva

    with patch.object(Workiva, "__init__", lambda self, **kw: None):
        w = Workiva.__new__(Workiva)
        w._base_client = MagicMock()
        w._config = MagicMock()

        # Mock the spreadsheets namespace
        mock_ns = MagicMock()
        completed_op = Operation.model_validate({"id": "op-1", "status": "completed"})
        mock_ns.copy_sheet_async = AsyncMock(return_value=completed_op)
        w.spreadsheets = mock_ns

        return w


class TestCopySheets:
    """Batch copy_sheets convenience method."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_returns_operations_in_order(self):
        w = _mock_workiva()
        ops = [
            Operation.model_validate({"id": f"op-{i}", "status": "completed"})
            for i in range(3)
        ]
        w.spreadsheets.copy_sheet_async = AsyncMock(side_effect=ops)

        results = await w.copy_sheets(
            spreadsheet_id="ss-1",
            copies=[
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "A"},
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "B"},
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "C"},
            ],
        )

        assert len(results) == 3
        assert results[0].id == "op-0"
        assert results[2].id == "op-2"

    @pytest.mark.asyncio(loop_scope="function")
    async def test_empty_copies_returns_empty(self):
        w = _mock_workiva()

        results = await w.copy_sheets(spreadsheet_id="ss-1", copies=[])

        assert results == []
        w.spreadsheets.copy_sheet_async.assert_not_called()

    @pytest.mark.asyncio(loop_scope="function")
    async def test_passes_wait_true_and_timeout(self):
        w = _mock_workiva()

        await w.copy_sheets(
            spreadsheet_id="ss-1",
            copies=[{"sheet_id": "t1", "spreadsheet": "ss-1"}],
            wait_timeout=60,
        )

        _, kwargs = w.spreadsheets.copy_sheet_async.call_args
        assert kwargs["wait"] is True
        assert kwargs["wait_timeout"] == 60
        assert kwargs["spreadsheet_id"] == "ss-1"

    @pytest.mark.asyncio(loop_scope="function")
    async def test_propagates_exception(self):
        w = _mock_workiva()
        w.spreadsheets.copy_sheet_async = AsyncMock(
            side_effect=RuntimeError("API failed")
        )

        with pytest.raises(RuntimeError, match="API failed"):
            await w.copy_sheets(
                spreadsheet_id="ss-1",
                copies=[{"sheet_id": "t1", "spreadsheet": "ss-1"}],
            )


class TestCopySheetsSync:
    def test_returns_operations_in_order(self):
        w = _mock_workiva()
        ops = [
            Operation.model_validate({"id": f"op-{i}", "status": "completed"})
            for i in range(3)
        ]
        w.spreadsheets.copy_sheet = MagicMock(side_effect=ops)

        results = w.copy_sheets_sync(
            spreadsheet_id="ss-1",
            copies=[
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "A"},
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "B"},
                {"sheet_id": "t1", "spreadsheet": "ss-1", "sheet_name": "C"},
            ],
        )

        assert len(results) == 3
        assert results[0].id == "op-0"
        assert results[2].id == "op-2"

    def test_empty_copies_returns_empty(self):
        w = _mock_workiva()
        w.spreadsheets.copy_sheet = MagicMock()

        results = w.copy_sheets_sync(spreadsheet_id="ss-1", copies=[])

        assert results == []
        w.spreadsheets.copy_sheet.assert_not_called()

    def test_passes_wait_true_and_timeout(self):
        w = _mock_workiva()
        op = Operation.model_validate({"id": "op-1", "status": "completed"})
        w.spreadsheets.copy_sheet = MagicMock(return_value=op)

        w.copy_sheets_sync(
            spreadsheet_id="ss-1",
            copies=[{"sheet_id": "t1", "spreadsheet": "ss-1"}],
            wait_timeout=60,
        )

        _, kwargs = w.spreadsheets.copy_sheet.call_args
        assert kwargs["wait"] is True
        assert kwargs["wait_timeout"] == 60
        assert kwargs["spreadsheet_id"] == "ss-1"
