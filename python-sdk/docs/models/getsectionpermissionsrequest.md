# GetSectionPermissionsRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `document_id`                              | *str*                                      | :heavy_check_mark:                         | The unique identifier of the document      |                                            |
| `section_id`                               | *str*                                      | :heavy_check_mark:                         | The unique identifier of the section       |                                            |
| `dollar_filter`                            | *Optional[str]*                            | :heavy_minus_sign:                         | The properties to filter the results by.   |                                            |
| `dollar_maxpagesize`                       | *Optional[int]*                            | :heavy_minus_sign:                         | The maximum number of results to retrieve  |                                            |
| `dollar_next`                              | *Optional[str]*                            | :heavy_minus_sign:                         | Pagination cursor for next set of results. | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA        |