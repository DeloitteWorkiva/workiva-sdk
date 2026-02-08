# GetSectionPermissionsRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `document_id`                              | *str*                                      | :heavy_check_mark:                         | The unique identifier of the document      |                                            |
| `filter_`                                  | *Optional[str]*                            | :heavy_minus_sign:                         | The properties to filter the results by.   |                                            |
| `maxpagesize`                              | *Optional[int]*                            | :heavy_minus_sign:                         | The maximum number of results to retrieve  |                                            |
| `next`                                     | *Optional[str]*                            | :heavy_minus_sign:                         | Pagination cursor for next set of results. | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA        |
| `section_id`                               | *str*                                      | :heavy_check_mark:                         | The unique identifier of the section       |                                            |