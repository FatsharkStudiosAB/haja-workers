from __future__ import annotations

import asyncio

from python_execution_server.handlers.inbound_workflow_handler import handle_incoming_workflow
from python_execution_server.state.global_state import GlobalState


async def activate(gs: GlobalState) -> None:
    # Start dispatcher workers
    await gs.dispatcher.start(workers=4)
    # Start inbound workflow reader
    asyncio.create_task(handle_incoming_workflow(gs))
