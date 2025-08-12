# Codex Workflows Python Workers

A Python-based worker implementation for Codex Workflows that provides function execution capabilities via gRPC communication.

## Architecture

This project consists of two Python packages:

- **SDK** (`/sdk`): `codex-workers-sdk-py` - Reusable library for building workflow functions
- **Server** (`/server`): `codex-workers-server-py` - Runnable worker server with examples

## Quick Start

### Prerequisites

- Python 3.10 or later
- pip or uv package manager
- Access to a Codex Workflows gRPC server

### Installation & Usage

#### Option 1: Direct GitHub Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/FatsharkStudiosAB/codex.git
cd codex/workflows/workers/python

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install SDK and server
pip install -e ./sdk
pip install -e ./server

# Run the worker
python -m codex_workers_server.main

# Or use the console script
codex-worker
```

#### Option 2: Install from Local Path

If you have the code locally but want to install as packages:

```bash
# Install SDK first
pip install /path/to/codex/workflows/workers/python/sdk

# Install server (includes SDK dependency)
pip install /path/to/codex/workflows/workers/python/server

# Run
codex-worker
```

#### Option 3: Development Installation

For active development:

```bash
cd codex/workflows/workers/python

# Install in editable mode with development dependencies
pip install -e "./sdk[dev]"
pip install -e "./server[dev]"

# Run with environment variables
export SERVER_NAME="my-python-worker"
export GRPC_SERVER_ADDRESS="localhost:9090"
export SERVER_API_TOKEN="your-token-here"
python -m codex_workers_server.main
```

### Example Usage

Create a custom worker with your own functions:

```python
# my_worker.py
import asyncio
from dataclasses import dataclass
from codex_workers_sdk.sdk import Server
from codex_workers_sdk.function import Function

@dataclass
class GreetingInput:
    name: str

@dataclass  
class GreetingOutput:
    message: str

def create_greeting_function():
    fn = Function[GreetingInput, GreetingOutput](
        name="greeting",
        version="1.0.0", 
        description="Generate a personalized greeting"
    )
    
    async def handler(inputs: GreetingInput, event, gs) -> GreetingOutput:
        return GreetingOutput(message=f"Hello, {inputs.name}!")
    
    return fn.with_handler(handler)

async def main():
    server = Server()
    server.register_function(create_greeting_function())
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())
```

Run your custom worker:

```bash
python my_worker.py
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SERVER_NAME` | `python-execution-server` | Unique identifier for this worker |
| `GRPC_SERVER_ADDRESS` | `localhost:9090` | Address of the Codex Workflows server |
| `SERVER_API_TOKEN` | _(empty)_ | Authentication token (optional) |
| `CACHE_TTL_SECONDS` | `300` | Default cache TTL for functions |

### Configuration via Code

```python
from codex_workers_sdk.config import Config
from codex_workers_sdk.sdk import Server

config = Config(
    server_name="my-custom-worker",
    grpc_server_address="localhost:9090",
    server_api_token="your-token",
    cache_ttl_seconds=600
)

server = Server(config)
```

## Docker Usage

```bash
# Navigate to server directory
cd server

# Build Docker image
docker build -t my-codex-worker .

# Run with environment variables
docker run -e SERVER_NAME=my-worker \
           -e GRPC_SERVER_ADDRESS=host.docker.internal:9090 \
           -e SERVER_API_TOKEN=your-token \
           my-codex-worker
```

## Development

### Development Setup

```bash
# Clone repository
git clone https://github.com/FatsharkStudiosAB/codex.git
cd codex/workflows/workers/python

# Create development environment
python -m venv .venv
source .venv/bin/activate

# Install in editable mode
pip install -e ./sdk
pip install -e ./server

# Install development tools (optional)
pip install black isort mypy pytest

# Run tests
python -m pytest sdk/tests/
python -m pytest server/tests/
```

### Creating Custom Functions

#### Basic Function

```python
from dataclasses import dataclass
from codex_workers_sdk.function import Function

