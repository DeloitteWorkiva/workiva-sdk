# DeleteDatasetBySheetIDRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `spreadsheet_id`                                                  | *str*                                                             | :heavy_check_mark:                                                | The unique identifier of the spreadsheet                          |                                                                   |
| `sheet_id`                                                        | *str*                                                             | :heavy_check_mark:                                                | The unique identifier of the sheet                                |                                                                   |
| `deletevalues`                                                    | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Indicates whether values should be deleted along with the dataset | false                                                             |