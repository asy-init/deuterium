from asyncio import sleep

import discord


def initial_start(
    rpc,
    self,
    cogs,
):
    def load_commands(self):
        for cog in cogs:
            try:
                print(f"• loading {cog}")
                self.load_extension(f"commands.{cog}")
                print(f"• loaded {cog}")
            except Exception:
                print(
                    f"failed to load extension {cog}\n {type(Exception).__name__} : {Exception}"
                )

    async def update_rpc(self, rpc):
        for x in rpc:
            await self.change_presence(activity=discord.Game(name=x))
            await sleep(10)

    load_commands(self)
    self.loop.create_task(update_rpc(self=self, rpc=rpc))
