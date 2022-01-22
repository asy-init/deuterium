from asyncio import sleep

import discord
from discord.ext import tasks


def initial_start(rpc, self, cogs):
    def load_commands(self):
        for cog in cogs:
            try:
                self.load_extension(f"commands.{cog}")
                print(f"loaded {cog}")
            except Exception:
                print(
                    f"failed to load extension {cog}\n {type(Exception).__name__} : {Exception}"
                )

    load_commands(self)


async def update_rpc(self, rpc):
    for x in rpc:
        await self.change_presence(activity=discord.Game(name=x))
        await sleep(10)
