# SheetUpdateMergeRanges

Merge ranges


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `force`                                                            | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Force the merge through source links, xbrl facts, connections, etc |
| `merge_type`                                                       | [Optional[models.MergeType]](../models/mergetype.md)               | :heavy_minus_sign:                                                 | How cells should be merged                                         |
| `ranges`                                                           | List[[Nullable[models.Range]](../models/range.md)]                 | :heavy_check_mark:                                                 | The ranges to merge                                                |