# PartiallyUpdateSlideByIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request_body`                                                     | List[[models.JSONPatchOperation](../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                 | A collection of patch operations to apply to the slide.            |
| `presentation_id`                                                  | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the presentation                          |
| `slide_id`                                                         | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the slide                                 |