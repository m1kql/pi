import discord
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
            help_embed.add_field(name="```^suggestion <your suggestion>```", value="make a suggestion for the bot (do not abuse it, there is a cooldown)")
            await ctx.send(embed=help_embed)
            help_embed2 = discord.Embed(title="Help Pt.2", description="Avalible Categories", color=0xD6C18A)
            help_embed2.add_field(name="```math```", value="math category")
            help_embed2.add_field(name="```code```", value="code category")
            help_embed2.add_field(name="```music```", value="music category")
            await ctx.send(embed=help_embed2)
        elif arg == 'math' or arg == 'Math':
            math_embed = discord.Embed(title="Math Contest Commands", description="All the relevant info", color=0xD6C18A)
            math_embed.add_field(name="```^fetchamc <year> <contest version> <problem number>```", value="fetches any AIME problem from any given year")
            math_embed.add_field(name="```^fetchaime <year> <contest version> <problem number>```", value="fetches any AIME problem from any given year")
            math_embed.add_field(name="```^fetchusamo <year> <problem number>```", value="fetches any USAMO problem from any given year")
            math_embed.add_field(name="```^fetchusajmo <year> <problem number>```", value="fetches any USAJMO problem from any given year")
            await ctx.send(embed=math_embed)
            math_embed2 = discord.Embed(title="Math Contest Commands Pt.2", description="Ranked Commands - Either gain or lose points", color=0xD6C18A)
            math_embed.add_field(name="```^stats```", value="gives you your statistics. Type `^help statistics` for more info")
            math_embed.add_field(name="```^last5 <year>```", value="returns the last 5 of any AMC contest (Ranked)")
            math_embed.add_field(name="```^amc10 <diffculty level>```", value="gives any AMC10 problem of that difficulty (Ranked)")
            math_embed.add_field(name="```^amc12 <diffculty level>```", value="gives any AMC12 problem of that difficulty (Ranked)")
            math_embed.add_field(name="```^random <contest name>```", value="fetches any problem from a specified contest (Ranked)")
            await ctx.send(embed=math_embed2)
        elif arg == 'code' or arg == 'Code':
            code_embed = discord.Embed(title="Code Commands", description="Code Commands - To run any piece of code without input", color=0xD6C18A)
            code_embed.add_field(name="```^run <lang> <your program>```", value="runs your program through any specified language")
            await ctx.send(embed=code_embed)
            code_embed2 = discord.Embed(title="Code Commands Pt.2", description="Supported Languages", color=0xD6C18A)
            code_embed2.add_field(name="Languages", value="```ada, assembly, bash, c#, c++, c, clojure, common lisp, d, elixir, erlang, f#, fortran, go, haskell, java, javascript, kotlin, lua, node.js\nocaml, octave, obj-c, pascal, perl, php, prolog, python, python3, R, rust, ruby, scala, scheme, swift, tcl, visual basic```")
            await ctx.send(embed=code_embed2)
        
        elif arg == 'music' or arg == 'Music':
            music_embed = discord.Embed(title="Music Commands", description="Music Commands - For playing some music", color=0xD6C18A)
            music_embed.add_field(name="```^join```", value="joins whichever voice chat you are in at the moment")
            await ctx.send(embed=music_embed)

    @commands.command()
    async def about(self, ctx):
        about_embed = discord.Embed(title="About", description="This bot was originally created to help students with an interest in STEM by practicing various problems and providing a suite of tools. We plan on adding more functionality in the near future.\n\nIf you would like to invite it, click [here](https://discord.com/api/oauth2/authorize?client_id=799423483968618566&permissions=0&scope=bot).\nWant to contribute? Fork us [here](https://github.com/yak-fumblepack/pi)", color=0xD6C18A)
        await ctx.send(embed=about_embed)


def setup(bot):
    bot.add_cog(Help(bot))
