# RestoreFileByIDRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `file_id`                                                    | *str*                                                        | :heavy_check_mark:                                           | The unique identifier of the file                            |
| `file_restore_options`                                       | [models.FileRestoreOptions](../models/filerestoreoptions.md) | :heavy_check_mark:                                           | Request body for File restore endpoint                       |