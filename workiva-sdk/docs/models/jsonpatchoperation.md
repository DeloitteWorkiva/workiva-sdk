# JSONPatchOperation

Represents a single JSON Patch operation. For more information, refer to the [PATCH Update documentation](ref:patch-updates).



## Fields

| Field                        | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `from_`                      | *Optional[str]*              | :heavy_minus_sign:           | N/A                          |
| `op`                         | [models.Op](../models/op.md) | :heavy_check_mark:           | N/A                          |
| `path`                       | *str*                        | :heavy_check_mark:           | N/A                          |
| `value`                      | *OptionalNullable[Any]*      | :heavy_minus_sign:           | N/A                          |