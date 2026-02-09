# RichTextEditResult

A reference to a resource that was created by a rich text edit.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `rich_text`                                                                    | *OptionalNullable[str]*                                                        | :heavy_minus_sign:                                                             | The unique identifier of the rich text created by the rich text edit.          | WA2NiYGJgm7cWr4W6Ka9BHScz56m2AT2FqTmBgekyk399M99I9Bb69BoEt3WHCag               |
| `table`                                                                        | *OptionalNullable[str]*                                                        | :heavy_minus_sign:                                                             | The unique identifier of the table created by the rich text edit.              | 8610c7b132e944cb9e5c11daf08b1b1c                                               |
| `type`                                                                         | [Optional[models.RichTextEditResultType]](../models/richtexteditresulttype.md) | :heavy_minus_sign:                                                             | The type of resource created from a rich text edit.                            |                                                                                |