from discord.ext import commands
from firebase_admin import firestore
from ..utility.db import (
    db,
    open_user_db,
    questions_attempted,
    questions_failed,
    questions_solved,
    amc10_attempted,
    amc10_failed,
    amc10_solved,
    amc10_points,
)
import requests
import discord
import random
from .contest_problems import (
    reactions,
    questions_attempted_amount,
    questions_failed_amount,
    questions_solved_amount,
    amc10_failed_amount,
    amc10_id,
    amc10_solved_amount,
    amc10_correct_amount_easy,
    amc10_correct_amount_med,
    amc10_correct_amount_hard,
    amc10_attempted_amount,
    amc10_wrong_amount_easy,
    amc10_wrong_amount_hard,
    amc10_wrong_amount_med,
)

# AMC10 help
amc10_help = {
    "name": "=amc10 help info",
    "description_name": "Description",
    "description": "Returns an AMC10 problem from the following difficulties:\n- `easy` or `e`\n- `medium` or `med`\n- `hard` or `h`\n**This command is ranked and will give points**",  # noqa E501
    "usage_name": "Usage",
    "usage_description": "`=amc10 <difficulty>`\nExample: `=amc10 med`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}


class AMC10(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("AMC10 cog has been loaded sucessfully")

    @commands.command()
    async def amc10(self, ctx, difficulty):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id
        await open_user_db(user_guild_id, user_id)

        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        status_color = {"easy": 0x3CB371, "medium": 0xFF8C00, "hard": 0xED1C24}

        tried = []

        if difficulty.lower() == "e" or difficulty.lower() == "easy":
            randomyear = str(random.randint(2002, 2019))
            amc_easy = str(random.randint(1, 10))
            amc10_contestid = str(random.choice(amc10_id))

            question_embed = discord.Embed(
                title=f"{randomyear} AMC {amc10_contestid} Problem {amc_easy}",
                color=status_color["easy"],
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_easy}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

            sol = str(
                (
                    requests.get(
                        f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_easy}/sol.txt"
                    ).text
                ).strip()
            )

            for emoji in reactions:
                await question.add_reaction(emoji)

            reaction, user = await self.bot.wait_for(
                "reaction_add",
                check=(
                    lambda reaction, user: (
                        reaction.message.id == question.id
                        and user == ctx.message.author
                        and reaction.emoji in reactions
                        and user.id not in tried
                    )
                ),
            )

            if reactions[reaction.emoji] == sol:
                question_embed.description = (
                    f"<@{ctx.author.id}> Correct. However, you may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_easy})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                        amc10_points: firestore.Increment(amc10_correct_amount_easy),
                        amc10_solved: firestore.Increment(amc10_solved_amount),
                    }
                )
            elif reactions[reaction.emoji] == "quit":
                question_embed.description = f"<@{ctx.author.id}> You quit."
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                    }
                )
            else:
                question_embed.description = (
                    f"<@{ctx.author.id}> Incorrect. You may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_easy})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_failed: firestore.Increment(questions_failed_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                        amc10_points: firestore.Increment(amc10_wrong_amount_easy),
                        amc10_failed: firestore.Increment(amc10_failed_amount),
                    }
                )

        if difficulty.lower() == "m" or difficulty.lower() == "medium":
            randomyear = str(random.randint(2002, 2019))
            amc_medium = str(random.randint(11, 16))
            amc10_contestid = str(random.choice(amc10_id))

            question_embed = discord.Embed(
                title=f"{randomyear} AMC {amc10_contestid} Problem {amc_medium}",
                color=status_color["medium"],
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_medium}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

            sol = str(
                (
                    requests.get(
                        f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_medium}/sol.txt"
                    ).text
                ).strip()
            )

            for emoji in reactions:
                await question.add_reaction(emoji)

            reaction, user = await self.bot.wait_for(
                "reaction_add",
                check=(
                    lambda reaction, user: (
                        reaction.message.id == question.id
                        and user == ctx.message.author
                        and reaction.emoji in reactions
                        and user.id not in tried
                    )
                ),
            )

            if reactions[reaction.emoji] == sol:
                question_embed.description = (
                    f"<@{ctx.author.id}> Correct. However, you may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_medium})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                        amc10_points: firestore.Increment(amc10_correct_amount_med),
                        amc10_solved: firestore.Increment(amc10_solved_amount),
                    }
                )
            elif reactions[reaction.emoji] == "quit":
                question_embed.description = f"<@{ctx.author.id}> You quit."
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                    }
                )
            else:
                question_embed.description = (
                    f"<@{ctx.author.id}> Incorrect. You may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_medium})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_failed: firestore.Increment(questions_failed_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                        amc10_points: firestore.Increment(amc10_wrong_amount_med),
                        amc10_failed: firestore.Increment(amc10_failed_amount),
                    }
                )

        if difficulty.lower() == "h" or difficulty.lower() == "hard":
            randomyear = str(random.randint(2002, 2019))
            amc_hard = str(random.randint(17, 25))
            amc10_contestid = str(random.choice(amc10_id))

            question_embed = discord.Embed(
                title=f"{randomyear} AMC {amc10_contestid} Problem {amc_hard}",
                color=status_color["hard"],
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_hard}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

            sol = str(
                (
                    requests.get(
                        f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_hard}/sol.txt"
                    ).text
                ).strip()
            )

            for emoji in reactions:
                await question.add_reaction(emoji)

            reaction, user = await self.bot.wait_for(
                "reaction_add",
                check=(
                    lambda reaction, user: (
                        reaction.message.id == question.id
                        and user == ctx.message.author
                        and reaction.emoji in reactions
                        and user.id not in tried
                    )
                ),
            )

            if reactions[reaction.emoji] == sol:
                question_embed.description = (
                    f"<@{ctx.author.id}> Correct. However, you may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_hard})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                        amc10_points: firestore.Increment(amc10_correct_amount_hard),
                        amc10_solved: firestore.Increment(amc10_solved_amount),
                    }
                )
            elif reactions[reaction.emoji] == "quit":
                question_embed.description = f"<@{ctx.author.id}> You quit."
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                    }
                )
            else:
                question_embed.description = (
                    f"<@{ctx.author.id}> Incorrect. You may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_hard})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_failed: firestore.Increment(questions_failed_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc10_attempted_amount),
                        amc10_points: firestore.Increment(amc10_wrong_amount_hard),
                        amc10_failed: firestore.Increment(amc10_failed_amount),
                    }
                )


def setup(bot):
    bot.add_cog(AMC10(bot))
