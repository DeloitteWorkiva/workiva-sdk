# PartiallyUpdateSampleByIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request_body`                                                     | List[[models.JSONPatchOperation](../models/jsonpatchoperation.md)] | :heavy_check_mark:                                                 | A collection of patch operations to apply to the sample.           |
| `matrix_id`                                                        | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the matrix                                |
| `sample_id`                                                        | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the sample                                |
| `test_form_id`                                                     | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the test form                             |
| `test_phase_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the test phase                            |