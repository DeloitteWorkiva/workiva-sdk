# Milestones

## Overview

Endpoints for working with Milestones. See [**Introduction to Milestones Endpoints**](ref:milestones-guide) for more information.

### Available Operations

* [milestone_creation](#milestone_creation) - Initiates a request to create a new milestone
* [get_milestone_by_id](#get_milestone_by_id) - Retrieve a milestone by id
* [delete_milestone_by_id](#delete_milestone_by_id) - Deletes a milestone
* [partially_update_milestone_by_id](#partially_update_milestone_by_id) - Partially updates a milestone

## milestone_creation

Create a new [`Milestone`](ref:milestones#milestone) using a [`MilestoneCreation`](ref:milestones#milestonecreation) request. This is a long running operation. Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the creation completes, its status will be `completed`, and the response body includes a `resourceURL`. To GET the new milestone, perform a GET on the `resourceURL` with the same authentication credentials and flow as the initial request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="milestoneCreation" method="post" path="/milestones/creation" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.milestones.milestone_creation(request={
        "type": models.MilestoneResourceType.DOCUMENT,
        "document": "16b1f641613847469b7aa1ca29af40b1",
        "presentation": "16b1f641613847469b7aa1ca29af40b1",
        "spreadsheet": "16b1f641613847469b7aa1ca29af40b1",
        "title": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MilestoneCreation](../../models/milestonecreation.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MilestoneCreationResponse](../../models/milestonecreationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 401, 403        | application/json     |
| errors.ErrorResponse | 500                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## get_milestone_by_id

Returns a [`Milestone`](ref:milestones#milestone) given its id

### Example Usage

<!-- UsageSnippet language="python" operationID="getMilestoneById" method="get" path="/milestones/{milestoneId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.milestones.get_milestone_by_id(milestone_id="WW91IGZvdW5kIG1d5kIGSd2lIQ")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `milestone_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of a milestone.                               | WW91IGZvdW5kIG1d5kIGSd2lIQ                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Milestone](../../models/milestone.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_milestone_by_id

Deletes the [`Milestone`](ref:milestones#milestone) with a given id.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMilestoneById" method="delete" path="/milestones/{milestoneId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.milestones.delete_milestone_by_id(milestone_id="WW91IGZvdW5kIG1d5kIGSd2lIQ")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `milestone_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of a milestone.                               | WW91IGZvdW5kIG1d5kIGSd2lIQ                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 401, 403, 404   | application/json     |
| errors.ErrorResponse | 500                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## partially_update_milestone_by_id

Partially updates a [`Milestone`](ref:milestones#milestone) with a given id.

### Options
| Path                   | PATCH Operations Supported         | Value Type             |
|------------------------|------------------------------------|------------------------|
| `/title`               | `replace`                          | `string`               |
| `/remarks`             | `replace`                          | `string`, `null`       |


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateMilestoneById" method="patch" path="/milestones/{milestoneId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.milestones.partially_update_milestone_by_id(milestone_id="WW91IGZvdW5kIG1d5kIGSd2lIQ", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "New name",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `milestone_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of a milestone.                                 | WW91IGZvdW5kIG1d5kIGSd2lIQ                                            |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | The batch of JSON patch operations to apply                           |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.Milestone](../../models/milestone.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 401, 403, 404   | application/json     |
| errors.ErrorResponse | 500                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |