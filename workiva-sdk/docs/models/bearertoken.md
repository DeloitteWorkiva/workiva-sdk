# BearerToken

[Bearer token](ref:helpers#bearertoken) to use in subsequent requests to the Workiva APIs.



## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `access_token`                                                              | *str*                                                                       | :heavy_check_mark:                                                          | The opaque string used to authorize and make requests on behalf of the user |
| `expires_in`                                                                | *int*                                                                       | :heavy_check_mark:                                                          | The number of seconds the access token is valid                             |
| `scope`                                                                     | *str*                                                                       | :heavy_check_mark:                                                          | The limits of the user's access with the token, such as Read or Create      |
| `token_type`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | The type of access token; typically bearer                                  |