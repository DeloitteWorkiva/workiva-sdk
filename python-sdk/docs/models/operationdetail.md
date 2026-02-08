# OperationDetail

An OperationDetail contains extra information about an Operation


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `code`                                             | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | The error code for specified error details         |                                                    |
| `message`                                          | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | A message describing the detail                    | Attempted to modify locked cells                   |
| `target`                                           | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | For failures, this will be the target of the error |                                                    |