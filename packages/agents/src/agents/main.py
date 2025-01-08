from dataclasses import dataclass

import httpx

from .agents import get_agent


@dataclass
class MyDeps:
    http_client: httpx.AsyncClient


async def main():
    async with httpx.AsyncClient() as client:
        deps = MyDeps(http_client=client)
        agent = get_agent({"provider": "openai", "model": "gpt-4o", "deps": deps})
        result = await agent.run("Tell me a joke.")
        print(result.data)
