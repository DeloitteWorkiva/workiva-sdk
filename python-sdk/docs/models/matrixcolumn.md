# MatrixColumn

Details about a matrix column including its ID and name.


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `external_id`                             | *Optional[str]*                           | :heavy_minus_sign:                        | A user defined external ID for the column | TA05                                      |
| `id`                                      | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | The unique ID of the matrix column        | fbd818ec-4fd1-42ad-9112-3c80e71dc2dc      |
| `name`                                    | *Optional[str]*                           | :heavy_minus_sign:                        | The name of the matrix column             | PO #                                      |
| `testable`                                | *OptionalNullable[bool]*                  | :heavy_minus_sign:                        | Whether the column is testable            | true                                      |