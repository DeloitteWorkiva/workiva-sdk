# TokenDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When the entity was created                                          |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The entity's unique identifier                                       |
| `object_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | The object's unique identifier                                       |
| `updated`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When the entity was last updated                                     |
| `use_flat_key`                                                       | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Create token using flat query results key; Ignored unless true.      |
| `user_id`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The owner of the entity                                              |
| `version`                                                            | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The version of the current representation of the entity              |