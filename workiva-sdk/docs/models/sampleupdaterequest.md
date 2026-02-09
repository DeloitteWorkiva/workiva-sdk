# SampleUpdateRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request_body`                                                   | List[[models.MatrixSampleInput](../models/matrixsampleinput.md)] | :heavy_check_mark:                                               | Details about the samples to update                              |
| `matrix_id`                                                      | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the matrix                              |
| `test_form_id`                                                   | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the test form                           |
| `test_phase_id`                                                  | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the test phase                          |