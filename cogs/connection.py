from discord.ext.commands import Cog, Bot, command

class DiscordClient(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self._last_member = None

    @Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} succesfully logged in!')
    
    @Cog.listener()
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    @command()
    async def ping(self, ctx):
        await ctx.send('pong!')

async def setup(bot: Bot):
    await bot.add_cog(DiscordClient(bot))