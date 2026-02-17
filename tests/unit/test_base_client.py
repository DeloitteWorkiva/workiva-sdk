"""Tests for BaseClient URL building, request preparation, and lazy client creation."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from workiva._client import BaseClient
from workiva._config import SDKConfig
from workiva._constants import Region, _API, get_base_url


def _make_client(region: Region = Region.EU) -> BaseClient:
    """Create a BaseClient with mocked auth so no real HTTP calls happen."""
    config = SDKConfig(region=region)
    with patch("workiva._client.OAuth2ClientCredentials"):
        return BaseClient(
            client_id="test-id",
            client_secret="test-secret",
            config=config,
        )


class TestBuildUrl:
    """Tests for BaseClient._build_url."""

    def test_platform_url(self):
        client = _make_client(Region.EU)
        url = client._build_url(_API.PLATFORM, "/files")
        assert url == "https://api.eu.wdesk.com/files"

    def test_chains_url(self):
        client = _make_client(Region.US)
        url = client._build_url(_API.CHAINS, "/v1/chains")
        assert url == "https://h.app.wdesk.com/s/wdata/oc/api/v1/chains"

    def test_wdata_url(self):
        client = _make_client(Region.APAC)
        url = client._build_url(_API.WDATA, "/api/v1/tables")
        assert url == "https://h.apac.wdesk.com/s/wdata/prep/api/v1/tables"

    def test_all_regions_platform(self):
        for region in Region:
            client = _make_client(region)
            url = client._build_url(_API.PLATFORM, "/test")
            expected = get_base_url(_API.PLATFORM, region) + "/test"
            assert url == expected, f"Failed for region {region}"

    def test_path_param_substitution(self):
        client = _make_client()
        url = client._build_url(
            _API.PLATFORM,
            "/files/{fileId}",
            path_params={"fileId": "abc-123"},
        )
        assert url == "https://api.eu.wdesk.com/files/abc-123"

    def test_multiple_path_params(self):
        client = _make_client()
        url = client._build_url(
            _API.PLATFORM,
            "/files/{fileId}/sections/{sectionId}",
            path_params={"fileId": "f-1", "sectionId": "s-2"},
        )
        assert url == "https://api.eu.wdesk.com/files/f-1/sections/s-2"

    def test_path_param_url_encodes_special_chars(self):
        client = _make_client()
        url = client._build_url(
            _API.PLATFORM,
            "/files/{fileId}",
            path_params={"fileId": "has spaces/and+slashes"},
        )
        # Spaces → %20, slashes → %2F, plus → %2B
        assert "has%20spaces%2Fand%2Bslashes" in url
        assert " " not in url
        assert "/has spaces" not in url

    def test_path_param_encodes_unicode(self):
        client = _make_client()
        url = client._build_url(
            _API.PLATFORM,
            "/files/{fileId}",
            path_params={"fileId": "café"},
        )
        assert "caf%C3%A9" in url

    def test_no_path_params_leaves_template_untouched(self):
        client = _make_client()
        url = client._build_url(_API.PLATFORM, "/files/{fileId}")
        assert "{fileId}" in url

    def test_empty_path_params_dict_leaves_template(self):
        client = _make_client()
        url = client._build_url(
            _API.PLATFORM,
            "/files/{fileId}",
            path_params={},
        )
        # Empty dict is falsy, so template remains
        assert "{fileId}" in url


class TestPrepareRequest:
    """Tests for BaseClient._prepare_request."""

    def test_filters_none_query_params(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            query_params={"limit": 10, "cursor": None, "offset": None},
        )
        assert kwargs["params"] == {"limit": 10}

    def test_all_none_query_params_excluded(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            query_params={"cursor": None, "offset": None},
        )
        # All values are None → filtered dict is empty → falsy → no "params" key
        assert "params" not in kwargs

    def test_passes_json_body(self):
        client = _make_client()
        body = {"name": "My File", "type": "document"}
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            json_body=body,
        )
        assert kwargs["json"] == body

    def test_passes_content(self):
        client = _make_client()
        raw = b"binary-data-here"
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files/{fileId}/upload",
            path_params={"fileId": "f-1"},
            content=raw,
        )
        assert kwargs["content"] is raw
        assert "json" not in kwargs

    def test_passes_files_multipart(self):
        client = _make_client()
        file_payload = {"file": ("report.pdf", b"pdf-bytes", "application/pdf")}
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files/upload",
            files=file_payload,
        )
        assert kwargs["files"] is file_payload
        assert "json" not in kwargs
        assert "content" not in kwargs

    def test_files_with_data(self):
        client = _make_client()
        file_payload = {"file": ("report.pdf", b"pdf-bytes", "application/pdf")}
        form_data = {"description": "Quarterly report"}
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files/upload",
            files=file_payload,
            data=form_data,
        )
        assert kwargs["files"] is file_payload
        assert kwargs["data"] is form_data

    def test_preserves_false_in_query_params(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            query_params={"includeArchived": False, "limit": 10},
        )
        assert kwargs["params"]["includeArchived"] is False

    def test_preserves_zero_in_query_params(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            query_params={"offset": 0, "limit": 50},
        )
        assert kwargs["params"]["offset"] == 0

    def test_preserves_empty_string_in_query_params(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            query_params={"filter": "", "limit": 10},
        )
        assert kwargs["params"]["filter"] == ""

    def test_json_body_takes_priority_over_content(self):
        """json_body is checked first; content is ignored if json_body is set."""
        client = _make_client()
        body = {"key": "value"}
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            json_body=body,
            content=b"raw",
        )
        assert "json" in kwargs
        assert "content" not in kwargs

    def test_returns_correct_url(self):
        client = _make_client(Region.US)
        url, _kwargs = client._prepare_request(
            _API.PLATFORM,
            "/operations/{operationId}",
            path_params={"operationId": "op-99"},
        )
        assert url == "https://api.app.wdesk.com/operations/op-99"

    def test_no_query_params_omits_params_key(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(_API.PLATFORM, "/files")
        assert "params" not in kwargs

    def test_custom_headers_passed_through(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            headers={"X-Custom": "value"},
        )
        assert kwargs["headers"]["X-Custom"] == "value"

    def test_timeout_passed_through(self):
        client = _make_client()
        _url, kwargs = client._prepare_request(
            _API.PLATFORM,
            "/files",
            timeout=30.0,
        )
        assert kwargs["timeout"] == 30.0


class TestLazyClientCreation:
    """Tests that sync/async clients are NOT created until first use."""

    def test_sync_client_not_created_at_init(self):
        client = _make_client()
        assert client._client is None
        assert client._client_created is False

    def test_async_client_not_created_at_init(self):
        client = _make_client()
        assert client._async_client is None
        assert client._async_client_created is False

    def test_sync_client_created_on_request(self):
        """Calling _get_sync_client() lazily creates the httpx.Client."""
        client = _make_client()
        assert client._client is None

        sync_client = client._get_sync_client()

        assert sync_client is not None
        assert client._client is sync_client
        assert client._client_created is True
        sync_client.close()

    def test_async_client_created_on_request(self):
        """Calling _get_async_client() lazily creates the httpx.AsyncClient."""
        client = _make_client()
        assert client._async_client is None

        async_client = client._get_async_client()

        assert async_client is not None
        assert client._async_client is async_client
        assert client._async_client_created is True

    def test_sync_creation_does_not_create_async(self):
        """Getting the sync client must NOT create the async client."""
        client = _make_client()
        client._get_sync_client()

        assert client._client_created is True
        assert client._async_client is None
        assert client._async_client_created is False
        client._client.close()

    def test_async_creation_does_not_create_sync(self):
        """Getting the async client must NOT create the sync client."""
        client = _make_client()
        client._get_async_client()

        assert client._async_client_created is True
        assert client._client is None
        assert client._client_created is False

    def test_supplied_sync_client_not_recreated(self):
        """When a sync client is supplied, _get_sync_client returns it as-is."""
        import httpx

        supplied = httpx.Client()
        config = SDKConfig(region=Region.EU)
        with patch("workiva._client.OAuth2ClientCredentials"):
            client = BaseClient(
                client_id="id",
                client_secret="secret",
                config=config,
                client=supplied,
            )

        assert client._get_sync_client() is supplied
        assert client._client_supplied is True
        supplied.close()
