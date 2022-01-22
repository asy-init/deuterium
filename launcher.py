#!/usr/bin/env python

from discord.ext import commands

import main
import settings

bot = commands.Bot(
    command_prefix=settings.PREFIX, intents=settings.INTENT, help_command=None
)


@bot.event
async def on_ready():

    print(f"• logged in  as {bot.user}\n• Connected to {len(bot.guilds)} Severs")
    main.initial_start(rpc=settings.RPC, self=bot, cogs=settings.COGS)


if __name__ == "__main__":
    bot.run(settings.TOKEN)
