"""Tests for auth hardening: timeouts, close(), SHA-256, error sanitization."""

import hashlib
from unittest.mock import MagicMock

import httpx
import pytest

from workiva._auth import OAuth2ClientCredentials, TokenAcquisitionError


class TestTokenClientTimeout:
    """Token client must have an explicit timeout."""

    def test_token_client_has_timeout(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )
        # Token client is None before first fetch
        assert auth._token_client is None

        # Provide a mock transport so _fetch_token creates the client
        def handler(request):
            return httpx.Response(
                200,
                json={
                    "access_token": "tok",
                    "token_type": "bearer",
                    "expires_in": 3600,
                },
            )

        auth._token_transport = httpx.MockTransport(handler)
        auth._fetch_token()

        assert auth._token_client is not None
        assert auth._token_client.timeout.connect == 10.0
        assert auth._token_client.timeout.read == 30.0
        assert auth._token_client.timeout.write == 30.0
        assert auth._token_client.timeout.pool == 30.0
        auth.close()


class TestAuthClose:
    """OAuth2ClientCredentials.close() must release resources."""

    def test_close_closes_token_client(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )
        mock_client = MagicMock()
        auth._token_client = mock_client

        auth.close()

        mock_client.close.assert_called_once()
        assert auth._token_client is None

    def test_close_when_no_client(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )
        # Should not raise when no token client exists
        auth.close()

    def test_close_idempotent(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )
        mock_client = MagicMock()
        auth._token_client = mock_client

        auth.close()
        auth.close()  # Second call should be a no-op

        mock_client.close.assert_called_once()


class TestSessionKeyAlgorithm:
    """Session key must use SHA-256, not MD5."""

    def test_session_key_is_sha256(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )
        expected = hashlib.sha256(b"test-id:test-secret").hexdigest()
        assert auth._session_key == expected
        assert len(auth._session_key) == 64  # SHA-256 hex = 64 chars

    def test_session_key_not_md5(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )
        md5_value = hashlib.md5(b"test-id:test-secret").hexdigest()
        assert auth._session_key != md5_value
        assert len(auth._session_key) != 32  # MD5 hex = 32 chars


class TestTokenErrorSanitization:
    """Token error messages must NOT include response body."""

    def test_error_message_no_body(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )

        def handler(request):
            return httpx.Response(
                401,
                json={"error": "invalid_client", "secret_detail": "leaked-info"},
            )

        auth._token_client = httpx.Client(transport=httpx.MockTransport(handler))

        with pytest.raises(TokenAcquisitionError) as exc_info:
            auth._fetch_token()

        error_msg = str(exc_info.value)
        assert "leaked-info" not in error_msg
        assert "invalid_client" not in error_msg
        assert "401" in error_msg
        auth.close()

    def test_error_message_no_text_body(self):
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://example.com/oauth2/token",
        )

        def handler(request):
            return httpx.Response(
                500,
                text="Internal Server Error: database connection string=postgres://user:pass@host",
            )

        auth._token_client = httpx.Client(transport=httpx.MockTransport(handler))

        with pytest.raises(TokenAcquisitionError) as exc_info:
            auth._fetch_token()

        error_msg = str(exc_info.value)
        assert "postgres://" not in error_msg
        assert "pass@host" not in error_msg
        assert "500" in error_msg
        auth.close()
