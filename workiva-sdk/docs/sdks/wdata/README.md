# Wdata

## Overview

### Available Operations

* [delete_workspace](#delete_workspace) - Delete a single workspace
* [export_workspace](#export_workspace) - Export a single workspace
* [import_data](#import_data) - Import data
* [find_workspace_files_by_size](#find_workspace_files_by_size) - Retrieve workspace files by size
* [get_workspace_query_usage](#get_workspace_query_usage) - Retrieve workspace query usage
* [get_workspace_upload_usage](#get_workspace_upload_usage) - Retrieve workspace upload usage
* [validate_files](#validate_files) - Validate files
* [validate_tables](#validate_tables) - Validate tables
* [list_connections](#list_connections) - List connections
* [refresh_batch](#refresh_batch) - Refresh batch of connections
* [get_refresh_batch_status](#get_refresh_batch_status) - Gets the status of a batch refresh
* [get_connection](#get_connection) - Get connection details
* [refresh_connection](#refresh_connection) - Refresh connection
* [get_refresh_status](#get_refresh_status) - Get connection refresh status
* [search](#search) - Search
* [get_files](#get_files) - Retrieve a list of files
* [upload_file](#upload_file) - Upload a single file
* [validate_filename](#validate_filename) - Validate whether a file with the filename can be uploaded to the table
* [delete_file](#delete_file) - Delete a single file
* [get_file](#get_file) - Retrieve a single file
* [download_file_1](#download_file_1) - Download a single file
* [get_errors](#get_errors) - Retrieve errors
* [export_file_to_spreadsheets](#export_file_to_spreadsheets) - Export a file to spreadsheets
* [list_folders](#list_folders) - Retrieve a list of folders
* [create_folder](#create_folder) - Create a new folder
* [delete_folder](#delete_folder) - Delete a single folder
* [get_folder](#get_folder) - Retrieve a single folder
* [update_folder](#update_folder) - Update a single folder
* [list_children](#list_children) - Retrieve list of folder contents
* [set_children](#set_children) - Move content into a folder
* [list_parameters](#list_parameters) - Get Parameters
* [create_parameter](#create_parameter) - Create parameter
* [delete_parameter](#delete_parameter) - Delete Parameter
* [get_parameter](#get_parameter) - Get Parameter
* [update_parameter](#update_parameter) - Update Parameter
* [list_pivot_views](#list_pivot_views) - Retrieve a list of pivot views
* [create_pivot_view](#create_pivot_view) - Create a new pivot view
* [delete_pivot_view](#delete_pivot_view) - Delete a single pivot view
* [get_pivot_view](#get_pivot_view) - Retrieve a single pivot view
* [update_pivot_view](#update_pivot_view) - Update a single pivot view
* [list_queries](#list_queries) - Retrieve list of queries
* [create_query](#create_query) - Create a new query
* [get_query_column_data](#get_query_column_data) - Retrieve query column data
* [is_query_valid](#is_query_valid) - Parses the query to determine if it is valid
* [delete_query](#delete_query) - Delete a single query
* [get_query](#get_query) - Retrieve a single query
* [update_query](#update_query) - Update a single query
* [get_dependencies](#get_dependencies) - Retrieve dependencies
* [get_tables_dependent_on_query](#get_tables_dependent_on_query) - Retrieve a list of dependents
* [describe_query](#describe_query) - List the output columns of a query
* [list_query_results](#list_query_results) - Retrieve a list of query results
* [run_query](#run_query) - Execute a query
* [cancel_query](#cancel_query) - Cancel a running query
* [get_query_result](#get_query_result) - Retrieve a single query result
* [download_query_result](#download_query_result) - Download a query result
* [export_query_result_to_spreadsheets](#export_query_result_to_spreadsheets) - Export query result to spreadsheets
* [list_select_lists](#list_select_lists) - Retrieve a list of select lists
* [create_select_list](#create_select_list) - Create a new select list
* [delete](#delete) - Delete a single select list
* [get_select_list](#get_select_list) - Retrieve a single select list
* [update_select_list](#update_select_list) - Update a single select list
* [list_shared_tables](#list_shared_tables) - Retrieve a list of shared tables
* [create_shared_table](#create_shared_table) - Create a new shared table
* [delete_shared_table](#delete_shared_table) - Delete a single shared table
* [get_shared_table](#get_shared_table) - Retrieve a single shared table
* [get_tables](#get_tables) - Retrieve a list of tables
* [create_table](#create_table) - Create a new table
* [delete_table](#delete_table) - Delete a single table
* [get_table](#get_table) - Retrieve a single table
* [update_table](#update_table) - Update a single table
* [get_dependents](#get_dependents) - Retrieve a list of dependents
* [import_file](#import_file) - Import a single file
* [unimport_file](#unimport_file) - Unimport a single file
* [get_import_info](#get_import_info) - Retrieve import information
* [import_from_spreadsheets](#import_from_spreadsheets) - Import from spreadsheets
* [list_tags](#list_tags) - Retrieve a list of tags
* [create_tag](#create_tag) - Create a new tag
* [delete_tag](#delete_tag) - Delete a single tag
* [update_tag](#update_tag) - Update a single tag
* [create_token](#create_token) - Create a new token
* [download_file](#download_file) - Download a single file
* [parse_date](#parse_date) - Parse a date
* [health_check](#health_check) - Health check

## delete_workspace

Deletes all information in the workspace of the request. <b>This is a final operation and can't be undone</b>. Any state left in the workspace due to an error is in an indeterminate state and shouldn't be trusted. Some non-private information may be kept for auditing and metric purposes.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteWorkspace" method="delete" path="/api/v1/admin/account" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_workspace()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## export_workspace

Creates a file representing the entirety of the requested workspace and returns a
token. Use the [`Download a single file endpoint`](ref:wdata-downloadfile) to
exchange the token for the file.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_exportWorkspace" method="get" path="/api/v1/admin/export" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.export_workspace()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseTokenDto](../../models/baseresponsetokendto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## import_data

By default, deletes all information in the workspace of the request. <b>This is a final
operation and can't be undone.</b>  Any state left in the workspace due to an error is
in an indeterminate state and shouldn't be trusted. Some non-private information may be
kept for auditing and metric purposes. After the delete, it then imports the tables, tags,
and queries in the provided cb file into the workspace. <br><br>
This is an asynchronous operation. Returns a 201 when the file is correctly decoded and
its tables, queries, and tags are saved. Files continue to import after this call
completes.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_importData" method="post" path="/api/v1/admin/import" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.import_data(wipe=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `wipe`                                                                                    | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `request_body`                                                                            | [Optional[models.WdataImportDataRequestBody]](../../models/wdataimportdatarequestbody.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |
| `server_url`                                                                              | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | An optional server URL to use.                                                            |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## find_workspace_files_by_size

Returns a paged collection of the file meta associated with the workspace of the request,
ordered by size.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_findWorkspaceFilesBySize" method="get" path="/api/v1/admin/usage/filesBySize" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.find_workspace_files_by_size()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of file meta objects to return, from 1 to 1000; by default, 1000   |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataFindWorkspaceFilesBySizeResponse](../../models/wdatafindworkspacefilesbysizeresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_workspace_query_usage

Returns a Long that represents the number of bytes queried by the workspace of the
request since the start time provided.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getWorkspaceQueryUsage" method="get" path="/api/v1/admin/usage/query" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_workspace_query_usage(start_date="1970-01-01", stop_date="9999-01-01")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `start_date`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The earliest date of usage to consider                              |
| `stop_date`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The end date of usage to consider                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseLong](../../models/baseresponselong.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_workspace_upload_usage

Returns a Long that represents the number of bytes uploaded by the workspace associated with this request from the start time provided to now.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getWorkspaceUploadUsage" method="get" path="/api/v1/admin/usage/upload" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_workspace_upload_usage(start_date="1970-01-01", stop_date="9999-01-01")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `start_date`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The starting point to begin considering usage                       |
| `stop_date`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ending point when considering usage                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseLong](../../models/baseresponselong.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## validate_files

Validates files associated with the provided table ID. Validation repairs any files in
an inconsistent state, and deletes those without enough state to recover. All files
deleted or repaired are returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_validateFiles" method="post" path="/api/v1/admin/validation/files" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.validate_files(request={
        "table_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.StartValidateFilesDto](../../models/startvalidatefilesdto.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |
| `server_url`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | An optional server URL to use.                                        |

### Response

**[models.BaseResponseValidateFilesDto](../../models/baseresponsevalidatefilesdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## validate_tables

Validates the tables in the workspace associated with the request. Validation returns an entity that indicates the tables deleted due to bad state, and those with enough state and repaired.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_validateTables" method="post" path="/api/v1/admin/validation/tables" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.validate_tables()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseValidateTablesDto](../../models/baseresponsevalidatetablesdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_connections

A pageable endpoint to list data connections between features of the Workiva platform. When filtering by source or destination, the corresponding ID is required.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listConnections" method="get" path="/api/v1/connections" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_connections()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.WdataListConnectionsRequest](../../models/wdatalistconnectionsrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |
| `server_url`                                                                      | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | An optional server URL to use.                                                    |

### Response

**[models.WdataListConnectionsResponse](../../models/wdatalistconnectionsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## refresh_batch

Refreshes multiple incoming connections within the same spreadsheet, based on ID. When connecting to multiple spreadsheets, tables or other destinations, use the [`singular refresh connection`](ref:wdata-refreshconnection) instead.
 `usePreviousDestinationParameters` and  `usePreviousSourceParameters` will use the exact parameters of your previous run; any new parameters you’ve provided will be ignored. This endpoint only works for outgoing connections if they are all connected to the same workbook. This endpoint has a limit of 100 refreshes per request.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_refreshBatch" method="post" path="/api/v1/connections/batch/refresh" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.refresh_batch(request_body=[
        {},
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                 | List[[models.RefreshConnectionDto](../../models/refreshconnectiondto.md)]                                                                      | :heavy_check_mark:                                                                                                                             | N/A                                                                                                                                            |
| `cancel_unwritables`                                                                                                                           | *Optional[bool]*                                                                                                                               | :heavy_minus_sign:                                                                                                                             | Allow individual connections in the batch to be canceled if they have a destination that is unwritable. This will NOT cancel the entire batch. |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |
| `server_url`                                                                                                                                   | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | An optional server URL to use.                                                                                                                 |

### Response

**[models.BaseResponseRefreshBatchDto](../../models/baseresponserefreshbatchdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_refresh_batch_status

Returns details about a specific batch refresh, based on its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getRefreshBatchStatus" method="get" path="/api/v1/connections/batch/refresh/{batchId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_refresh_batch_status(batch_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `batch_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the batch to return details about                         |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseRefreshBatchDto](../../models/baseresponserefreshbatchdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_connection

Returns details about a specific connection, based on its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getConnection" method="get" path="/api/v1/connections/{connectionId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_connection(connection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the connection to return details about                    |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseConnectionDto](../../models/baseresponseconnectiondto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## refresh_connection

Refreshes a specific connection, based on its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_refreshConnection" method="post" path="/api/v1/connections/{connectionId}/refresh" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.refresh_connection(connection_id="<id>", refresh_connection_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `refresh_connection_dto`                                            | [models.RefreshConnectionDto](../../models/refreshconnectiondto.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseConnectionRunDto](../../models/baseresponseconnectionrundto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_refresh_status

Returns details about a specific connection refresh status, based on its ID. To retrieve details about a specific refresh, provide its 'jobId'.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getRefreshStatus" method="get" path="/api/v1/connections/{connectionId}/status" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_refresh_status(connection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the connection to return details about                    |
| `job_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the job running for a connection                          |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseConnectionRunDto](../../models/baseresponseconnectionrundto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## search

Returns a list of all entities that match the provided criteria. Both name and
description are fuzzy matches; they match _any_ entity that contains the provided
string. The type is used to filter results based on the provided type of entity.
The consumer must have READ access on all returned entities.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_search" method="get" path="/api/v1/entity" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.search(request={})

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.WdataSearchRequest](../../models/wdatasearchrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.WdataSearchResponse](../../models/wdatasearchresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_files

Returns a paged list of all files associated with the provided table ID, as well
as metadata associated with each file.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getFiles" method="get" path="/api/v1/file" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_files(request={
        "table_id": "<id>",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.WdataGetFilesRequest](../../models/wdatagetfilesrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.WdataGetFilesResponse](../../models/wdatagetfilesresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## upload_file

Accepts CSV, TSV, or JSON files, or a ZIP file that contains a single CSV, TSV, or
JSON file. If a ZIP, it must contain a CSV, TSV, or JSON file, and the name of the
CSV, TSV, or JSON file is also used with the imported file. Downloading this file
again downloads the source. Note that all files uploaded must have a .csv, .tsv, or .json
extension. JSON files are expected to have a single JSON record per line; a JSON file is
a series of JSON objects delimited by a newline character.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_uploadFile" method="post" path="/api/v1/file" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.upload_file(request={
        "table_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.WdataUploadFileRequest](../../models/wdatauploadfilerequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |
| `server_url`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | An optional server URL to use.                                          |

### Response

**[models.BaseResponseFileMetaDto](../../models/baseresponsefilemetadto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## validate_filename

If the filename is valid, this returns 200. If the table already has a file with the same name, this returns 409. If the user isn't allowed to read the table, or if the table isn't found, this returns 404.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_validateFilename" method="get" path="/api/v1/file/validateName" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.validate_filename(table_id="<id>", filename="example.file")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the table to upload the file to                           |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The name of the file to upload                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 409, 429 | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## delete_file

Unstages the file with the provided ID. The file must have a STAGED status; if the
file isn't STAGED, returns a 409 status. If the file isn't found, this is a no-op.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteFile" method="delete" path="/api/v1/file/{fileId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_file(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 409, 429 | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_file

Returns the file meta that matches the provided ID, or a 404 if an associated file
can't be found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getFile" method="get" path="/api/v1/file/{fileId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_file(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseFileMetaDto](../../models/baseresponsefilemetadto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## download_file_1

Returns a file with the provided ID, which points to a file meta ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_downloadFile_1" method="get" path="/api/v1/file/{fileId}/download" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.download_file_1(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_errors

Returns a paged list of operation errors during the upload, import, or tagging
processes for the provided file ID, if they exist. This list is immutable and may be
empty if no errors have occurred. If errors exist we recommend fixing them and
reimporting your file

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getErrors" method="get" path="/api/v1/file/{fileId}/error" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_errors(file_id="<id>", limit=50)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `file_id`                                                                     | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier of the file                                             |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of errors to return, from 1 to 50; by default, 50                  |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataGetErrorsResponse](../../models/wdatageterrorsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## export_file_to_spreadsheets

Exports the file ID identified in the path to the spreadsheet identified by the
provided URL. If the URL string is empty, creates and returns a new spreadsheet and
its sheet IDs.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_exportFileToSpreadsheets" method="post" path="/api/v1/file/{fileId}/export" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.export_file_to_spreadsheets(file_id="<id>", export_file_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |
| `export_file_dto`                                                   | [models.ExportFileDto](../../models/exportfiledto.md)               | :heavy_check_mark:                                                  | The representation of the file to export                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseSpreadsheetInfoDto](../../models/baseresponsespreadsheetinfodto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_folders

Returns a paged list of all folders associated with the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listFolders" method="get" path="/api/v1/folder" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_folders(limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of folders to return, from 1 to 1000; by default, 1000             |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataListFoldersResponse](../../models/wdatalistfoldersresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_folder

Creates a folder using the provided information and returns the folder meta.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createFolder" method="post" path="/api/v1/folder" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_folder(request={
        "name": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FolderDtoInput](../../models/folderdtoinput.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseFolderDto](../../models/baseresponsefolderdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_folder

Deletes the folder with the provided ID.  If the folder is not found, this is a
no-op. <b>All files and sub-folders are also recursively deleted.</b>

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteFolder" method="delete" path="/api/v1/folder/{folderId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_folder(folder_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the folder                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_folder

Returns a folder with the provided ID, or a 404 if no matching folder is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getFolder" method="get" path="/api/v1/folder/{folderId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_folder(folder_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the folder                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseFolderDto](../../models/baseresponsefolderdto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_folder

Updates the folder that matches the provided ID with the details provided in the
body.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_updateFolder" method="put" path="/api/v1/folder/{folderId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.update_folder(folder_id="<id>", folder_dto={
        "name": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the folder                                 |
| `folder_dto`                                                        | [models.FolderDtoInput](../../models/folderdtoinput.md)             | :heavy_check_mark:                                                  | The representation of the folder to update                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseFolderDto](../../models/baseresponsefolderdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_children

Returns a paged list of all children whose parent ID matches the provided folder
ID.  If the folder ID in the path is the literal 'null' value, returns a list of
all entities with no parent.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listChildren" method="get" path="/api/v1/folder/{folderId}/children" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_children(folder_id="<id>", limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `folder_id`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier of the folder                                           |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of folders to return, from 1 to 1000; by default, 1000             |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataListChildrenResponse](../../models/wdatalistchildrenresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## set_children

Sets the children of a folder using the entities' types and IDs provided in the
body. If the entities previously resided under a folder, including the root,
they move to the folder with the provided ID. If the provided ID is 'null',
the entities move to the root folder.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_setChildren" method="post" path="/api/v1/folder/{folderId}/children" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.set_children(folder_id="<id>", request_body=[
        {
            "id": "<id>",
            "type": 247955,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `folder_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the folder                                   |
| `request_body`                                                        | List[[models.FolderableDtoInput](../../models/folderabledtoinput.md)] | :heavy_check_mark:                                                    | The representation of the entities to drop into the folder            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |
| `server_url`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | An optional server URL to use.                                        |

### Response

**[models.BaseResponseCollectionFolderableDto](../../models/baseresponsecollectionfolderabledto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_parameters

Returns a list of all parameters associated with the workspace.  By default, these
parameters are ordered by their names in ascending order.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listParameters" method="get" path="/api/v1/parameter" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_parameters(limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `cursor`                                                                                  | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | A paging cursor; if included the limit is ignored                                         |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | The number of parameters to return, must be between 1 and 1000, will default<br/>to 1000  |
| `offset`                                                                                  | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | The item to start with on the page, must be greater than or equal to 0, will default to 0 |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |
| `server_url`                                                                              | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | An optional server URL to use.                                                            |

### Response

**[models.WdataListParametersResponse](../../models/wdatalistparametersresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_parameter

Creates a parameter.  If there is a parameter with the same ID, a 409 is returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createParameter" method="post" path="/api/v1/parameter" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_parameter(request={
        "mode": models.GlobalParameterDtoMode.SINGLE_SELECT,
        "name": "<value>",
        "type": models.GlobalParameterDtoType.NESTED_QUERY_PARAMETER,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GlobalParameterDtoInput](../../models/globalparameterdtoinput.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |
| `server_url`                                                              | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | An optional server URL to use.                                            |

### Response

**[models.BaseResponseGlobalParameterDto](../../models/baseresponseglobalparameterdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_parameter

Deletes the parameter with the provided parameter ID.  If the parameter is not found, this is a no-op.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteParameter" method="delete" path="/api/v1/parameter/{parameterId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_parameter(parameter_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `parameter_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the parameter                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_parameter

Returns a parameter matching the provided parameter ID.  If no matching entity can be found, a 404 status is returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getParameter" method="get" path="/api/v1/parameter/{parameterId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_parameter(parameter_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `parameter_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the parameter                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseGlobalParameterDto](../../models/baseresponseglobalparameterdto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_parameter

Updates the parameter matching the provided ID in the provided payload.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_updateParameter" method="put" path="/api/v1/parameter/{parameterId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.update_parameter(parameter_id="<id>", global_parameter_dto={
        "mode": models.GlobalParameterDtoMode.MULTI_SELECT,
        "name": "<value>",
        "type": models.GlobalParameterDtoType.DATE,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `parameter_id`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | The unique identifier of the parameter                                    |
| `global_parameter_dto`                                                    | [models.GlobalParameterDtoInput](../../models/globalparameterdtoinput.md) | :heavy_check_mark:                                                        | The representation of the parameter to update                             |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |
| `server_url`                                                              | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | An optional server URL to use.                                            |

### Response

**[models.BaseResponseGlobalParameterDto](../../models/baseresponseglobalparameterdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_pivot_views

Returns a paged list of views in the workspace of the request. If queryId is provided, the results are limited to only views associated with the query ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listPivotViews" method="get" path="/api/v1/pivotview" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_pivot_views(query_id="<id>", limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `query_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | The unique query identifier to filter the views                               |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of views to return, from 1 to 1000; by default, 1000               |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataListPivotViewsResponse](../../models/wdatalistpivotviewsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_pivot_view

Creates a view from the provided information. Currently, persists the provided
`additionalMetadata` field, which can store an arbitrary JSON definition of a pivot
table view. This pivot table must be associated with a query, and can optionally be
associated with a query result. When a query is deleted, its associated views are
also deleted.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createPivotView" method="post" path="/api/v1/pivotview" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_pivot_view(request={
        "name": "<value>",
        "query_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PivotViewDtoInput](../../models/pivotviewdtoinput.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponsePivotViewDto](../../models/baseresponsepivotviewdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_pivot_view

Deletes a view that matches the provided ID.  This is an administrative method and
should be assumed a hard-delete, given no capability to restore a deleted view is
available.  A no-op if no such view exists.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deletePivotView" method="delete" path="/api/v1/pivotview/{pivotViewId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_pivot_view(pivot_view_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pivot_view_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the pivot view                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_pivot_view

Returns a view with the provided ID, or a 404 if no view matches the ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getPivotView" method="get" path="/api/v1/pivotview/{pivotViewId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_pivot_view(pivot_view_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pivot_view_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the pivot view                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponsePivotViewDto](../../models/baseresponsepivotviewdto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_pivot_view

Updates the view that matches the provided ID with the details provided in the
body. The associated query can't be updated, so providing the query ID has no effect.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_updatePivotView" method="put" path="/api/v1/pivotview/{pivotViewId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.update_pivot_view(pivot_view_id="<id>", pivot_view_dto={
        "name": "<value>",
        "query_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pivot_view_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the pivot view                             |
| `pivot_view_dto`                                                    | [models.PivotViewDtoInput](../../models/pivotviewdtoinput.md)       | :heavy_check_mark:                                                  | The representation of the pivot view to create                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponsePivotViewDto](../../models/baseresponsepivotviewdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_queries

Returns a list of all non-temporary queries associated with the workspace. By default, these queries are ordered by their names, in ascending order.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listQueries" method="get" path="/api/v1/query" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_queries(limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of queries to return, from 1 to 1000; by default, 1000             |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `ids`                                                                         | List[*str*]                                                                   | :heavy_minus_sign:                                                            | A list of ids to filter the returned list by                                  |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataListQueriesResponse](../../models/wdatalistqueriesresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_query

Creates a query object and validates full permissions to ensure the requestor has
access to all data sources being queried. This endpoint _doesn't_ execute the query;
to execute, call the POST /queryresult method.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createQuery" method="post" path="/api/v1/query" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_query(request={
        "name": "<value>",
        "query_text": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.QueryDtoInput](../../models/querydtoinput.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryDto](../../models/baseresponsequerydto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_query_column_data

Returns a QueryColumnDataDto representing the column data for the given query text.
If the query isn't valid, returns a 400.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getQueryColumnData" method="post" path="/api/v1/query/data" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_query_column_data(request={
        "query_text": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.QueryTextDto](../../models/querytextdto.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryColumnDataDto](../../models/baseresponsequerycolumndatadto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## is_query_valid

Returns the provided QueryDto

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_isQueryValid" method="post" path="/api/v1/query/validation" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.is_query_valid(request={
        "name": "<value>",
        "query_text": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.QueryDtoInput](../../models/querydtoinput.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryDto](../../models/baseresponsequerydto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_query

Deletes the query that matches the provided ID. If no such query is found, this is
a no-op.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteQuery" method="delete" path="/api/v1/query/{queryId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_query(query_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_query

Returns a query that matches the provided ID, or a 404 if no matching query is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getQuery" method="get" path="/api/v1/query/{queryId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_query(query_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryDto](../../models/baseresponsequerydto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_query

Updates the query that matches the provided ID with the details provided in the
body.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_updateQuery" method="put" path="/api/v1/query/{queryId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.update_query(query_id="<id>", query_dto={
        "name": "<value>",
        "query_text": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query                                  |
| `query_dto`                                                         | [models.QueryDtoInput](../../models/querydtoinput.md)               | :heavy_check_mark:                                                  | The representation of the query to update                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryDto](../../models/baseresponsequerydto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_dependencies

Returns an unordered collection of all tables the matching query uses as datasources, including any shared tables outside of this OAuth token's workspace. The endpoint verifies the user has read permissions on the query, but _not_ on the tables returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getDependencies" method="get" path="/api/v1/query/{queryId}/dependencies" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_dependencies(query_id="<id>", limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `query_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier of the query                                            |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of dependencies to return, from 1 to 1000; by default, 1000        |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataGetDependenciesResponse](../../models/wdatagetdependenciesresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_tables_dependent_on_query

Returns a list of all tables that use the query with provided ID as a datasource.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getTablesDependentOnQuery" method="get" path="/api/v1/query/{queryId}/dependents" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_tables_dependent_on_query(query_id="<id>", limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `query_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier of the query                                            |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of folders to return, from 1 to 1000; by default, 1000             |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataGetTablesDependentOnQueryResponse](../../models/wdatagettablesdependentonqueryresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## describe_query

List the output columns of a query, including the column name (or alias), catalog, schema,
table, type, type size in bytes, and a boolean indicating if the column is aliased.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_describeQuery" method="post" path="/api/v1/query/{queryId}/describe" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.describe_query(query_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseDescribeQueryResponseDto](../../models/baseresponsedescribequeryresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_query_results

Returns a paged list of query results that match the provided query ID, or an empty
list if no matching query is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listQueryResults" method="get" path="/api/v1/queryresult" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_query_results(request={
        "query_id": "<id>",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.WdataListQueryResultsRequest](../../models/wdatalistqueryresultsrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |
| `server_url`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | An optional server URL to use.                                                      |

### Response

**[models.WdataListQueryResultsResponse](../../models/wdatalistqueryresultsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## run_query

Runs a query and immediately returns a query result entity, which has an ID that
can be used to poll the status from the GET /queryresult method. A status of
COMPLETED or ERROR indicates the query has completed.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_runQuery" method="post" path="/api/v1/queryresult" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.run_query(request={
        "query_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.QueryResultDtoInput](../../models/queryresultdtoinput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryResultDto](../../models/baseresponsequeryresultdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## cancel_query

Cancels a running query based on the provided result ID, and returns a cancelled
result unless the query's already in a COMPLETED state.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_cancelQuery" method="delete" path="/api/v1/queryresult/{queryResultId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.cancel_query(query_result_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_result_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query result                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryResultDto](../../models/baseresponsequeryresultdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_query_result

Returns a single query result that matches the provided ID, or a 404 if no such
query result is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getQueryResult" method="get" path="/api/v1/queryresult/{queryResultId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_query_result(query_result_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_result_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query result                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseQueryResultDto](../../models/baseresponsequeryresultdto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## download_query_result

Uses the Token Management API to create a token with the query result ID, which it
then uses to download a CSV file of the query results.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_downloadQueryResult" method="get" path="/api/v1/queryresult/{queryResultId}/download" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.download_query_result(query_result_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_result_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query result                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## export_query_result_to_spreadsheets

Exports a query result with the provided ID to Spreadsheets. To determine where to
export the results, the request body should include a URL copied and pasted from the
Spreadsheets UI. Returns a 404 if no matching query result is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_exportQueryResultToSpreadsheets" method="post" path="/api/v1/queryresult/{queryResultId}/export" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.export_query_result_to_spreadsheets(query_result_id="<id>", export_query_result_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_result_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the query result                           |
| `export_query_result_dto`                                           | [models.ExportQueryResultDto](../../models/exportqueryresultdto.md) | :heavy_check_mark:                                                  | The representation of the export query result                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_select_lists

Returns a list of select lists associated with the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listSelectLists" method="get" path="/api/v1/selectlist" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_select_lists()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of select lists to return, from 1 to 1000; by default, 1000        |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataListSelectListsResponse](../../models/wdatalistselectlistsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_select_list

Creates a select list using the provided information and returns the select list meta.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createSelectList" method="post" path="/api/v1/selectlist" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_select_list(request={
        "name": "<value>",
        "value_type": models.ValueType.INTEGER,
        "values": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SelectListDtoInput](../../models/selectlistdtoinput.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseSelectListDto](../../models/baseresponseselectlistdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Deletes a select list with the provided ID. If no such select list exists, this is
a no-op.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_delete" method="delete" path="/api/v1/selectlist/{selectListId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete(select_list_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `select_list_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the select list                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 409, 429 | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_select_list

Returns a select list that matches the provided ID, or a 404 if no matching select
list is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getSelectList" method="get" path="/api/v1/selectlist/{selectListId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_select_list(select_list_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `select_list_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the select list                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseSelectListDto](../../models/baseresponseselectlistdto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_select_list

Updates the select list with the provided ID with the details provided  in the
body.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_updateSelectList" method="put" path="/api/v1/selectlist/{selectListId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.update_select_list(select_list_id="<id>", select_list_dto={
        "name": "<value>",
        "value_type": models.ValueType.TIME,
        "values": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `select_list_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the select list                            |
| `select_list_dto`                                                   | [models.SelectListDtoInput](../../models/selectlistdtoinput.md)     | :heavy_check_mark:                                                  | The representation of the select list to update                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseSelectListDto](../../models/baseresponseselectlistdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_shared_tables

Returns a list of shared tables associated with the workspace of the request.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listSharedTables" method="get" path="/api/v1/sharedtable" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_shared_tables(request={})

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.WdataListSharedTablesRequest](../../models/wdatalistsharedtablesrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |
| `server_url`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | An optional server URL to use.                                                      |

### Response

**[models.WdataListSharedTablesResponse](../../models/wdatalistsharedtablesresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_shared_table

Creates a shared table instance between the workspace of the request and the workspace provided in the body.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createSharedTable" method="post" path="/api/v1/sharedtable" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_shared_table(request={
        "destination_workspace_id": "<id>",
        "source_table_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SharedTableDtoInput](../../models/sharedtabledtoinput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseSharedTableDto](../../models/baseresponsesharedtabledto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_shared_table

Deletes the linkages between the source and destination of a shared table that matches
the provided ID; the actual table itself is left intact. If no such shared table exists,
this is a no-op.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteSharedTable" method="delete" path="/api/v1/sharedtable/{sharedTableId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_shared_table(shared_table_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `shared_table_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the shared table                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_shared_table

Returns a shared table that matches the provided ID, or a 404 if no matching shared table is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getSharedTable" method="get" path="/api/v1/sharedtable/{sharedTableId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_shared_table(shared_table_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `shared_table_id`                                                                                                             | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | The unique identifier of the shared table                                                                                     |
| `shared_with_me`                                                                                                              | *Optional[bool]*                                                                                                              | :heavy_minus_sign:                                                                                                            | If true, returns a shared table with the provided ID that has been shared _to_—rather than from—the workspace of the request. |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |
| `server_url`                                                                                                                  | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | An optional server URL to use.                                                                                                |

### Response

**[models.BaseResponseSharedTableDto](../../models/baseresponsesharedtabledto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_tables

Returns all tables available in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getTables" method="get" path="/api/v1/table" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_tables(include_shared=False, limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `include_shared`                                                                                                                     | *Optional[bool]*                                                                                                                     | :heavy_minus_sign:                                                                                                                   | If true, returns all tables shared with the workspace associated with the request. If false, returns only tables the workspace owns. |
| `cursor`                                                                                                                             | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | a paging cursor; if included the limit is ignored                                                                                    |
| `limit`                                                                                                                              | *Optional[int]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | the number of folders to return, from 1 to 1000; by default, 1000                                                                    |
| `offset`                                                                                                                             | *Optional[int]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | The item to start with on the page, must be greater than or equal to 0, will default to 0                                            |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |
| `server_url`                                                                                                                         | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | An optional server URL to use.                                                                                                       |

### Response

**[models.WdataGetTablesResponse](../../models/wdatagettablesresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_table

Creates a table in the database with the specified schema. For type, specify either a dimension or data table. In the interface, data tables appear as fact tables.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createTable" method="post" path="/api/v1/table" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_table(request={
        "name": "<value>",
        "table_schema": {
            "columns": [],
        },
        "type": models.TableDtoType.HIERARCHY,
        "unique_table_constraints": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TableDtoInput](../../models/tabledtoinput.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseTableDto](../../models/baseresponsetabledto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_table

Soft-deletes the table with the provided ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteTable" method="delete" path="/api/v1/table/{tableId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_table(table_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the table                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_table

Returns a table with the provided ID, or a 404 if no such table is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getTable" method="get" path="/api/v1/table/{tableId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_table(table_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the table                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseTableDto](../../models/baseresponsetabledto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_table

Updates an existing table with the provided information. Include all user-defined
table columns with the request. For type, specify either a dimension or data table.
In the interface, data tables appear as fact tables. 
* If the table has no imported
data, user-defined columns not included with the request are deleted, and columns are
sorted according to their order in the request. 
* If the table has imported data,
any columns with names not already in the table are considered new. This equality
check is case-insensitive. Any new columns appear after other user-defined columns,
but before any meta columns, which start with `_`.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_updateTable" method="put" path="/api/v1/table/{tableId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.update_table(table_id="<id>", table_dto={
        "name": "<value>",
        "table_schema": {
            "columns": [
                {
                    "name": "<value>",
                    "type": models.ColumnDtoType.BOOLEAN,
                },
            ],
        },
        "type": models.TableDtoType.LOOKUP,
        "unique_table_constraints": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the table                                  |
| `table_dto`                                                         | [models.TableDtoInput](../../models/tabledtoinput.md)               | :heavy_check_mark:                                                  | The representation of the table to update                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseTableDto](../../models/baseresponsetabledto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_dependents

Returns a list of all queries that use the table with provided ID as a datasource.
If a shared table, this may include queries outside of the current OAuth context.
Permission is checked only for the table ID provided, _not_ on the returned list of
queries.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getDependents" method="get" path="/api/v1/table/{tableId}/dependents" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_dependents(table_id="<id>", limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `table_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier of the table                                            |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of folders to return, from 1 to 1000; by default, 1000             |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataGetDependentsResponse](../../models/wdatagetdependentsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## import_file

Imports the provided file into the associated table, and immediately returns a
file meta object with an ID that can be used to poll the file controller for status.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_importFile" method="post" path="/api/v1/table/{tableId}/import" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.import_file(table_id="<id>", import_dto={
        "column_mappings": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "file_id": "<id>",
        "tags": {
            "key": "value",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the table                                  |
| `import_dto`                                                        | [models.ImportDto](../../models/importdto.md)                       | :heavy_check_mark:                                                  | The representation of the table to import                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseFileMetaDto](../../models/baseresponsefilemetadto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## unimport_file

Unimports the provided file from the provided table. Returns a 409 if the file is
not in an imported state, or a 404 if the file can't be found.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_unimportFile" method="delete" path="/api/v1/table/{tableId}/import/{fileId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.unimport_file(table_id="<id>", file_id="<id>", force="false")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the table                                  |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |
| `force`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | If true, unimports and deletes file from the table                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseFileMetaDto](../../models/baseresponsefilemetadto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_import_info

Returns information around imported files for a table.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_getImportInfo" method="get" path="/api/v1/table/{tableId}/importInfo" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.get_import_info(table_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the table                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseImportInfoDto](../../models/baseresponseimportinfodto.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## import_from_spreadsheets

Imports spreadsheet data and immediately returns a file meta result. This DTO has
an ID, which can be used to poll on status via the file controller.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_importFromSpreadsheets" method="post" path="/api/v1/table/{tableId}/spreadsheet/import" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.import_from_spreadsheets(table_id="<id>", import_from_spreadsheet_dto={
        "name": "<value>",
        "url": "https://great-certification.org",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `table_id`                                                                  | *str*                                                                       | :heavy_check_mark:                                                          | The unique identifier of the table                                          |
| `import_from_spreadsheet_dto`                                               | [models.ImportFromSpreadsheetDto](../../models/importfromspreadsheetdto.md) | :heavy_check_mark:                                                          | The representation of the table to update                                   |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |
| `server_url`                                                                | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | An optional server URL to use.                                              |

### Response

**[models.BaseResponseFileMetaDto](../../models/baseresponsefilemetadto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_tags

Returns a paged list of all tags associated with the workspace of the request.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_listTags" method="get" path="/api/v1/tag" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.list_tags(limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of tags to return, from 1 to 1000; by default, 1000                |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.WdataListTagsResponse](../../models/wdatalisttagsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 403, 404, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## create_tag

Creates a tag. If another tag already has the same key, returns a 409. There is a limit of 300 values for a tag.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createTag" method="post" path="/api/v1/tag" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_tag(request={
        "key": "<key>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TagDtoInput](../../models/tagdtoinput.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseTagDto](../../models/baseresponsetagdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_tag

Deletes the tag with the provided ID. If no such tag is found, this is a no-op.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_deleteTag" method="delete" path="/api/v1/tag/{tagId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.delete_tag(tag_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tag_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the tag                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.SingleError | 401, 403, 429      | application/json   |
| errors.SingleError | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_tag

Updates the tag that matches the provided ID with the details provided in the body.
Ignores the provided key, as keys are immutable once set.
There is a limit of 300 values for a tag.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_updateTag" method="put" path="/api/v1/tag/{tagId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.update_tag(tag_id="<id>", tag_dto={
        "key": "<key>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tag_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the tag                                    |
| `tag_dto`                                                           | [models.TagDtoInput](../../models/tagdtoinput.md)                   | :heavy_check_mark:                                                  | The representation of the tag to update                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseTagDto](../../models/baseresponsetagdto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## create_token

Creates a temporary token—valid for only a short period of time—to download a table
dataset file or query result, given its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_createToken" method="post" path="/api/v1/token" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.create_token(request={
        "object_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TokenDtoInput](../../models/tokendtoinput.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseTokenDto](../../models/baseresponsetokendto.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## download_file

Downloads a table dataset or query result as a file, given its token from the [`Create a new token endpoint`](ref:wdata-createtoken). If no matching entity is found, returns a 404.

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_downloadFile" method="get" path="/api/v1/token/{tokenId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.download_file(token_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `token_id`                                                                   | *str*                                                                        | :heavy_check_mark:                                                           | The unique identifier of the token                                           |
| `filename`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | A filename for the download; if included, the default filename is overridden |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |
| `server_url`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | An optional server URL to use.                                               |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## parse_date

Provides a simple endpoint to check whether a given date candidate parses with
the provided format string.  Both the date candidate and format strings are required.
Returns a 200 if the date parses, or a 400 with a message if not. If the date parses,
the provided format can be provided as column metadata, and the imported values parse
correctly. The format string is java DateTimeFormatter style e.g. dateFormat =
"MM/dd/yyyy" and candidate = "07/28/1987"

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_parseDate" method="post" path="/api/v1/util/datetime" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.parse_date(request={
        "candidate": "<value>",
        "date_format": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DatetimeDto](../../models/datetimedto.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseString](../../models/baseresponsestring.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.MultiError       | 400                     | application/json        |
| errors.SingleError      | 401, 403, 404, 409, 429 | application/json        |
| errors.SingleError      | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## health_check

Returns the status of the API WSGI servers

### Example Usage

<!-- UsageSnippet language="python" operationID="wdata_healthCheck" method="get" path="/health" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.health_check()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.BaseResponseMapStringString](../../models/baseresponsemapstringstring.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |