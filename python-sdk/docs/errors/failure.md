# Failure

An error response. All fields other than "errors" are optional


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `errors`                                                                                  | List[[errors.Errors](../errors/errors.md)]                                                | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `jsonapi`                                                                                 | [Optional[errors.Jsonapi]](../errors/jsonapi.md)                                          | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `links`                                                                                   | Dict[str, *Any*]                                                                          | :heavy_minus_sign:                                                                        | A list of URLs.                                                                           |
| `meta`                                                                                    | Dict[str, *Any*]                                                                          | :heavy_minus_sign:                                                                        | Non-standard meta-information that cannot be represented as an attribute or relationship. |