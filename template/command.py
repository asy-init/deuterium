from discord.ext import commands


class class_name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def command_name(self, ctx):
        await ctx.send("hello world!")


def setup(bot):
    bot.add_cog(class_name(bot))
