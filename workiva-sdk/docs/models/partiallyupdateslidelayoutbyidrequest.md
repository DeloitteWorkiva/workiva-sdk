# PartiallyUpdateSlideLayoutByIDRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request_body`                                                         | List[[models.JSONPatchOperation](../models/jsonpatchoperation.md)]     | :heavy_check_mark:                                                     | Patch document representing the changes to be made to the slide layout |
| `presentation_id`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the presentation                              |
| `slide_layout_id`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the slide layout                              |