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
    async def leaderboard(self, ctx, top_users=10):
        user_guild_id = ctx.guild.id
        users = await get_guild_db(user_guild_id)

        leaderboard_tuple = []

        for index, user in enumerate(users):
            if index == top_users:
                break
            user_dict = user.to_dict()
            total = user_dict.get("total_weighted_points") or 0
            if total != 0:
                leaderboard_tuple.append((total, user.id))
                print(leaderboard_tuple[-1][1])

        leaderboard_tuple.sort(key=lambda user: user[0], reverse=True)
        print(f"LEADERBOARD USERS: {list(map(lambda user: user[0], leaderboard_tuple))}")

        leaderboard_embed = discord.Embed(
            title=f"Leaderboard for guild: `{ctx.guild.name}`",
            description=f"Showing the top {top_users} users",
            color=0xA4D0DA,
        )

        for score, user_id in leaderboard_tuple:
            print(f"User id: {user_id}")
            user_object = await self.bot.fetch_user(user_id)
            user_name = user_object.name
            user_discriminator = user_object.discriminator
            print(f"User name: {user_name}")
            print(f"User discriminator: {user_discriminator}")
            leaderboard_embed.add_field(
                name=f"{index}. {user_name}#{user_discriminator}", value=f"`{score}` points", inline=False
            )

        await ctx.send(embed=leaderboard_embed)


def setup(bot):
    bot.add_cog(Leaderboard(bot))
