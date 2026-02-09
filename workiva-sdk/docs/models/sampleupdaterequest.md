# SampleUpdateRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `test_form_id`                                                   | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the test form                           |
| `test_phase_id`                                                  | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the test phase                          |
| `matrix_id`                                                      | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the matrix                              |
| `request_body`                                                   | List[[models.MatrixSampleInput](../models/matrixsampleinput.md)] | :heavy_check_mark:                                               | Details about the samples to update                              |