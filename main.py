import time

import discord
from discord.ext import tasks


def initial_start(rpc, self, cogs):
    @tasks.loop(seconds=15)
    async def update_rpc(self):
        for x in rpc:
            await self.change_presence(activity=discord.Game(name=x))
            time.sleep(10)

    def load_commands(self):
        for cog in cogs:
            try:
                self.load_extension(f"commands.{cog}")
                print(f"loaded {cog}")
            except Exception:
                print(
                    f"failed to load extension {cog}\n {type(Exception).__name__} : {Exception}"
                )

    update_rpc.start(self)
    load_commands(self)
