# Documents

## Overview

Documents enable you to organize and review data in collaborative files with linked text, documents, and images. Use these endpoints to manage documents and their sections in the Workiva Platform.

### Available Operations

* [get_documents](#get_documents) - Retrieve a list of documents
* [get_document_by_id](#get_document_by_id) - Retrieve a single document
* [partially_update_document_by_id](#partially_update_document_by_id) - Partially update a single document
* [document_export](#document_export) - Initiate a document export
* [document_filters_reapplication](#document_filters_reapplication) - Reapply filters to the document
* [document_links_publication](#document_links_publication) - Initiate publication of links in a document
* [get_document_milestones](#get_document_milestones) - Retrieve a list of milestones for a document
* [get_document_permissions](#get_document_permissions) - Retrieve permissions for a document
* [document_permissions_modification](#document_permissions_modification) - Modify permissions on a document
* [get_sections](#get_sections) - Retrieve a list of sections
* [create_section](#create_section) - Create a new section in a document
* [delete_section_by_id](#delete_section_by_id) - Delete a single section
* [get_section_by_id](#get_section_by_id) - Retrieve a single section
* [partially_update_section_by_id](#partially_update_section_by_id) - Partially update a single section
* [copy_section](#copy_section) - Copy section
* [edit_sections](#edit_sections) - Initiate sections edits
* [get_section_permissions](#get_section_permissions) - Retrieve permissions for a section in a document
* [section_permissions_modification](#section_permissions_modification) - Modify permissions on a given section of a document

## get_documents

Returns a paginated list of [documents](ref:documents#document).

### Example Usage

<!-- UsageSnippet language="python" operationID="getDocuments" method="get" path="/documents" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.get_documents(dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `dollar_filter`                                                                             | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The properties to filter the results by.                                                    |                                                                                             |
| `dollar_order_by`                                                                           | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | One or more comma-separated expressions to indicate the order in which to sort the results. |                                                                                             |
| `dollar_maxpagesize`                                                                        | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The maximum number of results to retrieve                                                   |                                                                                             |
| `dollar_next`                                                                               | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Pagination cursor for next set of results.                                                  | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.GetDocumentsResponse](../../models/getdocumentsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_document_by_id

Retrieves a [document](ref:documents#document) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDocumentById" method="get" path="/documents/{documentId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.get_document_by_id(document_id="<id>", dollar_expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |                                                                     |
| `dollar_expand`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Document](../../models/document.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_document_by_id

Updates the properties of a [document](ref:documents#document).

This is a long running operation. Responses include a `Location` header,
which indicates where to poll for results. For more details on long-running job polling,
see [Operations endpoint](ref:getoperationbyid).

### Options

|Path                             |PATCH Operations Supported        |
|---------------------------------|----------------------------------|
|`/customFields/<custom field id>`|`add`, `remove`, `replace`, `test`|
|`/customFieldGroups`             |`add`, `remove`, `replace`, `test`|
|`/sectionCustomFieldGroups`      |`add`, `remove`, `replace`, `test`|
|`/lock`                          |`replace`                         |

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

<!-- UsageSnippet language="python" operationID="partiallyUpdateDocumentById" method="patch" path="/documents/{documentId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.partially_update_document_by_id(document_id="<id>", request_body=[
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

<!-- UsageSnippet language="python" operationID="partiallyUpdateDocumentById" method="patch" path="/documents/{documentId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.partially_update_document_by_id(document_id="<id>", request_body=[
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
| `document_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the document                                 |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the document.            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PartiallyUpdateDocumentByIDResponse](../../models/partiallyupdatedocumentbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## document_export

Asynchronously exports a [document](ref:documents#document) as .PDF or .DOCX., or .XHTML. Options are specified using a [DocumentExport](ref:documents#documentexport) object.
When exporting XHTML that you plan to edit or modify, use the `editableXhtml` option. Otherwise, the export retains fidelity so it visually matches the document as it appears in the browser.
Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="documentExport" method="post" path="/documents/{documentId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.document_export(document_id="<id>", document_export={
        "docx_options": {
            "include_leader_dots": True,
            "show_table_cell_shading": True,
        },
        "format_": models.DocumentExportFormat.DOCX,
        "sections": [
            "a8b3adb687644b27fafcb3a9875f0f0d_18",
            "a8b3adb687644b27fafcb3a9875f0f0d_19",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    | Example                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                                                                                  | *str*                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                             | The unique identifier of the document                                                                                                                                                          |                                                                                                                                                                                                |
| `document_export`                                                                                                                                                                              | [models.DocumentExport](../../models/documentexport.md)                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                             | Details about the document export.                                                                                                                                                             | {<br/>"docxOptions": {<br/>"includeLeaderDots": true,<br/>"showTableCellShading": true<br/>},<br/>"format": "docx",<br/>"sections": [<br/>"a8b3adb687644b27fafcb3a9875f0f0d_18",<br/>"a8b3adb687644b27fafcb3a9875f0f0d_19"<br/>]<br/>} |
| `retries`                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                            |                                                                                                                                                                                                |

### Response

**[models.DocumentExportResponse](../../models/documentexportresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## document_filters_reapplication

Performs a [`DocumentFiltersReapplication`](ref:content#documentfiltersreapplication) on the specified document.
This endpoint is used to refresh the document's filters based on the latest state or configuration changes.
The filters are reapplied in the context of the document's current data state.

This is a long-running operation. Responses include a `Location` header, which indicates where to poll for results.
For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="documentFiltersReapplication" method="post" path="/documents/{documentId}/filters/reapplication" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.document_filters_reapplication(document_id="<id>", document_filters_reapplication={
        "force_hide_footnotes": True,
        "ignore_non_editable_filters": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `document_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | The unique identifier of the document                                               |                                                                                     |
| `document_filters_reapplication`                                                    | [models.DocumentFiltersReapplication](../../models/documentfiltersreapplication.md) | :heavy_check_mark:                                                                  | The filter reapplication request to apply                                           | {<br/>"forceHideFootnotes": true,<br/>"ignoreNonEditableFilters": true<br/>}        |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.DocumentFiltersReapplicationResponse](../../models/documentfiltersreapplicationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## document_links_publication

Publishes the links in a document - either all (as document owner) or only one's own. Content at the latest document revision will be used for publish.
The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="documentLinksPublication" method="post" path="/documents/{documentId}/links/publication" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.document_links_publication(document_id="<id>", links_publication_options={
        "publish_type": models.PublishType.ALL_LINKS,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `document_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | The unique identifier of the document                                     |
| `links_publication_options`                                               | [models.LinksPublicationOptions](../../models/linkspublicationoptions.md) | :heavy_check_mark:                                                        | Details about the link publication.                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.DocumentLinksPublicationResponse](../../models/documentlinkspublicationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_document_milestones

Returns [MilestoneListResult](ref:milestones#milestonelistresult).

### Example Usage

<!-- UsageSnippet language="python" operationID="getDocumentMilestones" method="get" path="/documents/{documentId}/milestones" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.get_document_milestones(document_id="<id>", dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDocumentMilestonesResponse](../../models/getdocumentmilestonesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_document_permissions

Retrieves a paginated list of permissions for a given document


### Example Usage

<!-- UsageSnippet language="python" operationID="getDocumentPermissions" method="get" path="/documents/{documentId}/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.get_document_permissions(document_id="<id>", dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |                                                                     |
| `dollar_filter`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The properties to filter the results by.                            |                                                                     |
| `dollar_maxpagesize`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDocumentPermissionsResponse](../../models/getdocumentpermissionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## document_permissions_modification

Assign and/or revoke permissions on a document. If any modification in a request fails, all modifications on that request fail. <br /><br /> _To modify an existing permission, the existing permission must first be  explicitly revoked. Then, the new permission needs to be assigned. This  can be done in a single request by sending `toAssign` and `toRevoke` in  the request body._


### Example Usage

<!-- UsageSnippet language="python" operationID="documentPermissionsModification" method="post" path="/documents/{documentId}/permissions/modification" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.documents.document_permissions_modification(document_id="<id>", resource_permissions_modification={
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
| `document_id`                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the document                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                        |
| `resource_permissions_modification`                                                                                                                                                                                                                    | [models.ResourcePermissionsModification](../../models/resourcepermissionsmodification.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                     | Details about the document permissions modification.                                                                                                                                                                                                   | {<br/>"toAssign": [<br/>{<br/>"permission": "598e8fa3-3e7c-4fb7-b662-f44522216e2b",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>],<br/>"toRevoke": [<br/>{<br/>"permission": "85aa87ee-beb9-4417-8fa0-420e9de63534",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sections

Returns a list of [sections](ref:documents#section).


### Example Usage

<!-- UsageSnippet language="python" operationID="getSections" method="get" path="/documents/{documentId}/sections" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.get_sections(document_id="<id>", dollar_revision="1A2B3C4D", dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |                                                                     |
| `dollar_revision`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `dollar_maxpagesize`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSectionsResponse](../../models/getsectionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_section

Creates a new [section](ref:documents#section) in a [document](ref:documents#document), given its properties. By default, the new section appears at the top-most position.


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="createSection" method="post" path="/documents/{documentId}/sections" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.create_section(document_id="<id>", section={
        "id": "a8b3adb687644b27fafcb3a9875f0f0d_18",
        "index": 1,
        "name": "Risk factors",
        "non_printing": True,
    })

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="createSection" method="post" path="/documents/{documentId}/sections" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.create_section(document_id="<id>", section={
        "name": "Risk Factor",
        "parent": {
            "id": "a8b3adb687644b27fafcb3a9875f0f0d_18",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |
| `section`                                                           | [models.SectionInput](../../models/sectioninput.md)                 | :heavy_check_mark:                                                  | The properties of the section to create                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Section](../../models/section.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_section_by_id

Deletes a [section](ref:documents#section) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSectionById" method="delete" path="/documents/{documentId}/sections/{sectionId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.documents.delete_section_by_id(document_id="<id>", section_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |
| `section_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the section                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_section_by_id

Retrieves a [section](ref:documents#section) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSectionById" method="get" path="/documents/{documentId}/sections/{sectionId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.get_section_by_id(document_id="<id>", section_id="<id>", dollar_expand="?$expand=relationships\n", dollar_revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |                                                                     |
| `section_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the section                                |                                                                     |
| `dollar_expand`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `dollar_revision`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Section](../../models/section.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_section_by_id

Updates the properties of a [section](ref:documents#section).

This is a long running operation. Responses include a `Location` header,
which indicates where to poll for results. For more details on long-running job polling,
see [Operations endpoint](ref:getoperationbyid).

### Options

| Path                                     | PATCH Operations Supported         |
|------------------------------------------|------------------------------------|
| `/name`                                  | `replace`                          |
| `/parent`                                | `replace`                          |
| `/parent/id`                             | `replace`                          |
| `/index`                                 | `replace`                          |
| `/nonPrinting`                           | `replace`                          |
| `/customFields`                          | `add`, `remove`, `replace`, `test` |
| `/customFields/<customFieldId>`          | `add`, `remove`, `replace`, `test` |
| `/lock`                                  | `replace`                          |
| `/properties/margins/top`                | `replace`                          |
| `/properties/margins/bottom`             | `replace`                          |
| `/properties/margins/right`              | `replace`                          |
| `/properties/margins/left`               | `replace`                          |
| `/properties/pageBreakBefore`            | `replace`                          |
| `/properties/exhibit`                    | `replace`                          |
| `/properties/edgarKeepTogether`          | `replace`                          |
| `/properties/pageNumber/reset`           | `replace`                          |
| `/properties/pageNumber/startAt`         | `replace`                          |
| `/properties/background/color`           | `replace`                          |
| `/properties/background/image`           | `replace`                          |
| `/properties/restartFootnoteNumbering`   | `replace`                          |
| `/properties/header/alternatingPage`     | `replace`                          |
| `/properties/header/differentFirstPage`  | `replace`                          |
| `/properties/header/differentLastPage`   | `replace`                          |
| `/properties/header/margin/right`        | `replace`                          |
| `/properties/header/margin/left`         | `replace`                          |
| `/properties/header/matchSectionMargins` | `replace`                          |
| `/properties/header/positionFromTop`     | `replace`                          |
| `/properties/header/sameAsPrevious`      | `replace`                          |
| `/properties/footer/alternatingPage`     | `replace`                          |
| `/properties/footer/differentFirstPage`  | `replace`                          |
| `/properties/footer/differentLastPage`   | `replace`                          |
| `/properties/footer/margin/right`        | `replace`                          |
| `/properties/footer/margin/left`         | `replace`                          |
| `/properties/footer/matchSectionMargins` | `replace`                          |
| `/properties/footer/positionFromBottom`  | `replace`                          |
| `/properties/footer/sameAsPrevious`      | `replace`                          |

### Examples

#### Update the name of a section

```json
[
  {
    "op": "replace",
    "path": "/name",
    "value": "Introduction"
  }
]
```

#### Update the parent of a section (preserving its index)

```json
[
  {
    "op": "replace",
    "path": "/parent",
    "value": {
      "id": "b9b3ddb587744a27aafda3c9865f1f0a_1"
    }
  }
]
```

#### Update the parent of a section (making it the first child)

```json
[
  {
    "op": "replace",
    "path": "/parent",
    "value": {
      "id": "b9b3ddb587744a27aafda3c9865f1f0a_1"
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

<!-- UsageSnippet language="python" operationID="partiallyUpdateSectionById" method="patch" path="/documents/{documentId}/sections/{sectionId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.partially_update_section_by_id(document_id="<id>", section_id="<id>", request_body=[
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

<!-- UsageSnippet language="python" operationID="partiallyUpdateSectionById" method="patch" path="/documents/{documentId}/sections/{sectionId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.partially_update_section_by_id(document_id="<id>", section_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "My Section",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `document_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the document                                 |
| `section_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the section                                  |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the section.             |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PartiallyUpdateSectionByIDResponse](../../models/partiallyupdatesectionbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## copy_section

Asynchronously copies a [section](ref:documents#section) given details about the copy's destination within the same or another document. Options are specified using a [SectionCopy](ref:documents#sectioncopy) object.

Copies only the section's content — not any labels, comments, tasks, or formatting from a style guide. Unless otherwise specified, the copy appears at the top level of its destination document, with an index of 0, and with the same name as the original section.

### Example Usage

<!-- UsageSnippet language="python" operationID="copySection" method="post" path="/documents/{documentId}/sections/{sectionId}/copy" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.copy_section(document_id="<id>", section_id="<id>", section_copy={
        "document": "327afa1a152f372fa1aeadb35ed28925d",
        "section_index": 2,
        "section_name": "October 2020",
        "section_parent": "327afa1a152f372fa1aeadb35ed28925d_1",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |
| `section_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the section                                |
| `section_copy`                                                      | [models.SectionCopy](../../models/sectioncopy.md)                   | :heavy_check_mark:                                                  | A SectionCopy object                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CopySectionResponse](../../models/copysectionresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## edit_sections

Updates the properties of a collection of [sections](ref:documents#section) in a document using [SectionsEdits](ref:documents#sectionsedit) request. This is a long running operation.
Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the update completes, its status will be `completed`.


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="editSections" method="post" path="/documents/{documentId}/sections/edit" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.edit_sections(document_id="<id>", sections_edits={
        "data": [
            {
                "set_non_printing": {
                    "non_printing": True,
                    "selection": [
                        "9fdff0887cb5425292dfb1fdd759753a_35",
                        "9fdff0887cb5425292dfb1fdd759753a_50",
                    ],
                },
                "type": models.SectionEditType.SET_NON_PRINTING,
            },
            {
                "set_non_printing": {
                    "non_printing": False,
                    "selection": [
                        "9fdff0887cb5425292dfb1fdd759753a_45",
                        "9fdff0887cb5425292dfb1fdd759753a_40",
                    ],
                },
                "type": models.SectionEditType.SET_NON_PRINTING,
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="editSections" method="post" path="/documents/{documentId}/sections/edit" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.edit_sections(document_id="<id>", sections_edits={
        "data": [
            {
                "set_non_printing": {
                    "non_printing": True,
                    "selection": [
                        "9fdff0887cb5425292dfb1fdd759753a_35",
                        "9fdff0887cb5425292dfb1fdd759753a_50",
                    ],
                },
                "type": models.SectionEditType.SET_NON_PRINTING,
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                              | The unique identifier of the document                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                 |
| `sections_edits`                                                                                                                                                                                                                                                                                                                                                | [models.SectionsEdits](../../models/sectionsedits.md)                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                              | The edits for one or more sections in a document                                                                                                                                                                                                                                                                                                                | {<br/>"data": [<br/>{<br/>"setNonPrinting": {<br/>"nonPrinting": true,<br/>"selection": [<br/>"9fdff0887cb5425292dfb1fdd759753a_35",<br/>"9fdff0887cb5425292dfb1fdd759753a_50"<br/>]<br/>},<br/>"type": "setNonPrinting"<br/>},<br/>{<br/>"setNonPrinting": {<br/>"nonPrinting": false,<br/>"selection": [<br/>"9fdff0887cb5425292dfb1fdd759753a_45",<br/>"9fdff0887cb5425292dfb1fdd759753a_40"<br/>]<br/>},<br/>"type": "setNonPrinting"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.EditSectionsResponse](../../models/editsectionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_section_permissions

Retrieves a paginated list of permissions for the given section in a document


### Example Usage

<!-- UsageSnippet language="python" operationID="getSectionPermissions" method="get" path="/documents/{documentId}/sections/{sectionId}/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.documents.get_section_permissions(request={
        "document_id": "<id>",
        "section_id": "<id>",
        "dollar_next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.GetSectionPermissionsRequest](../../models/getsectionpermissionsrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GetSectionPermissionsResponse](../../models/getsectionpermissionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## section_permissions_modification

Assign and/or revoke permissions on a section. If any modification in a request fails, all modifications on that request fail. <br /><br /> _To modify an existing permission, the existing permission must first be  explicitly revoked. Then, the new permission needs to be assigned. This  can be done in a single request by sending `toAssign` and `toRevoke` in  the request body._


### Example Usage

<!-- UsageSnippet language="python" operationID="sectionPermissionsModification" method="post" path="/documents/{documentId}/sections/{sectionId}/permissions/modification" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    sdk.documents.section_permissions_modification(document_id="<id>", section_id="<id>", resource_permissions_modification={
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
| `document_id`                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the document                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                        |
| `section_id`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The unique identifier of the section                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                        |
| `resource_permissions_modification`                                                                                                                                                                                                                    | [models.ResourcePermissionsModification](../../models/resourcepermissionsmodification.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                     | Details about the section permissions modification.                                                                                                                                                                                                    | {<br/>"toAssign": [<br/>{<br/>"permission": "598e8fa3-3e7c-4fb7-b662-f44522216e2b",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>],<br/>"toRevoke": [<br/>{<br/>"permission": "85aa87ee-beb9-4417-8fa0-420e9de63534",<br/>"principal": "V0ZVc2VyHzU2NDg2NjU2MjQ0NDQ5Mjg"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |