# BatchUpsertionMetricValuesRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `program_id`                                                     | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the program                             |
| `metric_id`                                                      | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the metric                              |
| `metric_value_upsertion`                                         | [models.MetricValueUpsertion](../models/metricvalueupsertion.md) | :heavy_check_mark:                                               | The metric values to upsert                                      |