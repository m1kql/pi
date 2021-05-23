import discord
from discord.ext import commands
from firebase_admin import firestore
from ..utility.db import db, open_user_db, questions_attempted, questions_failed, questions_solved
import firebase_admin
import requests

# Fetch contest problems help
fetch_help = {
    "name": "=fetch help info",
    "description_name": "Description",
    "description": "Fetch a problem from the given contests:\n- AMC 10A, 10B, 12A, 12B\n- USAMO\n- USAJMO\n- AIME",
    "usage_name": "Usage",
    "usage_description": "`=fetch <contest name> <contest year> [contest version] <problem number>`\nExample: `=fetch amc 2010 10b 16`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

questions_solved_amount = 1
amc10_points_amount = 1
amc12_points_amount = 1
amc12_weight = 0.75
amc10_weight = 0.25
amc10_id = ["10A","10B"]
amc12_id = ["12A","12B"]
amc_id = ["10A", "10B", "12A", "12B"]
aime_id = ["1", "2"]
reactions = {"🇦": "a", "🇧": "b", "🇨": "c", "🇩": "d", "🇪": "e", "❎": "quit"}

class ContestProblems(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Contest problems cog has been loaded sucessfully")

    @commands.command()
    async def fetch(self, ctx, *, args=None):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id
        user = ctx.author
        await open_user_db(user_guild_id, user_id)
        if args != None:
            user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))
            requested_path = args.upper().replace(" ", "/")

            tried = []

            def check_answer(reaction, user):
                return (
                    user == ctx.message.author
                    and reaction.emoji in reactions
                    and user.id not in tried
                )

            question = await ctx.send(
                f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/{requested_path}/statement.png"
            )
            sol = str(
                (
                    requests.get(
                        f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/{requested_path}/sol.txt"
                    ).text
                ).strip()
            )

            while True:
                for emoji in reactions:
                    await question.add_reaction(emoji)
                reaction, user = await self.bot.wait_for("reaction_add", check=check_answer)

                if reactions[reaction.emoji] == sol:
                    await ctx.send("Correct.")
                    user_collection_ref.update({
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(questions_solved_amount)
                    })
                    break
                elif reactions[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    user_collection_ref.update({
                        questions_attempted: firestore.Increment(questions_solved_amount)
                    })
                    break
                else:
                    await ctx.send("Wrong")
                    user_collection_ref.update({
                        questions_failed: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(questions_solved_amount)
                    })
                    break





def setup(bot):
    bot.add_cog(ContestProblems(bot))
