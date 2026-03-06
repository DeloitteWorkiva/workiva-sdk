"""Usability audit — verifies the SDK is INTUITIVE, NON-VERBOSE, and SAFE.

Each test class documents a usability guarantee that must never regress.
Tests are intentionally short (3-5 lines) so they double as usage examples.
"""

from __future__ import annotations

import re
from unittest.mock import MagicMock

import httpx
import pytest


# ---------------------------------------------------------------------------
# 1. Everything importable from top-level
# ---------------------------------------------------------------------------


class TestImports:
    """Users should never need deep imports for common SDK objects."""

    def test_client_importable(self):
        from workiva import Workiva  # noqa: F401

    def test_version_importable_and_semver(self):
        from workiva import __version__

        assert isinstance(__version__, str)
        assert re.match(r"^\d+\.\d+\.\d+$", __version__), f"Bad semver: {__version__}"

    def test_config_classes_importable(self):
        from workiva import RetryConfig, Region  # noqa: F401

    def test_all_exceptions_importable(self):
        from workiva import (  # noqa: F401
            WorkivaError,
            WorkivaAPIError,
            BadRequestError,
            AuthenticationError,
            ForbiddenError,
            NotFoundError,
            ConflictError,
            RateLimitError,
            ServerError,
            TokenAcquisitionError,
            OperationFailed,
            OperationCancelled,
            OperationTimeout,
            PaginationError,
        )

    def test_poller_importable(self):
        from workiva import OperationPoller  # noqa: F401


# ---------------------------------------------------------------------------
# 2. Single catch-all for ALL SDK errors
# ---------------------------------------------------------------------------


class TestErrorHierarchy:
    """``except WorkivaError`` must catch EVERYTHING the SDK throws."""

    @pytest.mark.parametrize(
        "exc_path",
        [
            "workiva._errors.WorkivaAPIError",
            "workiva._errors.BadRequestError",
            "workiva._errors.AuthenticationError",
            "workiva._errors.ForbiddenError",
            "workiva._errors.NotFoundError",
            "workiva._errors.ConflictError",
            "workiva._errors.RateLimitError",
            "workiva._errors.ServerError",
            "workiva.exceptions.OperationFailed",
            "workiva.exceptions.OperationCancelled",
            "workiva.exceptions.OperationTimeout",
            "workiva.exceptions.PaginationError",
            "workiva._auth.TokenAcquisitionError",
        ],
    )
    def test_all_exceptions_are_workiva_error(self, exc_path: str):
        import importlib

        from workiva import WorkivaError

        module_path, cls_name = exc_path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        exc_cls = getattr(module, cls_name)
        assert issubclass(exc_cls, WorkivaError), f"{cls_name} is not a WorkivaError"

    def test_catch_all_pattern(self):
        """The single-catch pattern must work in practice."""
        from workiva import WorkivaError, NotFoundError

        with pytest.raises(WorkivaError):
            raise NotFoundError(
                "not found",
                status_code=404,
                response=httpx.Response(404, request=httpx.Request("GET", "/")),
            )


# ---------------------------------------------------------------------------
# 3. Non-verbose error handling patterns
# ---------------------------------------------------------------------------


class TestErrorPatterns:
    """Error handling should be clean and informative."""

    def _make_api_error(self, status: int = 404) -> httpx.Response:
        return httpx.Response(
            status,
            json={"error": {"code": "NOT_FOUND", "message": "File xyz not found"}},
            request=httpx.Request("GET", "https://api.eu.wdesk.com/platform/v1/files/xyz"),
        )

    def test_broad_catch_gives_useful_message(self):
        from workiva._errors import raise_for_status, WorkivaError

        with pytest.raises(WorkivaError) as exc_info:
            raise_for_status(self._make_api_error(404))
        assert "404" in str(exc_info.value)

    def test_specific_catch_exposes_status_code(self):
        from workiva import NotFoundError
        from workiva._errors import raise_for_status

        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(self._make_api_error(404))
        assert exc_info.value.status_code == 404

    def test_error_message_contains_context(self):
        from workiva._errors import raise_for_status, WorkivaAPIError

        with pytest.raises(WorkivaAPIError) as exc_info:
            raise_for_status(self._make_api_error(404))
        msg = str(exc_info.value)
        assert "NOT_FOUND" in msg or "File xyz not found" in msg


