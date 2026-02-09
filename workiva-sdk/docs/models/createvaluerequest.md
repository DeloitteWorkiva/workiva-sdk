# CreateValueRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `program_id`                                             | *str*                                                    | :heavy_check_mark:                                       | The unique identifier of the program                     |
| `metric_id`                                              | *str*                                                    | :heavy_check_mark:                                       | The unique identifier of the metric                      |
| `metric_value`                                           | [models.MetricValueInput](../models/metricvalueinput.md) | :heavy_check_mark:                                       | The properties of the metric value to create             |