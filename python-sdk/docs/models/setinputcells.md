# SetInputCells

Sets the input cells for a range of cells in a table. Setting input cells requires the input mode ability. The operation will no-op if the cell is already in the state associated with the input cell.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `input_cell`                                     | *bool*                                           | :heavy_check_mark:                               | Whether the cells should be input cells.         | false                                            |
| `ranges`                                         | List[[models.CellRange](../models/cellrange.md)] | :heavy_check_mark:                               | A collection of cell ranges in a table.<br/>     |                                                  |