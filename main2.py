import os
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class DiscordClient(discord.Client):

    async def setup_hook(self, tasks) -> None:
        # create the background task and run it in the background

        for task in task:
            self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def send_message(self, message: str) -> None:
        await self.wait_until_ready()
        channel = self.get_channel(296102857906847744)
        await channel.send(message)

intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)

class DiscordManager:
    def __init__(self, client: DiscordClient):
        self.client = client

    async def send_message(self, message: str) -> None:
        await self.client.wait_until_ready()
        channel = self.client.get_channel(296102857906847744)
        await channel.send(message)
    
discord_manager = DiscordManager(client)

# client.loop.create_task(client.send_message('Good morning'))

async def main():
    async with client:
        client.loop.create_task(discord_manager.send_message('Good morning'))
        await client.run('token')

asyncio.run(main())

