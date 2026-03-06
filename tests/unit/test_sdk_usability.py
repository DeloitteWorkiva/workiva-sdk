"""SDK usability and developer experience tests.

Verifies that the SDK is intuitive, non-verbose, and doesn't have
silent failure modes. These tests catch DX regressions.
"""

from __future__ import annotations

import pytest


class TestPopulateByName:
    """Issue #11: snake_case field names must work on all models."""

    def test_metric_value_accepts_snake_case(self):
        """MetricValue(reporting_period=...) must NOT silently drop the field."""
        from workiva.models.platform import MetricValue, ReportingPeriod

        period = ReportingPeriod(start=1, end=12, year=2025)
        mv = MetricValue(reporting_period=period)

        assert mv.reporting_period is not None
        assert mv.reporting_period.year == 2025

    def test_metric_value_accepts_alias(self):
        """camelCase alias still works for backwards compatibility."""
        from workiva.models.platform import MetricValue, ReportingPeriod

        period = ReportingPeriod(start=1, end=12, year=2025)
        mv = MetricValue(reportingPeriod=period)

        assert mv.reporting_period is not None

    def test_snake_case_serializes_with_alias(self):
        """Even when constructed with snake_case, JSON output uses camelCase."""
        from workiva.models.platform import MetricValue, ReportingPeriod

        period = ReportingPeriod(start=1, end=12, year=2025)
        mv = MetricValue(reporting_period=period)
        data = mv.model_dump(by_alias=True, exclude_none=True)

        assert "reportingPeriod" in data
        assert "reporting_period" not in data

    def test_file_copy_options_snake_case(self):
        """FileCopyOptions fields work with snake_case."""
        from workiva.models.platform import FileCopyOptions

        opts = FileCopyOptions(email_on_complete=True)
        data = opts.model_dump(by_alias=True, exclude_none=True)

        assert "emailOnComplete" in data
        assert "email_on_complete" not in data

    def test_extra_fields_still_allowed(self):
        """extra='allow' still works alongside populate_by_name."""
        from workiva.models.platform import File

        f = File(name="test.xlsx", custom_field="hello")
        extras = f.model_extra or {}
        assert "custom_field" in extras


class TestBatchDeletionTypeSafety:
    """Issue #12: batch_deletion_metric_values accepts MetricValue objects."""

    def test_signature_accepts_metric_value_list(self):
        """The data param should accept list[MetricValue], not list[dict]."""
        import inspect
        from workiva._operations.sustainability import Sustainability

        sig = inspect.signature(Sustainability.batch_deletion_metric_values)
        data_param = sig.parameters["data"]
        # The annotation should reference MetricValue, not dict
        annotation_str = str(data_param.annotation)
        assert "MetricValue" in annotation_str
        assert "dict" not in annotation_str


class TestTrashFileOptionalBody:
    """Issue #13: trash_file_by_id body is optional."""

    def test_body_is_optional_in_signature(self):
        """body should default to None — no need to pass FileTrashOptions()."""
        import inspect
        from workiva._operations.files import Files

        sig = inspect.signature(Files.trash_file_by_id)
        body_param = sig.parameters["body"]
        assert body_param.default is None

    def test_restore_file_body_is_optional(self):
        """restore_file_by_id also has an empty body schema."""
        import inspect
        from workiva._operations.files import Files

        sig = inspect.signature(Files.restore_file_by_id)
        body_param = sig.parameters["body"]
        assert body_param.default is None


class TestWaitParameterExists:
    """Issue #15: long-running operations have wait/wait_timeout params."""

    def test_copy_file_has_wait_param(self):
        import inspect
        from workiva._operations.files import Files

        sig = inspect.signature(Files.copy_file)
        assert "wait" in sig.parameters
        assert "wait_timeout" in sig.parameters
        assert sig.parameters["wait"].default is False
        assert sig.parameters["wait_timeout"].default == 300

    def test_copy_sheet_has_wait_param(self):
        import inspect
        from workiva._operations.spreadsheets import Spreadsheets

        sig = inspect.signature(Spreadsheets.copy_sheet)
        assert "wait" in sig.parameters

    def test_non_202_operation_has_no_wait_param(self):
        """get_files (200 response) should NOT have wait param."""
        import inspect
        from workiva._operations.files import Files

        sig = inspect.signature(Files.get_files)
        assert "wait" not in sig.parameters


class TestDeepSerialize:
    """_deep_serialize handles Pydantic models, Enums, and nested structures."""

    def test_pydantic_model(self):
        from workiva._client import _deep_serialize
        from workiva.models.platform import MetricValue, ReportingPeriod

        period = ReportingPeriod(start=1, end=12, year=2025)
        mv = MetricValue(reporting_period=period)
        result = _deep_serialize(mv)

        assert isinstance(result, dict)
        assert "reportingPeriod" in result

    def test_enum_value(self):
        from workiva._client import _deep_serialize
        from workiva._constants import Region

        result = _deep_serialize(Region.US)
        assert result == "us"

    def test_nested_list_of_models(self):
        from workiva._client import _deep_serialize
        from workiva.models.platform import MetricValue

        values = [MetricValue(), MetricValue()]
        result = _deep_serialize(values)

        assert isinstance(result, list)
        assert all(isinstance(v, dict) for v in result)

    def test_plain_values_pass_through(self):
        from workiva._client import _deep_serialize

        assert _deep_serialize("hello") == "hello"
        assert _deep_serialize(42) == 42
        assert _deep_serialize(None) is None
        assert _deep_serialize(True) is True
