# Presentations

## Overview

Endpoints to manage presentations

### Available Operations

* [get_presentation_by_id](#get_presentation_by_id) - Retrieve a single presentation
* [get_presentation_milestones](#get_presentation_milestones) - Retrieve a list of milestones for a presentation
* [get_slide_by_id](#get_slide_by_id) - Retrieve a single slide
* [get_slide_layout_by_id](#get_slide_layout_by_id) - Retrieve a single slide layout
* [get_slide_layouts](#get_slide_layouts) - Retrieve a list of slide layouts
* [get_slides](#get_slides) - Retrieve a list of slides
* [partially_update_presentation_by_id](#partially_update_presentation_by_id) - Partially updates a single presentation
* [partially_update_slide_by_id](#partially_update_slide_by_id) - Partially update a single slide
* [partially_update_slide_layout_by_id](#partially_update_slide_layout_by_id) - Partially update a single slide layout
* [presentation_export](#presentation_export) - Initiate a presentation export
* [presentation_filters_reapplication](#presentation_filters_reapplication) - Reapply filters to the presentation
* [presentation_links_publication](#presentation_links_publication) - Initiate publication of links in a presentation

## get_presentation_by_id

Retrieves a presentation given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPresentationById" method="get" path="/presentations/{presentationId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.get_presentation_by_id(presentation_id="<id>", dollar_revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `presentation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the presentation                           |                                                                     |
| `dollar_revision`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Presentation](../../models/presentation.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_presentation_milestones

Returns [MilestoneListResult](ref:milestones#milestonelistresult).

### Example Usage

<!-- UsageSnippet language="python" operationID="getPresentationMilestones" method="get" path="/presentations/{presentationId}/milestones" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.get_presentation_milestones(presentation_id="<id>", dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `presentation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the presentation                           |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetPresentationMilestonesResponse](../../models/getpresentationmilestonesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_slide_by_id

Retrieves a slide given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSlideById" method="get" path="/presentations/{presentationId}/slides/{slideId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.get_slide_by_id(presentation_id="<id>", slide_id="<id>", dollar_revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `presentation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the presentation                           |                                                                     |
| `slide_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the slide                                  |                                                                     |
| `dollar_revision`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Slide](../../models/slide.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_slide_layout_by_id

Retrieves a slide layout given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSlideLayoutById" method="get" path="/presentations/{presentationId}/slideLayouts/{slideLayoutId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.get_slide_layout_by_id(presentation_id="<id>", slide_layout_id="<id>", dollar_revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `presentation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the presentation                           |                                                                     |
| `slide_layout_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the slide layout                           |                                                                     |
| `dollar_revision`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SlideLayout](../../models/slidelayout.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_slide_layouts

Returns a list of slide layouts.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSlideLayouts" method="get" path="/presentations/{presentationId}/slideLayouts" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.get_slide_layouts(presentation_id="<id>", dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", dollar_revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `presentation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the presentation                           |                                                                     |
| `dollar_maxpagesize`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `dollar_revision`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSlideLayoutsResponse](../../models/getslidelayoutsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_slides

Returns a list of slides.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSlides" method="get" path="/presentations/{presentationId}/slides" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.get_slides(presentation_id="<id>", dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", dollar_revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `presentation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the presentation                           |                                                                     |
| `dollar_maxpagesize`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `dollar_next`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `dollar_revision`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSlidesResponse](../../models/getslidesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_presentation_by_id

Updates the properties of a [presentation](ref:presentations#presentation).

This is a long running operation. Responses include a `Location` header,
which indicates where to poll for results. For more details on long-running
job polling, see [Operations endpoint](ref:getoperationbyid).


### Options

| Path                              | PATCH Operations Supported         |
|-----------------------------------|------------------------------------|
| `/customFields/<custom field id>` | `add`, `remove`, `replace`, `test` |
| `/customFieldGroups`              | `add`, `remove`, `replace`, `test` |
| `/slideCustomFieldGroups`         | `add`, `remove`, `replace`, `test` |
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


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdatePresentationById" method="patch" path="/presentations/{presentationId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.partially_update_presentation_by_id(presentation_id="<id>", request_body=[
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
| `presentation_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the presentation                             |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the presentation.        |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PartiallyUpdatePresentationByIDResponse](../../models/partiallyupdatepresentationbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_slide_by_id

Updates one or more properties of a single slide.

This is a long running operation. Responses include a `Location` header,
which indicates where to poll for results. For more details on long-running
job polling, see [Operations endpoint](ref:getoperationbyid).

### Options

| Path                              | PATCH Operations Supported         |
|-----------------------------------|------------------------------------|
| `/name`                           | `replace`                          |
| `/index`                          | `replace`                          |
| `/parent`                         | `replace`                          |
| `/customFields/<custom field id>` | `add`, `remove`, `replace`, `test` |
| `/lock`                           | `replace`                          |

### Examples

#### Update the name of a slide

```json
[
  {
    "op": "replace",
    "path": "/name",
    "value": "Risk Factor"
  }
]
```

#### Update the parent of a slide (preserving its index)

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

#### Update the parent of a slide (making it the first child)

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


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateSlideById" method="patch" path="/presentations/{presentationId}/slides/{slideId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.partially_update_slide_by_id(presentation_id="<id>", slide_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Slide 1",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `presentation_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the presentation                             |
| `slide_id`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the slide                                    |
| `request_body`                                                        | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                    | A collection of patch operations to apply to the slide.               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PartiallyUpdateSlideByIDResponse](../../models/partiallyupdateslidebyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_slide_layout_by_id

Updates one or more properties of a single slide layout.

This is a long running operation. Responses include a `Location` header,
which indicates where to poll for results. For more details on long-running
job polling, see [Operations endpoint](ref:getoperationbyid).

### Options

| Path            | PATCH Operations Supported |
|-----------------|----------------------------|
| `/name`         | `replace`                  |
| `/index`        | `replace`                  |
| `/lock`         | `replace`                  |


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateSlideLayoutById" method="patch" path="/presentations/{presentationId}/slideLayouts/{slideLayoutId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.partially_update_slide_layout_by_id(presentation_id="<id>", slide_layout_id="<id>", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/name",
            "value": "Slide Layout Name",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `presentation_id`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the presentation                              |
| `slide_layout_id`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the slide layout                              |
| `request_body`                                                         | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]  | :heavy_check_mark:                                                     | Patch document representing the changes to be made to the slide layout |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.PartiallyUpdateSlideLayoutByIDResponse](../../models/partiallyupdateslidelayoutbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## presentation_export

Asynchronously export a presentation as .PDF or .PPTX. Options are specified using a [PresentationExport](ref:presentations#presentationexport) object.

Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [ Operations endpoint ](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="presentationExport" method="post" path="/presentations/{presentationId}/export" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.presentation_export(presentation_id="<id>", presentation_export={
        "format_": models.PresentationExportFormat.PPTX,
        "pptx_options": {
            "include_unused_layout_slides": True,
        },
        "slides": [
            "a8b3adb687644b27fafcb3a9875f0f0d_18",
            "a8b3adb687644b27fafcb3a9875f0f0d_19",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            | Example                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `presentation_id`                                                                                                                                                      | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | The unique identifier of the presentation                                                                                                                              |                                                                                                                                                                        |
| `presentation_export`                                                                                                                                                  | [models.PresentationExport](../../models/presentationexport.md)                                                                                                        | :heavy_check_mark:                                                                                                                                                     | Details about the presentation export.                                                                                                                                 | {<br/>"format": "pptx",<br/>"pptxOptions": {<br/>"includeUnusedLayoutSlides": true<br/>},<br/>"slides": [<br/>"a8b3adb687644b27fafcb3a9875f0f0d_18",<br/>"a8b3adb687644b27fafcb3a9875f0f0d_19"<br/>]<br/>} |
| `retries`                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                    |                                                                                                                                                                        |

### Response

**[models.PresentationExportResponse](../../models/presentationexportresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## presentation_filters_reapplication

Performs a [`PresentationFiltersReapplication`](ref:content#presentationfiltersreapplication) on the specified presentation.
This endpoint is used to refresh the presentation's filters based on the latest state or configuration changes.
The filters are reapplied in the context of the presentation's current data state.

This is a long-running operation. Responses include a `Location` header, which indicates where to poll for results.
For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="presentationFiltersReapplication" method="post" path="/presentations/{presentationId}/filters/reapplication" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.presentation_filters_reapplication(presentation_id="<id>", presentation_filters_reapplication={
        "ignore_non_editable_filters": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `presentation_id`                                                                           | *str*                                                                                       | :heavy_check_mark:                                                                          | The unique identifier of the presentation                                                   |                                                                                             |
| `presentation_filters_reapplication`                                                        | [models.PresentationFiltersReapplication](../../models/presentationfiltersreapplication.md) | :heavy_check_mark:                                                                          | The filter reapplication request to apply                                                   | {<br/>"ignoreNonEditableFilters": true<br/>}                                                |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.PresentationFiltersReapplicationResponse](../../models/presentationfiltersreapplicationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## presentation_links_publication

Publishes the links in a presentation - either all (as document owner) or only one's own. Content at the latest presentation revision will be used for publish.
The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="presentationLinksPublication" method="post" path="/presentations/{presentationId}/links/publication" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.presentations.presentation_links_publication(presentation_id="<id>", links_publication_options={
        "publish_type": models.PublishType.OWN_LINKS,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `presentation_id`                                                         | *str*                                                                     | :heavy_check_mark:                                                        | The unique identifier of the presentation                                 |
| `links_publication_options`                                               | [models.LinksPublicationOptions](../../models/linkspublicationoptions.md) | :heavy_check_mark:                                                        | Details about the link publication.                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.PresentationLinksPublicationResponse](../../models/presentationlinkspublicationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |