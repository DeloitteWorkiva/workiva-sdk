# CsvOptions

Optional options to export the spreadsheet as a comma-separated values (.CSV) file. If no options are provided, `exportAsFormulas` defaults to False.


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `export_as_formulas`                                                                                | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Whether to export cells containing formulas as the formula or the formula result. False by default. | true                                                                                                |