# RemoveLinks

A text edit for removing source and destination links in rich text. This operation will be a no-op if no links exist within the range of text.



## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `selection`                                                                                      | [models.RichTextSelection](../models/richtextselection.md)                                       | :heavy_check_mark:                                                                               | Describes a selection within piece of rich text                                                  | {<br/>"start": {<br/>"offset": 0,<br/>"paragraphIndex": 0<br/>},<br/>"stop": {<br/>"offset": 10,<br/>"paragraphIndex": 2<br/>}<br/>} |