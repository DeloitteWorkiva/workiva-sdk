# DeleteText

An edit to delete text from a range of rich text.  Note that all content, such as tables, images, charts, or footnotes, will also be deleted. Links must be removed from the selection using a [`RemoveLinks`](ref:content#removelinks) [links edit](ref:richtextlinksbatchedit) before deleting a selection containing links.



## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `selection`                                                                                      | [models.RichTextSelection](../models/richtextselection.md)                                       | :heavy_check_mark:                                                                               | Describes a selection within piece of rich text                                                  | {<br/>"start": {<br/>"offset": 0,<br/>"paragraphIndex": 0<br/>},<br/>"stop": {<br/>"offset": 10,<br/>"paragraphIndex": 2<br/>}<br/>} |