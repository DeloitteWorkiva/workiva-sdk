# Tasks

## Overview

Tasks enable users to manage projects, organize responsibilities, and meet deadlines in the Workiva platform. Use these endpoints to create and manage tasks.


### Available Operations

* [create_task](#create_task) - Create a new task
* [delete_task_by_id](#delete_task_by_id) - Delete a single task
* [get_task_by_id](#get_task_by_id) - Retrieve a single task
* [get_tasks](#get_tasks) - Retrieve a list of tasks
* [partially_update_task_by_id](#partially_update_task_by_id) - Partially update a single task
* [submit_task_action](#submit_task_action) - Initiate a task action submission

## create_task

Creates a new [task](ref:tasks#task) given its properties.


### Example Usage

<!-- UsageSnippet language="python" operationID="createTask" method="post" path="/tasks" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.tasks.create_task(request={
        "approval_steps": [
            {
                "completion_mode": models.CompletionMode.ONE,
                "participants": [
                    {
                        "id": "V0ZVc2VyHzU1MDg3OTc0MDE4MDg4OTY",
                        "type": models.TaskUserType.USER,
                    },
                    {
                        "id": "V0ZVc2VyHzU1MDg3OTc0MDE4MDg4OTY",
                        "type": models.TaskUserType.USER,
                    },
                ],
            },
        ],
        "assignees": [
            {
                "id": "V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD",
                "type": models.TaskUserType.USER,
            },
        ],
        "description": "Review document for spelling and grammar",
        "location": {
            "resource": "124efa2a142f472ba1ceab34ed18915f",
            "segment": "465ttdh2a142y75ehsft5ab34edf5675",
        },
        "title": "Review Document",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TaskInput](../../models/taskinput.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Task](../../models/task.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_task_by_id

Deletes a [task](ref:tasks#task) given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteTaskById" method="delete" path="/tasks/{taskId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.tasks.delete_task_by_id(task_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the task                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_task_by_id

Retrieves a [task](ref:tasks#task) given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getTaskById" method="get" path="/tasks/{taskId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.tasks.get_task_by_id(task_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the task                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Task](../../models/task.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_tasks

> Returns a paginated list of [tasks](ref:tasks#task). Currently this endpoint returns general tasks
(such as those created as part of editing documents, sheets, and presentations) and tasks that have been associated  with a Sustainability Program.
It does not return tasks created as part of a process.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTasks" method="get" path="/tasks" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.tasks.get_tasks(dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `dollar_filter`                                                                             | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The properties to filter the results by.                                                    |                                                                                             |
| `dollar_maxpagesize`                                                                        | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The maximum number of results to retrieve                                                   |                                                                                             |
| `dollar_next`                                                                               | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Pagination cursor for next set of results.                                                  | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                                         |
| `dollar_order_by`                                                                           | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | One or more comma-separated expressions to indicate the order in which to sort the results. |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.GetTasksResponse](../../models/gettasksresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_task_by_id

Partially updates the properties of a [task](ref:tasks#task).
Please note: Tasks are automatically restarted when the following properties are updated:
- `assignees`
- `approvalSteps`: If any `participants` who have already approved are updated, the task will be restarted.
- `location`
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/approvalSteps`|`replace`|
|`/assignees`|`replace`|
|`/description`|`replace`|
|`/dueDate`|`replace`|
|`/location`|`replace`|
|`/owner`|`replace`|
|`/title`|`replace`|


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateTaskById" method="patch" path="/tasks/{taskId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.tasks.partially_update_task_by_id(task_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/title",
            "value": "New Title",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `task_id`                                                             | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the task                                     |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the task.                |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Task](../../models/task.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## submit_task_action

This endpoint enables submitting actions on a [task](ref:tasks#task). For tasks with multiple approval steps, it's the only way to advance a task through the approval process.


### Example Usage

<!-- UsageSnippet language="python" operationID="submitTaskAction" method="post" path="/tasks/{taskId}/actionSubmission" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.tasks.submit_task_action(task_id="<id>", task_action={
        "action": models.TaskActionAction.APPROVE,
        "comment": "Data confirmed",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the task                                   |
| `task_action`                                                       | [models.TaskAction](../../models/taskaction.md)                     | :heavy_check_mark:                                                  | The action to be applied on the task.                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Task](../../models/task.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |