# InsertColumns

Insert one or more columns into the table next to the given column on specified side



## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `count`                                        | *Optional[int]*                                | :heavy_minus_sign:                             | The number of columns to insert                | 10                                             |
| `next_to`                                      | *Optional[int]*                                | :heavy_minus_sign:                             | The position after which to insert the columns | 5                                              |
| `side`                                         | [Optional[models.Side]](../models/side.md)     | :heavy_minus_sign:                             | The direction where to insert nextTo           | putAfter                                       |