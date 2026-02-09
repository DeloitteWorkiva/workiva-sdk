# SharedTableDtoInput


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `destination_workspace_id`                                   | *str*                                                        | :heavy_check_mark:                                           | The id of the workspace being shared to.                     |
| `source_table_id`                                            | *str*                                                        | :heavy_check_mark:                                           | The id of the table being shared.                            |
| `table`                                                      | [Optional[models.TableDtoInput]](../models/tabledtoinput.md) | :heavy_minus_sign:                                           | N/A                                                          |