<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from workiva import SDK, models

async def main():

    async with SDK(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:

        res = await sdk.activities.get_activity_action_by_id_async(activity_action_id="com.workiva.activity.retention_policy.update")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->