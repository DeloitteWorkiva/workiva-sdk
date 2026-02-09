# ParagraphSelection

A selection of one or more paragraphs, starting from the start paragraph and ending with the stop paragraph. Both start and stop paragraph indexes are inclusive.



## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `start`                                                 | *Optional[int]*                                         | :heavy_minus_sign:                                      | The zero-based inclusive starting index of a paragraph. | 1                                                       |
| `stop`                                                  | *Optional[int]*                                         | :heavy_minus_sign:                                      | The zero-based inclusive stopping index of a paragraph. | 3                                                       |