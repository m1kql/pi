import discord
from discord.ext import commands

from ..math.latex import latex_help
from ..math.stats import statistics_help
from ..math.contest_problems import fetch_help
from ..misc.report import suggest_help, report_help
from ..misc.info import invite_help, info_help

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help cog has been loaded sucessfully")

    @commands.command(aliases=["h"])
    async def help(self, ctx, args=None):
        if args is not None:
            if "math" in args:
                help_embed = discord.Embed(
                    title="Math commands",
                    description="`=statistics`,`=tex`",
                    color=0xA4D0DA,
                )
                help_embed.set_footer(
                    text="For more info on each of the commands, type `=help <command name>`"
                )
                await ctx.send(embed=help_embed)
            elif "fetch" in args:
                help_embed = discord.Embed(title=f"{fetch_help.get('name')}", color=0xA4D0DA)
                help_embed.add_field(name=f"{fetch_help.get('description_name')}", value=f"{fetch_help.get('description')}", inline=False)
                help_embed.add_field(name=f"{fetch_help.get('usage_name')}", value=f"{fetch_help.get('usage_description')}", inline=False)
                help_embed.add_field(name=f"{fetch_help.get('alias_name')}", value=f"{fetch_help.get('alias_description')}", inline=False)
                help_embed.add_field(name=f"{fetch_help.get('usage_syntax_name')}", value=f"{fetch_help.get('usage_syntax')}", inline=False)
                help_embed.set_footer(text=f"{fetch_help.get('footer')}")
                await ctx.send(embed=help_embed)
            elif "bot" in args:
                pass
            elif ("misc" or "miscellaneous") in args:
                help_embed = discord.Embed(title="Miscellaneous commands", description="`=info`, `=invite`, `=suggest`, `=report`", color=0xA4D0DA)
                help_embed.set_footer(
                    text="For more info on each of the commands, type `=help <command name>`"
                )
                await ctx.send(embed=help_embed)
            elif "suggest" in args:
                help_embed = discord.Embed(title=f"{suggest_help.get('name')}", color=0xA4D0DA)
                help_embed.add_field(name=f"{suggest_help.get('description_name')}", value=f"{suggest_help.get('description')}", inline=False)
                help_embed.add_field(name=f"{suggest_help.get('usage_name')}", value=f"{suggest_help.get('usage_description')}", inline=False)
                help_embed.add_field(name=f"{suggest_help.get('alias_name')}", value=f"{suggest_help.get('alias_description')}", inline=False)
                help_embed.add_field(name=f"{suggest_help.get('usage_syntax_name')}", value=f"{suggest_help.get('usage_syntax')}", inline=False)
                help_embed.set_footer(text=f"{suggest_help.get('footer')}")
                await ctx.send(embed=help_embed)
            elif "report" in args:
                help_embed = discord.Embed(title=f"{report_help.get('name')}", color=0xA4D0DA)
                help_embed.add_field(name=f"{report_help.get('description_name')}", value=f"{report_help.get('description')}", inline=False)
                help_embed.add_field(name=f"{report_help.get('usage_name')}", value=f"{report_help.get('usage_description')}", inline=False)
                help_embed.add_field(name=f"{report_help.get('alias_name')}", value=f"{report_help.get('alias_description')}", inline=False)
                help_embed.add_field(name=f"{report_help.get('usage_syntax_name')}", value=f"{report_help.get('usage_syntax')}", inline=False)
                help_embed.set_footer(text=f"{report_help.get('footer')}")
                await ctx.send(embed=help_embed)
            elif "info" in args:
                help_embed = discord.Embed(title=f"{info_help.get('name')}", color=0xA4D0DA)
                help_embed.add_field(name=f"{info_help.get('description_name')}", value=f"{info_help.get('description')}", inline=False)
                help_embed.add_field(name=f"{info_help.get('usage_name')}", value=f"{info_help.get('usage_description')}", inline=False)
                help_embed.add_field(name=f"{info_help.get('alias_name')}", value=f"{info_help.get('alias_description')}", inline=False)
                help_embed.add_field(name=f"{info_help.get('usage_syntax_name')}", value=f"{info_help.get('usage_syntax')}", inline=False)
                help_embed.set_footer(text=f"{info_help.get('footer')}")
                await ctx.send(embed=help_embed)
            elif "invite" in args:
                help_embed = discord.Embed(title=f"{invite_help.get('name')}", color=0xA4D0DA)
                help_embed.add_field(name=f"{invite_help.get('description_name')}", value=f"{invite_help.get('description')}", inline=False)
                help_embed.add_field(name=f"{invite_help.get('usage_name')}", value=f"{invite_help.get('usage_description')}", inline=False)
                help_embed.add_field(name=f"{invite_help.get('alias_name')}", value=f"{invite_help.get('alias_description')}", inline=False)
                help_embed.add_field(name=f"{invite_help.get('usage_syntax_name')}", value=f"{invite_help.get('usage_syntax')}", inline=False)
                help_embed.set_footer(text=f"{invite_help.get('footer')}")
                await ctx.send(embed=help_embed)
            elif ("stats" or "statistics") in args:
                help_embed = discord.Embed(title=f"{statistics_help.get('name')}", color=0xA4D0DA)
                help_embed.add_field(name=f"{statistics_help.get('description_name')}", value=f"{statistics_help.get('description')}", inline=False)
                help_embed.add_field(name=f"{statistics_help.get('usage_name')}", value=f"{statistics_help.get('usage_description')}", inline=False)
                help_embed.add_field(name=f"{statistics_help.get('alias_name')}", value=f"{statistics_help.get('alias_description')}", inline=False)
                help_embed.add_field(name=f"{statistics_help.get('usage_syntax_name')}", value=f"{statistics_help.get('usage_syntax')}", inline=False)
                help_embed.set_footer(text=f"{statistics_help.get('footer')}")
                await ctx.send(embed=help_embed)
            elif ("tex" or "latex") in args:
                help_embed = discord.Embed(title=f"{latex_help.get('name')}", color=0xA4D0DA)
                help_embed.add_field(name=f"{latex_help.get('description_name')}", value=f"{latex_help.get('description')}", inline=False)
                help_embed.add_field(name=f"{latex_help.get('usage_name')}", value=f"{latex_help.get('usage_description')}", inline=False)
                help_embed.add_field(name=f"{latex_help.get('alias_name')}", value=f"{latex_help.get('alias_description')}", inline=False)
                help_embed.add_field(name=f"{latex_help.get('usage_syntax_name')}", value=f"{latex_help.get('usage_syntax')}", inline=False)
                help_embed.set_footer(text=f"{latex_help.get('footer')}")
                await ctx.send(embed=help_embed)
        else:
            # embed
            help_embed = discord.Embed(title="Help", color=0xA4D0DA)
            help_embed.set_footer(
                text="All problems sourced by this bot are property of their respective owners. Use of these names, images, and text does not imply sponsorship or endorsement."
            )
            help_embed.add_field(name="Bot", value="`=help bot`")
            help_embed.add_field(name="Math", value="`=help math`")
            help_embed.add_field(name="Miscellaneous", value="`=help misc`")
            await ctx.send(embed=help_embed)


def setup(bot):
    bot.add_cog(Help(bot))
