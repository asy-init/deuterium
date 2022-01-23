#!/usr/bin/env python

from discord.ext import commands

import main
import settings

bot = commands.Bot(command_prefix=settings.PREFIX, intents=settings.INTENT)


@bot.event
async def on_ready():
    print()
    print(f"• logged in as {bot.user}\n• Connected to {len(bot.guilds)} Severs")
    print()

    main.initial_start(rpc=settings.RPC, self=bot, cogs=settings.COGS)


@bot.event
async def on_message_delete(message):
    if message.author.id == 805412409174654986:
        await message.channel.send("anti-snipe -> on", delete_after=0.01)


if __name__ == "__main__":
    bot.run(settings.TOKEN)
