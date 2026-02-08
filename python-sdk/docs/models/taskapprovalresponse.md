# TaskApprovalResponse

A response to an approval step, including the user, action taken, timestamp, and optional comment.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `action`                                                                       | [models.TaskApprovalResponseAction](../models/taskapprovalresponseaction.md)   | :heavy_check_mark:                                                             | N/A                                                                            | REJECT                                                                         |
| `comment`                                                                      | *OptionalNullable[str]*                                                        | :heavy_minus_sign:                                                             | An optional comment left by the user.                                          | please refine                                                                  |
| `created`                                                                      | [models.TaskApprovalResponseCreated](../models/taskapprovalresponsecreated.md) | :heavy_check_mark:                                                             | N/A                                                                            |                                                                                |