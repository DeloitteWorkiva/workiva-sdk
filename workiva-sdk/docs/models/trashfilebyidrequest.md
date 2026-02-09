# TrashFileByIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `file_id`                                                          | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the file                                  |
| `file_trash_options`                                               | [Nullable[models.FileTrashOptions]](../models/filetrashoptions.md) | :heavy_check_mark:                                                 | The request body for the file trash endpoint                       |