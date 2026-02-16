"""Shared fixtures for the Workiva SDK test suite."""

from __future__ import annotations

import pytest

from workiva._auth import OAuth2ClientCredentials


@pytest.fixture(autouse=True)
def _clear_oauth_cache():
    """Clear the class-level OAuth token cache between tests."""
    OAuth2ClientCredentials._clear_cache()
    yield
    OAuth2ClientCredentials._clear_cache()
