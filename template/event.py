from discord.ext import commands


class class_name(commands.COg):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def event_name(self, message):
        print(message)


def setup(bot):
    bot.add_cog(class_name(bot))