# ---------------------------------------------------------------------------
# 4. Config is simple
# ---------------------------------------------------------------------------


class TestConfigSimplicity:
    """Configuration must work with sensible defaults — zero required params."""

    def test_sdk_config_no_params(self):
        from workiva import SDKConfig

        cfg = SDKConfig()
        assert cfg.region is not None

    def test_region_enum_discoverable(self):
        from workiva import Region

        assert Region.EU.value == "eu"
        assert Region.US.value == "us"
        assert Region.APAC.value == "apac"

    def test_retry_config_sane_defaults(self):
        from workiva import RetryConfig

        cfg = RetryConfig()
        assert cfg.max_retries > 0
        assert cfg.initial_interval_ms > 0

    def test_retry_param_accepted(self):
        from workiva import Workiva, RetryConfig
        client = Workiva(
            client_id="id", client_secret="secret",
            retry=RetryConfig(max_retries=10),
        )
        assert client._config.retry.max_retries == 10
        client.close()

    def test_config_param_removed(self):
        """SDKConfig should not be a constructor parameter."""
        import inspect
        from workiva.client import Workiva
        sig = inspect.signature(Workiva.__init__)
        assert "config" not in sig.parameters


# ---------------------------------------------------------------------------
# 5. Namespace discovery works
# ---------------------------------------------------------------------------


class TestNamespaceDiscovery:
    """IDE autocompletion and dir() must reveal all API namespaces."""

    def _make_stub_client(self):
        from workiva.client import Workiva

        w = Workiva.__new__(Workiva)
        w._base_client = MagicMock()
        w._config = MagicMock()
        return w

    def test_dir_includes_all_namespaces(self):
        w = self._make_stub_client()
        attrs = dir(w)
        expected = [
            "files", "spreadsheets", "documents", "presentations",
            "chains", "wdata", "reports", "tasks", "operations",
        ]
        for ns in expected:
            assert ns in attrs, f"Namespace '{ns}' missing from dir()"

    def test_at_least_18_namespaces(self):
        from workiva.client import Workiva

        assert len(Workiva._NAMESPACE_MAP) >= 18

    def test_nonexistent_namespace_raises_attribute_error(self):
        w = self._make_stub_client()
        with pytest.raises(AttributeError, match="no attribute 'nonexistent_api'"):
            w.nonexistent_api


# ---------------------------------------------------------------------------
# 6. SDK doesn't silently fail
# ---------------------------------------------------------------------------


class TestNoSilentFailures:
    """Bad input must fail FAST with clear messages."""

    def test_empty_client_id_raises(self):
        from workiva import Workiva

        with pytest.raises(ValueError, match="client_id"):
            Workiva(client_id="", client_secret="secret")

    def test_none_client_id_raises(self):
        from workiva import Workiva

        with pytest.raises((ValueError, TypeError)):
            Workiva(client_id=None, client_secret="secret")

    def test_wait_on_wrong_type_raises(self):
        from workiva.client import Workiva

        w = Workiva.__new__(Workiva)
        w._base_client = MagicMock()
        w._config = MagicMock()

        with pytest.raises(TypeError, match="httpx.Response"):
            w.wait({"status": "completed"})


# ---------------------------------------------------------------------------
# 7. Models work with snake_case
# ---------------------------------------------------------------------------


class TestSnakeCaseModels:
    """Python users write snake_case. The SDK must accept and preserve it."""

    def test_construct_with_snake_case(self):
        from workiva.models.platform import MetricValue, ReportingPeriod

        rp = ReportingPeriod(start=1, end=12, year=2025)
        mv = MetricValue(reporting_period=rp)
        assert mv.reporting_period.year == 2025

    def test_serializes_with_camel_case(self):
        from workiva.models.platform import MetricValue, ReportingPeriod

        mv = MetricValue(reporting_period=ReportingPeriod(start=1, end=12, year=2025))
        data = mv.model_dump(by_alias=True, exclude_none=True)
        assert "reportingPeriod" in data

    def test_snake_case_not_silently_dropped(self):
        from workiva.models.platform import MetricValue, ReportingPeriod

        mv = MetricValue(reporting_period=ReportingPeriod(start=1, end=12, year=2025))
        assert mv.reporting_period is not None
        assert mv.reporting_period.start == 1
        assert mv.reporting_period.end == 12
