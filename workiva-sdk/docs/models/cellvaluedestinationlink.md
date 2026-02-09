# CellValueDestinationLink

A cell-level destination link. The content of cell destination links cannot be edited with rich cell edits, but other  cell edits are supported.



## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `destination_link`                                                                     | [models.DestinationLinkRef](../models/destinationlinkref.md)                           | :heavy_check_mark:                                                                     | A reference to a destination link.                                                     | {<br/>"destinationLink": "WA7i5vbm7lNaEn6XT9AtcW5vb22BJjMrqxmru",<br/>"revision": "24601abc"<br/>} |
| `paragraphs`                                                                           | List[[models.SourceParagraph](../models/sourceparagraph.md)]                           | :heavy_check_mark:                                                                     | Paragraphs contained in this cell.                                                     |                                                                                        |