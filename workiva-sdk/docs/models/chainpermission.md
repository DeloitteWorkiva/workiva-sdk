# ChainPermission

An object containing information about access permission to particular chains resources.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | The unique identifier of a resource (can be a GUID). | 74                                                   |
| `name`                                               | [Optional[models.Name]](../models/name.md)           | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `object_id`                                          | *Optional[str]*                                      | :heavy_minus_sign:                                   | The unique identifier of a resource (can be a GUID). | 74                                                   |
| `object_name`                                        | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `object_type`                                        | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `user_groups`                                        | List[[models.UserGroup](../models/usergroup.md)]     | :heavy_minus_sign:                                   | N/A                                                  |                                                      |