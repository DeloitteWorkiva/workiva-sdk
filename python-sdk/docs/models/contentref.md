# ContentRef

A reference to a specific content item.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `drawing`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Identifier of a drawing or null if the content isn't a drawing.     |                                                                     |
| `rich_text`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Identifier of a rich text or null if the content isn't a rich text. |                                                                     |
| `table`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Identifier of a table or null if the content isn't a table.         | WA7i5vbm7lNaEn6XT97lNaEn6XT9AtcW5vb22BJjMrqxmrujMrqxmru             |
| `type`                                                              | [Optional[models.ContentRefType]](../models/contentreftype.md)      | :heavy_minus_sign:                                                  | The type of content.                                                | richText                                                            |