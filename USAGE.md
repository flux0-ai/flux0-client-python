<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from flux0_client import Flux0


with Flux0() as flux0:

    res = flux0.agents.list()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from flux0_client import Flux0

async def main():

    async with Flux0() as flux0:

        res = await flux0.agents.list_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->