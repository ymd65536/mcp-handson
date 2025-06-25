# MCP

## コマンド

```bash
# Create a new directory for our project
uv init sample
cd sample

# Create virtual environment and activate it
uv venv
source .venv/bin/activate
```

```bash
uv pip install fastmcp
```

```bash
fastmcp run server.py
```

```bash
python server.py
```

```bash
# Install dependencies
uv add "mcp[cli]" httpx
```
