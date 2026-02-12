# Left

The border of a rectangle for properties of objects such as a table cell.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `color`                                                                   | [models.Color](../models/color.md)                                        | :heavy_check_mark:                                                        | Represents a color.                                                       | {<br/>"blue": 128,<br/>"green": 128,<br/>"red": 128<br/>}                 |
| `style`                                                                   | [models.TableCellsEditStyle](../models/tablecellseditstyle.md)            | :heavy_check_mark:                                                        | The style of the border to apply.                                         |                                                                           |
| `weight`                                                                  | *float*                                                                   | :heavy_check_mark:                                                        | The thickness of the border, in points. Rounded to the nearest hundredth. | 1.5                                                                       |