import discord
from discord.ext import commands
import datetime

# info help
info_help = {
    "name": "=info help info",
    "description_name": "Description",
    "description": "Get some info about this bot",
    "usage_name": "Usage",
    "usage_description": "`=info`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

# invite_help
invite_help = {
    "name": "=invite help info",
    "description_name": "Description",
    "description": "Get the invite link",
    "usage_name": "Usage",
    "usage_description": "`=invite`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Info cog has been loaded sucessfully")

    @commands.command()
    async def info(self, ctx):
        bot_id = 843607968401719296
        bot_user_object = self.bot.get_user(bot_id)
        info_embed = discord.Embed(
            title="Info about Pi",
            description=f"Pi is a discord bot for those interested in contest math to practice their skills while engaging in a casual conversation with their fellow mathematicians or friends.\n\nSome features include:\n- Ability to fetch problems from USAMO, USAJMO, AIME, AMC 10 & 12\n- Fully rendered problems (using LaTeX) with solution links\n- Robust points system to promote healthy competition\n- Can render LaTeX equations\n- Extensible core module, simply make a pull request with your cog and we can add it in without a problem!\n\n```c++\nWe are running in | {str(len(self.bot.guilds))} | servers\nThe ping in milliseconds is: | {round(self.bot.latency*1000, 1)} |\nThe date is: | {datetime.date.today()} |```\n\nWant to contribute? [Fork us!](https://github.com/yak-fumblepack/pi/tree/rewrite)",
            color=0xA4D0DA,
        )
        info_embed.set_thumbnail(url=bot_user_object.avatar_url)
        await ctx.send(embed=info_embed)

    @commands.command()
    async def invite(self, ctx):
        invite_embed = discord.Embed(
            title="Invite link",
            description="[Bot invite link](https://discord.com/api/oauth2/authorize?client_id=842500814625832990&permissions=0&scope=bot)\n[Support server link](https://discord.gg/FrdqSyzg4t)",
            color=0xA4D0DA,
        )
        await ctx.send(embed=invite_embed)


def setup(bot):
    bot.add_cog(Info(bot))
