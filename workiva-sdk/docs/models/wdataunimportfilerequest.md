# WdataUnimportFileRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `table_id`                                         | *str*                                              | :heavy_check_mark:                                 | The unique identifier of the table                 |
| `file_id`                                          | *str*                                              | :heavy_check_mark:                                 | The unique identifier of the file                  |
| `force`                                            | *Optional[str]*                                    | :heavy_minus_sign:                                 | If true, unimports and deletes file from the table |