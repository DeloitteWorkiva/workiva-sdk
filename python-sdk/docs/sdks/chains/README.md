# Chains

## Overview

### Available Operations

* [chain_filter_search](#chain_filter_search) - Search previous chain runs
* [chain_inputs_search](#chain_inputs_search) - Search previous chain runs for an input value
* [chain_run_history](#chain_run_history) - Return run history for a chain
* [export_chain](#export_chain) - Export a chain
* [get_authorizations_activity](#get_authorizations_activity) - Return a list of authorization activities
* [get_chain](#get_chain) - Return chain properties
* [get_chain_run](#get_chain_run) - Return chain run properties
* [get_chain_run_nodes](#get_chain_run_nodes) - Return chain run properties with nodes
* [get_chains](#get_chains) - Return a list of chains for an environment
* [get_commands](#get_commands) - Return command properties
* [get_environment](#get_environment) - Return environment properties
* [get_environments](#get_environments) - Return a list of environments for a workspace
* [get_login_activity](#get_login_activity) - Return a list of login activity events
* [get_permissions](#get_permissions) - Return a list of all permissions for a company
* [get_user](#get_user) - Return user properties
* [get_user_group](#get_user_group) - Return user group properties
* [get_user_group_permissions](#get_user_group_permissions) - Return a list of permissions for a user group
* [get_user_groups](#get_user_groups) - Return a list of all user groups
* [get_user_user_groups](#get_user_user_groups) - Return a list of user groups
* [get_users](#get_users) - Return a list of users
* [get_workspace](#get_workspace) - Return workspace properties
* [get_workspaces](#get_workspaces) - Return a list of workspaces
* [import_chain](#import_chain) - Import a chain
* [publish](#publish) - Publish draft version of a mapping group
* [publish_chain](#publish_chain) - Publish a chain
* [search_chains](#search_chains) - Search chains
* [start_chain](#start_chain) - Execute a chain
* [stop_chain](#stop_chain) - Stop a running chain
* [update_rules](#update_rules) - Update mapping group rules

## chain_filter_search

Returns a list of all previous chain runs that match the provided criteria. The environment IDs specify which environments should be searched for the chain run. The chain IDs specify which specific chains should be returned. The state specified returns only those chains that are in that state (e.g. "completed"). If a cursor is provided, the corresponding page will be returned.


### Example Usage

<!-- UsageSnippet language="python" operationID="chains_chainFilterSearch" method="get" path="/v1/execute/chain_run/search" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.chain_filter_search(request={
        "chain_id": [
            "574",
        ],
        "cursor": "",
        "end_date": "1616143293",
        "environment_id": [
            "139",
            "140",
            "141",
        ],
        "sort": models.Sort.DESC,
        "start_date": "1616143293",
        "state": models.QueryParamState.COMPLETED,
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.ChainsChainFilterSearchRequest](../../models/chainschainfiltersearchrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |
| `server_url`                                                                            | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | An optional server URL to use.                                                          |

### Response

**[models.ChainsChainFilterSearchResponse](../../models/chainschainfiltersearchresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404, 422           | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## chain_inputs_search

Returns a list of all chain runs whose inputs match the provided search criteria. The search text is fuzzy matched; it matches any input value that contains the provided string. For example, a command that takes a File ID of "my_file_id" as an input can be searched using "my_file_id" as the search text input. The environment ID specifies which environment should be searched for chain run input parameters. The limit and cursor help determine the page size and which page to return.


### Example Usage

<!-- UsageSnippet language="python" operationID="chains_chainInputsSearch" method="get" path="/v1/execute/environment/{environment_id}/chain/inputs_search" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.chain_inputs_search(environment_id="130", search_text="List File", cursor="", limit="10")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the environment to search for chains run inputs.          | 74                                                                  |
| `search_text`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The fuzzy input value to search for.                                | List File                                                           |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor value returned from the API, indicating page information.    |                                                                     |
| `limit`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Limit number of chainExecutors returned (Max 50).                   | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsChainInputsSearchResponse](../../models/chainschaininputssearchresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404, 422           | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## chain_run_history

Retrieves a list of run history for a chain.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_chainRunHistory" method="get" path="/v1/execute/environment/{environment_id}/chain/{chain_id}/history" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.chain_run_history(request={
        "chain_id": "54865",
        "end_date": "1616143293",
        "environment_id": "139",
        "limit": "10",
        "start_date": "1616143293",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.ChainsChainRunHistoryRequest](../../models/chainschainrunhistoryrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |
| `server_url`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | An optional server URL to use.                                                      |

### Response

**[models.ChainsChainRunHistoryResponse](../../models/chainschainrunhistoryresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## export_chain

Returns an encoded string to be stored in a file with a `.chain` extension. The `.chain` file can then be used later during an import chain call.
> **Note:** The exported chain will automatically expire and become unusable after 14 days. This has no bearing on the original chain or any imported copies.


### Example Usage

<!-- UsageSnippet language="python" operationID="chains_exportChain" method="post" path="/v1/chains/{chain_id}/export" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.export_chain(chain_id="54865")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `chain_id`                                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                     | The ID of the Chain.                                                                                                                                                                                                                                                                                                                                   | 54865                                                                                                                                                                                                                                                                                                                                                  |
| `wk_target_workspace`                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                     | The `wk-target-workspace` header is only required for requests made by a service provider application. This does not apply to the majority of Workiva Chains API users. This header specifies the ID of the target workspace on which the service provider application wishes to take action. This workspace must be managed by the service provider.<br/> |                                                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
| `server_url`                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                     | An optional server URL to use.                                                                                                                                                                                                                                                                                                                         | http://localhost:8080                                                                                                                                                                                                                                                                                                                                  |

### Response

**[models.ChainsExportChainResponse](../../models/chainsexportchainresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 400, 401, 404           | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_authorizations_activity

Returns a list of recent authorization activity events.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getAuthorizationsActivity" method="get" path="/v1/security/authorizations_activity" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_authorizations_activity(page=3, page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to retrieve in the paginated results (0-based index).   | 3                                                                   |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of results returned (Max 100).                         | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsGetAuthorizationsActivityResponse](../../models/chainsgetauthorizationsactivityresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_chain

Returns properties for a chain with the provided ID, or a 404 if no such chain is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getChain" method="get" path="/v1/metadata/environment/{environment_id}/chain/{chain_id}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_chain(chain_id="61549", environment_id="139")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chain_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Chain.                                                | 61549                                                               |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Environment.                                          | 139                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainResponse](../../models/chainresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_chain_run

Returns properties for a chain run with the provided ID, or a 404 if no such chain run is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getChainRun" method="get" path="/v1/execute/chain_run/{chain_run_id}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_chain_run(chain_run_id="94532")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chain_run_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Chain Run.                                            | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainRunResponse](../../models/chainrunresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_chain_run_nodes

Returns properties and nodes for a chain run with the provided ID, or a 404 if no such chain run is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getChainRunNodes" method="get" path="/v1/execute/chain_run/{chain_run_id}/nodes" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_chain_run_nodes(chain_run_id="54309")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chain_run_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Chain Run.                                            | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainRunWithNodesResponse](../../models/chainrunwithnodesresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_chains

Retrieves a list of chains for an environment.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getChains" method="get" path="/v1/metadata/environment/{environment_id}/chain" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_chains(environment_id="139")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Environment.                                          | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsEnvironmentResponse](../../models/chainsenvironmentresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_commands

Returns properties for a command with the provided ID, or a 404 if no such command is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getCommands" method="get" path="/v1/metadata/environment/{environment_id}/chain/{chain_id}/command" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_commands(chain_id="2339", environment_id="139")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chain_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Chain.                                                | 2339                                                                |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Environment.                                          | 139                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.CommandsResponse](../../models/commandsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_environment

Return properties for an environment in a workspace with the provided IDs, or a 404 if no such workspace is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getEnvironment" method="get" path="/v1/metadata/workspace/{workspace_id}/environment/{environment_id}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_environment(environment_id="139", workspace_id="12")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Environment.                                          | 74                                                                  |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Workspace.                                            | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.EnvironmentResponse](../../models/environmentresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_environments

Return a list of environments for a workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getEnvironments" method="get" path="/v1/metadata/workspace/{workspace_id}/environment" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_environments(workspace_id="12")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Workspace.                                            | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.EnvironmentsResponse](../../models/environmentsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_login_activity

Returns a list of recent login activity events.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getLoginActivity" method="get" path="/v1/security/login_activity" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_login_activity(page=3, page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to retrieve in the paginated results (0-based index).   | 3                                                                   |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of results returned (Max 100).                         | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsGetLoginActivityResponse](../../models/chainsgetloginactivityresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_permissions

Returns a list of all permissions for a company.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getPermissions" method="get" path="/v1/security/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_permissions(page=3, page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to retrieve in the paginated results (0-based index).   | 3                                                                   |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of results returned (Max 100).                         | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsGetPermissionsResponse](../../models/chainsgetpermissionsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_user

Returns properties for a user with the provided ID, or a 404 if no such user is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getUser" method="get" path="/v1/security/users/{userId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_user(user_id="1")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the User.                                                 | 1                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.UserResponse](../../models/userresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_user_group

Return properties for a user group with the provided ID, or a 404 if no such user group is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getUserGroup" method="get" path="/v1/security/user_groups/{userGroupId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_user_group(user_group_id="21")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_group_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the User Group.                                           | 21                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.UserGroupResponse](../../models/usergroupresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_user_group_permissions

Returns properties for a user group with the provided ID, or a 404 if no such user group is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getUserGroupPermissions" method="get" path="/v1/security/user_groups/{userGroupId}/permissions" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_user_group_permissions(user_group_id="1", page=3, page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_group_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the User Group.                                           | 1                                                                   |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to retrieve in the paginated results (0-based index).   | 3                                                                   |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of results returned (Max 100).                         | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsGetUserGroupPermissionsResponse](../../models/chainsgetusergrouppermissionsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_user_groups

Returns a list of all user groups in a company.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getUserGroups" method="get" path="/v1/security/user_groups" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_user_groups(page=3, page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to retrieve in the paginated results (0-based index).   | 3                                                                   |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of results returned (Max 100).                         | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsGetUserGroupsResponse](../../models/chainsgetusergroupsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_user_user_groups

Returns a list of all groups that a user is a part of in a particular company.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getUserUserGroups" method="get" path="/v1/security/users/{userId}/groups" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_user_user_groups(user_id="1", page=3, page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the User.                                                 | 1                                                                   |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to retrieve in the paginated results (0-based index).   | 3                                                                   |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of results returned (Max 100).                         | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsGetUserUserGroupsResponse](../../models/chainsgetuserusergroupsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_users

Returns a list of all users in a particular company.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getUsers" method="get" path="/v1/security/users" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_users(page=3, page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to retrieve in the paginated results (0-based index).   | 3                                                                   |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of results returned (Max 100).                         | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsGetUsersResponse](../../models/chainsgetusersresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_workspace

Returns properties for a workspace with the provided ID, or a 404 if no such workspace is found.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getWorkspace" method="get" path="/v1/metadata/workspace/{workspace_id}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_workspace(workspace_id="12")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Workspace.                                            | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.WorkspaceResponse](../../models/workspaceresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_workspaces

Retrieves a list of workspaces for a company.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_getWorkspaces" method="get" path="/v1/metadata/workspace" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.get_workspaces()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.WorkspacesResponse](../../models/workspacesresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## import_chain

Takes a .chain file and imports it into the provided environment. Returns chain metadata for the imported chain.
> **Note:** .chain export files will automatically expire and become unusable after 14 days.  Expired .chain files remain on the exported system until removed manually.


### Example Usage

<!-- UsageSnippet language="python" operationID="chains_importChain" method="post" path="/v1/environments/{environment_id}/import_chain" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.import_chain(environment_id="139", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `environment_id`                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                     | The ID of the Environment.                                                                                                                                                                                                                                                                                                                             | 74                                                                                                                                                                                                                                                                                                                                                     |
| `request_body`                                                                                                                                                                                                                                                                                                                                         | [models.ChainsImportChainRequestBody](../../models/chainsimportchainrequestbody.md)                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                     | The .chain file to import.                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                        |
| `wk_target_workspace`                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                     | The `wk-target-workspace` header is only required for requests made by a service provider application. This does not apply to the majority of Workiva Chains API users. This header specifies the ID of the target workspace on which the service provider application wishes to take action. This workspace must be managed by the service provider.<br/> |                                                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
| `server_url`                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                     | An optional server URL to use.                                                                                                                                                                                                                                                                                                                         | http://localhost:8080                                                                                                                                                                                                                                                                                                                                  |

### Response

**[models.ChainsImportChainResponse](../../models/chainsimportchainresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 400, 401, 403           | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## publish

Publish a draft version of a mapping group, specified by the mapping group GUID.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_publish" method="post" path="/v1/dataprep/mapping_groups/{mappingGroupGuid}/publish" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.publish(mapping_group_guid="4ef64a1e-55da-4071-8168-d3387d99035d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `mapping_group_guid`                                                | *str*                                                               | :heavy_check_mark:                                                  | The GUID of the Mapping Group.                                      | 4ef64a1e-55da-4071-8168-d3387d99035d                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainsPublishResponseBody](../../models/chainspublishresponsebody.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ErrorWithoutLineNumber | 400                           | application/json              |
| errors.SDKError               | 4XX, 5XX                      | \*/\*                         |

## publish_chain

Publishes the chain specified by the chain_id.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_publishChain" method="post" path="/v1/chains/{chain_id}/publish" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.publish_chain(chain_id="54865")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `chain_id`                                                                                      | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the Chain.                                                                            | 54865                                                                                           |
| `request_body`                                                                                  | [Optional[models.ChainsPublishChainRequestBody]](../../models/chainspublishchainrequestbody.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |                                                                                                 |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |
| `server_url`                                                                                    | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | An optional server URL to use.                                                                  | http://localhost:8080                                                                           |

### Response

**[models.ChainsPublishChainResponse](../../models/chainspublishchainresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 400, 401, 403           | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## search_chains

Returns a list of all chains that match the provided criteria. The name of the change is fuzzy matched; it matches any chain name that contains the provided string. The workspace, external workspace, and environment IDs all help filter down the results to a particular setting. Setting the parallel execution enabled flag will only return chains whose commands run in parallel.


### Example Usage

<!-- UsageSnippet language="python" operationID="chains_searchChains" method="get" path="/v1/metadata/chains/search" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.search_chains(request={
        "environment_id": 193,
        "external_workspace_id": "201",
        "name": "Monthly Reports",
        "parallel_execution_enabled": False,
        "workspace_id": 66,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.ChainsSearchChainsRequest](../../models/chainssearchchainsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.ChainsResponse](../../models/chainsresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## start_chain

Starts a chain run for a specific chain in an environment, specified by the Chain and Environment ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_startChain" method="post" path="/v1/execute/environment/{environment_id}/chain/{chain_id}/start" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.start_chain(chain_id="34090", environment_id="139", request_body={
        "runtime_variables": {
            "variableName": "variableValue",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `chain_id`                                                                        | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the Chain.                                                              | 34090                                                                             |
| `environment_id`                                                                  | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the Environment.                                                        | 74                                                                                |
| `request_body`                                                                    | [models.ChainsStartChainRequestBody](../../models/chainsstartchainrequestbody.md) | :heavy_check_mark:                                                                | The runtime variables that have been pre-defined for a Chain.                     |                                                                                   |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |
| `server_url`                                                                      | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | An optional server URL to use.                                                    | http://localhost:8080                                                             |

### Response

**[models.ChainRunResponse](../../models/chainrunresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404, 422           | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## stop_chain

Stop a chain run with the specified ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_stopChain" method="post" path="/v1/execute/chain_run/{chain_run_id}/stop" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.stop_chain(chain_run_id="543459")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chain_run_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Chain Run.                                            | 74                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.ChainRunResponse](../../models/chainrunresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ChainSingleError | 401, 404, 422           | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## update_rules

Update a mapping group ruleset, specified by the mapping group GUID.

### Example Usage

<!-- UsageSnippet language="python" operationID="chains_updateRules" method="post" path="/v1/dataprep/mapping_groups/{mappingGroupGuid}/update_rules" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.chains.update_rules(mapping_group_guid="4ef64a1e-55da-4071-8168-d3387d99035d", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `mapping_group_guid`                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The GUID of the Mapping Group.                                                      | 4ef64a1e-55da-4071-8168-d3387d99035d                                                |
| `request_body`                                                                      | [models.ChainsUpdateRulesRequestBody](../../models/chainsupdaterulesrequestbody.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |
| `server_url`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | An optional server URL to use.                                                      | http://localhost:8080                                                               |

### Response

**[models.MappingRuleUploadResult](../../models/mappingruleuploadresult.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.MappingRuleUploadResult       | 400                                  | application/json                     |
| errors.ChainsUpdateRulesResponseBody | 401                                  | application/json                     |
| errors.SDKError                      | 4XX, 5XX                             | \*/\*                                |