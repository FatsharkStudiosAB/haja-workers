# Workers - Python Implementation

A clean, standard Python implementation for building and running workflow functions.

## Architecture

This project follows Python packaging best practices with two packages:

- **SDK** (`/sdk`): `workers-core` - Reusable library for building workflow functions
- **Server** (`/server`): `workers-server` - Runnable worker server with examples

## Project Structure

```
python/
├── sdk/                           # Core SDK package
│   ├── src/workers_core/          # Main SDK implementation
│   │   ├── __init__.py           # Clean API surface
│   │   ├── sdk.py                # Server class
│   │   ├── function.py           # Function builders
│   │   ├── config.py             # Configuration
│   │   ├── communication/        # gRPC communication
│   │   ├── state/                # State management  
│   │   ├── handlers/             # Request handlers
│   │   ├── types/                # Type definitions
│   │   └── [other modules...]    # Core functionality
│   └── pyproject.toml            # SDK package definition
└── server/                       # Executable server
    ├── src/workers_server/       # Server implementation
    │   ├── __init__.py
    │   ├── main.py               # Main entry point
    │   └── examples/             # Server examples
    └── pyproject.toml            # Server package (depends on SDK)
```

## Quick Start

### Prerequisites

- Python 3.10 or later
- pip or uv package manager
- Access to a Codex Workflows gRPC server

### Installation & Usage

#### Option 1: Development Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/FatsharkStudiosAB/haja-workers.git
cd haja-workers/python

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install SDK and server in editable mode
pip install -e ./sdk
pip install -e ./server

# Run the worker
workers-server

# Or run directly
python -m workers_server.main
```

#### Option 2: Install from Local Path

```bash
# Install SDK first
pip install /path/to/haja-workers/python/sdk

# Install server (includes SDK dependency)
pip install /path/to/haja-workers/python/server

# Run
workers-server
```

### Example Usage

Create a custom worker with your own functions:

```python
# my_worker.py
import asyncio
from dataclasses import dataclass
from workers_core import Server, Function

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

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SERVER_NAME` | `python-execution-server` | Unique identifier for this worker |
| `GRPC_SERVER_ADDRESS` | `localhost:50051` | Address of the Codex Workflows server |
| `SERVER_API_TOKEN` | _(empty)_ | Authentication token (optional) |
| `CACHE_TTL_SECONDS` | `300` | Default cache TTL for functions |

### Configuration via Code

```python
from workers_core import Config, Server

config = Config(
    server_name="my-custom-worker",
    grpc_server_address="localhost:50051",
    server_api_token="your-token",
    cache_ttl_seconds=600
)

server = Server(config)
```

### .env File Configuration

The configuration loader searches for `.env` files in this order:

1. **Current working directory upward** (using standard .env discovery)
2. **Project root**: `/path/to/haja-workers/.env` (recommended)
3. **Python directory**: `/path/to/haja-workers/python/.env`
4. **Package directory**: `/path/to/haja-workers/python/sdk/.env`

**Recommended .env file location**: Place at project root for entire project or in `python/` directory for Python-specific configuration.

Example `.env` file:
```bash
# Workers Configuration
SERVER_NAME=my-python-worker
GRPC_SERVER_ADDRESS=localhost:50051
SERVER_API_TOKEN=your-token-here
CACHE_TTL_SECONDS=300
```

## Development

### Development Setup

```bash
# Clone repository
git clone https://github.com/FatsharkStudiosAB/haja-workers.git
cd haja-workers/python

# Create development environment
python -m venv .venv
source .venv/bin/activate

# Install in editable mode
pip install -e ./sdk
pip install -e ./server

# Install development tools (optional)
pip install black isort mypy pytest
```

### Creating Custom Functions

#### Basic Function

```python
from dataclasses import dataclass
from workers_core import Function

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

## API Reference

### Main Classes

- `workers_core.Server` - Main server class for running workers
- `workers_core.Function` - Function builder with full access to global state
- `workers_core.SimpleFunction` - Simplified function builder
- `workers_core.FunctionInterface` - Base interface for function implementations
- `workers_core.Config` - Configuration class
- `workers_core.load_config` - Configuration loader with .env support

### Type Classes

- `workers_core.EventMessage` - Event message type for function handlers
- `workers_core.EventState` - Event state information

### Key Improvements

This restructured implementation provides:

✅ **Standard Python Packaging** - Follows Python packaging best practices  
✅ **Clean API Surface** - Simple imports: `from workers_core import Server, Function`  
✅ **Proper Dependencies** - Server depends on SDK, no code duplication  
✅ **Editable Installation** - Easy development workflow  
✅ **Console Scripts** - `workers-server` command available after installation  
✅ **Type Safety** - Full type hints throughout  
✅ **Lazy Imports** - No import errors during development  

## Troubleshooting

### Common Issues

**Import Errors**: Make sure both SDK and server are installed:
```bash
pip install -e ./sdk -e ./server
python -c "from workers_core import Server, Function; print('✅ All imports successful!')"
```

**Module Not Found**: Verify the packages are installed in the correct environment:
```bash
pip list | grep workers
```

**Connection Issues**: Check your gRPC server address and ensure the Codex Workflows server is running.

**Testing the Server**: You can test the server startup with:
```bash
# Run for a few seconds to test startup
timeout 5s workers-server || echo "Server started successfully"
```

The server will show output like:
```
[INFO] workers_core.config: Loaded .env from /path/to/.env
[INFO] workers_core.config: Config loaded: server_name=my-worker grpc_server_address=localhost:50051
Server 'my-worker' registered with workflow server
[INFO] workers_core.communication.grpc_communicator: GrpcCommunicator: connecting to localhost:50051
```

## License

Part of the Codex Workflows project. See main repository for license details.