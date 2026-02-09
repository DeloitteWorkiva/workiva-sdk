# Stroke

Line stroke setting for things like shape edges. Use a null to indicate no stroke line.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `color`                                                      | [models.Color](../models/color.md)                           | :heavy_check_mark:                                           | Represents a color.                                          | {<br/>"blue": 128,<br/>"green": 128,<br/>"red": 128<br/>}    |
| `pattern`                                                    | [Optional[models.StrokePattern]](../models/strokepattern.md) | :heavy_minus_sign:                                           | The pattern to apply to the stroke.                          | solid                                                        |
| `width`                                                      | *Optional[float]*                                            | :heavy_minus_sign:                                           | The width of the stroke in points.                           | 2                                                            |