# GetTypeByIDRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `type_id`                                               | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the type                       |                                                         |
| `dollar_expand`                                         | *Optional[str]*                                         | :heavy_minus_sign:                                      | Returns related resources inline with the main resource | ?$expand=relationships<br/>                             |