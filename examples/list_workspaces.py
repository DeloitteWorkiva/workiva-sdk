"""Example: List workspaces and recent activities using the Workiva SDK."""

from workiva._hooks.client import Workiva


def main():
    with Workiva(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    ) as client:
        # --- Platform API (api.app.wdesk.com) ---
        activities = client.activities.get_organization_activities()
        print(f"Activities: {activities}")

        workspaces = client.admin.get_workspaces()
        print(f"Workspaces: {workspaces}")

        # --- Wdata API (h.app.wdesk.com/s/wdata/prep) ---
        tables = client.wdata.get_tables()
        print(f"Tables: {tables}")

        # --- Chains API (h.app.wdesk.com/s/wdata/oc/api) ---
        chains = client.chains.get_chains()
        print(f"Chains: {chains}")


if __name__ == "__main__":
    main()
