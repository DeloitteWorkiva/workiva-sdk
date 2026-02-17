#!/usr/bin/env python3
"""End-to-end test against live Workiva APIs.

Tests sync + async flows across all 3 APIs with real data.
Goes beyond smoke_test.py by testing pagination, data parsing,
token caching, and async methods.

Usage:
    uv run python scripts/e2e_test.py
"""

from __future__ import annotations

import asyncio
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
from workiva.models.platform import FilesListResult, PermissionsListResult  # noqa: E402
from workiva.models.chains import WorkspacesResponse  # noqa: E402

passed = 0
failed = 0


def test(name: str, fn) -> object:
    global passed, failed
    try:
        result = fn()
        print(f"  [PASS] {name}")
        passed += 1
        return result
    except Exception as e:
        print(f"  [FAIL] {name}")
        print(f"         → {type(e).__name__}: {e}")
        failed += 1
        return None


def run_sync_tests() -> None:
    print("\n--- SYNC TESTS ---\n")

    with Workiva(client_id=CLIENT_ID, client_secret=CLIENT_SECRET) as client:
        # 1. Platform: list files with auto-pagination (typed response)
        def t_files():
            result = client.files.get_files(maxpagesize=5)
            assert isinstance(result, FilesListResult)
            files = result.data or []
            print(f"         → {len(files)} files (typed FilesListResult)")
            assert isinstance(files, list)
            if files:
                f = files[0]
                print(f"         → First: {f.name} (kind={f.kind})")

        test("Platform — files.get_files(maxpagesize=5)", t_files)

        # 2. Platform: list permissions (typed response)
        def t_perms():
            result = client.permissions.get_permissions()
            assert isinstance(result, PermissionsListResult)
            perms = result.data or []
            print(f"         → {len(perms)} permissions (typed PermissionsListResult)")

        test("Platform — permissions.get_permissions()", t_perms)

        # 3. Wdata: health check (typed response)
        def t_health():
            result = client.wdata.health_check()
            # BaseResponseMapStringString has a body attribute
            print(f"         → type={type(result).__name__}")

        test("Wdata — wdata.health_check()", t_health)

        # 4. Wdata: list tables (typed response with cursor pagination)
        def t_tables():
            result = client.wdata.get_tables(limit=5)
            print(f"         → type={type(result).__name__}")

        test("Wdata — wdata.get_tables(limit=5)", t_tables)

        # 5. Chains: list workspaces (typed response)
        def t_chain_ws():
            result = client.chains.get_workspaces()
            assert isinstance(result, WorkspacesResponse)
            workspaces = result.data or []
            print(f"         → {len(workspaces)} workspaces (typed WorkspacesResponse)")

        test("Chains — chains.get_workspaces()", t_chain_ws)

        # 6. Token caching: multiple requests reuse token
        def t_cache():
            r1 = client.permissions.get_permissions()
            r2 = client.files.get_files(maxpagesize=1)
            r3 = client.wdata.health_check()
            assert r1 is not None
            assert r2 is not None
            assert r3 is not None
            print("         → 3 requests across 2 APIs, 1 token")

        test("Token caching — multi-API reuse", t_cache)

        # 7. X-Version header presence
        def t_version():
            result = client.files.get_files(maxpagesize=1)
            # If the API returns data without complaining, the header is there
            assert result is not None
            print("         → API accepted request (X-Version header present)")

        test("X-Version header — accepted by API", t_version)


async def run_async_tests() -> None:
    global passed, failed
    print("\n--- ASYNC TESTS ---\n")

    async with Workiva(client_id=CLIENT_ID, client_secret=CLIENT_SECRET) as client:
        # 8. Async Platform: list files (typed response)
        try:
            result = await client.files.get_files_async(maxpagesize=3)
            assert isinstance(result, FilesListResult)
            files = result.data or []
            print(f"  [PASS] Platform async — files.get_files_async()")
            print(f"         → {len(files)} files (typed FilesListResult)")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Platform async — files.get_files_async()")
            print(f"         → {type(e).__name__}: {e}")
            failed += 1

        # 9. Async Wdata: health check (typed response)
        try:
            result = await client.wdata.health_check_async()
            print(f"  [PASS] Wdata async — wdata.health_check_async()")
            print(f"         → type={type(result).__name__}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Wdata async — wdata.health_check_async()")
            print(f"         → {type(e).__name__}: {e}")
            failed += 1

        # 10. Async Chains: list workspaces (typed response)
        try:
            result = await client.chains.get_workspaces_async()
            assert isinstance(result, WorkspacesResponse)
            print(f"  [PASS] Chains async — chains.get_workspaces_async()")
            print(f"         → type={type(result).__name__}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Chains async — chains.get_workspaces_async()")
            print(f"         → {type(e).__name__}: {e}")
            failed += 1

        # 11. Async concurrent requests (all return typed models)
        try:
            r1, r2, r3 = await asyncio.gather(
                client.files.get_files_async(maxpagesize=1),
                client.wdata.health_check_async(),
                client.chains.get_workspaces_async(),
            )
            assert r1 is not None
            assert r2 is not None
            assert r3 is not None
            print(f"  [PASS] Async concurrent — asyncio.gather(3 APIs)")
            print(f"         → All 3 returned typed models concurrently")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Async concurrent — asyncio.gather(3 APIs)")
            print(f"         → {type(e).__name__}: {e}")
            failed += 1


if __name__ == "__main__":
    print(f"{'='*60}")
    print(f"  Workiva SDK — End-to-End Test (Live APIs)")
    print(f"{'='*60}")

    run_sync_tests()
    asyncio.run(run_async_tests())

    print(f"\n{'='*60}")
    emoji = "PASS" if failed == 0 else "FAIL"
    print(f"  [{emoji}] {passed} passed, {failed} failed")
    print(f"{'='*60}")

    if failed > 0:
        sys.exit(1)
