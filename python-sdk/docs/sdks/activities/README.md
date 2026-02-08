# Activities

## Overview

Activities enable you to retrieve a list of actions performed in the organization or a specific workspace, such as: <ul> <li>User logins</li> <li>Added users</li> <li>Changes to roles</li> <li>Changes to organization or workspace settings</li> </ul> These activities are also available in the Workiva platform and can be exported from Organization Admin or Workspace Settings. <br /><br /> To access activities through this API or in Workiva, a user must have a valid admin role: <ul> <li>Org User Admin</li> <li>Org Workspace Admin</li> <li>Org Security Admin, for organization activities</li> <li>Workspace Owner, for workspace activities</li> </ul> Learn more about these roles [here](https://support.workiva.com/hc/en-us/articles/360036006051-Organization-roles) and Workiva activities [here](https://support.workiva.com/hc/en-us/articles/360035646392-View-organization-activities).


### Available Operations

* [get_activity_by_id](#get_activity_by_id) - Retrieve a single activity
* [get_activity_actions](#get_activity_actions) - Retrieve a list of activity actions
* [get_activity_action_by_id](#get_activity_action_by_id) - Retrieve a single activity action
* [get_organization_activities](#get_organization_activities) - Retrieve a list of activities for an organization
* [get_organization_workspace_activities](#get_organization_workspace_activities) - Retrieve a list of activities for a workspace

## get_activity_by_id

Retrieves an activity given its ID.

:::{admonition} Attention
:class: danger
The Workiva Platform does not guarantee that actions taken in the platform will always result in the same Activity ID. Please rely on the ActivityAction `alias` field to determine if an activity is relevant to your use case.
:::


### Example Usage

<!-- UsageSnippet language="python" operationID="getActivityById" method="get" path="/activities/{activityId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_by_id(activity_id="NjE0MjIxODItOTVkYi00YmFjLWI4ZjktNzRkMDg1OTdlMDgwOlFYVmthWFJNYjJjZVFYVmthWFJNYjJjNk5ETXpaamN4TUdVMU5HRTBOR1V5Tm1JeU5ERmtOREJsWXpNMlpHWXhNVFE=")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  | Example                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `activity_id`                                                                                                                                | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | The unique identifier of the activity                                                                                                        | NjE0MjIxODItOTVkYi00YmFjLWI4ZjktNzRkMDg1OTdlMDgwOlFYVmthWFJNYjJjZVFYVmthWFJNYjJjNk5ETXpaamN4TUdVMU5HRTBOR1V5Tm1JeU5ERmtOREJsWXpNMlpHWXhNVFE= |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |                                                                                                                                              |

### Response

**[models.Activity](../../models/activity.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_activity_actions

Retrieves a list of actions performed that may produce activities.

:::{admonition} Attention
:class: danger
The Workiva Platform does not guarantee that actions taken in the platform will always result in the same Activity ID. Please rely on the ActivityAction `alias` field to determine if an activity is relevant to your use case.
:::


### Example Usage

<!-- UsageSnippet language="python" operationID="getActivityActions" method="get" path="/activityActions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_actions(dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `dollar_maxpagesize`                                                                        | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The maximum number of results to retrieve                                                   |                                                                                             |
| `dollar_next`                                                                               | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Pagination cursor for next set of results.                                                  | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                                         |
| `dollar_order_by`                                                                           | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | One or more comma-separated expressions to indicate the order in which to sort the results. |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.GetActivityActionsResponse](../../models/getactivityactionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_activity_action_by_id

Returns an action performed, given its ID

:::{admonition} Attention
:class: danger
The Workiva Platform does not guarantee that actions taken in the platform will always result in the same Activity ID. Please rely on the ActivityAction `alias` field to determine if an activity is relevant to your use case.
:::


### Example Usage

<!-- UsageSnippet language="python" operationID="getActivityActionById" method="get" path="/activityActions/{activityActionId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `activity_action_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the activity action                        | com.workiva.activity.retention_policy.update                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ActivityAction](../../models/activityaction.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_activities

Returns a paginated list of activities for a given organization.

:::{admonition} Attention
:class: danger
The Workiva Platform does not guarantee that actions taken in the platform will always result in the same Activity ID. Please rely on the ActivityAction `alias` field to determine if an activity is relevant to your use case.
:::


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationActivities" method="get" path="/organizations/{organizationId}/activities" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_organization_activities(request={
        "organization_id": "d6e178fd-4dd5-47e5-9457-68dd64b03655",
        "dollar_next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.GetOrganizationActivitiesRequest](../../models/getorganizationactivitiesrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.GetOrganizationActivitiesResponse](../../models/getorganizationactivitiesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_organization_workspace_activities

Returns a paginated list of activities for a given organization and workspace.

:::{admonition} Attention
:class: danger
The Workiva Platform does not guarantee that actions taken in the platform will always result in the same Activity ID. Please rely on the ActivityAction `alias` field to determine if an activity is relevant to your use case.
:::


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationWorkspaceActivities" method="get" path="/organizations/{organizationId}/workspaces/{workspaceId}/activities" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_organization_workspace_activities(request={
        "organization_id": "d6e178fd-4dd5-47e5-9457-68dd64b03655",
        "workspace_id": "<id>",
        "dollar_next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.GetOrganizationWorkspaceActivitiesRequest](../../models/getorganizationworkspaceactivitiesrequest.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.GetOrganizationWorkspaceActivitiesResponse](../../models/getorganizationworkspaceactivitiesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |