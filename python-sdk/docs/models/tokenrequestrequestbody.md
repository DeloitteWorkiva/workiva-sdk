# TokenRequestRequestBody


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `client_id`                                                      | *Optional[str]*                                                  | :heavy_minus_sign:                                               | A previously obtained client id.                                 |
| `client_secret`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | A previously obtained client secret.                             |
| `grant_type`                                                     | [models.GrantType](../models/granttype.md)                       | :heavy_check_mark:                                               | The grant type for the Bearer token. Must be client_credentials. |
| `scope`                                                          | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The scope of the access request.                                 |