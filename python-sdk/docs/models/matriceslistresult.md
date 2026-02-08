# MatricesListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`Matrix`](ref:testforms#matrix) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `at_next_link`                              | *OptionalNullable[str]*                     | :heavy_minus_sign:                          | The pagination link for next set of results | <opaque_url>                                |
| `data`                                      | List[[models.Matrix](../models/matrix.md)]  | :heavy_check_mark:                          | A list of `Matrix` objects                  |                                             |