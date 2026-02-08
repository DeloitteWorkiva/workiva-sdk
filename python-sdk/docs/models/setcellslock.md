# SetCellsLock

Locks or unlocks cells in the given ranges of a table. The operation will no-op if the cell is already in the state associated with the lock.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `lock`                                           | *bool*                                           | :heavy_check_mark:                               | Whether to lock or unlock the ranges of cells.   | false                                            |
| `ranges`                                         | List[[models.CellRange](../models/cellrange.md)] | :heavy_check_mark:                               | A collection of cell ranges in a table.<br/>     |                                                  |