import discord
from discord.ext import commands


class Errors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Check Error cog has been loaded sucessfully')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            n, m = divmod(error.retry_after, 60)
            h, n = divmod(n, 60)
            if int(h) == 0 and int(n) == 0:
                await ctx.send(f"you are on cooldown. please wait {int(m)} seconds before trying again.")
            elif int(h) == 0 and int(n) != 0:
                await ctx.send(f"you are on cooldown. please wait {int(n)} minutes and {int(m)} seconds before trying again.")
            else:
                await ctx.send(f"you are on cooldown. please wait {int(h)} hours, {int(n)} minutes and {int(m)} seconds before trying again.")
        elif isinstance(error.CheckFailure):
            await ctx.send("sorry, you lack the permissions to do this.")
        raise error


def setup(bot):
    bot.add_cog(Errors(bot))
