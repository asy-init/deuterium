from discord.ext import commands
from discord import Embed


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["latency", "timeit"])
    async def ping(self, ctx):

        embed = Embed(
            description=f" **:ping_pong: Latency**\n\n ⌛ {round(self.bot.latency*1000)}ms"
        )
        embed.set_footer(text="command.ping")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ping(bot))
