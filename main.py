# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

@bot.command(name="hello")
async def hello(ctx):
    print('enter')
    await ctx.send('Pong')

bot.run(TOKEN)