# Operations

## Overview

Use these endpoints to manage operations, such as to check their status.

### Available Operations

* [get_batch_upsertion_metric_values_results](#get_batch_upsertion_metric_values_results) - Retrieve the results of a metric values batch upsertion operation
* [get_copy_file_results](#get_copy_file_results) - Retrieve copy file results for a single operation
* [get_destination_link_source_conversion_results](#get_destination_link_source_conversion_results) - Retrieves the results from a destination link source conversion.
* [get_image_upload_creation_results](#get_image_upload_creation_results) - Retrieve results for a image upload
* [get_import_file_results](#get_import_file_results) - Retrieve import file results for a single operation
* [get_milestone_creation_results](#get_milestone_creation_results) - Retrieve results for a milestone creation
* [get_operation_by_id](#get_operation_by_id) - Retrieve a single operation
* [get_patch_document_results](#get_patch_document_results) - Retrieve results for a patch document
* [get_patch_presentation_results](#get_patch_presentation_results) - Retrieve results for a patch presentation
* [get_patch_section_results](#get_patch_section_results) - Retrieve results for a patch Section
* [get_patch_sheet_results](#get_patch_sheet_results) - Retrieve results for a patch sheet
* [get_patch_slide_layout_results](#get_patch_slide_layout_results) - Retrieve results for a patch slide layout
* [get_patch_slide_results](#get_patch_slide_results) - Retrieve results for a patch slide
* [get_patch_spreadsheet_results](#get_patch_spreadsheet_results) - Retrieve results for a patch spreadsheet
* [get_patch_table_properties_results](#get_patch_table_properties_results) - Retrieve results for a patch table properties
* [get_range_link_edit_results](#get_range_link_edit_results) - Retrieve results for a range link edit
* [get_rich_text_anchor_creation_results](#get_rich_text_anchor_creation_results) - Retrieve results for a rich text anchor creation
* [get_rich_text_batch_edit_results](#get_rich_text_batch_edit_results) - Retrieve results for a rich text batch edit
* [get_rich_text_duplication_edit_results](#get_rich_text_duplication_edit_results) - Retrieve results for a rich text duplication edit
* [get_rich_text_links_batch_edit_results](#get_rich_text_links_batch_edit_results) - Retrieve results for a rich text links batch edit
* [get_table_anchor_creation_results](#get_table_anchor_creation_results) - Retrieve results for a table anchor creation
* [get_table_cell_edit_results](#get_table_cell_edit_results) - Retrieve results for a table cell edit
* [get_table_edit_results](#get_table_edit_results) - Retrieve results for a table edit
* [get_table_links_edit_results](#get_table_links_edit_results) - Retrieve results for a table links edit
* [get_table_reapply_filter_results](#get_table_reapply_filter_results) - Retrieve results for a table reapply filter

## get_batch_upsertion_metric_values_results

Returns a [`MetricValuesListResult`](ref:sustainability#metricvalueslistresult) describing the results of a metric values batch upsertion operation. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 1 request per second. When polling for updates, examine the `Retry-After` header and retry after that many seconds.


### Example Usage

<!-- UsageSnippet language="python" operationID="getBatchUpsertionMetricValuesResults" method="get" path="/operations/{operationId}/metricValuesBatchUpsertionResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_batch_upsertion_metric_values_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetBatchUpsertionMetricValuesResultsResponse](../../models/getbatchupsertionmetricvaluesresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_copy_file_results

Returns a [`CopyFileListResult`](ref:operations#copyfilelistresult) describing the results of a file copy operation. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 1 request per second. When polling for updates, examine the `Retry-After` header and retry after that many seconds.


### Example Usage

<!-- UsageSnippet language="python" operationID="getCopyFileResults" method="get" path="/operations/{operationId}/copyFileResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_copy_file_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCopyFileResultsResponse](../../models/getcopyfileresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_destination_link_source_conversion_results

Returns the results for a destination link source conversion.
This will include the new source anchor's ID and the destination link ID for the old source (if any).


### Example Usage

<!-- UsageSnippet language="python" operationID="getDestinationLinkSourceConversionResults" method="get" path="/operations/{operationId}/destinationLinkSourceConversionResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_destination_link_source_conversion_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDestinationLinkSourceConversionResultsResponse](../../models/getdestinationlinksourceconversionresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_image_upload_creation_results

Returns a [`ImageUploadResultCollection`](ref:operations#imageuploadresultcollection) describing the results of a image upload.

### Example Usage

<!-- UsageSnippet language="python" operationID="getImageUploadCreationResults" method="get" path="/operations/{operationId}/imageUploadResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_image_upload_creation_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetImageUploadCreationResultsResponse](../../models/getimageuploadcreationresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_import_file_results

Returns a [`ImportFileListResult`](ref:operations#importfilelistresult) describing the results of a file import operation. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 1 request per second. When polling for updates, examine the `Retry-After` header and retry after that many seconds.


### Example Usage

<!-- UsageSnippet language="python" operationID="getImportFileResults" method="get" path="/operations/{operationId}/importFileResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_import_file_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetImportFileResultsResponse](../../models/getimportfileresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_milestone_creation_results

Returns a [`MilestoneCreationListResult`](ref:operations#milestonecreationlistresult) describing the results of a milestone creation.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMilestoneCreationResults" method="get" path="/operations/{operationId}/milestoneCreationResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_milestone_creation_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetMilestoneCreationResultsResponse](../../models/getmilestonecreationresultsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 401, 403, 404   | application/json     |
| errors.ErrorResponse | 500                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## get_operation_by_id

Retrieves an [operation](ref:operations#operation) given its ID. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 1 request per second. When polling for updates, examine the `Retry-After` header and retry after that many seconds.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOperationById" method="get" path="/operations/{operationId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_operation_by_id(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOperationByIDResponse](../../models/getoperationbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_document_results

Returns a [`PatchDocumentListResult`](ref:operations#patchdocumentlistresult) describing the results of a patch document.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchDocumentResults" method="get" path="/operations/{operationId}/patchDocumentResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_document_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchDocumentListResult](../../models/patchdocumentlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_presentation_results

Returns a [`PatchPresentationListResult`](ref:operations#patchpresentationlistresult) describing the results of a patch presentation.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchPresentationResults" method="get" path="/operations/{operationId}/patchPresentationResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_presentation_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchPresentationListResult](../../models/patchpresentationlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_section_results

Returns a [`PatchSectionListResult`](ref:operations#patchsectionlistresult) describing the results of a patch section.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchSectionResults" method="get" path="/operations/{operationId}/patchSectionResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_section_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchSectionListResult](../../models/patchsectionlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_sheet_results

Returns a [`PatchSheetListResult`](ref:operations#patchsheetlistresult) describing the results of a patch sheet.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchSheetResults" method="get" path="/operations/{operationId}/patchSheetResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_sheet_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchSheetListResult](../../models/patchsheetlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_slide_layout_results

Returns a [`PatchSlideLayoutListResult`](ref:operations#patchslidelayoutlistresult) describing the results of a patch slide layout.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchSlideLayoutResults" method="get" path="/operations/{operationId}/patchSlideLayoutResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_slide_layout_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchSlideLayoutListResult](../../models/patchslidelayoutlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_slide_results

Returns a [`PatchSlideListResult`](ref:operations#patchslidelistresult) describing the results of a patch slide.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchSlideResults" method="get" path="/operations/{operationId}/patchSlideResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_slide_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchSlideListResult](../../models/patchslidelistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_spreadsheet_results

Returns a [`PatchSpreadsheetListResult`](ref:operations#patchspreadsheetlistresult) describing the results of a patch spreadsheet.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchSpreadsheetResults" method="get" path="/operations/{operationId}/patchSpreadsheetResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_spreadsheet_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchSpreadsheetListResult](../../models/patchspreadsheetlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_patch_table_properties_results

Returns a [`PatchTablePropertiesListResult`](ref:operations#patchtablepropertieslistresult) describing the results of a patch table properties.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPatchTablePropertiesResults" method="get" path="/operations/{operationId}/patchTablePropertiesResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_patch_table_properties_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchTablePropertiesListResult](../../models/patchtablepropertieslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_range_link_edit_results

Returns a [`RangeLinkEditResultCollection`](ref:operations#rangelinkeditresultcollection) describing the results of a range link edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRangeLinkEditResults" method="get" path="/operations/{operationId}/rangeLinkEditResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_range_link_edit_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRangeLinkEditResultsResponse](../../models/getrangelinkeditresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_rich_text_anchor_creation_results

Returns a [`RichTextAnchorCreationResultCollection`](ref:operations#richtextanchorcreationresultcollection) describing the results of a rich text anchor creation.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextAnchorCreationResults" method="get" path="/operations/{operationId}/richTextAnchorCreationResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_rich_text_anchor_creation_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRichTextAnchorCreationResultsResponse](../../models/getrichtextanchorcreationresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_rich_text_batch_edit_results

Returns a [`RichTextEditListResult`](ref:operations#richtexteditlistresult) describing the results of a rich text batch edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextBatchEditResults" method="get" path="/operations/{operationId}/richTextBatchEditResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_rich_text_batch_edit_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRichTextBatchEditResultsResponse](../../models/getrichtextbatcheditresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_rich_text_duplication_edit_results

Returns a [`RichTextDuplicationEditListResult`](ref:operations#richtextduplicationeditlistresult) describing the results of a rich text duplication edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextDuplicationEditResults" method="get" path="/operations/{operationId}/richTextDuplicationEditResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_rich_text_duplication_edit_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRichTextDuplicationEditResultsResponse](../../models/getrichtextduplicationeditresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_rich_text_links_batch_edit_results

Returns a [`RichTextLinksEditListResult`](ref:operations#richtextlinkseditlistresult) describing the results of a rich text batch edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextLinksBatchEditResults" method="get" path="/operations/{operationId}/richTextLinksBatchEditResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_rich_text_links_batch_edit_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRichTextLinksBatchEditResultsResponse](../../models/getrichtextlinksbatcheditresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_anchor_creation_results

Returns a [`TableAnchorCreationResultCollection`](ref:operations#tableanchorcreationresultcollection) describing the results of a table anchor creation.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableAnchorCreationResults" method="get" path="/operations/{operationId}/tableAnchorCreationResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_table_anchor_creation_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetTableAnchorCreationResultsResponse](../../models/gettableanchorcreationresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_cell_edit_results

Returns a [`TableCellEditListResult`](ref:operations#tablecelleditlistresult) describing the results of a table cell edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableCellEditResults" method="get" path="/operations/{operationId}/tableCellEditResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_table_cell_edit_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableCellEditListResult](../../models/tablecelleditlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_edit_results

Returns a [`TableEditListResult`](ref:operations#tableeditlistresult) describing the results of a table edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableEditResults" method="get" path="/operations/{operationId}/tableEditResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_table_edit_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableEditListResult](../../models/tableeditlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_links_edit_results

Returns a [`TableLinksEditListResult`](ref:operations#tablelinkseditlistresult) describing the results of a table links edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableLinksEditResults" method="get" path="/operations/{operationId}/tableLinksEditResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_table_links_edit_results(operation_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetTableLinksEditResultsResponse](../../models/gettablelinkseditresultsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_reapply_filter_results

Returns a [`TableReapplyFilterListResult`](ref:operations#tablereapplyfilterlistresult) describing the results of a table reapply filter.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableReapplyFilterResults" method="get" path="/operations/{operationId}/tableReapplyFilterResults" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.operations.get_table_reapply_filter_results(operation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `operation_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the operation                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableReapplyFilterListResult](../../models/tablereapplyfilterlistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |