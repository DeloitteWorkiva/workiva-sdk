# Precision

Precision to use when rounding numbers for display. Valid for AUTOMATIC, ACCOUNTING, CURRENCY, NUMBER, and PERCENT.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `auto`                                                         | *OptionalNullable[bool]*                                       | :heavy_minus_sign:                                             | Render with automatic precision based on the value in the cell |
| `value`                                                        | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | Explicit precision value to use. Required unless auto is true. |