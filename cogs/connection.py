from discord.utils import find
from discord.ext.commands import Cog, Bot, command, Context
from discord import Guild, Message

class DiscordClient(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self._last_member = None

    @Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} succesfully logged in!')
    
    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        print(f'Message from {message.author}: {message.content}')

    @Cog.listener()
    async def on_guild_join(self, guild: Guild):
        general = find(lambda x: x.name == 'general',  guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            await general.send('Hello next Yagsons from {}!'.format(guild.name))
        
        members = guild.members
        for member in members:
            print(member)

    @command()
    async def ping(self, ctx: Context) -> None:
        await ctx.send('pong!')

async def setup(bot: Bot) -> None:
    await bot.add_cog(DiscordClient(bot))