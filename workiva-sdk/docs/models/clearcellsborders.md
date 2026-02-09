# ClearCellsBorders

Clears the cell borders from all the cells in the given ranges of a table.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `clear_all`                                      | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether to clear all cell borders.<br/>          |
| `ranges`                                         | List[[models.CellRange](../models/cellrange.md)] | :heavy_check_mark:                               | A collection of cell ranges in a table.<br/>     |