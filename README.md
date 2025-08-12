# Haja Workers SDK

This repository contains the Haja Workers SDK, providing both Go and Python implementations for building workers that integrate with the Haja workflow system.

## Structure

- **go/**: Go SDK and worker implementation
  - `sdk/`: Go SDK for building workers
  - `cmd/worker/`: Example worker server implementation
  - `internal/`: Internal Go packages

- **python/**: Python SDK and worker implementation
  - `sdk/`: Python SDK for building workers
  - `server/`: Python worker server implementation

## Getting Started

### Go Workers
See [go/README.md](go/README.md) for Go-specific documentation.

### Python Workers
See [python/README.md](python/README.md) for Python-specific documentation.

## Examples

Both Go and Python directories contain example implementations showing how to:
- Create input functions
- Store chat history
- Handle workflow events
- Communicate with the Haja workflow system

## Development

This repository was moved from `codex/workflows/workers` to provide a dedicated space for the Haja Workers SDK development.
