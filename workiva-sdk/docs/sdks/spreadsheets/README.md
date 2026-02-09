# Spreadsheets

## Overview

Spreadsheets enable you to work with large, complex data in a familiar, collaborative, and controlled environment. Use these endpoints to manage spreadsheets and their sheets in the Workiva platform.

### Available Operations

* [get_spreadsheets](#get_spreadsheets) - Retrieve a list of spreadsheets
* [get_spreadsheet_by_id](#get_spreadsheet_by_id) - Retrieve a single spreadsheet
* [partially_update_spreadsheet_by_id](#partially_update_spreadsheet_by_id) - Partially update a single spreadsheet
* [get_datasets](#get_datasets) - Retrieve a list of datasets
* [upsert_datasets](#upsert_datasets) - Bulk upsert of datasets
* [spreadsheet_export](#spreadsheet_export) - Initiate a spreadsheet export
* [spreadsheet_filters_reapplication](#spreadsheet_filters_reapplication) - Reapply filters to the spreadsheet
* [spreadsheet_links_publication](#spreadsheet_links_publication) - Initiate publication of links in a spreadsheet
* [get_spreadsheet_milestones](#get_spreadsheet_milestones) - Retrieve a list of milestones for a spreadsheet
* [get_spreadsheet_permissions](#get_spreadsheet_permissions) - Retrieve permissions for a spreadsheet
* [spreadsheet_permissions_modification](#spreadsheet_permissions_modification) - Modify permissions on a spreadsheet
* [get_sheets](#get_sheets) - Retrieve a list of sheets
* [create_sheet](#create_sheet) - Create a new sheet in a spreadsheet
* [delete_sheet_by_id](#delete_sheet_by_id) - Delete a single sheet
* [get_sheet_by_id](#get_sheet_by_id) - Retrieve a single sheet
* [partially_update_sheet_by_id](#partially_update_sheet_by_id) - Partially update a single sheet
* [copy_sheet](#copy_sheet) - Copy sheet
* [delete_dataset_by_sheet_id](#delete_dataset_by_sheet_id) - Delete a single dataset
* [get_sheet_permissions](#get_sheet_permissions) - Retrieve permissions for a sheet in a spreadsheet
* [sheet_permissions_modification](#sheet_permissions_modification) - Modify permissions on a given sheet of a spreadsheet
* [get_sheet_data](#get_sheet_data) - Retrieve data from a sheet
* [update_sheet](#update_sheet) - Update sheet content
* [get_values_by_range](#get_values_by_range) - Retrieve a list of range values
* [update_values_by_range](#update_values_by_range) - Update values in a range

## get_spreadsheets

Returns a paginated list of [spreadsheets](ref:spreadsheets#spreadsheet).


### Example Usage

<!-- UsageSnippet language="python" operationID="getSpreadsheets" method="get" path="/spreadsheets" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_spreadsheets(maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `filter_`                                                                                   | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The properties to filter the results by.                                                    |                                                                                             |
| `order_by`                                                                                  | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | One or more comma-separated expressions to indicate the order in which to sort the results. |                                                                                             |
| `maxpagesize`                                                                               | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The maximum number of results to retrieve                                                   |                                                                                             |
| `next`                                                                                      | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Pagination cursor for next set of results.                                                  | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.GetSpreadsheetsResponse](../../models/getspreadsheetsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_spreadsheet_by_id

Retrieves a [spreadsheet](ref:spreadsheets#spreadsheet) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSpreadsheetById" method="get" path="/spreadsheets/{spreadsheetId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_spreadsheet_by_id(spreadsheet_id="<id>", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |                                                                     |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Spreadsheet](../../models/spreadsheet.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_spreadsheet_by_id

Updates the properties of a [spreadsheet](ref:spreadsheets#spreadsheet).

This is a long running operation. Responses include a `Location` header,
which indicates where to poll for results. For more details on long-running job polling,
see [Operations endpoint](ref:getoperationbyid).

### Options
| Path                              | PATCH Operations Supported         |
|-----------------------------------|------------------------------------|
| `/customFields/<custom field id>` | `add`, `remove`, `replace`, `test` |
| `/customFieldGroups`              | `add`, `remove`, `replace`, `test` |
| `/sheetCustomFieldGroups`         | `add`, `remove`, `replace`, `test` |
| `/lock`                           | `replace`                          |

### Examples

#### Add a custom field value

```json
[
  {
    "op": "add",
    "path": "/customFields/com.workiva.gsr.legal_entity",
    "value": "Workiva"
  }
]
```

#### Remove a custom field value

```json
[
  {
    "op": "remove",
    "path": "/customFields/com.workiva.gsr.legal_entity"
  }
]
```

#### Replace a custom field value

```json
[
  {
    "op": "replace",
    "path": "/customFields/com.workiva.gsr.legal_entity",
    "value": "Workiva, Inc."
  }
]
```

#### Verifying customFieldGroup is empty before replacing the list

```json
[
  {
    "op": "test",
    "path": "/customFieldGroups",
    "value": []
  },
  {
    "op": "replace",
    "path": "/customFieldGroups",
    "value": ["gsr.reporting"]
  }
]
```

#### Adding a customFieldGroup to the end of a list

```json
[
  {
    "op": "add",
    "path": "/customFieldGroups/-",
    "value": "gsr.reporting"
  }
]
```


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateSpreadsheetById" method="patch" path="/spreadsheets/{spreadsheetId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.partially_update_spreadsheet_by_id(spreadsheet_id="<id>", request_body=[
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

<!-- UsageSnippet language="python" operationID="partiallyUpdateSpreadsheetById" method="patch" path="/spreadsheets/{spreadsheetId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.partially_update_spreadsheet_by_id(spreadsheet_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/customFields/com.workiva.gsr.legal_entity",
            "value": "US Entity",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `spreadsheet_id`                                                      | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the spreadsheet                              |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the spreadsheet.         |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PartiallyUpdateSpreadsheetByIDResponse](../../models/partiallyupdatespreadsheetbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_datasets

Returns a list of [datasets](ref:spreadsheets#dataset). <br /><br /> Use this endpoint to identify any datasets that exist within a given [spreadsheet](ref:spreadsheets#spreadsheet), up to one per [sheet](ref:spreadsheets#sheet).

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatasets" method="get" path="/spreadsheets/{spreadsheetId}/datasets" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_datasets(spreadsheet_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetsListResult](../../models/datasetslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## upsert_datasets

Asynchronously upserts an array of [datasets](ref:spreadsheets#dataset) to a [spreadsheet](ref:spreadsheets#spreadsheet), given their properties. Each [sheet](ref:spreadsheets#sheet) can have only one dataset, and its range will always start with `A1`. <br /><br /> Bulk upsertion creates or updates datasets in sheets and performs any calculations after it completes. When complete, the dataset's range is locked through both the UI and endpoints that write values to a sheet. To change the values in a dataset, either upsert new values using this endpoint again, or delete the dataset. <br /><br /> If any dataset fails to upsert, no datasets upsert, and no changes commit. <br /><br /> Each dataset in the array requires `sheet` and `values`. Partial upserts are not supported. <br /><br /> Values may be strings, numbers, integers, or booleans. To indicate an empty cell, provide an empty string.

### Example Usage

<!-- UsageSnippet language="python" operationID="upsertDatasets" method="post" path="/spreadsheets/{spreadsheetId}/datasets/bulkUpsert" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.upsert_datasets(spreadsheet_id="<id>", request_body=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |
| `request_body`                                                      | List[[models.DatasetInput](../../models/datasetinput.md)]           | :heavy_check_mark:                                                  | An array of datasets                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpsertDatasetsResponse](../../models/upsertdatasetsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## spreadsheet_export

Asynchronously exports a [spreadsheet](ref:spreadsheets#spreadsheet) as .XLSX, .PDF, or .CSV.

Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).

Note: To export to .PDF, the spreadsheet can have no more than 250,000 cells.


### Example Usage

<!-- UsageSnippet language="python" operationID="spreadsheetExport" method="post" path="/spreadsheets/{spreadsheetId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.spreadsheet_export(spreadsheet_id="<id>", spreadsheet_export={
        "format_": models.SpreadsheetExportFormat.XLSX,
        "sheets": [
            "7c8d8c4a46784455bg68t36f9d8232d8",
            "54bgd83b471e5902f1a8e8c9a299c9fb",
        ],
        "xlsx_options": {
            "export_as_formulas": True,
            "export_precision": models.ExportPrecision.DISPLAYED,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                               | Type                                                                                                                                                                                    | Required                                                                                                                                                                                | Description                                                                                                                                                                             | Example                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spreadsheet_id`                                                                                                                                                                        | *str*                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                      | The unique identifier of the spreadsheet                                                                                                                                                |                                                                                                                                                                                         |
| `spreadsheet_export`                                                                                                                                                                    | [models.SpreadsheetExport](../../models/spreadsheetexport.md)                                                                                                                           | :heavy_check_mark:                                                                                                                                                                      | Details about the spreadsheet export, including its format and options                                                                                                                  | {<br/>"format": "xlsx",<br/>"sheets": [<br/>"7c8d8c4a46784455bg68t36f9d8232d8",<br/>"54bgd83b471e5902f1a8e8c9a299c9fb"<br/>],<br/>"xlsxOptions": {<br/>"exportAsFormulas": true,<br/>"exportPrecision": "displayed"<br/>}<br/>} |
| `retries`                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                     |                                                                                                                                                                                         |

### Response

**[models.SpreadsheetExportResponse](../../models/spreadsheetexportresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## spreadsheet_filters_reapplication

Performs a [`SpreadsheetFiltersReapplication`](ref:content#spreadsheetfiltersreapplication) on the specified spreadsheet.
This endpoint is used to refresh the spreadsheet's filters based on the latest state or configuration changes.
The filters are reapplied in the context of the spreadsheet's current data state.

This is a long-running operation. Responses include a `Location` header, which indicates where to poll for results.
For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="spreadsheetFiltersReapplication" method="post" path="/spreadsheets/{spreadsheetId}/filters/reapplication" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.spreadsheet_filters_reapplication(spreadsheet_id="<id>", spreadsheet_filters_reapplication={
        "ignore_non_editable_filters": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `spreadsheet_id`                                                                          | *str*                                                                                     | :heavy_check_mark:                                                                        | The unique identifier of the spreadsheet                                                  |                                                                                           |
| `spreadsheet_filters_reapplication`                                                       | [models.SpreadsheetFiltersReapplication](../../models/spreadsheetfiltersreapplication.md) | :heavy_check_mark:                                                                        | The filter reapplication request to apply                                                 | {<br/>"ignoreNonEditableFilters": true<br/>}                                              |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.SpreadsheetFiltersReapplicationResponse](../../models/spreadsheetfiltersreapplicationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## spreadsheet_links_publication

Publishes the links in a spreadsheet - either all (as document owner) or only one's own. Content at the latest spreadsheet revision will be used for publish.
The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="spreadsheetLinksPublication" method="post" path="/spreadsheets/{spreadsheetId}/links/publication" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.spreadsheet_links_publication(spreadsheet_id="<id>", links_publication_options={
        "publish_type": models.PublishType.ALL_LINKS,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `spreadsheet_id`                                                          | *str*                                                                     | :heavy_check_mark:                                                        | The unique identifier of the spreadsheet                                  |
| `links_publication_options`                                               | [models.LinksPublicationOptions](../../models/linkspublicationoptions.md) | :heavy_check_mark:                                                        | Details about the link publication.                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SpreadsheetLinksPublicationResponse](../../models/spreadsheetlinkspublicationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_spreadsheet_milestones

Returns [MilestoneListResult](ref:milestones#milestonelistresult).

### Example Usage

<!-- UsageSnippet language="python" operationID="getSpreadsheetMilestones" method="get" path="/spreadsheets/{spreadsheetId}/milestones" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_spreadsheet_milestones(spreadsheet_id="<id>", next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSpreadsheetMilestonesResponse](../../models/getspreadsheetmilestonesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_spreadsheet_permissions

Retrieves a paginated list of permissions for a given spreadsheet


### Example Usage

<!-- UsageSnippet language="python" operationID="getSpreadsheetPermissions" method="get" path="/spreadsheets/{spreadsheetId}/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_spreadsheet_permissions(spreadsheet_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |                                                                     |
| `filter_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The properties to filter the results by.                            |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSpreadsheetPermissionsResponse](../../models/getspreadsheetpermissionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## spreadsheet_permissions_modification

Assign and/or revoke permissions on a spreadsheet. If any modification in a request fails, all modifications on that request fail. <br /><br /> _To modify an existing permission, the existing permission must first be  explicitly revoked. Then, the new permission needs to be assigned. This  can be done in a single request by sending `toAssign` and `toRevoke` in  the request body._


### Example Usage

<!-- UsageSnippet language="python" operationID="spreadsheetPermissionsModification" method="post" path="/spreadsheets/{spreadsheetId}/permissions/modification" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.spreadsheets.spreadsheet_permissions_modification(spreadsheet_id="<id>", resource_permissions_modification={
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
| `spreadsheet_id`                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the spreadsheet                                                                                                                                                                                                               |                                                                                                                                                                                                                                                        |
| `resource_permissions_modification`                                                                                                                                                                                                                    | [models.ResourcePermissionsModification](../../models/resourcepermissionsmodification.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                     | Details about the spreadsheet permissions modification.                                                                                                                                                                                                | {<br/>"toAssign": [<br/>{<br/>"permission": "598e8fa3-3e7c-4fb7-b662-f44522216e2b",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>],<br/>"toRevoke": [<br/>{<br/>"permission": "85aa87ee-beb9-4417-8fa0-420e9de63534",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sheets

Returns a list of [sheets](ref:spreadsheets#sheet).

### Example Usage

<!-- UsageSnippet language="python" operationID="getSheets" method="get" path="/spreadsheets/{spreadsheetId}/sheets" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_sheets(spreadsheet_id="<id>", revision="1A2B3C4D", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |                                                                     |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSheetsResponse](../../models/getsheetsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_sheet

Creates a new [sheet](ref:spreadsheets#sheet) in a [spreadsheet](ref:spreadsheets#spreadsheet), given its properties. If the sheet name provided isn't unique, a number is appended to make it unique. By default, creates a top-level sheet in the top-most position.


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="createSheet" method="post" path="/spreadsheets/{spreadsheetId}/sheets" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.create_sheet(spreadsheet_id="<id>", sheet={
        "id": "27f1b61c04ae4b0991bc73c631914e1d",
        "index": 1,
        "name": "Q1",
        "table": {
            "table": "WA7i5vbm7lNaEn6XT97lNaEn6XT9AtcW5vb22BJjMrqxmrujMrqxmru",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="createSheet" method="post" path="/spreadsheets/{spreadsheetId}/sheets" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.create_sheet(spreadsheet_id="<id>", sheet={
        "index": 2,
        "name": "Q3",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |
| `sheet`                                                             | [models.SheetInput](../../models/sheetinput.md)                     | :heavy_check_mark:                                                  | The properties of the sheet to create                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Sheet](../../models/sheet.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_sheet_by_id

Deletes a [sheet](ref:spreadsheets#sheet) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSheetById" method="delete" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.spreadsheets.delete_sheet_by_id(spreadsheet_id="<id>", sheet_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |
| `sheet_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the sheet                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sheet_by_id

Retrieves a [sheet](ref:spreadsheets#sheet) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSheetById" method="get" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_sheet_by_id(spreadsheet_id="<id>", sheet_id="<id>", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |                                                                     |
| `sheet_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the sheet                                  |                                                                     |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Sheet](../../models/sheet.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_sheet_by_id

Updates the properties of a [sheet](ref:spreadsheets#sheet).

This is a long running operation. Responses include a `Location` header,
which indicates where to poll for results. For more details on long-running job polling,
see [Operations endpoint](ref:getoperationbyid).

### Options
| Path                              | PATCH Operations Supported         |
|-----------------------------------|------------------------------------|
| `/name`                           | `replace`                          |
| `/index`                          | `replace`                          |
| `/parent`                         | `replace`                          |
| `/customFields/<custom field id>` | `add`, `remove`, `replace`, `test` |
| `/lock`                           | `replace`                          |

### Examples

#### Update the name of a sheet

```json
[
  {
    "op": "replace",
    "path": "/name",
    "value": "Q1 Draft"
  }
]
```

#### Update the parent of a sheet (preserving its index)

```json
[
  {
    "op": "replace",
    "path": "/parent",
    "value": {
      "id": "242a56d3cc0742c8abad0820bd318b23"
    }
  }
]
```

#### Update the parent of a sheet (making it the first child)

```json
[
  {
    "op": "replace",
    "path": "/parent",
    "value": {
      "id": "242a56d3cc0742c8abad0820bd318b23"
    }
  },
  {
    "op": "replace",
    "path": "/index",
    "value": 0
  }
]
```

#### Add a custom field value

```json
[
  {
    "op": "add",
    "path": "/customFields/com.workiva.gsr.legal_entity",
    "value": "Workiva"
  }
]
```

#### Remove a custom field value

```json
[
  {
    "op": "remove",
    "path": "/customFields/com.workiva.gsr.legal_entity"
  }
]
```

#### Replace a custom field value

```json
[
  {
    "op": "replace",
    "path": "/customFields/com.workiva.gsr.legal_entity",
    "value": "Workiva, Inc."
  }
]
```


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateSheetById" method="patch" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.partially_update_sheet_by_id(spreadsheet_id="<id>", sheet_id="<id>", request_body=[
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

<!-- UsageSnippet language="python" operationID="partiallyUpdateSheetById" method="patch" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.partially_update_sheet_by_id(spreadsheet_id="<id>", sheet_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Sheet 1",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `spreadsheet_id`                                                      | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the spreadsheet                              |
| `sheet_id`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the sheet                                    |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the sheet.               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PartiallyUpdateSheetByIDResponse](../../models/partiallyupdatesheetbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## copy_sheet

Asynchronously copies a [sheet](ref:spreadsheets#sheet) given details about the copy's destination within the same or another spreadsheet. Options are specified using a [SheetCopy](ref:spreadsheets#sheetcopy) object.

This endpoint copies a sheet's content, but does not copy labels, comments, or tasks. It will copy over most formatting, however it does not copy user-defined style guides across spreadsheets. So if the source sheet has  formatting that depends on a user-defined style guide, that formatting will be lost when copying to a new spreadsheet.

Unless otherwise specified, the copy appears at the top level of its  destination spreadsheet, with an index of 0, and with the same name as the original sheet.

### Example Usage

<!-- UsageSnippet language="python" operationID="copySheet" method="post" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/copy" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.copy_sheet(spreadsheet_id="<id>", sheet_id="<id>", sheet_copy={
        "sheet_index": 2,
        "sheet_name": "Q1",
        "sheet_parent": "5bbf8aa3cea54465762af96e3ca411c7",
        "spreadsheet": "c65d9572a7464037a383d6235633cf74",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |
| `sheet_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the sheet                                  |
| `sheet_copy`                                                        | [models.SheetCopy](../../models/sheetcopy.md)                       | :heavy_check_mark:                                                  | A SheetCopy object                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CopySheetResponse](../../models/copysheetresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_dataset_by_sheet_id

Deletes the [dataset](ref:spreadsheets#dataset) for the specified [sheet](ref:spreadsheets#sheet). <br /><br /> When you delete a dataset, you can select whether to leave its associated values in place. To delete its values, pass `true` for query parameter `$deletevalues` (default is `false`).

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDatasetBySheetId" method="delete" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/dataset" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.delete_dataset_by_sheet_id(spreadsheet_id="<id>", sheet_id="<id>", deletevalues=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |                                                                     |
| `sheet_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the sheet                                  |                                                                     |
| `deletevalues`                                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates whether values should be deleted along with the dataset   | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteDatasetBySheetIDResponse](../../models/deletedatasetbysheetidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sheet_permissions

Retrieves a paginated list of permissions for the given sheet in a spreadsheet


### Example Usage

<!-- UsageSnippet language="python" operationID="getSheetPermissions" method="get" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_sheet_permissions(request={
        "spreadsheet_id": "<id>",
        "sheet_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.GetSheetPermissionsRequest](../../models/getsheetpermissionsrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.GetSheetPermissionsResponse](../../models/getsheetpermissionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## sheet_permissions_modification

Assign and/or revoke permissions on a sheet. If any modification in a request fails, all modifications on that request fail. <br /><br /> _To modify an existing permission, the existing permission must first be  explicitly revoked. Then, the new permission needs to be assigned. This  can be done in a single request by sending `toAssign` and `toRevoke` in  the request body._


### Example Usage

<!-- UsageSnippet language="python" operationID="sheetPermissionsModification" method="post" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/permissions/modification" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.spreadsheets.sheet_permissions_modification(spreadsheet_id="<id>", sheet_id="<id>", resource_permissions_modification={
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
| `spreadsheet_id`                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the spreadsheet                                                                                                                                                                                                               |                                                                                                                                                                                                                                                        |
| `sheet_id`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the sheet                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                        |
| `resource_permissions_modification`                                                                                                                                                                                                                    | [models.ResourcePermissionsModification](../../models/resourcepermissionsmodification.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                     | Details about the sheet permissions modification.                                                                                                                                                                                                      | {<br/>"toAssign": [<br/>{<br/>"permission": "598e8fa3-3e7c-4fb7-b662-f44522216e2b",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>],<br/>"toRevoke": [<br/>{<br/>"permission": "85aa87ee-beb9-4417-8fa0-420e9de63534",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sheet_data

Retrieve data from a range in a sheet. Includes the value & formatting of cells, visibility of columns and cells, merged ranges, etc.
Limit the results to particular fields by providing a comma-separated list of paths, rooted at the `data` object.
Example: $fields=cells.calculatedValue,cells.formats.valueFormat <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 600 requests per minute.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSheetData" method="get" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/sheetdata" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_sheet_data(request={
        "spreadsheet_id": "<id>",
        "sheet_id": "<id>",
        "cellrange": "A2:B",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetSheetDataRequest](../../models/getsheetdatarequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSheetDataResponse](../../models/getsheetdataresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update_sheet

Asynchronously submits a [SheetUpdate](ref:spreadsheets#sheetupdate) to a [sheet](ref:spreadsheets#sheet). Each [SheetUpdate](ref:spreadsheets#sheetupdate) can have only one update field set per request. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 60 requests per minute.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSheet" method="post" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/update" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.update_sheet(spreadsheet_id="<id>", sheet_id="<id>", sheet_update=models.SheetUpdate(
        apply_borders=models.SheetUpdateApplyBorders(
            borders=[
                models.ApplyBorders(
                    bottom=models.Border(
                        style=models.Style.SINGLE,
                        weight=2,
                    ),
                    inner_horizontal=models.Border(
                        color="#808080",
                        style=models.Style.DASHED1,
                    ),
                    inner_vertical=models.Border(
                        color="#808080",
                        style=models.Style.DASHED1,
                    ),
                    left=models.Border(
                        style=models.Style.SINGLE,
                        weight=2,
                    ),
                    ranges=[
                        models.Range(
                            start_column=0,
                            start_row=0,
                            stop_column=3,
                            stop_row=3,
                        ),
                    ],
                    right=models.Border(
                        style=models.Style.SINGLE,
                        weight=2,
                    ),
                    top=models.Border(
                        style=models.Style.SINGLE,
                        weight=2,
                    ),
                ),
            ],
        ),
        apply_formats=models.SheetUpdateApplyFormats(
            formats=[
                models.ApplyFormats(
                    cell_format=models.CellFormatInput(
                        background_color="#d0e0f0",
                    ),
                    ranges=[
                        models.Range(
                            start_column=0,
                            start_row=0,
                            stop_column=None,
                            stop_row=0,
                        ),
                    ],
                    text_format=models.TextFormat(
                        bold=True,
                        font_color="#4bdf58",
                    ),
                    value_format=models.ValueFormat(
                        value_format_type=models.ValueFormatType.TEXT,
                    ),
                ),
            ],
        ),
        clear_borders=models.SheetUpdateClearBorders(
            ranges=[
                models.Range(
                    start_column=0,
                    start_row=0,
                    stop_column=3,
                    stop_row=3,
                ),
            ],
        ),
        clear_formats=models.SheetUpdateClearFormats(
            cell_format_fields=[
                "*",
            ],
            ranges=[
                models.Range(
                    start_column=0,
                    start_row=0,
                    stop_column=None,
                    stop_row=0,
                ),
            ],
            text_format_fields=[
                "*",
            ],
            value_format_fields=[
                "*",
            ],
        ),
        delete_columns=models.SheetUpdateDeleteColumns(
            force=True,
            intervals=[
                models.Interval(
                    end=3,
                    start=2,
                ),
            ],
        ),
        delete_rows=models.SheetUpdateDeleteRows(
            force=True,
            intervals=[
                models.Interval(
                    end=7,
                    start=5,
                ),
            ],
        ),
        edit_cells=models.SheetUpdateEditCells(
            cells=[
                models.CellEdit(
                    column=0,
                    row=0,
                    value="Alpha One",
                ),
                models.CellEdit(
                    column=1,
                    row=0,
                    value="Bravo One",
                ),
                models.CellEdit(
                    column=0,
                    row=1,
                    value="Alpha Two",
                ),
                models.CellEdit(
                    column=1,
                    row=1,
                    value="Bravo Two",
                ),
            ],
        ),
        edit_range=models.SheetUpdateEditRange(
            range=models.Range(
                start_column=0,
                start_row=0,
                stop_column=1,
                stop_row=1,
            ),
            values=[
                [
                    "Alpha One",
                    "Bravo One",
                ],
                [
                    "Alpha Two",
                    "Bravo Two",
                ],
            ],
        ),
        hide_columns=models.SheetUpdateHideColumns(
            force=True,
            intervals=[
                models.Interval(
                    end=5,
                    start=4,
                ),
            ],
        ),
        hide_rows=models.SheetUpdateHideRows(
            force=True,
            intervals=[
                models.Interval(
                    end=9,
                    start=7,
                ),
            ],
        ),
        insert_columns=models.SheetUpdateInsertColumns(
            inherit_from=models.InheritFrom.BEFORE,
            insertions=[
                models.Insertion(
                    count=1,
                    index=3,
                ),
            ],
        ),
        insert_rows=models.SheetUpdateInsertRows(
            inherit_from=models.InheritFrom.BEFORE,
            insertions=[
                models.Insertion(
                    count=2,
                    index=6,
                ),
            ],
        ),
        merge_ranges=models.SheetUpdateMergeRanges(
            force=True,
            merge_type=models.MergeType.HORIZONTAL,
            ranges=[
                models.Range(
                    start_column=0,
                    start_row=4,
                    stop_column=1,
                    stop_row=7,
                ),
            ],
        ),
        resize_columns=models.SheetUpdateResizeColumns(
            resize_intervals=[
                models.ResizeColumnIntervals(
                    intervals=[
                        models.Interval(
                            end=3,
                            start=0,
                        ),
                    ],
                    size=96,
                ),
            ],
        ),
        resize_columns_to_fit=models.SheetUpdateResizeColumnsToFit(
            intervals=[
                models.Interval(
                    end=3,
                    start=0,
                ),
            ],
        ),
        resize_rows=models.SheetUpdateResizeRows(
            resize_intervals=[
                models.ResizeRowIntervals(
                    intervals=[
                        models.Interval(
                            end=3,
                            start=0,
                        ),
                    ],
                    size=24,
                ),
            ],
        ),
        resize_rows_to_fit=models.SheetUpdateResizeRowsToFit(
            intervals=[
                models.Interval(
                    end=3,
                    start=0,
                ),
            ],
        ),
        unhide_columns=models.SheetUpdateUnhideColumns(
            intervals=[
                models.Interval(
                    end=5,
                    start=4,
                ),
            ],
        ),
        unhide_rows=models.SheetUpdateUnhideRows(
            intervals=[
                models.Interval(
                    end=9,
                    start=7,
                ),
            ],
        ),
        unmerge_ranges=models.SheetUpdateUnmergeRanges(
            ranges=[
                models.Range(
                    start_column=0,
                    start_row=4,
                    stop_column=1,
                    stop_row=7,
                ),
            ],
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |
| `sheet_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the sheet                                  |
| `sheet_update`                                                      | [models.SheetUpdate](../../models/sheetupdate.md)                   | :heavy_check_mark:                                                  | A SheetUpdate                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateSheetResponse](../../models/updatesheetresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_values_by_range

Returns the paginated values for a specified range.
When you retrieve values from a range, Ones scale is used regardless of the cell's scale formatting.

### Example Usage

<!-- UsageSnippet language="python" operationID="getValuesByRange" method="get" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/values/{range}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.get_values_by_range(request={
        "spreadsheet_id": "<id>",
        "sheet_id": "<id>",
        "range": None,
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "valuestyle": models.ValueStyle.RAW,
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetValuesByRangeRequest](../../models/getvaluesbyrangerequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GetValuesByRangeResponse](../../models/getvaluesbyrangeresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update_values_by_range

Overwrites all values in a range with new values. The provided range must not exceed the specified range. If the provided range of values is *smaller* than the specified range, it clears all cells in the range **and** those not covered by the range values. Rows of values in the provided range must be of equal length. An empty range of values is valid and may be used to clear a range.
To indicate that a cell's value shouldn't be replaced, use the special cell value `null`.
When you add a value to a cell, it uses Ones scale regardless of the cell's scale formatting.

### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="updateValuesByRange" method="put" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/values/{range}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.update_values_by_range(spreadsheet_id="<id>", sheet_id="<id>", range="<value>", range_values={
        "range": "A1:B2",
        "values": [
            [
                1,
                4,
            ],
            [
                2,
                "",
            ],
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="updateValuesByRange" method="put" path="/spreadsheets/{spreadsheetId}/sheets/{sheetId}/values/{range}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.spreadsheets.update_values_by_range(spreadsheet_id="<id>", sheet_id="<id>", range="<value>", range_values={
        "values": [
            [
                1,
                4,
            ],
            [
                2,
                "",
            ],
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `spreadsheet_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the spreadsheet                            |
| `sheet_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the sheet                                  |
| `range`                                                             | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The range of values, in A1-style notation                           |
| `range_values`                                                      | [models.RangeValues](../../models/rangevalues.md)                   | :heavy_check_mark:                                                  | All values for the range, not just those to update                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateValuesByRangeResponse](../../models/updatevaluesbyrangeresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |