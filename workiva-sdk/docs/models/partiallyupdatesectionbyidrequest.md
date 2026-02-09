# PartiallyUpdateSectionByIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `document_id`                                                      | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the document                              |
| `section_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the section                               |
| `request_body`                                                     | List[[models.JSONPatchOperation](../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                 | A collection of patch operations to apply to the section.          |