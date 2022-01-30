from discord.ext import commands

from utils.loader import load_combine
from utils.status import load_status

import settings


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(settings.PREFIX), intents=settings.INTENT
)


@bot.event
async def on_ready():
    print(f"\n• logged in as {bot.user}\n• Connected to {len(bot.guilds)} Severs\n")
    await load_combine(self=bot)
    bot.loop.create_task(load_status(self=bot, status=settings.STATUS))


if __name__ == "__main__":
    bot.run(settings.TOKEN)
