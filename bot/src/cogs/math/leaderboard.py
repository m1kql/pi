import discord
from discord.ext import commands
from ..utility.db import (
    get_user_db,
)

# leaderboard help
leaderboard_help = {
    "name": "=leaderboard help info",
    "description_name": "Description",
    "description": "View your server's leaderboard and see who has the most points. Retrieves the top 10 users.",
    "usage_name": "Usage",
    "usage_description": "`=leaderboard`",
    "alias_name": "Aliases",
    "alias_description": "`rank`, `lb`",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}


class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Leaderboard cog has been loaded sucessfully")

    @commands.command(aliases=["rank", "lb"])
    async def leaderboard(self, ctx):

        user_guild_id = ctx.guild.id

        leaderboard = []

        for user in ctx.guild.members:
            score = await get_user_db(user_guild_id, user.id)
            points = score.get("total_weighted_points")
            if points is None:
                points = 0
                leaderboard.append((user.name, points))
            else:
                leaderboard.append((user.name, points))

        sorted_leaderboard = sorted(
            leaderboard, key=lambda x: (x[1], x[1]), reverse=True
        )

        sorted_names = [i[0] for i in sorted_leaderboard]
        sorted_scores = [i[1] for i in sorted_leaderboard]
        sorted_amount = len([i[1] for i in sorted_leaderboard])

        description_string = ""
        if sorted_amount > 10:
            for i in range(10):
                description_string += (
                    f"**{sorted_names[i]}** - `{sorted_scores[i]}` points\n"
                )
        elif sorted_amount <=10:
            for i in range(sorted_amount):
                description_string += (
                    f"**{sorted_names[i]}** - `{sorted_scores[i]}` points\n"
            )

        # embed
        leaderboard_embed = discord.Embed(
            title=f"Leaderboard for guild: `{ctx.guild.name}`",
            color=0xA4D0DA,
            description=description_string,
        )
        leaderboard_embed.set_footer(
            text="Such scores are not indicative of a user's skill level or aptitude in mathematics or logical reasoning."
        )
        leaderboard_embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=leaderboard_embed)


def setup(bot):
    bot.add_cog(Leaderboard(bot))
