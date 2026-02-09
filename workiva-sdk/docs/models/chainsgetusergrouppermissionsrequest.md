# ChainsGetUserGroupPermissionsRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `page`                                                            | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Page number to retrieve in the paginated results (0-based index). | 3                                                                 |
| `page_size`                                                       | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Limit number of results returned (Max 100).                       | 10                                                                |
| `user_group_id`                                                   | *str*                                                             | :heavy_check_mark:                                                | The ID of the User Group.                                         | 1                                                                 |