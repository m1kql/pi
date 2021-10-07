import math

import discord
from discord.ext import commands

from ..math.contest_problems import amc10_weight, amc12_weight
from ..utility.db import (
    db,
    aime_attempted,
    amc10_attempted,
    amc10_failed,
    amc10_solved,
    amc12_attempted,
    amc12_failed,
    amc12_solved,
    get_user_db,
    open_user_db,
    questions_attempted,
    questions_failed,
    questions_solved,
    usajmo_attempted,
    usamo_attempted,
    cmo_attempted,
    total_weighted_points_string,
)

# statistics help
statistics_help = {
    "name": "=statistics help info",
    "description_name": "Description",
    "description": "View your statistics or someone else's statistics. If there is no mention or user id, it will return your statistics.\nWeights for AMC 10 is `35%`, and for the AMC 12 is `65%`",
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

        await open_user_db(user_guild_id, user_id)
        user_data_dict = await get_user_db(user_guild_id, user_id)

        total_unweighted_points = (
            user_data_dict["amc10_points"] + user_data_dict["amc12_points"]
        )
        total_weighted_points = (
            float(user_data_dict["amc10_points"]) * amc10_weight
        ) + (float(user_data_dict["amc12_points"]) * amc12_weight)
        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        user_collection_ref.update(
            {total_weighted_points_string: total_weighted_points}
        )

        user_object = self.bot.get_user(user_id)

        # embed
        statistics_embed = discord.Embed(
            title=f"{user_object.name}'s Statistics", color=0xA4D0DA
        )
        statistics_embed.set_thumbnail(url=user_object.avatar_url)
        statistics_embed.set_footer(
            text="Such scores are not indicative of a user's skill level or aptitude in mathematics or logical reasoning."
        )
        statistics_embed.add_field(
            name="Questions solved",
            value=f"AMC 10 solved: `{user_data_dict[amc10_solved]}`\nAMC 12 solved: `{user_data_dict[amc12_solved]}`\nTotal solved: `{user_data_dict[questions_solved]}`",
        )
        statistics_embed.add_field(
            name="Questions fetched",
            value=f"AMC 10 fetched: `{user_data_dict[amc10_attempted]}`\nAMC 12 fetched: `{user_data_dict[amc12_attempted]}`\nAIME fetched: `{user_data_dict[aime_attempted]}`\nUSAMO fetched: `{user_data_dict[usamo_attempted]}`\nUSAJMO fetched: `{user_data_dict[usajmo_attempted]}`\nCMO fetched: `{user_data_dict[cmo_attempted]}`\nTotal fetched: `{user_data_dict[questions_attempted]}`",  # noqa E501
        )
        statistics_embed.add_field(
            name="Questions failed",
            value=f"AMC 10 failed: `{user_data_dict[amc10_failed]}`\nAMC 12 failed: `{user_data_dict[amc12_failed]}`\nTotal failed: `{user_data_dict[questions_failed]}`",
        )
        statistics_embed.add_field(
            name="Points",
            value=f"AMC 10 points: `{user_data_dict['amc10_points']}`\nAMC 12 points: `{user_data_dict['amc12_points']}`\nTotal points: `{math.floor(total_weighted_points)}`\nTotal unweighted points: `{total_unweighted_points}`",
        )

        await ctx.send(embed=statistics_embed)


def setup(bot):
    bot.add_cog(Stats(bot))
