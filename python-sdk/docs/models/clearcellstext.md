# ClearCellsText

Deletes the text from all the cells in the ranges of a table. This will not remove the text formatting applied to the cells. The cells locations will remain, although empty, even if a complete row or column is specified by the range.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `ranges`                                         | List[[models.CellRange](../models/cellrange.md)] | :heavy_check_mark:                               | A collection of cell ranges in a table.<br/>     |