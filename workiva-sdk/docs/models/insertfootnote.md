# InsertFootnote

A text edit for inserting a footnote into rich text. The created rich text id associated with the footnote annotation area can be retrieved from the rich text edit operation results. This edit is not supported in table rich cell edits.



## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `insert_at`                                                                           | [models.Caret](../models/caret.md)                                                    | :heavy_check_mark:                                                                    | A caret (as in Caret Navigation) is a location between two characters in a paragraph. |