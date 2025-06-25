from fastmcp import Client

test_client = Client("http://localhost:8000/mcp")  # サーバーのURL

# 'add'ツールを呼び出し
result = test_client.call("add", a=3, b=5)
print("add(3, 5) =", result)
