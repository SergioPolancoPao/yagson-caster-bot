import os
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)
client.run(TOKEN)

channel = client.get_channel(296102857906847744)

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(channel.send('Hello'))
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()