import discord
from discord.ext import commands
from ..utility.db import (
    db,
    get_user_db,
    questions_attempted,
    questions_failed,
    questions_solved,
)
import firebase_admin

# statistics help
statistics_help = {
    "name": "=statistics help info",
    "description_name": "Description",
    "description": "View your statistics or someone else's statistics. If there is no mention or user id, it will return your statistics",
    "usage_name": "Usage",
    "usage_description": "`=statistics @user`\n`=statistics [user id]`\n`=statistics`",
    "alias_name": "Aliases",
    "alias_description": "`stats`",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Statistics cog has been loaded sucessfully")

    @commands.command(aliases=["stats"])
    async def statistics(self, ctx, user: discord.User = None):
        def parse_user(raw_user):
            if raw_user is not None:
                return raw_user.id
            elif raw_user is None:
                return ctx.author.id

        user_id = parse_user(user)

        user_guild_id = ctx.guild.id

        user_data_dict = await get_user_db(user_guild_id, user_id)

        user_object = self.bot.get_user(user_id)

        # embed
        statistics_embed = discord.Embed(
            title=f"{user_object.name}'s Statistics", color=0xA4D0DA
        )
        statistics_embed.set_thumbnail(url=user_object.avatar_url)
        statistics_embed.set_footer(
            text="Such scores and points are not indicative of a user's skill level or aptitude in mathematics or logical reasoning."
        )
        statistics_embed.add_field(
            name="Questions solved",
            value=f"Total solved: `{user_data_dict.get(questions_solved)}`",
        )
        statistics_embed.add_field(
            name="Questions attempted",
            value=f"Total attempted: `{user_data_dict.get(questions_attempted)}`",
        )
        statistics_embed.add_field(
            name="Questions failed",
            value=f"Total failed: `{user_data_dict.get(questions_failed)}`",
        )

        await ctx.send(embed=statistics_embed)


def setup(bot):
    bot.add_cog(Stats(bot))
