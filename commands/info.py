from os import getpid
from platform import version
from sys import path
from datetime import datetime
from pathlib import Path

from discord import Embed
from psutil import Process
from discord.ext import commands


class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):

        pyversion = version()
        mem = Process(getpid()).memory_full_info().rss / 1024 ** 2
        lib = "pycord[1.7.3]"
        pid = getpid()
        git = "https://noice.link/asy-bot"
        ping = round(self.bot.latency * 1000)

        servers = len(ctx.bot.guilds)
        users = len(self.bot.users)

        path.insert(0, "..")
        cmd = len([x.stem for x in Path("commands").glob("*.py")])
        eve = len([x.stem for x in Path("commands").glob("*.py")])

        embed = Embed(
            title="Bot Information",
            description="provides stats about the bot\n\u200b",
            timestamp=datetime.utcnow(),
            color=0x2E3440,
        )
        embed.add_field(name="python version", value=f"```{pyversion}```", inline=True)
        embed.add_field(name="memory used", value=f"```{mem:.2f} MB```", inline=True)
        embed.add_field(name="library", value=f"```{lib}```", inline=True)
        embed.add_field(name="latency", value=f"```{ping}```", inline=True)
        embed.add_field(name="PID", value=f"```{pid}```", inline=True)
        embed.add_field(name="git", value=f"```{git}```", inline=True)
        embed.add_field(name="servers", value=f"```{servers}```", inline=True)
        embed.add_field(name="users", value=f"```{users}```", inline=True)
        embed.add_field(
            name="commands.Cog", value=f"```{cmd} cmd, {eve} events```", inline=True
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BotInfo(bot))
