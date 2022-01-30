from discord.ext import commands


class AntiSnipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.id == 805412409174654986:
            await message.channel.send(f"AntiSnipe ➞ Triggered\n", delete_after=0.01)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.id == 805412409174654986:
            edit_msg = await before.channel.send(f"AntiSnipe ➞ Trigger")
            await edit_msg.edit(content="AntiSnipe ➞ Triggered", delete_after=0.01)


def setup(bot):
    bot.add_cog(AntiSnipe(bot))
