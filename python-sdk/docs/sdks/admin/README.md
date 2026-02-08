# Admin

## Overview

Endpoints to manage organizations, workspaces, groups, and users

### Available Operations

* [assign_organization_user_roles](#assign_organization_user_roles) - Assign roles for an Organization User
* [assign_user_to_organization](#assign_user_to_organization) - Assign existing user to organization
* [assign_workspace_membership_roles](#assign_workspace_membership_roles) - Assign roles for a Workspace Membership
* [create_organization_user](#create_organization_user) - Create a new organization User
* [create_workspace](#create_workspace) - Create a new workspace
* [create_workspace_group](#create_workspace_group) - Create a new group in a workspace
* [create_workspace_membership](#create_workspace_membership) - Create a new workspace membership
* [delete_organization_user_by_id](#delete_organization_user_by_id) - Delete an organization user
* [delete_workspace_group_by_id](#delete_workspace_group_by_id) - Delete a single group
* [delete_workspace_membership_by_id](#delete_workspace_membership_by_id) - Delete a workspace membership
* [get_organization_by_id](#get_organization_by_id) - Retrieve a single organization
* [get_organization_roles](#get_organization_roles) - Retrieve available roles within an organization
* [get_organization_solutions](#get_organization_solutions) - Retrieve available solutions within an organization
* [get_organization_user_by_id](#get_organization_user_by_id) - Retrieve a single user in an organization
* [get_organization_user_role_list](#get_organization_user_role_list) - List Roles assigned to an Organization User
* [get_organization_users](#get_organization_users) - Retrieve list of an organizations users
* [get_organization_workspace_membership_roles](#get_organization_workspace_membership_roles) - Retrieve available roles for a workspace membership
* [get_organization_workspace_roles](#get_organization_workspace_roles) - Retrieve available roles within a workspace
* [get_organizations](#get_organizations) - Retrieve a list of organizations
* [get_workspace_by_id](#get_workspace_by_id) - Retrieve a single workspace
* [get_workspace_group_by_id](#get_workspace_group_by_id) - Retrieve a single group
* [get_workspace_group_members](#get_workspace_group_members) - Retrieve list of group members
* [get_workspace_groups](#get_workspace_groups) - Retrieve list of groups
* [get_workspace_membership_by_id](#get_workspace_membership_by_id) - Retrieve a single workspace membership
* [get_workspace_memberships](#get_workspace_memberships) - Retrieve list of workspace memberships
* [get_workspace_solutions](#get_workspace_solutions) - Retrieve available solutions within a workspace
* [get_workspace_solutions_by_id](#get_workspace_solutions_by_id) - Retrieve a solution by id
* [get_workspaces](#get_workspaces) - Retrieve list of workspaces
* [modify_workspace_group_members](#modify_workspace_group_members) - Modify members in a group
* [partially_update_organization_by_id](#partially_update_organization_by_id) - Update a single organization
* [partially_update_organization_user_by_id](#partially_update_organization_user_by_id) - Partially update a single user in an organization
* [partially_update_workspace_by_id](#partially_update_workspace_by_id) - Update a single workspace
* [partially_update_workspace_group_by_id](#partially_update_workspace_group_by_id) - Update a single group
* [revoke_organization_user_roles](#revoke_organization_user_roles) - Revoke roles for an Organization User
* [revoke_workspace_membership_roles](#revoke_workspace_membership_roles) - Revoke roles for a Workspace Membership
* [workspace_membership_creation_with_options](#workspace_membership_creation_with_options) - Create a new workspace membership with options

## assign_organization_user_roles

Assign a User's roles within an Organization. If one assignment fails, all assignments fail.


### Example Usage

<!-- UsageSnippet language="python" operationID="assignOrganizationUserRoles" method="post" path="/organizations/{organizationId}/users/{userId}/roles/assignment" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.assign_organization_user_roles(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", user_id="<id>", request_body=[
        "3",
        "9",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the user                                   |                                                                     |
| `request_body`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | Editable details about the user's roles.                            | [<br/>"3",<br/>"9"<br/>]                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AssignOrganizationUserRolesResponse](../../models/assignorganizationuserrolesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## assign_user_to_organization

Assign an existing organization user to an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="assignUserToOrganization" method="post" path="/organizations/{organizationId}/users/assignment" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.assign_user_to_organization(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", organization_user_assignment={
        "user": "V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `organization_id`                                                               | *str*                                                                           | :heavy_check_mark:                                                              | The unique identifier of the organization                                       | d6e178fd-4dd5-47e5-9457-68dd64b03655                                            |
| `organization_user_assignment`                                                  | [models.OrganizationUserAssignment](../../models/organizationuserassignment.md) | :heavy_check_mark:                                                              | Configuration options for the assignment                                        |                                                                                 |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.OrganizationUser](../../models/organizationuser.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## assign_workspace_membership_roles

Assign a member's roles within a Workspace. If one assignment fails, all assignments fail.


### Example Usage

<!-- UsageSnippet language="python" operationID="assignWorkspaceMembershipRoles" method="post" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships/{workspaceMembershipId}/roles/assignment" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.assign_workspace_membership_roles(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_membership_id="<id>", request_body=[
        "7e65b8dd-c9ad-4473-a555-86ca6c6cc878",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `workspace_membership_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace membership                   |                                                                     |
| `request_body`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | Editable details about the workspace member's roles.                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AssignWorkspaceMembershipRolesResponse](../../models/assignworkspacemembershiprolesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_organization_user

Creates a new OrganizationUser resource


### Example Usage

<!-- UsageSnippet language="python" operationID="createOrganizationUser" method="post" path="/organizations/{organizationId}/users" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.create_organization_user(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", organization_user={
        "display_name": "John Doe",
        "email": "john.doe@example.com",
        "family_name": "Doe",
        "given_name": "John",
        "username": "john.doe@example.com",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `organization_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the organization                             | d6e178fd-4dd5-47e5-9457-68dd64b03655                                  |
| `organization_user`                                                   | [models.OrganizationUserInput](../../models/organizationuserinput.md) | :heavy_check_mark:                                                    | The properties of the user to create                                  |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.OrganizationUser](../../models/organizationuser.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_workspace

Creates a new workspace resource


### Example Usage

<!-- UsageSnippet language="python" operationID="createWorkspace" method="post" path="/organizations/{organizationId}/workspaces" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.create_workspace(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace={
        "name": "Quarterly Planning",
        "solutions": [
            {
                "id": "60",
                "name": "Connected Global Statutory Reporting (with Entity Management)",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace`                                                         | [models.WorkspaceInput](../../models/workspaceinput.md)             | :heavy_check_mark:                                                  | The properties of the workspace to create                           |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Workspace](../../models/workspace.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_workspace_group

Creates a new group resource


### Example Usage

<!-- UsageSnippet language="python" operationID="createWorkspaceGroup" method="post" path="/organizations/{organizationId}/workspaces/{workspaceId}/groups" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.create_workspace_group(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_group={
        "name": "All Users",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `workspace_group`                                                   | [models.WorkspaceGroupInput](../../models/workspacegroupinput.md)   | :heavy_check_mark:                                                  | The properties of the group to create                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WorkspaceGroup](../../models/workspacegroup.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_workspace_membership

Creates a new `WorkspaceMembership` resource


### Example Usage

<!-- UsageSnippet language="python" operationID="createWorkspaceMembership" method="post" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.create_workspace_membership(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_membership={
        "workspace": {
            "name": "Quarterly Planning",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `organization_id`                                                           | *str*                                                                       | :heavy_check_mark:                                                          | The unique identifier of the organization                                   | d6e178fd-4dd5-47e5-9457-68dd64b03655                                        |
| `workspace_id`                                                              | *str*                                                                       | :heavy_check_mark:                                                          | The unique identifier of the workspace                                      |                                                                             |
| `workspace_membership`                                                      | [models.WorkspaceMembershipInput](../../models/workspacemembershipinput.md) | :heavy_check_mark:                                                          | The properties of the workspace membership to create                        |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.WorkspaceMembership](../../models/workspacemembership.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_organization_user_by_id

Delete a user from an organization


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOrganizationUserById" method="delete" path="/organizations/{organizationId}/users/{userId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.admin.delete_organization_user_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", user_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the user                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_workspace_group_by_id

Deletes a group given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteWorkspaceGroupById" method="delete" path="/organizations/{organizationId}/workspaces/{workspaceId}/groups/{groupId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.admin.delete_workspace_group_by_id(group_id="V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3", organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the group                                  | V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3                    |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_workspace_membership_by_id

Revoke a user's membership to a `Workspace`.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteWorkspaceMembershipById" method="delete" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships/{workspaceMembershipId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.admin.delete_workspace_membership_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_membership_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `workspace_membership_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace membership                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_by_id

Retrieves an organization given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationById" method="get" path="/organizations/{organizationId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_roles

Retrieves available roles within an organization given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationRoles" method="get" path="/organizations/{organizationId}/roles" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_roles(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationRolesListResult](../../models/organizationroleslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_solutions

Retrieves available solutions within an organization given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationSolutions" method="get" path="/organizations/{organizationId}/solutions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_solutions(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationSolutionsListResult](../../models/organizationsolutionslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_user_by_id

Retrieves an organization user given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationUserById" method="get" path="/organizations/{organizationId}/users/{userId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_user_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the user                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationUser](../../models/organizationuser.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_user_role_list

Retrieve a User's roles within an Organization


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationUserRoleList" method="get" path="/organizations/{organizationId}/users/{userId}/roles" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_user_role_list(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the user                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationRolesListResult](../../models/organizationroleslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_users

Retrieve users in an organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationUsers" method="get" path="/organizations/{organizationId}/users" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_users(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `dollar_filter`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The properties to filter the results by.                            |                                                                     |
| `dollar_maxpagesize`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetOrganizationUsersResponse](../../models/getorganizationusersresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_workspace_membership_roles

Retrieves available roles for a workspace membership


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationWorkspaceMembershipRoles" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships/{workspaceMembershipId}/roles" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_workspace_membership_roles(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_membership_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `workspace_membership_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace membership                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WorkspaceMembershipRolesListResult](../../models/workspacemembershiproleslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_workspace_roles

Retrieves available roles within a workspace given an organization and workspace ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationWorkspaceRoles" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/roles" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_organization_workspace_roles(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WorkspaceRolesListResult](../../models/workspaceroleslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organizations

Returns a paginated list of [organizations](ref:admin#organization).
This functionality is only available to Managed Service Provider Applications. Contact your CSM for assistance.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizations" method="get" path="/organizations" -->
```python
from workiva import SDK


with SDK() as sdk:

    res = sdk.admin.get_organizations(request={
        "dollar_next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "wk_service_provider": "<value>",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetOrganizationsRequest](../../models/getorganizationsrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GetOrganizationsResponse](../../models/getorganizationsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_by_id

Retrieves a workspace given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceById" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", dollar_expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `dollar_expand`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Workspace](../../models/workspace.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_group_by_id

Retrieves a group given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceGroupById" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/groups/{groupId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_group_by_id(group_id="V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3", organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", dollar_expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the group                                  | V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3                    |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `dollar_expand`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WorkspaceGroup](../../models/workspacegroup.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_group_members

Retrieve a list of members in a workspace group

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceGroupMembers" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/groups/{groupId}/members" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_group_members(request={
        "dollar_next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "group_id": "V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3",
        "organization_id": "d6e178fd-4dd5-47e5-9457-68dd64b03655",
        "workspace_id": "<id>",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.GetWorkspaceGroupMembersRequest](../../models/getworkspacegroupmembersrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.GetWorkspaceGroupMembersResponse](../../models/getworkspacegroupmembersresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_groups

Retrieve a list of groups in a workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceGroups" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/groups" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_groups(request={
        "dollar_next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "organization_id": "d6e178fd-4dd5-47e5-9457-68dd64b03655",
        "workspace_id": "<id>",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.GetWorkspaceGroupsRequest](../../models/getworkspacegroupsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.GetWorkspaceGroupsResponse](../../models/getworkspacegroupsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_membership_by_id

Retrieves a workspace membership given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceMembershipById" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships/{workspaceMembershipId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_membership_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_membership_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `workspace_membership_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace membership                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WorkspaceMembership](../../models/workspacemembership.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_memberships

Retrieve all memberships of a workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceMemberships" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_memberships(request={
        "dollar_next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "organization_id": "d6e178fd-4dd5-47e5-9457-68dd64b03655",
        "workspace_id": "<id>",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.GetWorkspaceMembershipsRequest](../../models/getworkspacemembershipsrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.GetWorkspaceMembershipsResponse](../../models/getworkspacemembershipsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_solutions

Retrieves available solutions within a workspace given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceSolutions" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/solutions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_solutions(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WorkspaceSolutionsListResult](../../models/workspacesolutionslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspace_solutions_by_id

Retrieve a solutions within a workspace given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceSolutionsByID" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/solutions/{solutionId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspace_solutions_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", solution_id="<id>", workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `solution_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the solution                               |                                                                     |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Solution](../../models/solution.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_workspaces

Retrieve a list of workspaces in an organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaces" method="get" path="/organizations/{organizationId}/workspaces" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.get_workspaces(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", dollar_expand="?$expand=relationships\n", dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `dollar_expand`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `dollar_maxpagesize`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetWorkspacesResponse](../../models/getworkspacesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## modify_workspace_group_members

Add and/or remove members from a group. When failures are encountered for particular members, error responses are returned for each.


### Example Usage

<!-- UsageSnippet language="python" operationID="modifyWorkspaceGroupMembers" method="post" path="/organizations/{organizationId}/workspaces/{workspaceId}/groups/{groupId}/members/modification" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.admin.modify_workspace_group_members(group_id="V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3", organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", bulk_workspace_group_members_modification={
        "to_add": [
            "V0ZVc2VyHzExODjzNzM3NDA",
        ],
        "to_remove": [
            "V0ZVc2VyHzExSDkzMzM1NDC",
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `group_id`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The unique identifier of the group                                                                    | V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3                                                      |
| `organization_id`                                                                                     | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The unique identifier of the organization                                                             | d6e178fd-4dd5-47e5-9457-68dd64b03655                                                                  |
| `workspace_id`                                                                                        | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The unique identifier of the workspace                                                                |                                                                                                       |
| `bulk_workspace_group_members_modification`                                                           | [models.BulkWorkspaceGroupMembersModification](../../models/bulkworkspacegroupmembersmodification.md) | :heavy_check_mark:                                                                                    | Details about the group member modification.                                                          |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_organization_by_id

Updates the properties of an organization.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/name`|`replace`|


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateOrganizationById" method="patch" path="/organizations/{organizationId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.partially_update_organization_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Workiva Inc.",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `organization_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the organization                             | d6e178fd-4dd5-47e5-9457-68dd64b03655                                  |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the organization.        |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_organization_user_by_id

Partially update the properties of a [User](ref:admin#user) within an Organization.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/givenName`|`replace`|
|`/familyName`|`replace`|
|`/displayName`|`replace`|
|`/username`|`replace`|
|`/email`|`replace`|


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateOrganizationUserById" method="patch" path="/organizations/{organizationId}/users/{userId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.partially_update_organization_user_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", user_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/displayName",
            "value": "Smith, Jane",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `organization_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the organization                             | d6e178fd-4dd5-47e5-9457-68dd64b03655                                  |
| `user_id`                                                             | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the user                                     |                                                                       |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | Editable details about the User.                                      |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.OrganizationUser](../../models/organizationuser.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_workspace_by_id

Updates the properties of a workspace.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/name`|`replace`|


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateWorkspaceById" method="patch" path="/organizations/{organizationId}/workspaces/{workspaceId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.partially_update_workspace_by_id(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Legal Entity Reporting",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `organization_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the organization                             | d6e178fd-4dd5-47e5-9457-68dd64b03655                                  |
| `workspace_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the workspace                                |                                                                       |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the workspace.           |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.Workspace](../../models/workspace.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_workspace_group_by_id

Updates the properties of a group.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/name`|`replace`|


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateWorkspaceGroupById" method="patch" path="/organizations/{organizationId}/workspaces/{workspaceId}/groups/{groupId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.partially_update_workspace_group_by_id(group_id="V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3", organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Audit Team",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `group_id`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the group                                    | V0ZHcm91cB5XRkdyb3VwOkFMTF9VU0VSUznxMjD1NTVyNDg3                      |
| `organization_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the organization                             | d6e178fd-4dd5-47e5-9457-68dd64b03655                                  |
| `workspace_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the workspace                                |                                                                       |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the group.               |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.WorkspaceGroup](../../models/workspacegroup.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## revoke_organization_user_roles

Revoke a User's roles within an Organization. If one revocation fails, all revocations fail.


### Example Usage

<!-- UsageSnippet language="python" operationID="revokeOrganizationUserRoles" method="post" path="/organizations/{organizationId}/users/{userId}/roles/revocation" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.revoke_organization_user_roles(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", user_id="<id>", request_body=[
        "3",
        "9",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the user                                   |                                                                     |
| `request_body`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | Editable details about the user's roles.                            | [<br/>"3",<br/>"9"<br/>]                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RevokeOrganizationUserRolesResponse](../../models/revokeorganizationuserrolesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## revoke_workspace_membership_roles

Revoke a member's roles within a Workspace. If one revocation fails, all revocations fail.


### Example Usage

<!-- UsageSnippet language="python" operationID="revokeWorkspaceMembershipRoles" method="post" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships/{workspaceMembershipId}/roles/revocation" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.revoke_workspace_membership_roles(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_membership_id="<id>", request_body=[
        "c22b6a26-a790-48e2-8486-4a7bc82647e2",
        "79ff49b8-93df-499a-8bab-dd0abcad84e7",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace                              |                                                                     |
| `workspace_membership_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the workspace membership                   |                                                                     |
| `request_body`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | Editable details about the workspace member's roles.                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RevokeWorkspaceMembershipRolesResponse](../../models/revokeworkspacemembershiprolesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## workspace_membership_creation_with_options

Creates a new `WorkspaceMembership` and allows control over notification options.


### Example Usage

<!-- UsageSnippet language="python" operationID="workspaceMembershipCreationWithOptions" method="post" path="/organizations/{organizationId}/workspaces/{workspaceId}/memberships/membershipCreation" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.admin.workspace_membership_creation_with_options(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", workspace_id="<id>", workspace_membership_creation={
        "options": {
            "send_welcome_email": True,
        },
        "user": "V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The unique identifier of the organization                                                                        | d6e178fd-4dd5-47e5-9457-68dd64b03655                                                                             |
| `workspace_id`                                                                                                   | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The unique identifier of the workspace                                                                           |                                                                                                                  |
| `workspace_membership_creation`                                                                                  | [models.WorkspaceMembershipCreation](../../models/workspacemembershipcreation.md)                                | :heavy_check_mark:                                                                                               | Details about the workspace membership creation.                                                                 | {<br/>"options": {<br/>"notifyNewMember": false,<br/>"sendWelcomeEmail": true<br/>},<br/>"user": "V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD"<br/>} |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[models.WorkspaceMembership](../../models/workspacemembership.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |