from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio

async def main():
    async with streamablehttp_client("http://localhost:8050/mcp") as (read_stream,
        write_stream,
        get_session_id,):

        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Call our calculator tool
            result = await session.call_tool("add", arguments={"a": 2, "b": 3})
            print(f"2 + 3 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())