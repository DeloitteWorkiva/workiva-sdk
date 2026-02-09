# RangeValues


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `range`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | The range of values, in A1-style notation.                 | A1:B2                                                      |
| `values`                                                   | List[List[*Nullable[Any]*]]                                | :heavy_minus_sign:                                         | A row-major ordered multidimensional array of cell values. | [<br/>[<br/>1,<br/>4<br/>],<br/>[<br/>2,<br/>""<br/>]<br/>] |