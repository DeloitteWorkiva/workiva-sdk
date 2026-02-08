# ColumnInfoDto

Contains column name and derived type from the associated query.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The name of the column                                               |
| `type`                                                               | [Optional[models.ColumnInfoDtoType]](../models/columninfodtotype.md) | :heavy_minus_sign:                                                   | The column's type                                                    |