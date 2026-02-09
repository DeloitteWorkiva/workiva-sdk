# DatasetInput

Details about the dataset.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `sheet`                                                           | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The unique identifier of the sheet to which this dataset belongs. | 27f1b61c04ae4b0991bc73c631914e1d                                  |
| `values`                                                          | List[List[*Any*]]                                                 | :heavy_minus_sign:                                                | A row-major ordered multidimensional array of cell values.        | [<br/>[<br/>1,<br/>4<br/>],<br/>[<br/>2,<br/>""<br/>]<br/>]       |