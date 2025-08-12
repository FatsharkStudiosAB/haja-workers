from __future__ import annotations

import asyncio
import logging

from workers_server.examples.input import input_function
from workers_server.examples.store_chat_history import store_chat_history_function
from workers_server.examples.random_output import random_output_function
from workers_core import Server


def main() -> None:
    """Main entry point for the workers server console script."""
    asyncio.run(async_main())

async def async_main() -> None:
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s %(name)s: %(message)s")
    server = Server()
    server.register_function(input_function())
    server.register_function(store_chat_history_function())
    server.register_function(random_output_function())
    await server.start()


if __name__ == "__main__":
    main()
