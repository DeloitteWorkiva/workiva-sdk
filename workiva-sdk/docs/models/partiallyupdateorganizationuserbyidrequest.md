# PartiallyUpdateOrganizationUserByIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `organization_id`                                                  | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the organization                          | d6e178fd-4dd5-47e5-9457-68dd64b03655                               |
| `user_id`                                                          | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the user                                  |                                                                    |
| `request_body`                                                     | List[[models.JSONPatchOperation](../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                 | Editable details about the User.                                   |                                                                    |