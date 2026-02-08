# GetRichTextAnchorExtensionsRequest


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `dollar_maxpagesize`                           | *Optional[int]*                                | :heavy_minus_sign:                             | The maximum number of results to retrieve      |                                                |
| `dollar_next`                                  | *Optional[str]*                                | :heavy_minus_sign:                             | Pagination cursor for next set of results.     | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA            |
| `dollar_revision`                              | *Optional[str]*                                | :heavy_minus_sign:                             | Returns resources at a specific revision       | 1A2B3C4D                                       |
| `anchor_id`                                    | *str*                                          | :heavy_check_mark:                             | The unique identifier of the anchor            |                                                |
| `rich_text_id`                                 | *str*                                          | :heavy_check_mark:                             | The unique identifier of the rich text content |                                                |