@dataclass
class MyInput:
    value: str

@dataclass
class MyOutput:
    result: str

def my_function():
    fn = Function[MyInput, MyOutput](
        name="my_function",
        version="1.0.0",
        description="My custom function"
    )
    
    async def handler(inputs: MyInput, event, gs) -> MyOutput:
        # Your logic here
        return MyOutput(result=f"Processed: {inputs.value}")
    
    return fn.with_handler(handler)
```

#### Function with State Access

```python
async def advanced_handler(inputs: MyInput, event, gs) -> MyOutput:
    # Access workflow information
    workflow_id = event.workflow
    
    # Use gRPC cache
    cached_data = await gs.grpc_cache.get("my_key")
    
    # Use gRPC store for persistence
    await gs.grpc_store.set(workflow_id, "key", b"data")
    
    # Use RPC client to call other services
    # response = await gs.rpc_client.call(...)
    
    return MyOutput(result="Advanced processing complete")
```

#### Function with Caching

```python
def cached_function():
    return Function[MyInput, MyOutput](
        name="cached_function",
        version="1.0.0", 
        description="Function with custom cache TTL"
    ).with_handler(my_handler).with_cache_ttl(60)  # 60 second cache
```

## Package Structure

```
workflows/workers/python/
├── sdk/                           # Reusable SDK library
│   ├── pyproject.toml            # SDK package definition
│   ├── src/codex_workers_sdk/    # SDK source code
│   │   ├── sdk.py                # Main server class
│   │   ├── function.py           # Function builders
│   │   ├── config.py             # Configuration
│   │   ├── communication/        # gRPC communication
│   │   ├── state/                # Global state management
│   │   ├── types/                # Type definitions
│   │   └── workflowsgrpc/        # Generated gRPC stubs
│   └── README.md                 # SDK documentation
└── server/                       # Runnable worker server
    ├── pyproject.toml            # Server package definition
    ├── src/codex_workers_server/ # Server source code
    │   ├── main.py               # Server entrypoint
    │   └── examples/             # Example functions
    ├── Dockerfile                # Container build
    └── docker-compose.yml        # Local development
```

## Alternative Installation Methods

### Using uv (Fast Python Package Manager)

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create project and install
uv venv
source .venv/bin/activate
uv pip install -e ./sdk -e ./server
```

### Using Poetry

```bash
# In your project directory
poetry init
poetry add codex-workers-sdk-py @ {path = "/path/to/sdk", develop = true}
poetry add codex-workers-server-py @ {path = "/path/to/server", develop = true}
poetry install
poetry run codex-worker
```

### Using pip with Git URLs (Future)

When published to a Git repository:

```bash
# Install SDK
pip install git+https://github.com/FatsharkStudiosAB/codex.git#subdirectory=workflows/workers/python/sdk

# Install server  
pip install git+https://github.com/FatsharkStudiosAB/codex.git#subdirectory=workflows/workers/python/server
```

## Troubleshooting

### Common Issues

**Import Errors**: Make sure both SDK and server are installed:
```bash
pip install -e ./sdk -e ./server
python -c "import codex_workers_sdk, codex_workers_server; print('OK')"
```

**Module Not Found**: Verify the packages are installed in the correct environment:
```bash
pip list | grep codex-workers
```

**Connection Issues**: Check your gRPC server address and ensure the Codex Workflows server is running.

**Authentication Errors**: Verify `SERVER_API_TOKEN` is set correctly if required.

### Debug Mode

Enable verbose logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Or set environment variable:
```bash
export CODEX_LOG_LEVEL=DEBUG
python -m codex_workers_server.main
```

## Examples

See the `server/src/codex_workers_server/examples/` directory for:

- `input.py` - Simple input/output function
- `store_chat_history.py` - Function using persistent storage
- `random_output.py` - Function with caching behavior

## License

Part of the Codex Workflows project. See main repository for license details.
