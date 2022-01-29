from discord.ext import commands


class AntiSnipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print()


def setup(bot):
    bot.add_cog(AntiSnipe(bot))
