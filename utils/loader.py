import sys
from pathlib import Path

from rich import print as pprint

sys.path.insert(0, "..")
COGS = [x.stem for x in Path("commands").glob("*.py")]
EVENTS = [x.stem for x in Path("events").glob("*.py")]


async def load_commands(self):
    pprint(f">> Loading {len(COGS)} Commands\n")

    for cog in COGS:
        try:
            pprint(f">> Loading {cog}")
            self.load_extension(f"commands.{cog}")
            pprint(f">> Loaded {cog}\n")

        except Exception as e:
            pprint(f">> failed to load extension [u]{cog}[/]")
            pprint(f">> {type(e).__name__} : {e}")


async def load_events(self):
    pprint(f">> Loading {len(EVENTS)} Events\n")

    for event in EVENTS:
        try:
            pprint(f">> Loading {event}")
            self.load_extension(f"events.{event}")
            pprint(f">> Loaded {event}\n")

        except Exception as e:
            pprint(f">> failed to load extension [u]{event}[/]")
            pprint(f">> {type(e).__name__} : {e.with_traceback()}")


async def load_combine(self):
    await load_commands(self=self)
    await load_events(self=self)
