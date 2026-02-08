# Range

A range in a sheet. If any field is omitted or null, the range is unbounded in that direction.


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `start_column`                                        | *OptionalNullable[int]*                               | :heavy_minus_sign:                                    | The index of the first column of the range, inclusive |
| `start_row`                                           | *OptionalNullable[int]*                               | :heavy_minus_sign:                                    | The index of the first row of the range, inclusive    |
| `stop_column`                                         | *OptionalNullable[int]*                               | :heavy_minus_sign:                                    | The index of the last column of the range, inclusive  |
| `stop_row`                                            | *OptionalNullable[int]*                               | :heavy_minus_sign:                                    | The index of the last row of the range, inclusive     |