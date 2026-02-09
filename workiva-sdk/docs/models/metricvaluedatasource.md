# MetricValueDataSource

Represents the source of the value, which can be a Workiva spreadsheet or table cell or a Workiva document text region.
Only one of the connection types can be specified.



## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `connection_type`                                                                            | [Optional[models.ConnectionType]](../models/connectiontype.md)                               | :heavy_minus_sign:                                                                           | The type of connection to the value.                                                         | spreadsheetCell                                                                              |
| `spreadsheet_cell_connection`                                                                | [OptionalNullable[models.SpreadsheetCellConnection]](../models/spreadsheetcellconnection.md) | :heavy_minus_sign:                                                                           | Represents a connection to a value from a Workiva spreadsheet                                |                                                                                              |
| `table_cell_connection`                                                                      | [OptionalNullable[models.TableCellConnection]](../models/tablecellconnection.md)             | :heavy_minus_sign:                                                                           | Represents a connection to a value from a Workiva table cell                                 |                                                                                              |