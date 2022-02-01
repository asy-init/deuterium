from discord.ext import commands
import os
import sys
import discord

sys.path.insert(0, "..")


class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["refresh", "reload"])
    @commands.is_owner()
    async def restart(self, ctx):
        embed = discord.Embed(title="restarting...")
        embed.set_footer(text="bot.reload_extension( )")
        msg = await ctx.send(embed=embed)
        for filename in os.listdir("./commands/"):
            if filename.endswith(".py"):
                self.bot.reload_extension(f"commands.{filename[:-3]}")
        embed = discord.Embed(title="restarted...")
        embed.set_footer(text="bot.reload_extension( )")
        await msg.edit(embed=embed,delete_after=2)


def setup(bot):
    bot.add_cog(Restart(bot))
