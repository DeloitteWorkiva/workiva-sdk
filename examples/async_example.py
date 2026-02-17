"""Example: Async usage of the Workiva SDK."""

import asyncio

from workiva import Workiva


async def main():
    async with Workiva(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    ) as client:
        # Run multiple API calls concurrently across different APIs
        activities, workspaces, tables = await asyncio.gather(
            client.activities.get_organization_activities_async(),
            client.admin.get_workspaces_async(),
            client.wdata.get_tables_async(),
        )

        print(f"Activities: {activities}")
        for ws in workspaces.data:
            print(f"Workspace: {ws.name} (ID: {ws.id})")
        print(f"Tables: {tables}")


if __name__ == "__main__":
    asyncio.run(main())
