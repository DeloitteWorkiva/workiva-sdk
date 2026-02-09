# TableFiltersReapplication

A table filter reapply operation, which can reapply filters to a table and optionally force hide footnotes.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `force_hide_footnotes`                                                                 | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Whether the filter should be reapplied if doing so would cause footnotes to be hidden. | true                                                                                   |