# TagDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When the entity was created                                          |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The entity's unique identifier                                       |
| `key`                                                                | *str*                                                                | :heavy_check_mark:                                                   | Value for the key, maximum 100 characters in length                  |
| `updated`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When the entity was last updated                                     |
| `user_id`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The owner of the entity                                              |
| `values`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Set of values for the tag                                            |
| `version`                                                            | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The version of the current representation of the entity              |