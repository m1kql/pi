import discord
from bot.utils.commands import *
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog has been loaded sucessfully')

    @commands.command()
    async def help(self, ctx, arg=None):
        if arg is None:
            await ctx.send(default_help)

        elif arg == 'code':
            await ctx.send(code_help)
            await ctx.send(goback)
            def check(m):
                return m.author.id == ctx.author.id
            returnmsg = await self.bot.wait_for('message',check=check)
            if returnmsg.content == 'yes' or returnmsg.content=='ye' or returnmsg.content=='yee':
                await ctx.send(default_help)
            else:
                await ctx.send("ok")

        elif arg == 'math':
            await ctx.send(math_help)
            await ctx.send(goback)
            def check(m):
                return m.author.id == ctx.author.id
            returnmsg = await self.bot.wait_for('message',check=check)
            if returnmsg.content == 'yes' or returnmsg.content=='ye' or returnmsg.content=='yee':
                await ctx.send(default_help)
            else:
                await ctx.send("ok")
    
    @commands.command()
    async def invite(self, ctx):
        await ctx.send(invite)

def setup(bot):
    bot.add_cog(Help(bot))
