# SourceTextElement

A text element containing rich text content that is from a source link. This is a subset of TextElement and contains  only types that are allowed within source links.



## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `soft_return`                                                                                | [OptionalNullable[models.SoftReturn]](../models/softreturn.md)                               | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `text_span`                                                                                  | [OptionalNullable[models.SourceTextElementTextSpan]](../models/sourcetextelementtextspan.md) | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `type`                                                                                       | [Optional[models.SourceTextElementType]](../models/sourcetextelementtype.md)                 | :heavy_minus_sign:                                                                           | The type of the text element in rich text that is from a source link.                        |
| `unspecified`                                                                                | [OptionalNullable[models.Unspecified]](../models/unspecified.md)                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |