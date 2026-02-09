# MetricValueStatus

Represents the current status of a metric value.
The status can only be set to `complete` if it's currently `notStarted`,
and it can be reset to `notStarted` if it's `complete`.



## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `NOT_STARTED`       | notStarted          |
| `NOT_SENT`          | notSent             |
| `IN_PROGRESS`       | inProgress          |
| `SENT_FOR_APPROVAL` | sentForApproval     |
| `RETURNED`          | returned            |
| `COMPLETE`          | complete            |
| `ERROR`             | error               |