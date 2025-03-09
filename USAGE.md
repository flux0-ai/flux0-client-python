<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from flux0_client import Flux0Client


with Flux0Client() as fc_client:

    res = fc_client.agents.list()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from flux0_client import Flux0Client

async def main():

    async with Flux0Client() as fc_client:

        res = await fc_client.agents.list_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->