# InsertRows

Insert one or more rows into the table next to the given row on specified side



## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `count`                                                      | *Optional[int]*                                              | :heavy_minus_sign:                                           | The number of rows to insert                                 | 10                                                           |
| `next_to`                                                    | *Optional[int]*                                              | :heavy_minus_sign:                                           | The position after which to insert the rows                  | 5                                                            |
| `side`                                                       | [Optional[models.TableEditSide]](../models/tableeditside.md) | :heavy_minus_sign:                                           | The direction where to insert nextTo                         | putAfter                                                     |