from discord.ext import commands


class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        await ctx.send("works")


def setup(bot):
    bot.add_cog(about(bot))
