import discord
from discord.ext import commands
from ..utility.firebase import db
import firebase_admin

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Statistics cog has been loaded sucessfully")

    @commands.command(aliases=["stats"])
    async def statistics(self, ctx, user=None):
        def parse_user(raw_user):
            formatted_user = ""
            if user is not None:
              if "<" in raw_user:
                  formatted_user = raw_user.replace("<", "").replace(">", "").replace("@", "").replace("!", "")
                  print(raw_user.replace("<", "").replace(">", "").replace("@", "").replace("!", ""))
                  return formatted_user
              elif raw_user.isdigit():
                  return formatted_user
            elif user is None:
                return ctx.author.id

        user_id = parse_user(user)
        
        user_guild_id = ctx.guild.id
        data = {
            u'points': 1
        }
        collection_ref = db.collection(str(user_guild_id)).document(str(user_id)).set(data)
        await ctx.send(user_id)


def setup(bot):
    bot.add_cog(Stats(bot))

