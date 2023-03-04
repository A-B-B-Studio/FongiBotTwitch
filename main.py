from twitchio.ext import commands
from Modules.Utils import credentials as cr

# ================================================================================================

class FongiBot(commands.Bot):

    def __init__(self):
        super().__init__(token=cr.irc_token, prefix='!', initial_channels=['platon_neutron'])

    async def event_ready(self):
        print(f'Logged in as : {self.nick}')
        print(f'User id is : {self.user_id}')
        
    salutations = ["bonjour", "hello", "hi", "salut", "yo", "yop", "wesh"]
    async def event_message(self, message):
        lowerMessage = str(message.content).lower()
        
        for mots in self.salutations:
            if (mots in lowerMessage):
                getContext = await self.get_context(message)
                await getContext.send(f"Bien le bonsoir {message.author.mention}")

    '''@commands.command(name = "p")
    async def test(self, ctx: commands.Context):
        await ctx.send(f'prout {ctx.author.name}!')'''

# ================================================================================================

FongiBot = FongiBot()
FongiBot.run()