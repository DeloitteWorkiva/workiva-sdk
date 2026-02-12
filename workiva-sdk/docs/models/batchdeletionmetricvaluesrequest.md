# BatchDeletionMetricValuesRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `program_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the program                               |
| `metric_id`                                                        | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the metric                                |
| `metric_value_identifier`                                          | [models.MetricValueIdentifier](../models/metricvalueidentifier.md) | :heavy_check_mark:                                                 | The metric values to delete                                        |