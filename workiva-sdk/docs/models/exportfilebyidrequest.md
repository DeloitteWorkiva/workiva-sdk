# ExportFileByIDRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `file_id`                                            | *str*                                                | :heavy_check_mark:                                   | The unique identifier of the file                    |                                                      |
| `file_export_by_id`                                  | [models.FileExportByID](../models/fileexportbyid.md) | :heavy_check_mark:                                   | The details of the file export.                      | {<br/>"kind": "SupportingDocument"<br/>}             |