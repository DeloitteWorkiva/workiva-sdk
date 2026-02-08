# StyleGuideImportResponse

Response to a style guide import including the URL to upload the file to.



## Fields

| Field                                                                                                                                   | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `upload_url`                                                                                                                            | *str*                                                                                                                                   | :heavy_check_mark:                                                                                                                      | The signed URL used to upload the style guide. Make a POST request to this URL whose body is the contents of the style guide to upload. |