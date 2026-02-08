"""Example: Async usage of the Workiva SDK."""

import asyncio
from workiva import SDK


TOKEN = "YOUR_BEARER_TOKEN_HERE"


async def main():
    async with SDK(oauth=TOKEN) as sdk:
        # Run multiple API calls concurrently across different APIs
        activities, workspaces, tables = await asyncio.gather(
            sdk.activities.get_organization_activities_async(),
            sdk.admin.get_workspaces_async(),
            sdk.wdata.get_tables_async(),
        )

        print(f"Activities: {activities}")
        print(f"Workspaces: {workspaces}")
        print(f"Tables: {tables}")


if __name__ == "__main__":
    asyncio.run(main())
