"""Constants for the Workiva SDK — servers, regions, API version."""

from __future__ import annotations

from enum import Enum


class Region(str, Enum):
    """Workiva deployment region."""

    EU = "eu"
    US = "us"
    APAC = "apac"


class _API(str, Enum):
    """Internal API identifier for base-URL resolution."""

    PLATFORM = "platform"
    CHAINS = "chains"
    WDATA = "wdata"


API_VERSION = "2026-01-01"

# (api, region) → base URL
SERVERS: dict[tuple[_API, Region], str] = {
    # Platform
    (_API.PLATFORM, Region.EU): "https://api.eu.wdesk.com",
    (_API.PLATFORM, Region.US): "https://api.app.wdesk.com",
    (_API.PLATFORM, Region.APAC): "https://api.apac.wdesk.com",
    # Chains
    (_API.CHAINS, Region.EU): "https://h.eu.wdesk.com/s/wdata/oc/api",
    (_API.CHAINS, Region.US): "https://h.app.wdesk.com/s/wdata/oc/api",
    (_API.CHAINS, Region.APAC): "https://h.apac.wdesk.com/s/wdata/oc/api",
    # Wdata
    (_API.WDATA, Region.EU): "https://h.eu.wdesk.com/s/wdata/prep",
    (_API.WDATA, Region.US): "https://h.app.wdesk.com/s/wdata/prep",
    (_API.WDATA, Region.APAC): "https://h.apac.wdesk.com/s/wdata/prep",
}

# Token endpoint is always on the Platform base URL
TOKEN_PATH = "/oauth2/token"


def get_base_url(api: _API, region: Region) -> str:
    """Resolve the base URL for a given API and region."""
    try:
        return SERVERS[(api, region)]
    except KeyError:
        raise ValueError(
            f"No server configured for API {api.value!r} in region {region.value!r}. "
            f"Valid regions: {', '.join(r.value for r in Region)}"
        ) from None


def get_token_url(region: Region) -> str:
    """Resolve the full token endpoint URL for a region."""
    return get_base_url(_API.PLATFORM, region) + TOKEN_PATH
