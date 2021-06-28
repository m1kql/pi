import discord
from discord.ext import commands
from ..utility.db import (
    get_guild_db,
)

# leaderboard help
leaderboard_help = {
    "name": "=leaderboard help info",
    "description_name": "Description",
    "description": "View your server's leaderboard and see who has the most points. Retrieves the top 10 users by default.",
    "usage_name": "Usage",
    "usage_description": "`=leaderboard <number of users>`",
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
    async def leaderboard(self, ctx, top_users=None):

        if top_users is None:
            top_users = 10
        else:
            pass

        user_guild_id = ctx.guild.id
        users = await get_guild_db(user_guild_id)

        leaderboard_total = []
        leaderboard = {}

        for user in users:
            user_dict = user.to_dict()
            user_name_id = user.id
            total = user_dict.get("total_weighted_points")
            if total is None or total == 0:
                total = 0
            leaderboard[total] = user_name_id
            print(leaderboard[total])
            leaderboard_total.append(total)

        leaderboard_total = sorted(leaderboard_total, reverse=True)
        print("LEADERBOARD USERS:" + str(leaderboard_total))

        leaderboard_embed = discord.Embed(
            title=f"Leaderboard for guild: `{ctx.guild.name}`",
            description=f"Showing the top {top_users} users",
            color=0xA4D0DA,
        )

        index = 1

        for score in leaderboard_total:
            name_id = leaderboard[score]
            print("USER ID:" + str(name_id))
            user_object = await self.bot.fetch_user(name_id)
            user_name = user_object.name
            print(user_name)
            if score == 0:
                break
            leaderboard_embed.add_field(
                name=f"{index}. {user_name}", value=f"`{score}` points", inline=False
            )
            if index == top_users:
                break
            else:
                index += 1

        await ctx.send(embed=leaderboard_embed)


def setup(bot):
    bot.add_cog(Leaderboard(bot))
