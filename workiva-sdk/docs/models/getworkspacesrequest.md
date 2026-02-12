# GetWorkspacesRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `organization_id`                                       | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the organization               | d6e178fd-4dd5-47e5-9457-68dd64b03655                    |
| `maxpagesize`                                           | *Optional[int]*                                         | :heavy_minus_sign:                                      | The maximum number of results to retrieve               |                                                         |
| `next`                                                  | *Optional[str]*                                         | :heavy_minus_sign:                                      | Pagination cursor for next set of results.              | JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA                     |
| `expand`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Returns related resources inline with the main resource | ?$expand=relationships<br/>                             |