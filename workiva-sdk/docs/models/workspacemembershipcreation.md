# WorkspaceMembershipCreation

Details and Options for creating a new workspace membership.



## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `options`                                                | [OptionalNullable[models.Options]](../models/options.md) | :heavy_minus_sign:                                       | N/A                                                      | {<br/>"notifyNewMember": false,<br/>"sendWelcomeEmail": true<br/>} |
| `user`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | The user id that will be made a member of the workspace. |                                                          |