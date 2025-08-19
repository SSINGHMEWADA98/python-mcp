from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream,write_stream) as session:

            await session.initialize()

            tools_result = await session.list_tools()

            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            result = await session.call_tool("add",3,5)
            print("result",result.content[0].text)

if __name__ =="__main__":
    asyncio.run(main())