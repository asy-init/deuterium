from datetime import datetime

from discord import Embed
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["latency", "timeit"])
    async def ping(self, ctx):

        embed = Embed(
            description=f" **:ping_pong: Latency**\n\n ⌛ {round(self.bot.latency*1000)}ms",
            timestamp=datetime.utcnow(),
            color=0x2E3440,
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))
