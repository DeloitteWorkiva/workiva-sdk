# DrawingElementListResult

A collection of elements in a drawing. This contains the shapes, text boxes, and lines for drawing content including slides, layout slides, and drawings in documents. When there are no additional elements before the current  collection, the previous property will be null. When there are no additional elements after the current collection, the next property will be null.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `at_next_link`                                             | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | Pagination link for next set of results                    | <opaque_url>                                               |
| `data`                                                     | List[[models.DrawingElement](../models/drawingelement.md)] | :heavy_check_mark:                                         | Elements contained by this drawing.                        |                                                            |