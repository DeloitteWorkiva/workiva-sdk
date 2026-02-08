# SheetUpdateInsertColumns

Insert columns into the sheet


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `inherit_from`                                             | [models.InheritFrom](../models/inheritfrom.md)             | :heavy_check_mark:                                         | Where to inherit formats from when performing an insertion |
| `insertions`                                               | List[[models.Insertion](../models/insertion.md)]           | :heavy_check_mark:                                         | List of column insertions                                  |