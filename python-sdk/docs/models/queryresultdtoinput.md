# QueryResultDtoInput


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `is_explain`                                                 | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Determines if this query is to be explained and not executed |
| `parameters`                                                 | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | The query parameter map                                      |
| `query_dto`                                                  | [Optional[models.QueryDtoInput]](../models/querydtoinput.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `query_id`                                                   | *str*                                                        | :heavy_check_mark:                                           | The identifier of the original query                         |