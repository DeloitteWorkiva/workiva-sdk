# Iam

## Overview

Before your application can access private data using other Workiva APIs, it must obtain an access token that grants access to those APIs.

Use the IAM REST API endpoint to exchange your OAuth credentials (clientID and clientSecret) for a token.


### Available Operations

* [token_request](#token_request) - Retrieve a token

## token_request

Include the client_id and client_secret in the body of the request as form encoded parameters. For example, the body of the request would be `grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>`. The client can optionally specify a `scope` parameter to limit the scope of the returned [access token](ref:helpers#bearertoken). In turn, the server uses a `scope` response parameter to inform the client of the scope of the actual access token issued. The actual `scope` returned may not match the `scope` requested. Subsequent requests to Workiva APIs are authorized using the bearer token.


### Example Usage

<!-- UsageSnippet language="python" operationID="tokenRequest" method="post" path="/oauth2/token" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.iam.token_request()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.TokenRequestRequestBody](../../models/tokenrequestrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.BearerToken](../../models/bearertoken.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.IamError  | 400, 401         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |