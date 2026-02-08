# RemoveCellsLink

Removes source and destination links in a table range. This operation will be a no-op if no cell links exist within the table range.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `ranges`                                         | List[[models.CellRange](../models/cellrange.md)] | :heavy_check_mark:                               | The ranges to remove links from.                 |