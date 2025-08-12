from __future__ import annotations

import asyncio
import logging

from python_execution_server.examples.input import input_function
from python_execution_server.examples.store_chat_history import store_chat_history_function
from python_execution_server.examples.random_output import random_output_function
from python_execution_server.sdk.sdk import Server


async def main() -> None:
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s %(name)s: %(message)s")
    server = Server()
    server.register_function(input_function())
    server.register_function(store_chat_history_function())
    server.register_function(random_output_function())
    await server.start()


if __name__ == "__main__":
    asyncio.run(main())
