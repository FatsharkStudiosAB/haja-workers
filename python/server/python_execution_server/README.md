# SDK Usage

Example of registering functions and starting the server using the SDK.

```python
import asyncio
from python_execution_server.sdk.sdk import Server
from python_execution_server.sdk.function import SimpleFunction

async def main():
    server = Server()
    echo = SimpleFunction[dict, dict](
        name="echo", version="1.0.0", description="Echoes input"
    ).with_handler(lambda inputs: inputs)
    server.register_function(echo)
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())
```
