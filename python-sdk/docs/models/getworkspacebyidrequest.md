# GetWorkspaceByIDRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `dollar_expand`                                         | *Optional[str]*                                         | :heavy_minus_sign:                                      | Returns related resources inline with the main resource | ?$expand=relationships<br/>                             |
| `organization_id`                                       | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the organization               | d6e178fd-4dd5-47e5-9457-68dd64b03655                    |
| `workspace_id`                                          | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the workspace                  |                                                         |