from mcp.server import FastMCP

mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0", #for SSE
    port=8050, #for SSE
    stateless_http=True
)


@mcp.tool()
def add(a:int,b:int) -> int:
    "Add two numbers"
    return a + b
 
# Run the server
if __name__ == "__main__":
    transport = "streamable-http"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    elif transport == "streamable-http":
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"Unknown transport: {transport}")

