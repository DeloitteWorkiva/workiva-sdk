# TableTextElementProperties

The properties for a table text element.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `header_rows`                                                  | *Optional[int]*                                                | :heavy_minus_sign:                                             | The rows that are going to be headers                          |
| `table_breaking`                                               | [Nullable[models.TableBreaking]](../models/tablebreaking.md)   | :heavy_check_mark:                                             | The property that will dictate how the table will be broken up |
| `title_row`                                                    | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether the table has a title row                              |
| `title_suffix`                                                 | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | Optional table title suffix when title row is enabled.         |