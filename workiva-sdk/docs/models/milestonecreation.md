# MilestoneCreation

Parameters used to create a milestone in a document, presentation, or spreadsheet. The created milestone will be associated with the latest revision at the point of milestone creation.



## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `type`                                                             | [models.MilestoneResourceType](../models/milestoneresourcetype.md) | :heavy_check_mark:                                                 | The type of content associated with a milestone.                   | document                                                           |
| `document`                                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The unique identifier of the document being referred to            | 16b1f641613847469b7aa1ca29af40b1                                   |
| `presentation`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The unique identifier of the presentation being referred to        | 16b1f641613847469b7aa1ca29af40b1                                   |
| `spreadsheet`                                                      | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The unique identifier of the spreadsheet being referred to         | 16b1f641613847469b7aa1ca29af40b1                                   |
| `title`                                                            | *str*                                                              | :heavy_check_mark:                                                 | The title of the milestone                                         |                                                                    |
| `remarks`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The remarks associated with the milestone                          |                                                                    |