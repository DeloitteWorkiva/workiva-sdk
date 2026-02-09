# UpdateValuesByRangeRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `spreadsheet_id`                                   | *str*                                              | :heavy_check_mark:                                 | The unique identifier of the spreadsheet           |
| `sheet_id`                                         | *str*                                              | :heavy_check_mark:                                 | The unique identifier of the sheet                 |
| `range`                                            | *Nullable[str]*                                    | :heavy_check_mark:                                 | The range of values, in A1-style notation          |
| `range_values`                                     | [models.RangeValues](../models/rangevalues.md)     | :heavy_check_mark:                                 | All values for the range, not just those to update |