# ImageUploadResultCollection

A collection of created results from an image upload. When there are no additional results before the current collection, the previous property will be null. When there are no additional results after the current collection, the next property will be null.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `at_next_link`                                                   | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | Pagination link for next set of results                          | <opaque_url>                                                     |
| `data`                                                           | List[[models.ImageUploadResult](../models/imageuploadresult.md)] | :heavy_minus_sign:                                               | The current page of data.                                        |                                                                  |