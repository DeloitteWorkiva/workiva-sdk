# WdataListQueriesRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of queries to return, from 1 to 1000; by default, 1000             |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |
| `ids`                                                                         | List[*str*]                                                                   | :heavy_minus_sign:                                                            | A list of ids to filter the returned list by                                  |