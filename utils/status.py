from asyncio import sleep
from operator import truediv
from discord import Game


async def load_status(self, status):
    while True:
        for x in status:
            await self.change_presence(activity=Game(name=x))
            await sleep(20)
