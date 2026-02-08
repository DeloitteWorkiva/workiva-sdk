# TableFiltersReapplicationRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `table_id`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | The unique identifier for the table                                        | WW91IGZvdW5kfIG1lIQ                                                        |
| `table_filters_reapplication`                                              | [models.TableFiltersReapplication](../models/tablefiltersreapplication.md) | :heavy_check_mark:                                                         | The filter reapplication request to apply                                  | {<br/>"forceHideFootnotes": true<br/>}                                     |