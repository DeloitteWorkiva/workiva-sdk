"""Tests for _extract_operation_id and _get_retry_after."""

from __future__ import annotations

import pytest

from workiva.polling import _extract_operation_id, _get_retry_after


class TestExtractOperationId:
    def test_full_url(self):
        headers = {"location": "https://api.app.wdesk.com/platform/v1/operations/abc-123"}
        assert _extract_operation_id(headers) == "abc-123"

    def test_partial_path(self):
        headers = {"location": "/platform/v1/operations/xyz-789"}
        assert _extract_operation_id(headers) == "xyz-789"

    def test_header_as_list(self):
        headers = {"location": ["/operations/list-val"]}
        assert _extract_operation_id(headers) == "list-val"

    def test_missing_header_raises(self):
        with pytest.raises(ValueError, match="no 'location' header"):
            _extract_operation_id({})

    def test_no_match_raises(self):
        headers = {"location": "https://api.example.com/something/else"}
        with pytest.raises(ValueError, match="Could not extract"):
            _extract_operation_id(headers)

    def test_uuid_format(self):
        op_id = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        headers = {"location": f"/operations/{op_id}"}
        assert _extract_operation_id(headers) == op_id


class TestGetRetryAfter:
    def test_normal_value(self):
        assert _get_retry_after({"retry-after": "5"}) == 5.0

    def test_missing_returns_default(self):
        assert _get_retry_after({}) == 2.0

    def test_custom_default(self):
        assert _get_retry_after({}, default=10.0) == 10.0

    def test_capped_at_max(self):
        assert _get_retry_after({"retry-after": "120"}) == 60.0

    def test_negative_clamped_to_minimum(self):
        assert _get_retry_after({"retry-after": "-5"}) == 1.0

    def test_invalid_returns_default(self):
        assert _get_retry_after({"retry-after": "not-a-number"}) == 2.0

    def test_value_as_list(self):
        assert _get_retry_after({"retry-after": ["3"]}) == 3.0

    def test_float_value(self):
        assert _get_retry_after({"retry-after": "1.5"}) == 1.5

    def test_zero_value(self):
        assert _get_retry_after({"retry-after": "0"}) == 1.0


class TestRetryAfterMinimumFloor:
    """Retry-After values below 1.0 should be floored to 1.0."""

    def test_zero_retry_after_floored(self):
        """Retry-After: 0 → should return 1.0."""
        assert _get_retry_after({"retry-after": "0"}) == 1.0

    def test_half_second_floored(self):
        """Retry-After: 0.5 → should return 1.0."""
        assert _get_retry_after({"retry-after": "0.5"}) == 1.0

    def test_above_minimum_unchanged(self):
        """Retry-After: 2.0 → should stay 2.0."""
        assert _get_retry_after({"retry-after": "2.0"}) == 2.0

    def test_exactly_one_unchanged(self):
        """Retry-After: 1.0 → should stay 1.0."""
        assert _get_retry_after({"retry-after": "1.0"}) == 1.0
