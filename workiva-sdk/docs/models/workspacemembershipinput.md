# WorkspaceMembershipInput

Details about a user's membership in a workspace.



## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `user`                                                                       | [Optional[models.OrganizationUserInput]](../models/organizationuserinput.md) | :heavy_minus_sign:                                                           | The user that is a member of the workspace                                   |
| `workspace`                                                                  | [Optional[models.WorkspaceInput]](../models/workspaceinput.md)               | :heavy_minus_sign:                                                           | The workspace that this membership belongs to                                |