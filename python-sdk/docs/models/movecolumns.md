# MoveColumns

Moves one or more columns from one location in the table to next to the given column on the specified side of that column. The column to move the other columns next to may not be within the set of columns to move.



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `move`                                                                     | [OptionalNullable[models.ColumnRange]](../models/columnrange.md)           | :heavy_minus_sign:                                                         | Describes a column range<br/>                                              | {<br/>"startColumn": 5,<br/>"stopColumn": 5<br/>}                          |
| `next_to`                                                                  | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | The position after which to move the columns                               | 5                                                                          |
| `side`                                                                     | [Optional[models.TableEditSchemasSide]](../models/tableeditschemasside.md) | :heavy_minus_sign:                                                         | The direction where to move from nextTo                                    | putAfter                                                                   |