# FileExportByIDDocxOptions

Optional options to export the document as a Microsoft Word document (.DOCX). If no options are provided, all options default to False.



## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `include_leader_dots`                                                         | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Whether to include leader dots when exporting to .DOCX. False by default.     | true                                                                          |
| `show_table_cell_shading`                                                     | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Whether to show table cell shading when exporting to .DOCX. False by default. | true                                                                          |