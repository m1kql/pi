import discord
from bot.utils.sample_embeds import *
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
            help_embed = discord.Embed(title="Help", description="All the relevant info", color=0xD6C18A)
            help_embed.add_field(name="```^```", value="The Prefix", inline=False)
            help_embed.add_field(name="```^help <command category>```", value="for more info on a specific category of commands and all the commands within it")
            await ctx.send(embed=help_embed)
            help_embed2 = discord.Embed(title="Help Pt.2", description="Avalible Categories", color=0xD6C18A)
            help_embed2.add_field(name="```math```", value="math category")
            help_embed2.add_field(name="```code```", value="code category")
            help_embed2.add_field(name="```music```", value="music category")
            await ctx.send(embed=help_embed2)
        elif arg == 'math' or arg == 'Math':
            math_embed = discord.Embed(title="Math Commands", description="All the relevant info", color=0xD6C18A)
            math_embed.add_field(name="```^fetchamc <year> <contest version> <problem number>```", value="fetches any AIME problem from any given year")
            math_embed.add_field(name="```^fetchaime <year> <contest version> <problem number>```", value="fetches any AIME problem from any given year")
            math_embed.add_field(name="```^fetchusamo <year> <problem number>```", value="fetches any USAMO problem from any given year")
            math_embed.add_field(name="```^fetchusajmo <year> <problem number>```", value="fetches any USAJMO problem from any given year")
            await ctx.send(embed=math_embed)
            math_embed2 = discord.Embed(title="Math Commands Pt.2", description="Ranked Commands - Either gain or lose points", color=0xD6C18A)
            math_embed.add_field(name="```^stats```", value="gives you your statistics. Type `^help statistics` for more info")
            math_embed.add_field(name="```^last5 <year>```", value="returns the last 5 of any AMC contest (Ranked)")
            math_embed.add_field(name="```^amc10 <diffculty level>```", value="gives any AMC10 problem of that difficulty (Ranked)")
            math_embed.add_field(name="```^amc12 <diffculty level>```", value="gives any AMC12 problem of that difficulty (Ranked)")
            math_embed.add_field(name="```^random <contest name>```", value="fetches any problem from a specified contest (Ranked)")
            await ctx.send(embed=math_embed2)


    @commands.command()
    async def invite(self, ctx):
        await ctx.send("<https://discord.com/api/oauth2/authorize?client_id=799423483968618566&permissions=0&scope=bot>")

def setup(bot):
    bot.add_cog(Help(bot))
