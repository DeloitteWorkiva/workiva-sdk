# TableBreaking

The property that will dictate how the table will be broken up


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `breaking_percentage`                                                          | *OptionalNullable[int]*                                                        | :heavy_minus_sign:                                                             | The percentage the table will break at, only set when type is breakWhenExceeds |
| `type`                                                                         | [Optional[models.TableBreakingType]](../models/tablebreakingtype.md)           | :heavy_minus_sign:                                                             | The type of table breaking                                                     |