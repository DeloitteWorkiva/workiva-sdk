# Reports

## Overview

Endpoints used to generate Admin reports

### Available Operations

* [get_org_report_users](#get_org_report_users) - List organization users

## get_org_report_users

Similar to an organization admin's "People View" export, this returns a paged list of specific details about the organization's users, including their usernames, display names, email addresses, SAML IDs, last logins, workspace memberships, licenses and roles. Results are sorted by displayName. <br /><br /> To obtain an organization's users, you need its organizationId. To view the organizationId in Wdesk, click your name in the lower left, and select <strong>Organization Admin</strong>. In the URL in your browser, the organizationId appears as a GUID after the /o/ such as 371b5fc8-fcc4-404a-9d22-d07d8f46a7e0. To view the ID of another organization you manage, select <strong>Switch Organizations</strong> from the left-hand menu, and search for and select the organization. <br /><br /> <strong>Requires the calling user to be an organization admin</strong>.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrgReportUsers" method="get" path="/organizations/{organizationId}/orgReportUsers" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reports.get_org_report_users(organization_id="d6e178fd-4dd5-47e5-9457-68dd64b03655", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the organization                           | d6e178fd-4dd5-47e5-9457-68dd64b03655                                |
| `page_after`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Paging cursor                                                       |                                                                     |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return. Maximum of 1000.                         |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetOrgReportUsersResponse1](../../models/getorgreportusersresponse1.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Failure               | 400, 401, 403, 404, 405, 415 | application/json             |
| errors.Failure               | 500, 501, 503                | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |