# MCP

## Create Environment

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

## Run MCP Server

```bash
fastmcp run server.py
```

```bash
python server.py
```

## Run MCP Client

```bash
python client.py
```

## Option Setup

```bash
# Install dependencies
uv add "mcp[cli]" httpx
```

## Trying MCP with C#

ref: [quick start](https://learn.microsoft.com/ja-jp/dotnet/ai/quickstarts/build-mcp-server)

```bash
dotnet new console -n MinimalMcpServer
```
