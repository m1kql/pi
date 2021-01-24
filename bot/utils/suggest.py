import discord
from discord.ext import commands


class Suggest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Suggestion cog has been loaded sucessfully')

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def suggest(self, ctx, *, msg):
        user = ctx.message.author.name
        with open('suggestions.txt', 'a') as f:
            f.write("from: " + user + " - message: " + msg+'\n')
        await ctx.send("Suggestion has been noted. Have a nice day.")


def setup(bot):
    bot.add_cog(Suggest(bot))
