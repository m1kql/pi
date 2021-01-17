import discord
from discord.ext import commands

class Contestproblems(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Contest Math cog has been loaded sucessfully')

def setup(bot):
    bot.add_cog(Contestproblems(bot))