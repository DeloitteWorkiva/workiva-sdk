# Graph

## Overview

The Graph endpoints enable access to Integrated Risk workspaces, such as to pull reports and records, create and edit records, and more. <br /><br /> Please refer to the [Graph Guides](ref:graph-guide) for further documentation and examples.

### Available Operations

* [create_edits](#create_edits) - Create new record edits
* [get_record_by_id](#get_record_by_id) - Retrieve a single record
* [get_records](#get_records) - Retrieve a list of records
* [get_type_by_id](#get_type_by_id) - Retrieve a single type
* [get_types](#get_types) - Retrieve a list of types
* [graph_report_export](#graph_report_export) - Initiate a graph report export

## create_edits

Creates new record [edits](ref:graph#edit) given their properties. Each edit in the supplied array requires at least an `operation` and `targetId`. Up to 1000 edits may be processed per request.
If there are invalid edits, the error details will include a list of errors encountered. Each message will include the zero-based position of the failed edit in the provided list of edits.

### Example Usage

<!-- UsageSnippet language="python" operationID="createEdits" method="post" path="/graph/edits" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.graph.create_edits(request=[
        {
            "operation": models.EditOperation.CREATE_RECORD,
            "properties": {
                "id": {
                    "datatype": "string",
                    "value": "User ID for the issue",
                },
                "secondProperty": {
                    "datatype": "string",
                    "value": "This is a second property",
                },
            },
            "temporary_record_id": "<user-generated-temporary-id-for-this-issue-record>",
            "type": "Issue",
        },
        {
            "label": "indicates_issue_on_control",
            "operation": models.EditOperation.CREATE_RELATIONSHIP,
            "record_id": "<user-generated-temporary-id-for-this-issue-record>",
            "target_id": "085ce4f5-8687-4cb0-aad6-d5c4e1a89a3d",
        },
        {
            "operation": models.EditOperation.SET_PROPERTIES,
            "properties": {
                "customProperty": {
                    "datatype": "string",
                    "value": "This is a custom property",
                },
            },
            "record_id": "085ce4f5-8687-4cb0-aad6-d5c4e1a89a3d",
        },
        {
            "label": "severity_of_issue",
            "operation": models.EditOperation.DELETE_RELATIONSHIP,
            "record_id": "033a531f-c741-4a97-bc09-bb72358e75ad",
            "target_id": "008c4041-e941-4478-88ea-8ae74b21f6bf",
        },
        {
            "operation": models.EditOperation.DELETE_RECORD,
            "record_id": "033a531f-c741-4a97-bc09-bb72358e75ad",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.Edit]](../../models/.md)                               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EditsResult](../../models/editsresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_record_by_id

Retrieves a [record](ref:graph#record) given its ID. The unique identifier is typically a UUID, but it may be a different unique string in some cases.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRecordById" method="get" path="/graph/records/{recordId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.graph.get_record_by_id(record_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the record                                 |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Record](../../models/record.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_records

Returns a list of [records](ref:graph#record) matching the provided filters. At least one filter is required. If no filter is provided an error will be returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRecords" method="get" path="/graph/records" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.graph.get_records(expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `filter_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The properties to filter the results by.                            |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RecordsListResult](../../models/recordslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_type_by_id

Returns a record [type](ref:graph#type) given its ID (name)


### Example Usage

<!-- UsageSnippet language="python" operationID="getTypeById" method="get" path="/graph/types/{typeId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.graph.get_type_by_id(type_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the type                                   |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Type](../../models/type.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_types

The Types endpoint is used to discover what [types](ref:graph#type) of records exist and their attributes. This endpoint lets you know what to expect from the Records endpoints.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTypes" method="get" path="/graph/types" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.graph.get_types(expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TypesListResult](../../models/typeslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## graph_report_export

Asynchronously exports a graph report (only CSV available at this time).
This endpoint will execute the query of a saved report and export to the specified format (only CSV available at this time). The ID of the [record](ref:graph#record) containing the saved report is used for the `reportID` path element. Reports are stored in records of type `DataSource` and `ReportView`. The list of applicable records can be retrieved from the `/records` endpoint such as `GET /records?$filter=type eq DataSource or type eq ReportView`. A filter on the `title` property should be used to return a particular report.
Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="graphReportExport" method="post" path="/graph/reports/{reportId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.graph.graph_report_export(report_id="<id>", graph_report_export={
        "format_": models.GraphReportExportFormat.CSV,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `report_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the report                                 |                                                                     |
| `graph_report_export`                                               | [models.GraphReportExport](../../models/graphreportexport.md)       | :heavy_check_mark:                                                  | Details about the report export                                     | {<br/>"format": "csv"<br/>}                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GraphReportExportResponse](../../models/graphreportexportresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |