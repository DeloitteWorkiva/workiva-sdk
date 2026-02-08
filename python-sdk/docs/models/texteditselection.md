# TextEditSelection

The selection where the hyperlink will be applied. The selection range cannot contain any new lines, source links,
destination links, embedded content (tables, images, charts, etc.), footnotes, or any dynamic references (page numbers,
list item references, etc.)



## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `start`                                                                               | [models.Caret](../models/caret.md)                                                    | :heavy_check_mark:                                                                    | A caret (as in Caret Navigation) is a location between two characters in a paragraph. |
| `stop`                                                                                | [models.Caret](../models/caret.md)                                                    | :heavy_check_mark:                                                                    | A caret (as in Caret Navigation) is a location between two characters in a paragraph. |