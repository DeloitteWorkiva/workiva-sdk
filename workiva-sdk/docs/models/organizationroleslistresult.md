# OrganizationRolesListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of `OrganizationRole` objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `at_next_link`                                                 | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | Pagination link for next set of results                        | <opaque_url>                                                   |
| `data`                                                         | List[[models.OrganizationRole](../models/organizationrole.md)] | :heavy_check_mark:                                             | N/A                                                            |                                                                |