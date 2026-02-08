# StyleGuide

Content containing a style guide. This holds the text styles, table styles, and list styles which comprise a style guide.



## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `id`                                               | *Optional[str]*                                    | :heavy_minus_sign:                                 | The unique identifier of a style guide.            | af96388538e3448093a2eba192c86222                   |
| `ordered_list_styles`                              | List[[models.ListStyle](../models/liststyle.md)]   | :heavy_minus_sign:                                 | The ordered styles.                                |                                                    |
| `revision`                                         | *Optional[str]*                                    | :heavy_minus_sign:                                 | The current revision of the style guide            | 1A2B3C4D                                           |
| `table_styles`                                     | List[[models.TableStyle](../models/tablestyle.md)] | :heavy_minus_sign:                                 | The table styles.                                  |                                                    |
| `text_styles`                                      | List[[models.TextStyle](../models/textstyle.md)]   | :heavy_minus_sign:                                 | The text styles.                                   |                                                    |
| `unordered_list_styles`                            | List[[models.ListStyle](../models/liststyle.md)]   | :heavy_minus_sign:                                 | The unordered list styles.                         |                                                    |