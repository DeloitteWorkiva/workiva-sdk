"""Injects X-Version header required by the Workiva 2026-01-01 API.

See: https://developers.workiva.com/2022-01-01/2026-01-01-upgrade-guide.html
"""

import httpx
from typing import Union

from .types import BeforeRequestContext, BeforeRequestHook

API_VERSION = "2026-01-01"


class VersionHeaderHook(BeforeRequestHook):
    """Adds X-Version: 2026-01-01 to every outgoing API request."""

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        request.headers["X-Version"] = API_VERSION
        return request
