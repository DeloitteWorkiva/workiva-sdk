# MilestoneCreationResult

A reference to a resource that was created by an operation.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `type`                                                                         | [models.MilestoneCreationResultType](../models/milestonecreationresulttype.md) | :heavy_check_mark:                                                             | The type of resource created from a milestone creation                         |
| `milestone`                                                                    | *OptionalNullable[str]*                                                        | :heavy_minus_sign:                                                             | The ID of the milestone that was created.                                      |