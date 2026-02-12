# PartiallyUpdateSpreadsheetByIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `spreadsheet_id`                                                   | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the spreadsheet                           |
| `request_body`                                                     | List[[models.JSONPatchOperation](../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                 | A collection of patch operations to apply to the spreadsheet.      |