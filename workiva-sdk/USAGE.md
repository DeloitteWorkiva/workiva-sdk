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

    res = sdk.chains.export_chain(chain_id="54865")

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

        res = await sdk.chains.export_chain_async(chain_id="54865")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->