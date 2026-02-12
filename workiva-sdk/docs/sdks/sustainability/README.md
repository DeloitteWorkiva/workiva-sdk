# Sustainability

## Overview

Endpoints to manage Sustainability Programs

### Available Operations

* [get_programs](#get_programs) - Retrieve a list of programs
* [create_program](#create_program) - Create a new program
* [get_program_by_id](#get_program_by_id) - Retrieve a single program
* [partially_update_program_by_id](#partially_update_program_by_id) - Partially update a single program
* [get_dimensions](#get_dimensions) - Retrieve a list of dimensions
* [create_dimension](#create_dimension) - Create a new dimension
* [get_dimension_by_id](#get_dimension_by_id) - Retrieve a single dimension
* [partially_update_dimension_by_id](#partially_update_dimension_by_id) - Partially update a single dimension
* [get_metrics](#get_metrics) - Retrieve a list of metrics
* [create_metric](#create_metric) - Create a new metric
* [delete_metric_by_id](#delete_metric_by_id) - Delete a single metric
* [get_metric_by_id](#get_metric_by_id) - Retrieve a single metric
* [partially_update_metric_by_id](#partially_update_metric_by_id) - Partially update a single metric
* [get_values](#get_values) - Retrieve a list of metric values
* [create_value](#create_value) - Create a new metric value
* [delete_metric_value_by_id](#delete_metric_value_by_id) - Delete a single metric value
* [get_metric_value_by_id](#get_metric_value_by_id) - Retrieve a single metric value
* [partially_update_metric_value_by_id](#partially_update_metric_value_by_id) - Partially update a single metric value
* [batch_deletion_metric_values](#batch_deletion_metric_values) - Initiate a batch deletion of metric values
* [batch_upsertion_metric_values](#batch_upsertion_metric_values) - Initiate a batch upsertion of metric values
* [get_program_permissions](#get_program_permissions) - Retrieve permissions for a program
* [program_permissions_modification](#program_permissions_modification) - Modify permissions on a program
* [get_topics](#get_topics) - Retrieve a list of topics
* [create_topic](#create_topic) - Create a new topic
* [delete_topic_by_id](#delete_topic_by_id) - Delete a single topic
* [get_topic_by_id](#get_topic_by_id) - Retrieve a single topic
* [partially_update_topic_by_id](#partially_update_topic_by_id) - Partially update a single topic

## get_programs

Returns a paginated list of [programs](ref:sustainability#program).

### Example Usage

<!-- UsageSnippet language="python" operationID="getPrograms" method="get" path="/programs" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_programs(maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `maxpagesize`                                                                               | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The maximum number of results to retrieve                                                   |                                                                                             |
| `next`                                                                                      | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Pagination cursor for next set of results.                                                  | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                                         |
| `order_by`                                                                                  | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | One or more comma-separated expressions to indicate the order in which to sort the results. |                                                                                             |
| `filter_`                                                                                   | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The properties to filter the results by.                                                    |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.GetProgramsResponse](../../models/getprogramsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_program

Creates a new [program](ref:sustainability#program).


### Example Usage

<!-- UsageSnippet language="python" operationID="createProgram" method="post" path="/programs" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.create_program(request={
        "name": "Sustainability Program",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ProgramInput](../../models/programinput.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Program](../../models/program.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_program_by_id

Retrieves a [program](ref:sustainability#program) given its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="getProgramById" method="get" path="/programs/{programId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_program_by_id(program_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Program](../../models/program.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_program_by_id

Partially updates the properties of a [program](ref:sustainability#program). Only one property may be updated at a time.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/name`|`replace`, `test`|


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateProgramById" method="patch" path="/programs/{programId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_program_by_id(program_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "New name",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="partiallyUpdateProgramById" method="patch" path="/programs/{programId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_program_by_id(program_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Sustainability Program Draft",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `program_id`                                                                                                                                   | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | The unique identifier of the program                                                                                                           |
| `request_body`                                                                                                                                 | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]                                                                          | :heavy_check_mark:                                                                                                                             | A collection of patch operations to apply to the [program](ref:sustainability#program). Currently only one operation may be applied at a time. |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[models.Program](../../models/program.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_dimensions

Returns a paginated list of [dimensions](ref:sustainability#dimension).

### Example Usage

<!-- UsageSnippet language="python" operationID="getDimensions" method="get" path="/programs/{programId}/dimensions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_dimensions(request={
        "program_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetDimensionsRequest](../../models/getdimensionsrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDimensionsResponse](../../models/getdimensionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_dimension

Creates a new [dimension](ref:sustainability#dimension).


### Example Usage

<!-- UsageSnippet language="python" operationID="createDimension" method="post" path="/programs/{programId}/dimensions" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.create_dimension(program_id="<id>", dimension={
        "name": "Facility",
        "values": [
            {
                "id": "Ames, IA",
                "name": "Ames, Iowa",
            },
            {
                "id": "Portland, OR",
                "name": "Portland, Oregon",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            | Example                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `program_id`                                                                                                                                           | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | The unique identifier of the program                                                                                                                   |                                                                                                                                                        |
| `dimension`                                                                                                                                            | [models.DimensionInput](../../models/dimensioninput.md)                                                                                                | :heavy_check_mark:                                                                                                                                     | The properties of the dimension to create                                                                                                              | {<br/>"active": true,<br/>"name": "Facility",<br/>"values": [<br/>{<br/>"id": "Ames, IA",<br/>"name": "Ames, Iowa"<br/>},<br/>{<br/>"id": "Portland, OR",<br/>"name": "Portland, Oregon"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.Dimension](../../models/dimension.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_dimension_by_id

Retrieves a [dimension](ref:sustainability#dimension) given its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="getDimensionById" method="get" path="/programs/{programId}/dimensions/{dimensionId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_dimension_by_id(program_id="<id>", dimension_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `dimension_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the dimension                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Dimension](../../models/dimension.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_dimension_by_id

Partially updates the properties of a [dimension](ref:sustainability#dimension). Only one property may be updated at a time.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/active`|`replace`, `test`|
|`/name`|`replace`, `test`|
|`/values`|`replace`, `test`|


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateDimensionById" method="patch" path="/programs/{programId}/dimensions/{dimensionId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_dimension_by_id(program_id="<id>", dimension_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "New name",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="partiallyUpdateDimensionById" method="patch" path="/programs/{programId}/dimensions/{dimensionId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_dimension_by_id(program_id="<id>", dimension_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Updated Facility",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `program_id`                                                                                                                                       | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | The unique identifier of the program                                                                                                               |
| `dimension_id`                                                                                                                                     | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | The unique identifier of the dimension                                                                                                             |
| `request_body`                                                                                                                                     | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]                                                                              | :heavy_check_mark:                                                                                                                                 | A collection of patch operations to apply to the [dimension](ref:sustainability#dimension). Currently only one operation may be applied at a time. |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.Dimension](../../models/dimension.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_metrics

Returns a paginated list of [Metrics](ref:sustainability#metric).

### Example Usage

<!-- UsageSnippet language="python" operationID="getMetrics" method="get" path="/programs/{programId}/metrics" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_metrics(request={
        "program_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetMetricsRequest](../../models/getmetricsrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetMetricsResponse](../../models/getmetricsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_metric

Creates a new [metric](ref:sustainability#metric).


### Example Usage

<!-- UsageSnippet language="python" operationID="createMetric" method="post" path="/programs/{programId}/metrics" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.create_metric(program_id="<id>", metric={
        "code": 12,
        "description": "Covers all direct greenhouse gas emissions from sources owned or controlled by the reporting entity.",
        "id": "ae82b647-8e43-44c3-a4e7-2aa3294c87ac",
        "index": 0,
        "name": "Scope 1 Consolidated GHG Emissions",
        "topic": "cc507098-c403-4b8b-98b4-31a6c5a639f4",
        "unit": "Metric Ton",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `program_id`                                                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                     | The unique identifier of the program                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| `metric`                                                                                                                                                                                                                                                                                                                                                                                               | [models.MetricInput](../../models/metricinput.md)                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                     | The properties of the metric to create                                                                                                                                                                                                                                                                                                                                                                 | {<br/>"code": 12,<br/>"dataType": "text",<br/>"description": "Covers all direct greenhouse gas emissions from sources owned or controlled by the reporting entity.",<br/>"id": "ae82b647-8e43-44c3-a4e7-2aa3294c87ac",<br/>"index": 0,<br/>"name": "Scope 1 Consolidated GHG Emissions",<br/>"requireNotes": false,<br/>"requireSupportingAttachments": false,<br/>"topic": "cc507098-c403-4b8b-98b4-31a6c5a639f4",<br/>"unit": "Metric Ton"<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.Metric](../../models/metric.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_metric_by_id

Deletes a [metric](ref:sustainability#metric) given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMetricById" method="delete" path="/programs/{programId}/metrics/{metricId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.sustainability.delete_metric_by_id(program_id="<id>", metric_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `metric_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the metric                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_metric_by_id

Retrieves a [`Metric`](ref:sustainability#metric) given its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="getMetricById" method="get" path="/programs/{programId}/metrics/{metricId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_metric_by_id(program_id="<id>", metric_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `metric_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the metric                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Metric](../../models/metric.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_metric_by_id

Partially updates the properties of a [metric](ref:sustainability#metric). Only one property may be updated at a time.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/datatype`|`replace`|
|`/description`|`replace`, `test`|
|`/index`|`replace`, `test`|
|`/name`|`replace`, `test`|
|`/requireNotes`|`replace`, `test`|
|`/requireSupportingAttachments`|`replace`, `test`|
|`/topic`|`replace`, `test`|
|`/unit`|`replace`, `test`|


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateMetricById" method="patch" path="/programs/{programId}/metrics/{metricId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_metric_by_id(program_id="<id>", metric_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "New name",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: replaceName

<!-- UsageSnippet language="python" operationID="partiallyUpdateMetricById" method="patch" path="/programs/{programId}/metrics/{metricId}" example="replaceName" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_metric_by_id(program_id="<id>", metric_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Scope 1 Consolidated GHG Emissions",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `program_id`                                                                                                                                 | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | The unique identifier of the program                                                                                                         |
| `metric_id`                                                                                                                                  | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | The unique identifier of the metric                                                                                                          |
| `request_body`                                                                                                                               | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]                                                                        | :heavy_check_mark:                                                                                                                           | A collection of patch operations to apply to the [metric](ref:sustainability#metric). Currently only one operation may be applied at a time. |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.Metric](../../models/metric.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_values

Returns a paginated list of [metric Values](ref:sustainability#metricvalue)

### Example Usage

<!-- UsageSnippet language="python" operationID="getValues" method="get" path="/programs/{programId}/metrics/{metricId}/values" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_values(request={
        "program_id": "<id>",
        "metric_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetValuesRequest](../../models/getvaluesrequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetValuesResponse](../../models/getvaluesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_value

Creates a new [metric value](ref:sustainability#metricvalue)


### Example Usage

<!-- UsageSnippet language="python" operationID="createValue" method="post" path="/programs/{programId}/metrics/{metricId}/values" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.create_value(program_id="<id>", metric_id="<id>", metric_value={
        "coordinates": {
            "b38353ce-32bc-4ea7-852a-bf5e12b72d95": "Ames, IA",
        },
        "data_source": {
            "spreadsheet_cell_connection": {
                "cell": "A1",
                "sheet": "576696e0f7a143b4a0bc7c20a34480ab",
                "spreadsheet": "7a5e271acf1d49d480a6fbabc394a0fa",
            },
        },
        "fields_to_clear": [
            "notes",
        ],
        "id": "bf9aa2c3-f278-4c77-8acb-97584e843dcd",
        "notes": "metric value notes",
        "reporting_period": {
            "end": 12,
            "start": 1,
            "year": 2024,
        },
        "status": models.MetricValueStatus.COMPLETE,
        "value": "512.8768743",
        "task": "VGFMDU1MmJiOGEwZDVjZWYzNDlVhZDWU5Y2jYzY3zax5iMg",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `metric_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the metric                                 |
| `metric_value`                                                      | [models.MetricValueInput](../../models/metricvalueinput.md)         | :heavy_check_mark:                                                  | The properties of the metric value to create                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricValue](../../models/metricvalue.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_metric_value_by_id

Deletes a [metric value](ref:sustainability#metricvalue) value given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMetricValueById" method="delete" path="/programs/{programId}/metrics/{metricId}/values/{metricValueId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.sustainability.delete_metric_value_by_id(program_id="<id>", metric_id="<id>", metric_value_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `metric_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the metric                                 |
| `metric_value_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the value                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_metric_value_by_id

Retrieves a [metric value](ref:sustainability#metricvalue) value given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getMetricValueById" method="get" path="/programs/{programId}/metrics/{metricId}/values/{metricValueId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_metric_value_by_id(program_id="<id>", metric_id="<id>", metric_value_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `metric_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the metric                                 |
| `metric_value_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the value                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricValue](../../models/metricvalue.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_metric_value_by_id

Partially updates the properties of a [metric value](ref:sustainability#metricvalue) value. Only one property may be updated at a time.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/notes`|`replace`, `test`|
|`/value`|`replace`, `test`|


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateMetricValueById" method="patch" path="/programs/{programId}/metrics/{metricId}/values/{metricValueId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_metric_value_by_id(program_id="<id>", metric_id="<id>", metric_value_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "New name",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: replaceName

<!-- UsageSnippet language="python" operationID="partiallyUpdateMetricValueById" method="patch" path="/programs/{programId}/metrics/{metricId}/values/{metricValueId}" example="replaceName" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_metric_value_by_id(program_id="<id>", metric_id="<id>", metric_value_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/notes",
            "value": "Updated notes",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `program_id`                                                                                                          | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | The unique identifier of the program                                                                                  |
| `metric_id`                                                                                                           | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | The unique identifier of the metric                                                                                   |
| `metric_value_id`                                                                                                     | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | The unique identifier of the value                                                                                    |
| `request_body`                                                                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]                                                 | :heavy_check_mark:                                                                                                    | A collection of patch operations to apply to the metric value. Currently only one operation may be applied at a time. |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.MetricValue](../../models/metricvalue.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## batch_deletion_metric_values

Batch delete the given metric values.

For each value, provide either the id or both the reportingPeriod and coordinates (if any).
If both are provided, the given id will be used.


### Example Usage

<!-- UsageSnippet language="python" operationID="batchDeletionMetricValues" method="post" path="/programs/{programId}/metrics/{metricId}/values/batchDeletion" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.sustainability.batch_deletion_metric_values(program_id="<id>", metric_id="<id>", metric_value_identifier={
        "data": [
            {
                "coordinates": {
                    "b38353ce-32bc-4ea7-852a-bf5e12b72d95": "Ames, IA",
                },
                "reporting_period": {
                    "end": 12,
                    "start": 1,
                    "year": 2024,
                },
            },
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `program_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the program                                  |
| `metric_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the metric                                   |
| `metric_value_identifier`                                             | [models.MetricValueIdentifier](../../models/metricvalueidentifier.md) | :heavy_check_mark:                                                    | The metric values to delete                                           |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## batch_upsertion_metric_values

Batch upsert values for the given metric. The payload is limited to 10MB; break it into multiple requests if necessary.

For each value, provide either the id or both the reportingPeriod and coordinates (if any).
If both are provided, the given id will be used.

The API will validate the request and return a 202 Accepted status.
However, the operation will be processed asynchronously, so the values may take some time to appear in the system.
Poll the location provided in the Location header to check the status of the operation.

If any of the values fail to be processed, no changes will be stored in the system.


### Example Usage

<!-- UsageSnippet language="python" operationID="batchUpsertionMetricValues" method="post" path="/programs/{programId}/metrics/{metricId}/values/batchUpsertion" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.batch_upsertion_metric_values(program_id="<id>", metric_id="<id>", metric_value_upsertion={
        "data": [
            {
                "coordinates": {
                    "b38353ce-32bc-4ea7-852a-bf5e12b72d95": "Ames, IA",
                },
                "data_source": {
                    "spreadsheet_cell_connection": {
                        "cell": "A1",
                        "sheet": "576696e0f7a143b4a0bc7c20a34480ab",
                        "spreadsheet": "7a5e271acf1d49d480a6fbabc394a0fa",
                    },
                },
                "fields_to_clear": [
                    "notes",
                ],
                "id": "bf9aa2c3-f278-4c77-8acb-97584e843dcd",
                "notes": "metric value notes",
                "reporting_period": {
                    "end": 12,
                    "start": 1,
                    "year": 2024,
                },
                "status": models.MetricValueStatus.COMPLETE,
                "value": "512.8768743",
                "task": "VGFMDU1MmJiOGEwZDVjZWYzNDlVhZDWU5Y2jYzY3zax5iMg",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `metric_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the metric                                 |
| `metric_value_upsertion`                                            | [models.MetricValueUpsertion](../../models/metricvalueupsertion.md) | :heavy_check_mark:                                                  | The metric values to upsert                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatchUpsertionMetricValuesResponse](../../models/batchupsertionmetricvaluesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_program_permissions

Retrieves a paginated list of permissions for a given Sustainability Program


### Example Usage

<!-- UsageSnippet language="python" operationID="getProgramPermissions" method="get" path="/programs/{programId}/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_program_permissions(program_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |                                                                     |
| `filter_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The properties to filter the results by.                            |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetProgramPermissionsResponse](../../models/getprogrampermissionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## program_permissions_modification

Assign and/or revoke permissions on a Sustainability Program. If any modification in a request fails, all modifications on that request fail. <br /><br /> _To modify an existing permission, the existing permission must first be  explicitly revoked. Then, the new permission needs to be assigned. This  can be done in a single request by sending `toAssign` and `toRevoke` in  the request body._


### Example Usage

<!-- UsageSnippet language="python" operationID="programPermissionsModification" method="post" path="/programs/{programId}/permissions/modification" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.sustainability.program_permissions_modification(program_id="<id>", resource_permissions_modification={
        "to_assign": [
            {
                "permission": "598e8fa3-3e7c-4fb7-b662-f44522216e2b",
                "principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg",
            },
        ],
        "to_revoke": [
            {
                "permission": "85aa87ee-beb9-4417-8fa0-420e9de63534",
                "principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg",
            },
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `program_id`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the program                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                        |
| `resource_permissions_modification`                                                                                                                                                                                                                    | [models.ResourcePermissionsModification](../../models/resourcepermissionsmodification.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                     | Details about the Sustainability Program permissions modification.                                                                                                                                                                                     | {<br/>"toAssign": [<br/>{<br/>"permission": "598e8fa3-3e7c-4fb7-b662-f44522216e2b",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>],<br/>"toRevoke": [<br/>{<br/>"permission": "85aa87ee-beb9-4417-8fa0-420e9de63534",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_topics

Returns a paginated list of [topics](ref:sustainability#topic).

### Example Usage

<!-- UsageSnippet language="python" operationID="getTopics" method="get" path="/programs/{programId}/topics" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_topics(request={
        "program_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetTopicsRequest](../../models/gettopicsrequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTopicsResponse](../../models/gettopicsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_topic

Creates a new [topic](ref:sustainability#topic).


### Example Usage

<!-- UsageSnippet language="python" operationID="createTopic" method="post" path="/programs/{programId}/topics" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.create_topic(program_id="<id>", topic={
        "index": 0,
        "name": "Climate",
        "parent": "82bae647-8e43-44c3-a4e7-2aa3294c87ac",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `program_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | The unique identifier of the program                                                |                                                                                     |
| `topic`                                                                             | [models.TopicInput](../../models/topicinput.md)                                     | :heavy_check_mark:                                                                  | The properties of the topic to create                                               | {<br/>"index": 0,<br/>"name": "Climate",<br/>"parent": "82bae647-8e43-44c3-a4e7-2aa3294c87ac"<br/>} |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.Topic](../../models/topic.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_topic_by_id

Deletes a [topic](ref:sustainability#topic) given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteTopicById" method="delete" path="/programs/{programId}/topics/{topicId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.sustainability.delete_topic_by_id(program_id="<id>", topic_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `topic_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the topic                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_topic_by_id

Retrieves a [topic](ref:sustainability#topic) given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getTopicById" method="get" path="/programs/{programId}/topics/{topicId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.get_topic_by_id(program_id="<id>", topic_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `program_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the program                                |
| `topic_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the topic                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Topic](../../models/topic.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_topic_by_id

Partially updates the properties of a [topic](ref:sustainability#topic). Only one property may be updated at a time.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/index`|`replace`, `test`|
|`/name`|`replace`, `test`|
|`/parent`|`replace`, `test`|


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateTopicById" method="patch" path="/programs/{programId}/topics/{topicId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_topic_by_id(program_id="<id>", topic_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "New name",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="partiallyUpdateTopicById" method="patch" path="/programs/{programId}/topics/{topicId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.sustainability.partially_update_topic_by_id(program_id="<id>", topic_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Climate Report",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `program_id`                                                                                                                               | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | The unique identifier of the program                                                                                                       |
| `topic_id`                                                                                                                                 | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | The unique identifier of the topic                                                                                                         |
| `request_body`                                                                                                                             | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]                                                                      | :heavy_check_mark:                                                                                                                         | A collection of patch operations to apply to the [topic](ref:sustainability#topic). Currently only one operation may be applied at a time. |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[models.Topic](../../models/topic.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |