# ResourcePermissionsModification

Details about the permissions modification



## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `to_assign`                                                                  | List[[models.ResourcePermissionInput](../models/resourcepermissioninput.md)] | :heavy_minus_sign:                                                           | The list of permissions to be assigned to the resource                       |
| `to_revoke`                                                                  | List[[models.ResourcePermissionInput](../models/resourcepermissioninput.md)] | :heavy_minus_sign:                                                           | The list of permissions to be revoked from the resource                      |