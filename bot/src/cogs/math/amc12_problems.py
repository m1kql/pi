from discord.ext import commands
from firebase_admin import firestore
from ..utility.db import (
    db,
    open_user_db,
    questions_attempted,
    questions_failed,
    questions_solved,
    amc12_attempted,
    amc12_failed,
    amc12_solved,
    amc12_points,
)
import requests
import random
from .contest_problems import (
    reactions,
    questions_attempted_amount,
    questions_failed_amount,
    questions_solved_amount,
    amc12_failed_amount,
    amc12_id,
    amc12_solved_amount,
    amc12_correct_amount_easy,
    amc12_correct_amount_med,
    amc12_correct_amount_hard,
    amc12_attempted_amount,
    amc12_wrong_amount_easy,
    amc12_wrong_amount_hard,
    amc12_wrong_amount_med,
)

# AMC12 help
amc12_help = {
    "name": "=amc12 help info",
    "description_name": "Description",
    "description": "Returns an AMC12 problem from the following difficulties:\n- `easy` or `e`\n- `medium` or `med`\n- `hard` or `h`\n**This command is ranked and will give points**",  # noqa E501
    "usage_name": "Usage",
    "usage_description": "`=amc12 <difficulty>`\nExample: `=amc12 med`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}


class ContestProblems(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Contest problems cog has been loaded sucessfully")

    @commands.command()
    async def amc12(self, ctx, difficulty):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id
        await open_user_db(user_guild_id, user_id)

        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        tried = []

        def check_answer(reaction, user):
            return (
                user == ctx.message.author
                and reaction.emoji in reactions
                and user.id not in tried
            )

        if difficulty.lower() == ("e" or "easy"):
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_easy = str(random.randint(1, 10))
                amc12_contestid = str(random.choice(amc12_id))

                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc12_contestid}/{amc_easy}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc12_contestid}/{amc_easy}/sol.txt"
                        ).text
                    ).strip()
                )

                for emoji in reactions:
                    await question.add_reaction(emoji)

                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_answer
                )

                if reactions[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_easy}"
                    )
                    user_collection_ref.update(
                        {
                            questions_solved: firestore.Increment(
                                questions_solved_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                            amc12_points: firestore.Increment(
                                amc12_correct_amount_easy
                            ),
                            amc12_solved: firestore.Increment(amc12_solved_amount),
                        }
                    )
                    break
                elif reactions[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    user_collection_ref.update(
                        {
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                        }
                    )
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_easy}"
                    )
                    user_collection_ref.update(
                        {
                            questions_failed: firestore.Increment(
                                questions_failed_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                            amc12_points: firestore.Increment(amc12_wrong_amount_easy),
                            amc12_failed: firestore.Increment(amc12_failed_amount),
                        }
                    )
                    break

        if difficulty.lower() == ("med" or "medium"):
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_med = str(random.randint(11, 16))
                amc12_contestid = str(random.choice(amc12_id))

                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc12_contestid}/{amc_med}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc12_contestid}/{amc_med}/sol.txt"
                        ).text
                    ).strip()
                )

                for emoji in reactions:
                    await question.add_reaction(emoji)

                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_answer
                )

                if reactions[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_med}"
                    )
                    user_collection_ref.update(
                        {
                            questions_solved: firestore.Increment(
                                questions_solved_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                            amc12_points: firestore.Increment(amc12_correct_amount_med),
                            amc12_solved: firestore.Increment(amc12_solved_amount),
                        }
                    )
                    break
                elif reactions[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    user_collection_ref.update(
                        {
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                        }
                    )
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_med}"
                    )
                    user_collection_ref.update(
                        {
                            questions_failed: firestore.Increment(
                                questions_failed_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                            amc12_points: firestore.Increment(amc12_wrong_amount_med),
                            amc12_failed: firestore.Increment(amc12_failed_amount),
                        }
                    )
                    break

        if difficulty.lower() == ("hard" or "h"):
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_hard = str(random.randint(17, 25))
                amc12_contestid = str(random.choice(amc12_id))

                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc12_contestid}/{amc_hard}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc12_contestid}/{amc_hard}/sol.txt"
                        ).text
                    ).strip()
                )

                for emoji in reactions:
                    await question.add_reaction(emoji)

                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_answer
                )

                if reactions[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_hard}"
                    )
                    user_collection_ref.update(
                        {
                            questions_solved: firestore.Increment(
                                questions_solved_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                            amc12_points: firestore.Increment(
                                amc12_correct_amount_hard
                            ),
                            amc12_solved: firestore.Increment(amc12_solved_amount),
                        }
                    )
                    break
                elif reactions[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    user_collection_ref.update(
                        {
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                        }
                    )
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_hard}"
                    )
                    user_collection_ref.update(
                        {
                            questions_failed: firestore.Increment(
                                questions_failed_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc12_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                            amc12_points: firestore.Increment(amc12_wrong_amount_hard),
                            amc12_failed: firestore.Increment(amc12_failed_amount),
                        }
                    )
                    break


def setup(bot):
    bot.add_cog(ContestProblems(bot))
