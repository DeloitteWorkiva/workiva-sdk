# SingleError


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `body`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | A human-readable message describing the error                                |
| `code`                                                                       | *int*                                                                        | :heavy_check_mark:                                                           | A server-defined error code                                                  |
| `details`                                                                    | List[[models.BaseErrorResponseDetail](../models/baseerrorresponsedetail.md)] | :heavy_minus_sign:                                                           | Additional details of the error                                              |