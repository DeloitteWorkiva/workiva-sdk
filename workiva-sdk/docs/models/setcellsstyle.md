# SetCellsStyle

Applies a style to cells in the given ranges of a table. The "Normal" text style is not supported in table cells. Use the "Table (Normal)" style to apply normal styles to text in a table cell.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `ranges`                                         | List[[models.CellRange](../models/cellrange.md)] | :heavy_check_mark:                               | A collection of cell ranges in a table.<br/>     |                                                  |
| `style`                                          | *str*                                            | :heavy_check_mark:                               | The unique identifier of a style.                | c3R5bGUta2V5Ol90Ymw                              |