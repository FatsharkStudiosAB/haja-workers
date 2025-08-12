"""Workers Core SDK - Python implementation for Codex Workflows.

This package provides the core functionality for building and running
workflow functions in Python.
"""

__version__ = "0.1.0"

# Lazy imports to avoid import errors during development
def __getattr__(name):
    if name == "Server":
        from workers_core.sdk import Server
        return Server
    elif name == "Function":
        from workers_core.function import Function
        return Function
    elif name == "SimpleFunction":
        from workers_core.function import SimpleFunction
        return SimpleFunction
    elif name == "FunctionInterface":
        from workers_core.function import FunctionInterface
        return FunctionInterface
    elif name == "Config":
        from workers_core.config import Config
        return Config
    elif name == "load_config":
        from workers_core.config import load_config
        return load_config
    elif name == "EventMessage":
        from workers_core.types.message import EventMessage
        return EventMessage
    elif name == "EventState":
        from workers_core.types.events import EventState
        return EventState
    else:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

__all__ = [
    "Server",
    "Function", 
    "SimpleFunction",
    "FunctionInterface",
    "Config",
    "load_config",
    "EventMessage",
    "EventState",
]
