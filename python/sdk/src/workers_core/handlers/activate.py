from __future__ import annotations

import asyncio

from workers_core.handlers.inbound_workflow_handler import handle_incoming_workflow
from workers_core.state.global_state import GlobalState


async def activate(gs: GlobalState) -> None:
    # Start dispatcher workers
    await gs.dispatcher.start(workers=4)
    # Start inbound workflow reader
    asyncio.create_task(handle_incoming_workflow(gs))
