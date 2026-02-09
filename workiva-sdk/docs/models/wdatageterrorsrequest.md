# WdataGetErrorsRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `file_id`                                                                     | *str*                                                                         | :heavy_check_mark:                                                            | The unique identifier of the file                                             |
| `cursor`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A paging cursor; if included, `limit` is ignored                              |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The number of errors to return, from 1 to 50; by default, 50                  |
| `offset`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The item to start with on the page, greater than or equal to 0; by default, 0 |