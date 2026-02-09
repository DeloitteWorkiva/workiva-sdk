# Content

## Overview

Endpoints for reading and writing Workiva content. See [**Introduction to Content Endpoints**](ref:content-guide) for more information.

### Available Operations

* [destination_link_source_conversion](#destination_link_source_conversion) - Initiate a destination link conversion
* [get_anchor_by_id](#get_anchor_by_id) - Retrieve an anchor by ID
* [get_column_properties](#get_column_properties) - Retrieve table column properties
* [get_destination_link_by_id](#get_destination_link_by_id) - Retrieve a destination link by id
* [get_drawing_anchor_by_id](#get_drawing_anchor_by_id) - Retrieve a drawing anchor by ID
* [get_drawing_anchor_extensions](#get_drawing_anchor_extensions) - Retrieve a list of drawing anchor extensions
* [get_drawing_anchors](#get_drawing_anchors) - Retrieve a list of drawing anchors
* [get_drawing_elements_by_id](#get_drawing_elements_by_id) - Retrieve drawing elements by id
* [get_image_by_id](#get_image_by_id) - Retrieve an image by id
* [get_range_link_by_id](#get_range_link_by_id) - Retrieve a range link by id
* [get_range_link_destinations](#get_range_link_destinations) - Retrieve range link destinations for a source
* [get_range_links](#get_range_links) - Retrieve a list of range links
* [get_rich_text_anchor_by_id](#get_rich_text_anchor_by_id) - Retrieve a rich text anchor by id
* [get_rich_text_anchor_extensions](#get_rich_text_anchor_extensions) - Retrieve a list of rich text anchor extensions
* [get_rich_text_anchors](#get_rich_text_anchors) - Retrieve a list of rich text anchors
* [get_rich_text_paragraphs](#get_rich_text_paragraphs) - Retrieve rich text paragraphs
* [get_row_properties](#get_row_properties) - Retrieve table row properties
* [get_style_guide_by_id](#get_style_guide_by_id) - Retrieve a style guide by id
* [get_table_anchor_by_id](#get_table_anchor_by_id) - Retrieve a table anchor by ID
* [get_table_anchor_extensions](#get_table_anchor_extensions) - Retrieve a list of table anchor extensions
* [get_table_anchors](#get_table_anchors) - Retrieve a list of table anchors
* [get_table_cells](#get_table_cells) - Retrieve table cell content
* [get_table_properties](#get_table_properties) - Retrieve a table's properties by id
* [image_upload](#image_upload) - Initiate upload of an image
* [partially_update_table_properties](#partially_update_table_properties) - Partially update a table's properties
* [rich_text_anchor_creation](#rich_text_anchor_creation) - Initiate creation of a new rich text anchor
* [rich_text_batch_edit](#rich_text_batch_edit) - Initiate edits to rich text
* [rich_text_duplication_edit](#rich_text_duplication_edit) - Initiate duplication edits to rich text
* [rich_text_links_batch_edit](#rich_text_links_batch_edit) - Initiate edits to rich text links
* [style_guide_export](#style_guide_export) - Initiate a style guide export
* [style_guide_import](#style_guide_import) - Initiate import of a style guide
* [table_anchor_creation](#table_anchor_creation) - Initiate creation of a new table anchor
* [table_cells_batch_edit](#table_cells_batch_edit) - Initiate edits to table cells
* [table_edit](#table_edit) - Initiate edit to a table
* [table_filters_reapplication](#table_filters_reapplication) - Reapply filters to the table
* [table_links_batch_edit](#table_links_batch_edit) - Initiate edit to table links
* [table_range_links_edit](#table_range_links_edit) - Initiate range links edits on a table

## destination_link_source_conversion

Converts a destination link into a source link. The previous source, if any, will be converted into a destination link.

Responses include a `Location` header, which indicates where to poll for results. For more details on long-running
job polling, see [Operations endpoint](ref:getoperationbyid). When the source conversion
completes, its status will be `completed`, and the response body includes a `resourceURL`. For more details on the `resourceURL`
see [operation results endpoint](ref:getdestinationlinksourceconversionresults).
For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="destinationLinkSourceConversion" method="post" path="/content/destinationLinks/{destinationLinkId}/sourceConversion" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.destination_link_source_conversion(destination_link_id="WA5SVkJWXOy5MbSHX25Qf9BVz5xTvLfJadt5eXzqTxLT4o2Lo1ceQHmLbSppCdBhQUFBSE")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `destination_link_id`                                                  | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the destination link                          | WA5SVkJWXOy5MbSHX25Qf9BVz5xTvLfJadt5eXzqTxLT4o2Lo1ceQHmLbSppCdBhQUFBSE |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[models.DestinationLinkSourceConversionResponse](../../models/destinationlinksourceconversionresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_anchor_by_id

Returns an [`Anchor`](ref:content#anchor) given its id.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnchorById" method="get" path="/content/anchors/{anchorId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_anchor_by_id(anchor_id="<id>", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `anchor_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the anchor                                 |                                                                     |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Anchor](../../models/anchor.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_column_properties

Returns a [`ColumnPropertiesListResult`](ref:content#columnpropertieslistresult) for a table


### Example Usage

<!-- UsageSnippet language="python" operationID="getColumnProperties" method="get" path="/content/tables/{tableId}/properties/columns" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_column_properties(request={
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "revision": "1A2B3C4D",
        "start_column": 1,
        "stop_column": 1,
        "table_id": "WW91IGZvdW5kfIG1lIQ",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.GetColumnPropertiesRequest](../../models/getcolumnpropertiesrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.GetColumnPropertiesResponse](../../models/getcolumnpropertiesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_destination_link_by_id

Returns a [`DestinationLink`](ref:content#destinationlink) given its id

### Example Usage

<!-- UsageSnippet language="python" operationID="getDestinationLinkById" method="get" path="/content/destinationLinks/{destinationLinkId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_destination_link_by_id(destination_link_id="WA5SVkJWXOy5MbSHX25Qf9BVz5xTvLfJadt5eXzqTxLT4o2Lo1ceQHmLbSppCdBhQUFBSE", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `destination_link_id`                                                  | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the destination link                          | WA5SVkJWXOy5MbSHX25Qf9BVz5xTvLfJadt5eXzqTxLT4o2Lo1ceQHmLbSppCdBhQUFBSE |
| `revision`                                                             | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Returns resources at a specific revision                               | 1A2B3C4D                                                               |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[models.DestinationLink](../../models/destinationlink.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_drawing_anchor_by_id

Returns an [`Anchor`](ref:content#anchor) given its id.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDrawingAnchorById" method="get" path="/content/drawings/{drawingId}/anchors/{anchorId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_drawing_anchor_by_id(anchor_id="<id>", drawing_id="<id>", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `anchor_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the anchor                                 |                                                                     |
| `drawing_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of a drawing                                  |                                                                     |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Anchor](../../models/anchor.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_drawing_anchor_extensions

Returns a paginated list of [`AnchorExtensions`](ref:content#anchorextension) for a given anchorId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDrawingAnchorExtensions" method="get" path="/content/drawings/{drawingId}/anchors/{anchorId}/extensions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_drawing_anchor_extensions(request={
        "anchor_id": "<id>",
        "drawing_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "revision": "1A2B3C4D",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.GetDrawingAnchorExtensionsRequest](../../models/getdrawinganchorextensionsrequest.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.GetDrawingAnchorExtensionsResponse](../../models/getdrawinganchorextensionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_drawing_anchors

Returns an [`AnchorsListResult`](ref:content#anchorslistresult) for a given drawingId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDrawingAnchors" method="get" path="/content/drawings/{drawingId}/anchors" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_drawing_anchors(drawing_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `drawing_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of a drawing                                  |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDrawingAnchorsResponse](../../models/getdrawinganchorsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_drawing_elements_by_id

Returns a [`DrawingElementListResult`](ref:content#drawingelementlistresult) given its id

### Example Usage

<!-- UsageSnippet language="python" operationID="getDrawingElementsById" method="get" path="/content/drawings/{drawingId}/elements" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_drawing_elements_by_id(drawing_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `drawing_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of a drawing                                  |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDrawingElementsByIDResponse](../../models/getdrawingelementsbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_image_by_id

Returns a [`Image`](ref:content#image) given its id

### Example Usage

<!-- UsageSnippet language="python" operationID="getImageById" method="get" path="/content/images/{imageId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_image_by_id(image_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `image_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the image                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Image](../../models/image.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_range_link_by_id

Returns a [`RangeLink`](ref:content#rangelink) given its id

### Example Usage

<!-- UsageSnippet language="python" operationID="getRangeLinkById" method="get" path="/content/tables/{tableId}/rangeLinks/{rangeLinkId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_range_link_by_id(range_link_id="f649093edf354cfe8ce52fa60990a109", table_id="WW91IGZvdW5kfIG1lIQ", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `range_link_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of a range link.                              | f649093edf354cfe8ce52fa60990a109                                    |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the table                                 | WW91IGZvdW5kfIG1lIQ                                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RangeLink](../../models/rangelink.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse    | 400, 401, 403, 404, 429 | application/json        |
| errors.ErrorResponse    | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_range_link_destinations

Returns a [`RangeLinkListResult`](ref:content#rangelinklistresult) of destinations for a given source range link.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRangeLinkDestinations" method="get" path="/content/tables/{tableId}/rangeLinks/{rangeLinkId}/destinations" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_range_link_destinations(request={
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "range_link_id": "f649093edf354cfe8ce52fa60990a109",
        "revision": "1A2B3C4D",
        "table_id": "WW91IGZvdW5kfIG1lIQ",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.GetRangeLinkDestinationsRequest](../../models/getrangelinkdestinationsrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.GetRangeLinkDestinationsResponse](../../models/getrangelinkdestinationsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse    | 400, 401, 403, 404, 429 | application/json        |
| errors.ErrorResponse    | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_range_links

Returns a [`RangeLinkListResult`](ref:content#rangelinklistresult) for a given tableId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRangeLinks" method="get" path="/content/tables/{tableId}/rangeLinks" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_range_links(table_id="WW91IGZvdW5kfIG1lIQ", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the table                                 | WW91IGZvdW5kfIG1lIQ                                                 |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRangeLinksResponse](../../models/getrangelinksresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse    | 400, 401, 403, 404, 429 | application/json        |
| errors.ErrorResponse    | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_rich_text_anchor_by_id

Returns an [`Anchor`](ref:content#anchor) given its id.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextAnchorById" method="get" path="/content/richText/{richTextId}/anchors/{anchorId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_rich_text_anchor_by_id(anchor_id="<id>", rich_text_id="<id>", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `anchor_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the anchor                                 |                                                                     |
| `rich_text_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the rich text content                      |                                                                     |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Anchor](../../models/anchor.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_rich_text_anchor_extensions

Returns a paginated list of [`AnchorExtensions`](ref:content#anchorextension) for a given anchorId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextAnchorExtensions" method="get" path="/content/richText/{richTextId}/anchors/{anchorId}/extensions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_rich_text_anchor_extensions(request={
        "anchor_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "revision": "1A2B3C4D",
        "rich_text_id": "<id>",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.GetRichTextAnchorExtensionsRequest](../../models/getrichtextanchorextensionsrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.GetRichTextAnchorExtensionsResponse](../../models/getrichtextanchorextensionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_rich_text_anchors

Returns an [`AnchorsListResult`](ref:content#anchorslistresult) for a given richTextId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextAnchors" method="get" path="/content/richText/{richTextId}/anchors" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_rich_text_anchors(rich_text_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `rich_text_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the rich text content                      |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRichTextAnchorsResponse](../../models/getrichtextanchorsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_rich_text_paragraphs

Returns a [`ParagraphsListResult`](ref:content#paragraphslistresult) for a rich text object, given its id.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRichTextParagraphs" method="get" path="/content/richText/{richTextId}/paragraphs" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_rich_text_paragraphs(rich_text_id="<id>", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `rich_text_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the rich text content                      |                                                                     |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRichTextParagraphsResponse](../../models/getrichtextparagraphsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_row_properties

Returns a [`RowPropertiesListResult`](ref:content#rowpropertieslistresult) for a table


### Example Usage

<!-- UsageSnippet language="python" operationID="getRowProperties" method="get" path="/content/tables/{tableId}/properties/rows" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_row_properties(request={
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "revision": "1A2B3C4D",
        "start_row": 1,
        "stop_row": 1,
        "table_id": "WW91IGZvdW5kfIG1lIQ",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetRowPropertiesRequest](../../models/getrowpropertiesrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GetRowPropertiesResponse](../../models/getrowpropertiesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_style_guide_by_id

Returns the [`StyleGuide`](ref:content#styleguide) populated with the text styles, list styles, etc. The revision will ensure a static content.


### Example Usage

<!-- UsageSnippet language="python" operationID="getStyleGuideById" method="get" path="/content/styleGuides/{styleGuideId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_style_guide_by_id(style_guide_id="WW91IGZvdW5kIG1lIQ", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `style_guide_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the style guide                            | WW91IGZvdW5kIG1lIQ                                                  |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.StyleGuide](../../models/styleguide.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_anchor_by_id

Returns an [`Anchor`](ref:content#anchor) given its id.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableAnchorById" method="get" path="/content/tables/{tableId}/anchors/{anchorId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_table_anchor_by_id(anchor_id="<id>", table_id="WW91IGZvdW5kfIG1lIQ", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `anchor_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the anchor                                 |                                                                     |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the table                                 | WW91IGZvdW5kfIG1lIQ                                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Anchor](../../models/anchor.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_anchor_extensions

Returns a paginated list of [`AnchorExtensions`](ref:content#anchorextension) for a given anchorId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableAnchorExtensions" method="get" path="/content/tables/{tableId}/anchors/{anchorId}/extensions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_table_anchor_extensions(request={
        "anchor_id": "<id>",
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "revision": "1A2B3C4D",
        "table_id": "WW91IGZvdW5kfIG1lIQ",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.GetTableAnchorExtensionsRequest](../../models/gettableanchorextensionsrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.GetTableAnchorExtensionsResponse](../../models/gettableanchorextensionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_anchors

Returns an [`AnchorsListResult`](ref:content#anchorslistresult) given tableId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableAnchors" method="get" path="/content/tables/{tableId}/anchors" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_table_anchors(table_id="WW91IGZvdW5kfIG1lIQ", maxpagesize=1000, next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA", revision="1A2B3C4D")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the table                                 | WW91IGZvdW5kfIG1lIQ                                                 |
| `maxpagesize`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of results to retrieve                           |                                                                     |
| `next`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor for next set of results.                          | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetTableAnchorsResponse](../../models/gettableanchorsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_cells

Returns a [`TableCellsResult`](ref:content#tablecellsresult) for a given tableId.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTableCells" method="get" path="/content/tables/{tableId}/cells" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_table_cells(request={
        "next": "JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA",
        "revision": "1A2B3C4D",
        "start_column": 1,
        "start_row": 1,
        "stop_column": 1,
        "stop_row": 1,
        "table_id": "WW91IGZvdW5kfIG1lIQ",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetTableCellsRequest](../../models/gettablecellsrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTableCellsResponse](../../models/gettablecellsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_table_properties

Returns a [`TableProperties`](ref:content#tableproperties) for a table


### Example Usage

<!-- UsageSnippet language="python" operationID="getTableProperties" method="get" path="/content/tables/{tableId}/properties" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.get_table_properties(table_id="WW91IGZvdW5kfIG1lIQ", revision="1A2B3C4D")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `table_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the table                                 | WW91IGZvdW5kfIG1lIQ                                                 |
| `revision`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns resources at a specific revision                            | 1A2B3C4D                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TableProperties](../../models/tableproperties.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## image_upload

Retrieves a URL that can be used to upload an image, and an operationId to track the image upload progress. Once uploaded, the image can be inserted in content.

Image uploads must conform to the following constraints:

- An image must be uploaded once per usage in content.
- Image uploads must complete within ten minutes.
- The file size of the uploaded image must 75 MB or smaller.
- The total number of pixels in the uploaded image must be 50 Megapixels or smaller.
- The image must be inserted in content within 24 hours or it will be removed.

Responses include an `uploadUrl` which indicates where to upload the image. To upload the file,
perform a PUT against the `uploadUrl` with the same authentication credentials and flow as the import request.
For more details, see [Authentication documentation](ref:authentication). The response will also include
a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see
[Operations endpoint](ref:getoperationbyid). When the upload completes, its status will be
`completed`, and the response body includes a `resourceURL`.


### Example Usage

<!-- UsageSnippet language="python" operationID="imageUpload" method="post" path="/content/images/upload" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.image_upload(request={
        "file_name": "example.png",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ImageUpload](../../models/imageupload.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ImageUploadResponse1](../../models/imageuploadresponse1.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_table_properties

Partially updates a table's properties given its ID.

This is a long running operation. Responses include a `Location` header, which indicates where to poll for results.
For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).

### Options
| Path               | PATCH Operations Supported |
|--------------------|----------------------------|
| `/name`            | `replace`                  |
| `/resizeRowsToFit` | `replace`                  |
| `/lock`            | `replace`                  |


### Example Usage

<!-- UsageSnippet language="python" operationID="partiallyUpdateTableProperties" method="patch" path="/content/tables/{tableId}/properties" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.partially_update_table_properties(table_id="WW91IGZvdW5kfIG1lIQ", request_body=[
        {
            "op": models.Op.REPLACE,
            "path": "/resizeRowsToFit",
            "value": True,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `table_id`                                                                   | *str*                                                                        | :heavy_check_mark:                                                           | The unique identifier for the table                                          | WW91IGZvdW5kfIG1lIQ                                                          |
| `request_body`                                                               | List[[models.JSONPatchOperation](../../models/jsonpatchoperation.md)]        | :heavy_check_mark:                                                           | Patch document representing the changes to be made to the table's properties |                                                                              |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.PartiallyUpdateTablePropertiesResponse](../../models/partiallyupdatetablepropertiesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## rich_text_anchor_creation

Create a new [`Anchor`](ref:content#anchor) using a [`RichTextAnchorCreation`](ref:content#richtextanchorcreation) request. This is a long running operation.

Responses include a `Location` header, which indicates where to poll for
results. For more details on long-running job polling, see
[Operations endpoint](ref:getoperationbyid).
When the creation completes, its status will be `completed`, and the response
body includes a `resourceURL`. To GET the new rich text anchor, perform a GET
on the `resourceURL` with the same authentication credentials and flow as the
initial request. For more details, see
[Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="richTextAnchorCreation" method="post" path="/content/richText/{richTextId}/anchors/creation" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.rich_text_anchor_creation(rich_text_id="<id>", rich_text_anchor_creation=models.RichTextAnchorCreation(
        revision="24601abc",
        selection=models.RichTextSelection(
            start=models.Caret(
                offset=0,
                paragraph_index=0,
            ),
            stop=models.Caret(
                offset=10,
                paragraph_index=2,
            ),
        ),
        type=models.RichTextSelectionAnchorAttachmentPointType.SOURCE_LINK,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `rich_text_id`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | The unique identifier of the rich text content                          |
| `rich_text_anchor_creation`                                             | [models.RichTextAnchorCreation](../../models/richtextanchorcreation.md) | :heavy_check_mark:                                                      | The anchor creation requests                                            |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.RichTextAnchorCreationResponse](../../models/richtextanchorcreationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## rich_text_batch_edit

Sends a [`RichTextBatchEdit`](ref:content#richtextbatchedit) to perform as a batch on the rich text.
The optional revision property can be used to identify a stable version of the text to use for selections. The latest revision is used if not specified.
This is a long running operation. Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).
If the batch edit creates any new resources such as embedded tables, the `resourceUrl` field will be populated with a link to the [Rich Text Batch Edit Results endpoint](ref:getrichtextbatcheditresults) to retrieve the IDs of the new resources.

### Example Usage

<!-- UsageSnippet language="python" operationID="richTextBatchEdit" method="post" path="/content/richText/{richTextId}/edit" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.rich_text_batch_edit(rich_text_id="<id>", rich_text_batch_edit={
        "data": [
            models.TextEdit(
                insert_text=models.InsertText(
                    format_=models.ApplicableTextFormat(
                        bold=True,
                        font="Times New Roman",
                        italic=True,
                        size=14,
                        strikethrough=True,
                        underline=True,
                    ),
                    insert_at=models.Caret(
                        offset=5,
                        paragraph_index=0,
                    ),
                    text="Hello, world!",
                ),
                type=models.TextEditType.INSERT_TEXT,
            ),
        ],
        "islolate_edits": True,
        "revision": "24601abc",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rich_text_id`                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                  | The unique identifier of the rich text content                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                     |
| `rich_text_batch_edit`                                                                                                                                                                                                                                              | [models.RichTextBatchEdit](../../models/richtextbatchedit.md)                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                  | The rich text edits to apply                                                                                                                                                                                                                                        | {<br/>"data": [<br/>{<br/>"insertText": {<br/>"format": {<br/>"bold": true,<br/>"font": "Times New Roman"<br/>},<br/>"inheritFormats": true,<br/>"insertAt": {<br/>"offset": 5,<br/>"paragraphIndex": 0<br/>},<br/>"text": "Hello, world!"<br/>},<br/>"type": "insertText"<br/>}<br/>],<br/>"isolateEdits": false,<br/>"revision": "24601abc"<br/>} |
| `retries`                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                     |

### Response

**[models.RichTextBatchEditResponse](../../models/richtextbatcheditresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## rich_text_duplication_edit

Sends a [`RichTextDuplicationEdit`](ref:content#richtextduplicationedit) to perform on the rich text.
The optional revision property can be used to identify a stable version of the text to use for selections. The latest revision is used if not specified.
This is a long running operation. Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).
The `resourceUrl` field will be populated with a link to the [Rich Text Duplication Edit Results endpoint](ref:getrichtextduplicationeditresults) to retrieve the IDs of the new resources.

### Example Usage

<!-- UsageSnippet language="python" operationID="richTextDuplicationEdit" method="post" path="/content/richText/{richTextId}/duplication/edit" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.rich_text_duplication_edit(rich_text_id="<id>", rich_text_duplication_edit={
        "duplicate_table": {
            "insert_at": {
                "offset": 0,
                "paragraph_index": 2,
            },
            "source_table": "WAxsaHxoYvTB4D0twUm6YtiF99TNO0gBkSOhgYBed9AMB99EUxqELDQychBaGR9SkZucm5sK",
        },
        "revision": "24601abc",
        "type": models.RichTextDuplicationEditType.DUPLICATE_TABLE,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                               | Type                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                | Description                                                                                                                                                                                                             | Example                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rich_text_id`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                      | The unique identifier of the rich text content                                                                                                                                                                          |                                                                                                                                                                                                                         |
| `rich_text_duplication_edit`                                                                                                                                                                                            | [models.RichTextDuplicationEdit](../../models/richtextduplicationedit.md)                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                      | The rich text duplication edits to apply                                                                                                                                                                                | {<br/>"duplicateTable": {<br/>"insertAt": {<br/>"offset": 0,<br/>"paragraphIndex": 2<br/>},<br/>"sourceTable": "WAxsaHxoYvTB4D0twUm6YtiF99TNO0gBkSOhgYBed9AMB99EUxqELDQychBaGR9SkZucm5sK"<br/>},<br/>"revision": "24601abc",<br/>"type": "duplicateTable"<br/>} |
| `retries`                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                     |                                                                                                                                                                                                                         |

### Response

**[models.RichTextDuplicationEditResponse](../../models/richtextduplicationeditresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## rich_text_links_batch_edit

Sends a [`RichTextLinksBatchEdit`](ref:content#richtextlinksbatchedit) to perform as a batch on the rich text.
The optional revision property can be used to identify a stable version of the text to use for selections. The latest revision is used if not specified.
This is a long running operation. Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).
If the batch edit creates any new resources, such as destination links, the `resourceUrl` field will be populated with a link to the [Rich Text Links Batch Edit Results endpoint](ref:getrichtextlinksbatcheditresults) to retrieve the IDs of the new resources.

### Example Usage

<!-- UsageSnippet language="python" operationID="richTextLinksBatchEdit" method="post" path="/content/richText/{richTextId}/links/edit" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.rich_text_links_batch_edit(rich_text_id="<id>", rich_text_links_batch_edit={
        "data": [
            models.TextLinkEdit(
                insert_destination_link=models.InsertDestinationLink(
                    insert_at=models.Caret(
                        offset=10,
                        paragraph_index=4,
                    ),
                    source_anchor="WA7i5vbm7lNaEn6XT9AtcW5vb22BJjMrqxmru",
                ),
                type=models.TextLinkEditType.INSERT_DESTINATION_LINK,
            ),
        ],
        "revision": "24601abc",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rich_text_id`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                          | The unique identifier of the rich text content                                                                                                                                                                                              |                                                                                                                                                                                                                                             |
| `rich_text_links_batch_edit`                                                                                                                                                                                                                | [models.RichTextLinksBatchEdit](../../models/richtextlinksbatchedit.md)                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                          | The rich text link edits to apply                                                                                                                                                                                                           | {<br/>"data": [<br/>{<br/>"insertDestinationLink": {<br/>"insertAt": {<br/>"offset": 10,<br/>"paragraphIndex": 4<br/>},<br/>"sourceAnchor": "WA7i5vbm7lNaEn6XT9AtcW5vb22BJjMrqxmru"<br/>},<br/>"type": "insertDestinationLink"<br/>}<br/>],<br/>"isolateEdits": false,<br/>"revision": "24601abc"<br/>} |
| `retries`                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                         |                                                                                                                                                                                                                                             |

### Response

**[models.RichTextLinksBatchEditResponse](../../models/richtextlinksbatcheditresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## style_guide_export

Export the style guide with the given identifier. Options are
specified using a
[StyleGuideExport](ref:content#styleguideexport) object.

Responses include a `Location` header, which indicates where to poll for
results. For more details on long-running job polling, see
[Operations endpoint](ref:getoperationbyid).
When the export completes, its status will be `completed`, and the response
body includes a `resourceURL`. To GET the exported style guide, perform a GET
on the `resourceURL` with the same authentication credentials and flow as the
initial request. For more details, see
[Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="styleGuideExport" method="post" path="/content/styleGuides/{styleGuideId}/export" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.style_guide_export(style_guide_id="WW91IGZvdW5kIG1lIQ", style_guide_export={
        "revision": "1A2B3C4D",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     | Example                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `style_guide_id`                                                                                                                | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | The unique identifier of the style guide                                                                                        | WW91IGZvdW5kIG1lIQ                                                                                                              |
| `style_guide_export`                                                                                                            | [OptionalNullable[models.StyleGuideExport]](../../models/styleguideexport.md)                                                   | :heavy_minus_sign:                                                                                                              | Details about the style guide export. The most recent version will be exported if revision is omitted from the export details.<br/> | {<br/>"revision": "1A2B3C4D"<br/>}                                                                                              |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |                                                                                                                                 |

### Response

**[models.StyleGuideExportResponse](../../models/styleguideexportresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## style_guide_import

Imports a style guide to the given identifier. This operation will replace the current style guide.

Responses include an `uploadUrl` which indicates where to upload the style guide import. To upload the file,
perform a PUT against the `uploadUrl` with the same authentication credentials and flow as the import request.
For more details, see [Authentication documentation](ref:authentication). The response will also include
a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see
[Operations endpoint](ref:getoperationbyid). When the upload completes, its status will be
`completed`, and the response body includes a `resourceURL`. To GET the style guide, perform a GET
on the `resourceURL` with the same authentication credentials and flow as the initial request.


### Example Usage

<!-- UsageSnippet language="python" operationID="styleGuideImport" method="post" path="/content/styleGuides/{styleGuideId}/import" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.style_guide_import(style_guide_id="WW91IGZvdW5kIG1lIQ")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `style_guide_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the style guide                            | WW91IGZvdW5kIG1lIQ                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.StyleGuideImportResponse1](../../models/styleguideimportresponse1.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## table_anchor_creation

Create a new [`Anchor`](ref:content#anchor) using a [`TableAnchorCreation`](ref:content#tableanchorcreation) request. This is a long running operation.

Responses include a `Location` header, which indicates where to poll for
results. For more details on long-running job polling, see
[Operations endpoint](ref:getoperationbyid).
When the creation completes, its status will be `completed`, and the response
body includes a `resourceURL`. To GET the new table anchor, perform a GET
on the `resourceURL` with the same authentication credentials and flow as the
initial request. For more details, see
[Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="tableAnchorCreation" method="post" path="/content/tables/{tableId}/anchors/creation" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.table_anchor_creation(table_id="WW91IGZvdW5kfIG1lIQ", table_anchor_creation={
        "range": {
            "start_column": 0,
            "start_row": 5,
            "stop_column": 3,
            "stop_row": 9,
        },
        "revision": "24601abc",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `table_id`                                                                                              | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The unique identifier for the table                                                                     | WW91IGZvdW5kfIG1lIQ                                                                                     |
| `table_anchor_creation`                                                                                 | [models.TableAnchorCreation](../../models/tableanchorcreation.md)                                       | :heavy_check_mark:                                                                                      | The details of range for which the table anchor needs to be created                                     | {<br/>"range": {<br/>"startColumn": 0,<br/>"startRow": 5,<br/>"stopColumn": 3,<br/>"stopRow": 9<br/>},<br/>"revision": "24601abc"<br/>} |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |

### Response

**[models.TableAnchorCreationResponse](../../models/tableanchorcreationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## table_cells_batch_edit

Sends a [`TableCellsBatchEdit`](ref:content#tablecellsbatchedit) to perform on the cells in a table.

The optional revision property can be used to identify a stable cell location in the table. The latest revision is used if not specified.

Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see[ Operations endpoint ](ref:getoperationbyid). When the creation completes, its status will be `completed`, and the response\nbody includes a `resourceURL`.\n"


### Example Usage

<!-- UsageSnippet language="python" operationID="tableCellsBatchEdit" method="post" path="/content/tables/{tableId}/cells/edit" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.table_cells_batch_edit(table_id="WW91IGZvdW5kfIG1lIQ", table_cells_batch_edit={
        "data": [
            models.TableCellsEdit(
                clear_cells_format=models.ClearCellsFormat(
                    clear_background_color=True,
                    clear_character_spacing=True,
                    clear_italic=True,
                    clear_size=True,
                    clear_strike_through=True,
                    clear_text_color=True,
                    clear_underline=True,
                    ranges=[
                        models.CellRange(
                            start_column=0,
                            start_row=0,
                            stop_column=2,
                            stop_row=2,
                        ),
                    ],
                ),
                type=models.TableCellsEditType.CLEAR_CELLS_FORMAT,
            ),
        ],
        "revision": "24601abc",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `table_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                           | The unique identifier for the table                                                                                                                                                                                                                                                                                                                                                                                                                          | WW91IGZvdW5kfIG1lIQ                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `table_cells_batch_edit`                                                                                                                                                                                                                                                                                                                                                                                                                                     | [models.TableCellsBatchEdit](../../models/tablecellsbatchedit.md)                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                           | The table cell edit to apply                                                                                                                                                                                                                                                                                                                                                                                                                                 | {<br/>"data": [<br/>{<br/>"clearCellsFormat": {<br/>"clearAll": false,<br/>"clearBackgroundColor": true,<br/>"clearBold": false,<br/>"clearCharacterSpacing": true,<br/>"clearFont": false,<br/>"clearItalic": true,<br/>"clearSize": true,<br/>"clearStrikeThrough": true,<br/>"clearTextColor": true,<br/>"clearUnderline": true,<br/>"ranges": [<br/>{<br/>"startColumn": 0,<br/>"startRow": 0,<br/>"stopColumn": 2,<br/>"stopRow": 2<br/>}<br/>]<br/>},<br/>"type": "clearCellsFormat"<br/>}<br/>],<br/>"lockedCellEditMode": "strict",<br/>"revision": "24601abc"<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Response

**[models.TableCellsBatchEditResponse](../../models/tablecellsbatcheditresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## table_edit

Sends a single [`TableEdit`](ref:content#tableedit) to perform on the table.

Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see
[ Operations endpoint ](ref:getoperationbyid). When the creation completes, its status will be `completed`, and the response
body includes a `resourceURL`.


### Example Usage

<!-- UsageSnippet language="python" operationID="tableEdit" method="post" path="/content/tables/{tableId}/edit" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.table_edit(table_id="WW91IGZvdW5kfIG1lIQ", table_edit=models.TableEdit(
        delete_columns=models.DeleteColumns(
            columns=models.ColumnRange(
                start_column=0,
                stop_column=5,
            ),
        ),
        type=models.TableEditType.DELETE_COLUMNS,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `table_id`                                                                                         | *str*                                                                                              | :heavy_check_mark:                                                                                 | The unique identifier for the table                                                                | WW91IGZvdW5kfIG1lIQ                                                                                |
| `table_edit`                                                                                       | [models.TableEdit](../../models/tableedit.md)                                                      | :heavy_check_mark:                                                                                 | The table edit to apply                                                                            | {<br/>"deleteColumns": {<br/>"columns": {<br/>"startColumn": 0,<br/>"stopColumn": 5<br/>}<br/>},<br/>"type": "deleteColumns"<br/>} |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[models.TableEditResponse](../../models/tableeditresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## table_filters_reapplication

Performs a [`TableFiltersReapplication`](ref:content#tablefiltersreapplication) on the specified table.
This endpoint is used to refresh the table's filters based on the latest state or configuration changes.
The filters are reapplied in the context of the table's current data state.
This is a long running operation. Responses include a `Location` header, which indicates where to poll for results. For more details on
long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="tableFiltersReapplication" method="post" path="/content/tables/{tableId}/filters/reapplication" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.table_filters_reapplication(table_id="WW91IGZvdW5kfIG1lIQ", table_filters_reapplication={
        "force_hide_footnotes": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `table_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier for the table                                           | WW91IGZvdW5kfIG1lIQ                                                           |
| `table_filters_reapplication`                                                 | [models.TableFiltersReapplication](../../models/tablefiltersreapplication.md) | :heavy_check_mark:                                                            | The filter reapplication request to apply                                     | {<br/>"forceHideFootnotes": true<br/>}                                        |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.TableFiltersReapplicationResponse](../../models/tablefiltersreapplicationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## table_links_batch_edit

Sends a [`TableLinksBatchEdit`](ref:content#tablelinksbatchedit) to perform on the links in a table.

The optional revision property can be used to identify a stable cell location in the table. The latest revision is used if not specified.

If the edit creates any new resources, such as destination links, the `resourceUrl` field will be populated with a link to the [Table Links Edit Results endpoint](ref:gettablelinkseditresults) to retrieve the IDs of the new resources.


### Example Usage

<!-- UsageSnippet language="python" operationID="tableLinksBatchEdit" method="post" path="/content/tables/{tableId}/links/edit" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.table_links_batch_edit(table_id="WW91IGZvdW5kfIG1lIQ", table_links_batch_edit={
        "data": [
            models.TableLinksEdit(
                insert_cell_destination_link=models.InsertCellDestinationLink(
                    insert_at=models.Cell(
                        column=2,
                        row=41,
                    ),
                    source_anchor="WA7i5vbm7lNaEn6XT9AtcW5vb22BJjMrqxmru",
                ),
                type=models.TableLinksEditType.INSERT_CELL_DESTINATION_LINK,
            ),
        ],
        "revision": "24601abc",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `table_id`                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The unique identifier for the table                                                                                                                                                                                                               | WW91IGZvdW5kfIG1lIQ                                                                                                                                                                                                                               |
| `table_links_batch_edit`                                                                                                                                                                                                                          | [models.TableLinksBatchEdit](../../models/tablelinksbatchedit.md)                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                | The table link edits to apply                                                                                                                                                                                                                     | {<br/>"data": [<br/>{<br/>"insertCellDestinationLink": {<br/>"insertAt": {<br/>"column": 2,<br/>"row": 41<br/>},<br/>"sourceAnchor": "WA7i5vbm7lNaEn6XT9AtcW5vb22BJjMrqxmru"<br/>},<br/>"type": "insertCellDestinationLink"<br/>}<br/>],<br/>"lockedCellEditMode": "strict",<br/>"revision": "24601abc"<br/>} |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.TableLinksBatchEditResponse](../../models/tablelinksbatcheditresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## table_range_links_edit

Sends a [`RangeLinkEdit`](ref:content#rangelinkedit) to perform on the range links in a table.
This is a long running operation. Responses include a `Location` header, which indicates where to poll for results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="tableRangeLinksEdit" method="post" path="/content/tables/{tableId}/rangeLinks/edit" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.content.table_range_links_edit(table_id="WW91IGZvdW5kfIG1lIQ", range_link_edit=models.RangeLinkEdit(
        remove_source=models.RemoveSource(
            range_link="WAxsaHxoYvTB4D0twUm6YtiF99TNO0gBkSOhgYBed9AMB99EUxqELDQychBaGR9SkZucm5sK",
        ),
        type=models.RangeLinkEditType.REMOVE_SOURCE,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `table_id`                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The unique identifier for the table                                                                                                                                                                                  | WW91IGZvdW5kfIG1lIQ                                                                                                                                                                                                  |
| `range_link_edit`                                                                                                                                                                                                    | [models.RangeLinkEdit](../../models/rangelinkedit.md)                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The table range link edit to apply                                                                                                                                                                                   | {<br/>"removeSource": {<br/>"range": {<br/>"startColumn": 0,<br/>"startRow": 5,<br/>"stopColumn": 3,<br/>"stopRow": 9<br/>},<br/>"rangeLink": "WAxsaHxoYvTB4D0twUm6YtiF99TNO0gBkSOhgYBed9AMB99EUxqELDQychBaGR9SkZucm5sK"<br/>},<br/>"type": "removeSource"<br/>} |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.TableRangeLinksEditResponse](../../models/tablerangelinkseditresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |