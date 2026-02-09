# Interval

An interval of rows or columns. If either the start or end is null or omitted, the interval is unbounded in that direction.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `end`                                      | *OptionalNullable[int]*                    | :heavy_minus_sign:                         | The last index of the interval, inclusive  |
| `start`                                    | *OptionalNullable[int]*                    | :heavy_minus_sign:                         | The first index of the interval, inclusive |