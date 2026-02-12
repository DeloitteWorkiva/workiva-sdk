# RangeLinkListResult

Data model for range link list



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `data`                                           | List[[models.RangeLink](../models/rangelink.md)] | :heavy_minus_sign:                               | The current page of range links                  |                                                  |
| `at_next_link`                                   | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | Pagination link for next set of results          | <opaque_url>                                     |