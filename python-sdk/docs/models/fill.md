# Fill

A shape or box fill settings for things like shapes. Use a null to indicate no fill.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `color`                                                                                  | [models.Color](../models/color.md)                                                       | :heavy_check_mark:                                                                       | Represents a color.                                                                      | {<br/>"blue": 128,<br/>"green": 128,<br/>"red": 128<br/>}                                |
| `opacity`                                                                                | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | The opacity of a color where 1.0 is completely opaque and 0.0 is completely transparent. | 0.5                                                                                      |