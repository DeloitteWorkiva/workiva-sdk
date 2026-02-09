# WdataGetTablesDependentOnQueryRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of folders to return, from 1 to 1000; by default, 1000             |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `query_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier of the query                                            |