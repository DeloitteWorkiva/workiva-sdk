# GetSampleByIDRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `test_form_id`                                          | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the test form                  |                                                         |
| `test_phase_id`                                         | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the test phase                 |                                                         |
| `matrix_id`                                             | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the matrix                     |                                                         |
| `sample_id`                                             | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the sample                     |                                                         |
| `dollar_expand`                                         | *Optional[str]*                                         | :heavy_minus_sign:                                      | Returns related resources inline with the main resource | ?$expand=relationships<br/>                             |