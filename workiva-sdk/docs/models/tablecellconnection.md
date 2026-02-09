# TableCellConnection

Represents a connection to a value from a Workiva table cell


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `cell`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | The column-row identifier of a specific cell within a table (i.e. A1) | A1                                                                    |
| `document`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the connected document.                      | 944204de31eb4f078f531a25d7cdde2f                                      |
| `section`                                                             | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of a specific section within the document.      | 944204de31eb4f078f531a25d7cdde2f_34                                   |
| `table`                                                               | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of a specific table within the document.        | 576696e0f7a143b4a0bc7c20a34480ab                                      |