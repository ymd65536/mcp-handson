# MCP

## コマンド

```bash
# Create a new directory for our project
uv init sample
cd sample

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

uv pip install fastmcp

# Install dependencies
uv add "mcp[cli]" httpx
```
