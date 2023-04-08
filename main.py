# bot.py
import os
import asyncio

import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = Bot(command_prefix="!", intents=intents)

async def load_extensions(bot_instance: Bot) -> None:
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot_instance.load_extension(f"cogs.{filename[:-3]}")

async def main(bot_instance: Bot) -> None:
    async with bot_instance:
        await load_extensions(bot_instance)
        await bot_instance.start(TOKEN)

asyncio.run(main(bot))
