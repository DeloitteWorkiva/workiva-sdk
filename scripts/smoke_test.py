#!/usr/bin/env python3
"""Smoke test: verify all 3 APIs respond with a valid token.

Reads credentials from .env (WORKIVA_CLIENT_ID, WORKIVA_CLIENT_SECRET).
Run manually before a release to confirm the multi-server auth fix works.

Usage:
    cp .env.example .env   # fill in credentials
    cd workiva-sdk && uv run python ../scripts/smoke_test.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

CLIENT_ID = os.environ.get("WORKIVA_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("WORKIVA_CLIENT_SECRET", "")

if not CLIENT_ID or not CLIENT_SECRET:
    print("ERROR: Set WORKIVA_CLIENT_ID and WORKIVA_CLIENT_SECRET in .env")
    sys.exit(1)

from workiva import Workiva  # noqa: E402


def smoke_test() -> None:
    passed = 0
    failed = 0

    with Workiva(client_id=CLIENT_ID, client_secret=CLIENT_SECRET) as client:
        # --- Platform API ---
        try:
            res = client.permissions.get_permissions()
            print(f"  [PASS] Platform  — permissions.get_permissions() → {type(res).__name__}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Platform  — permissions.get_permissions() → {e}")
            failed += 1

        # --- Wdata API ---
        try:
            res = client.api_health.health_check()
            print(f"  [PASS] Wdata     — api_health.health_check() → {type(res).__name__}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Wdata     — api_health.health_check() → {e}")
            failed += 1

        # --- Chains API ---
        try:
            res = client.workspace.get_workspaces()
            print(f"  [PASS] Chains    — workspace.get_workspaces() → {type(res).__name__}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Chains    — workspace.get_workspaces() → {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"  {passed} passed, {failed} failed")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    print(f"Smoke test — 3 APIs, 1 token\n{'='*50}")
    smoke_test()
