# Border

The type of border that should be applied


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `color`                                                                   | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | A hex color code                                                          | #4bdf58                                                                   |
| `style`                                                                   | [models.Style](../models/style.md)                                        | :heavy_check_mark:                                                        | The type of border to apply                                               |                                                                           |
| `weight`                                                                  | *OptionalNullable[float]*                                                 | :heavy_minus_sign:                                                        | The thickness of the border, in points. Rounded to the nearest hundredth. |                                                                           |