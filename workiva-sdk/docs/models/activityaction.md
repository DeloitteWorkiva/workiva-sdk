# ActivityAction

Details about the activity action


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `alias`                                                            | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The legacy identifier of the activity action                       | workspace_membership_create                                        |
| `category`                                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Category of the activity action                                    | Administration                                                     |
| `deprecated`                                                       | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Whether or not the activity action has been identified for removal |                                                                    |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the activity action                       | com.workiva.administration.workspace_membership.create             |
| `name`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Name of the activity action                                        | Workspace membership created                                       |