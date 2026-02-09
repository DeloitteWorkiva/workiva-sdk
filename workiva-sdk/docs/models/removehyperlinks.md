# RemoveHyperlinks

Removes hyperlinks from a range of text. If a selection starts or stops in the middle of an existing hyperlink the selection will be expanded to include the start and stop of the existing hyperlink.



## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `selection`                                                                                               | [models.Selection](../models/selection.md)                                                                | :heavy_check_mark:                                                                                        | The selection where the hyperlinks will be removed. All hyperlinks within the selection will be removed.<br/> | {<br/>"start": {<br/>"offset": 0,<br/>"paragraphIndex": 0<br/>},<br/>"stop": {<br/>"offset": 10,<br/>"paragraphIndex": 2<br/>}<br/>} |