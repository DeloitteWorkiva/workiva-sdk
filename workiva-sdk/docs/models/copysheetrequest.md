# CopySheetRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `spreadsheet_id`                           | *str*                                      | :heavy_check_mark:                         | The unique identifier of the spreadsheet   |
| `sheet_id`                                 | *str*                                      | :heavy_check_mark:                         | The unique identifier of the sheet         |
| `sheet_copy`                               | [models.SheetCopy](../models/sheetcopy.md) | :heavy_check_mark:                         | A SheetCopy object                         |