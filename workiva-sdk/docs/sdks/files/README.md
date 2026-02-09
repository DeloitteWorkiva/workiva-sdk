# Files

## Overview

Endpoints to manage files and folders.

### Available Operations

* [get_files](#get_files) - Retrieve a list of files
* [create_file](#create_file) - Create a new file
* [import_file](#import_file) - Initiate a file import
* [get_trashed_files](#get_trashed_files) - Retrieve a list of trashed files
* [get_file_by_id](#get_file_by_id) - Retrieve a single file
* [partially_update_file_by_id](#partially_update_file_by_id) - Partially update a single file
* [copy_file](#copy_file) - Initiate a file copy
* [export_file_by_id](#export_file_by_id) - Initiate a file export by ID
* [restore_file_by_id](#restore_file_by_id) - Initiate restoration of a single file
* [trash_file_by_id](#trash_file_by_id) - Initiate trash of a single file
* [get_file_permissions](#get_file_permissions) - Retrieve permissions for a file
* [file_permissions_modification](#file_permissions_modification) - Modify permissions on a file

## get_files

Returns a paginated list of [files](ref:files#file).

### Example Usage

<!-- UsageSnippet language="python" operationID="getFiles" method="get" path="/files" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.get_files(maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

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

**[models.GetFilesResponse](../../models/getfilesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_file

Creates a new [file](ref:files#file). Requires name and kind. kind
must be one of `Document`, `Spreadsheet`, `Presentation`, or `Folder` and
is case-sensitive. Use the `container` attribute to specify the container that houses the file, such
as a folder. If empty, the root folder is the container. Files are created
asynchronously and may not immediately be available on a subsequent `GET`.

### Examples
#### Create a new document at the root of the file system
```json
{
  "name": "2019 Year-End Summary",
  "kind": "Document"
}
```

#### Create a folder within an existing folder
```json
{
  "name": "2019 Year-End Documents",
  "kind": "Folder",
  "container": "V0ZFYXRhSW50aXR5IkZvbGRlcjoxSkFGOTZGRjiENDk1Qzk4RjQ4OTgzN0M6ODdDNjZENi"
}
```


### Example Usage

<!-- UsageSnippet language="python" operationID="createFile" method="post" path="/files" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.create_file(request={
        "kind": models.Kind.DOCUMENT,
        "name": "Year-end review",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FileInput](../../models/fileinput.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.File](../../models/file.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## import_file

Import a file for conversion to a Workiva equivalent. This is a long running operation.
Response includes an `uploadUrl` which indicates where to upload the file for import. To upload the file, perform a PUT against the `uploadUrl` with the same authentication credentials and flow as the import request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="importFile" method="post" path="/files/import" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.import_file(request={
        "file_name": "signed_contract.pdf",
        "kind": models.FileImportKind.SUPPORTING_DOCUMENT,
        "supporting_document_import_options": {
            "container_id": "V0ZEYXRhRW5zVkNmU2Zi1mZjcE4EzNzk0ZmUwZjk",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FileImport](../../models/fileimport.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ImportFileResponse](../../models/importfileresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_trashed_files

Returns a paginated list of files that have been trashed.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTrashedFiles" method="get" path="/files/trash" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.get_trashed_files(maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetTrashedFilesResponse](../../models/gettrashedfilesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_file_by_id

Retrieves a [file](ref:files#file) given its ID


### Example Usage

<!-- UsageSnippet language="python" operationID="getFileById" method="get" path="/files/{fileId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.get_file_by_id(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.File](../../models/file.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_file_by_id

Partially updates the properties of a [file](ref:files#file). Only one property may be updated at a time.
Updates are applied asynchronously and may not immediately be reflected on a subsequent `GET`.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/container`|`replace`|
|`/name`|`replace`|


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateFileById" method="patch" path="/files/{fileId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.partially_update_file_by_id(file_id="<id>", request_body=[
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

<!-- UsageSnippet language="python" operationID="partiallyUpdateFileById" method="patch" path="/files/{fileId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.partially_update_file_by_id(file_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/container",
            "value": "",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `file_id`                                                                                                     | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The unique identifier of the file                                                                             |
| `request_body`                                                                                                | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]                                         | :heavy_check_mark:                                                                                            | A collection of patch operations to apply to the file. Currently only one operation may be applied at a time. |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.File](../../models/file.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## copy_file

Copy a file to a new location. This is a long running operation. Responses include a `Location` header, which indicates where to poll for copy results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).
Once the operation is completed, the `resourceUrl` field will be populated with a link to the   [Retrieve copy file results for a single operation endpoint](ref:getcopyfileresults)  to see the results of the File Copy Request.


### Example Usage

<!-- UsageSnippet language="python" operationID="copyFile" method="post" path="/files/{fileId}/copy" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.copy_file(file_id="<id>", file_copy={
        "destination_container": "V0ZEYXRhRW50aXR5HkZvbGRlcjox",
        "options": {
            "email_on_complete": True,
            "include_attachments": True,
            "include_comments": True,
            "include_document_markup": True,
            "include_input_cell_values": True,
            "include_outline_labels": True,
            "include_smart_link_metadata": True,
            "include_wdata_incoming_connections": True,
            "include_wdata_outgoing_connections": True,
            "include_xbrl": True,
            "include_xbrl_disconnected": True,
            "include_automations": True,
            "keep_input_mode_enabled": True,
            "remove_grc_links": True,
            "remove_links": True,
            "shallow_copy": True,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The unique identifier of the file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `file_copy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [models.FileCopy](../../models/filecopy.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The details of the file copy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | {<br/>"destinationContainer": "V0ZEYXRhRW50aXR5HkZvbGRlcjox",<br/>"options": {<br/>"emailOnComplete": true,<br/>"includeAttachments": true,<br/>"includeComments": true,<br/>"includeCustomFieldValues": true,<br/>"includeDocumentMarkup": true,<br/>"includeInputCellValues": true,<br/>"includeOutlineLabels": true,<br/>"includeSmartLinkMetadata": true,<br/>"includeWdataIncomingConnections": true,<br/>"includeWdataOutgoingConnections": true,<br/>"includeXBRL": true,<br/>"includeXBRLDisconnected": true,<br/>"includeAutomations": true,<br/>"keepInputModeEnabled": true,<br/>"removeGRCLinks": true,<br/>"removeLinks": true,<br/>"shallowCopy": true<br/>}<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Response

**[models.CopyFileResponse](../../models/copyfileresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## export_file_by_id

Export a file by its unique ID. This is a long running operation. Responses include a `Location` header, which indicates where to poll for export results. For  more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).
When the export process is complete, the status of the Operation  will change to completed. The `resourceUrl` field of the operation will contain  the download url of the exported file. To download the file, perform a GET against  the `resourceUrl` with the same authentication credentials and flow as the export request.  For more details, see Authentication documentation.
For more on Document, Spreadsheet, and Presentation export options, see the following: [Documents](https://developers.workiva.com/2026-01-01/platform-documentexport), [Spreadsheets](https://developers.workiva.com/2026-01-01/platform-spreadsheetexport), and [Presentations](https://developers.workiva.com/2026-01-01/platform-presentationexport).


### Example Usage

<!-- UsageSnippet language="python" operationID="exportFileById" method="post" path="/files/{fileId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.export_file_by_id(file_id="<id>", file_export_by_id={
        "kind": models.FileExportByIDKind.SUPPORTING_DOCUMENT,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |                                                                     |
| `file_export_by_id`                                                 | [models.FileExportByID](../../models/fileexportbyid.md)             | :heavy_check_mark:                                                  | The details of the file export.                                     | {<br/>"kind": "SupportingDocument"<br/>}                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ExportFileByIDResponse](../../models/exportfilebyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## restore_file_by_id

Restores a file given its ID. If the file being restored is a Folder, its contents will be recursively restored.

### Example Usage

<!-- UsageSnippet language="python" operationID="restoreFileById" method="post" path="/files/{fileId}/restore" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.restore_file_by_id(file_id="<id>", file_restore_options={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |
| `file_restore_options`                                              | [models.FileRestoreOptions](../../models/filerestoreoptions.md)     | :heavy_check_mark:                                                  | Request body for File restore endpoint                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RestoreFileByIDResponse](../../models/restorefilebyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## trash_file_by_id

Trashes a file given its ID. If the file being trashed is a Folder, its contents will be recursively trashed.

### Example Usage

<!-- UsageSnippet language="python" operationID="trashFileById" method="post" path="/files/{fileId}/trash" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.trash_file_by_id(file_id="<id>", file_trash_options={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `file_id`                                                             | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the file                                     |
| `file_trash_options`                                                  | [Nullable[models.FileTrashOptions]](../../models/filetrashoptions.md) | :heavy_check_mark:                                                    | The request body for the file trash endpoint                          |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.TrashFileByIDResponse](../../models/trashfilebyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_file_permissions

Retrieves a paginated list of permissions for a given file


### Example Usage

<!-- UsageSnippet language="python" operationID="getFilePermissions" method="get" path="/files/{fileId}/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.files.get_file_permissions(file_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the file                                   |                                                                     |
| `filter_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The properties to filter the results by.                            |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetFilePermissionsResponse](../../models/getfilepermissionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## file_permissions_modification

Assign and/or revoke permissions on a file. If any modification in a request fails, all modifications on that request fail. <br /><br /> _To modify an existing permission, the existing permission must first be  explicitly revoked. Then, the new permission needs to be assigned. This  can be done in a single request by sending `toAssign` and `toRevoke` in  the request body._


### Example Usage

<!-- UsageSnippet language="python" operationID="filePermissionsModification" method="post" path="/files/{fileId}/permissions/modification" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.files.file_permissions_modification(file_id="<id>", resource_permissions_modification={
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
| `file_id`                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the file                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                        |
| `resource_permissions_modification`                                                                                                                                                                                                                    | [models.ResourcePermissionsModification](../../models/resourcepermissionsmodification.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                     | Details about the file permissions modification.                                                                                                                                                                                                       | {<br/>"toAssign": [<br/>{<br/>"permission": "598e8fa3-3e7c-4fb7-b662-f44522216e2b",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>],<br/>"toRevoke": [<br/>{<br/>"permission": "85aa87ee-beb9-4417-8fa0-420e9de63534",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |