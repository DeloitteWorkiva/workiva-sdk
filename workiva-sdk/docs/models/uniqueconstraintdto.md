# UniqueConstraintDto


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `description`                                                          | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Description of this unique constraint. Max length: 1024                |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Id of the unique constraint                                            |
| `name`                                                                 | [models.UniqueConstraintDtoName](../models/uniqueconstraintdtoname.md) | :heavy_check_mark:                                                     | Name of this unique constraint. Max length: 100                        |
| `table_id`                                                             | *str*                                                                  | :heavy_check_mark:                                                     | Id of the table this unique constraint is associated with              |
| `values`                                                               | List[*str*]                                                            | :heavy_check_mark:                                                     | List of values in the unique constraint                                |