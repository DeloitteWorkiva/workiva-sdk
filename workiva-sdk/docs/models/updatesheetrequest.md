# UpdateSheetRequest


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `spreadsheet_id`                               | *str*                                          | :heavy_check_mark:                             | The unique identifier of the spreadsheet       |
| `sheet_id`                                     | *str*                                          | :heavy_check_mark:                             | The unique identifier of the sheet             |
| `sheet_update`                                 | [models.SheetUpdate](../models/sheetupdate.md) | :heavy_check_mark:                             | A SheetUpdate                                  |