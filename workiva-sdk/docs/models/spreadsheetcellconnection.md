# SpreadsheetCellConnection

Represents a connection to a value from a Workiva spreadsheet


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `cell`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | The column-row identifier of a specific cell within a sheet (i.e. A1) | A1                                                                    |
| `sheet`                                                               | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of a specific sheet within a spreadsheet.       | 576696e0f7a143b4a0bc7c20a34480ab                                      |
| `spreadsheet`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the connected spreadsheet.                   | 7a5e271acf1d49d480a6fbabc394a0fa                                      |