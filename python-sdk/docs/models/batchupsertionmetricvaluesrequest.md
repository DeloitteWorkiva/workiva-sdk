# BatchUpsertionMetricValuesRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `metric_value_upsertion`                                         | [models.MetricValueUpsertion](../models/metricvalueupsertion.md) | :heavy_check_mark:                                               | The metric values to upsert                                      |
| `metric_id`                                                      | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the metric                              |
| `program_id`                                                     | *str*                                                            | :heavy_check_mark:                                               | The unique identifier of the program                             |