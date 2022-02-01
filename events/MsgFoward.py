from discord.ext import commands
import discord


class MsgFoward(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if not message.author.bot:

            MsgFowardChannel = self.bot.get_channel(937019828668084284)

            embed = discord.Embed(
                title="`type:new`",
                description=f"[```message.content```]({message.jump_url})\n {message.content}\n ",
                color=0x5CB85C,
            )
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await MsgFowardChannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:

            MsgFowardChannel = self.bot.get_channel(937019828668084284)

            embed = discord.Embed(
                title="`type:del`",
                description=f"```message.content```\n {message.content}\n ",
                color=0xC02121,
            )
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await MsgFowardChannel.send(embed=embed)

    # 0xd6ae1f
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.author.bot:

            MsgFowardChannel = self.bot.get_channel(937019828668084284)

            embed = discord.Embed(
                title="`type:del`",
                description=f"```message.before.content```\n {before.content}```message.after.content```\n {after.content}\n ",
                color=0xB4B620,
            )
            embed.set_footer(text=before.author, icon_url=before.author.avatar_url)
            await MsgFowardChannel.send(embed=embed)


def setup(bot):
    bot.add_cog(MsgFoward(bot))
