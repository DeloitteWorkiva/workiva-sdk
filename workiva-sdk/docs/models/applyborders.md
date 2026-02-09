# ApplyBorders

Apply borders to ranges


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `bottom`                                               | [OptionalNullable[models.Border]](../models/border.md) | :heavy_minus_sign:                                     | The type of border that should be applied              | {<br/>"color": "#000000",<br/>"style": "SINGLE",<br/>"weight": 2<br/>} |
| `inner_horizontal`                                     | [OptionalNullable[models.Border]](../models/border.md) | :heavy_minus_sign:                                     | The type of border that should be applied              | {<br/>"color": "#000000",<br/>"style": "SINGLE",<br/>"weight": 2<br/>} |
| `inner_vertical`                                       | [OptionalNullable[models.Border]](../models/border.md) | :heavy_minus_sign:                                     | The type of border that should be applied              | {<br/>"color": "#000000",<br/>"style": "SINGLE",<br/>"weight": 2<br/>} |
| `left`                                                 | [OptionalNullable[models.Border]](../models/border.md) | :heavy_minus_sign:                                     | The type of border that should be applied              | {<br/>"color": "#000000",<br/>"style": "SINGLE",<br/>"weight": 2<br/>} |
| `ranges`                                               | List[[Nullable[models.Range]](../models/range.md)]     | :heavy_check_mark:                                     | The ranges to apply borders                            |                                                        |
| `right`                                                | [OptionalNullable[models.Border]](../models/border.md) | :heavy_minus_sign:                                     | The type of border that should be applied              | {<br/>"color": "#000000",<br/>"style": "SINGLE",<br/>"weight": 2<br/>} |
| `top`                                                  | [OptionalNullable[models.Border]](../models/border.md) | :heavy_minus_sign:                                     | The type of border that should be applied              | {<br/>"color": "#000000",<br/>"style": "SINGLE",<br/>"weight": 2<br/>} |