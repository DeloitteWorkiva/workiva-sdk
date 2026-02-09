# GetSectionByIDRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `document_id`                                           | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the document                   |                                                         |
| `section_id`                                            | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the section                    |                                                         |
| `expand`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Returns related resources inline with the main resource | ?$expand=relationships<br/>                             |
| `revision`                                              | *Optional[str]*                                         | :heavy_minus_sign:                                      | Returns resources at a specific revision                | 1A2B3C4D                                                |