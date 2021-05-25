from discord.ext import commands
from firebase_admin import firestore
from ..utility.db import (
    db,
    open_user_db,
    questions_attempted,
    questions_failed,
    questions_solved,
    aime_attempted,
    usajmo_attempted,
    usamo_attempted,
    amc10_attempted,
    amc10_failed,
    amc10_points,
    amc10_solved,
    amc12_attempted,
    amc12_failed,
    amc12_points,
    amc12_solved,
)
import requests
import random

# Fetch contest problems help
fetch_help = {
    "name": "=fetch help info",
    "description_name": "Description",
    "description": "Fetch a problem from the given contests:\n- AMC 10A, 10B, 12A, 12B\n- USAMO\n- USAJMO\n- AIME I, II\n**This command is unranked and will not give any points**",
    "usage_name": "Usage",
    "usage_description": "`=fetch <contest name> <contest year> [contest version] <problem number>`\nExample: `=fetch amc 2010 10b 16`, `=fetch aime 2000 1 15` or for contests before 2000 in the AIME `=fetch aime 1999 15`",  # noqa E501
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

# last5 contest problems help
last5_help = {
    "name": "=lastfive help info",
    "description_name": "Description",
    "description": "This command retrieves a random last five question from a specified contest.\n**This command is ranked and will give points**",
    "usage_name": "Usage",
    "usage_description": "`=lastfive <contest name>`",  # noqa E501
    "alias_name": "Aliases",
    "alias_description": "`last5`, `l5`",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

# random contest problems help
random_help = {
    "name": "=random help info",
    "description_name": "Description",
    "description": "Gives you a random question from either the AMC10 or AMC12. Best for when you want a surprise!\n**This command is ranked and will give points**",
    "usage_name": "Usage",
    "usage_description": "`=random`",  # noqa E501
    "alias_name": "Aliases",
    "alias_description": "`rnd`",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

questions_attempted_amount = 1
questions_failed_amount = 1
questions_solved_amount = 1

amc10_solved_amount = 1
amc12_solved_amount = 1
amc10_failed_amount = 1
amc12_failed_amount = 1

amc12_correct_amount_easy = 2
amc12_wrong_amount_easy = -2
amc12_correct_amount_med = 6
amc12_wrong_amount_med = -1.5
amc12_correct_amount_hard = 15
amc12_wrong_amount_hard = -0.5
amc12_attempted_amount = 1

amc10_correct_amount_easy = 2
amc10_wrong_amount_easy = -2
amc10_correct_amount_med = 6
amc10_wrong_amount_med = -1.5
amc10_correct_amount_hard = 15
amc10_wrong_amount_hard = -0.5
amc10_attempted_amount = 1

aime_attempted_amount = 1
usamo_attempted_amount = 1
usajmo_attempted_amount = 1

amc12_weight = 0.65
amc10_weight = 0.35
amc10_id = ["10A", "10B"]
amc12_id = ["12A", "12B"]
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
        await open_user_db(user_guild_id, user_id)

        async def parse_args(args):
            user_collection_ref = db.collection(str(user_guild_id)).document(
                str(user_id)
            )
            if "aime" in args.lower():
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        aime_attempted: firestore.Increment(aime_attempted_amount),
                    }
                )
            elif "usamo" in args.lower():
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        usamo_attempted: firestore.Increment(usamo_attempted_amount),
                    }
                )
            elif "usajmo" in args.lower():
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        usajmo_attempted: firestore.Increment(usajmo_attempted_amount),
                    }
                )

        await parse_args(args)
        if args is not None:
            user_collection_ref = db.collection(str(user_guild_id)).document(
                str(user_id)
            )
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

            if sol != "404: Not Found":
                while True:
                    for emoji in reactions:
                        await question.add_reaction(emoji)

                    reaction, user = await self.bot.wait_for(
                        "reaction_add", check=check_answer
                    )

                    if reactions[reaction.emoji] == sol:
                        await ctx.send(f"<@{ctx.author.id}> Correct.")
                        user_collection_ref.update(
                            {
                                questions_solved: firestore.Increment(
                                    questions_solved_amount
                                ),
                                questions_attempted: firestore.Increment(
                                    questions_attempted_amount
                                ),
                            }
                        )
                        break
                    elif reactions[reaction.emoji] == "quit":
                        await ctx.send(f"<@{ctx.author.id}> You quit.")
                        user_collection_ref.update(
                            {
                                questions_attempted: firestore.Increment(
                                    questions_attempted_amount
                                )
                            }
                        )
                        break
                    else:
                        await ctx.send(f"<@{ctx.author.id}> Wrong")
                        user_collection_ref.update(
                            {
                                questions_failed: firestore.Increment(
                                    questions_failed_amount
                                ),
                                questions_attempted: firestore.Increment(
                                    questions_attempted_amount
                                ),
                            }
                        )
                        break
            else:
                await ctx.send(
                    f"<@{ctx.author.id}> Sorry, there is no solution file for this question yet, we are working hard to add more files."
                )

    @commands.command(aliases=["l5", "last5", "lfive"])
    async def lastfive(self, ctx, args):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id
        await open_user_db(user_guild_id, user_id)

        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        async def parse_args(args):
            if "aime" in args.lower():
                return "aime"
            elif "usamo" in args.lower():
                return "usamo"
            elif "usajmo" in args.lower():
                return "usajmo"
            elif args.lower() == "amc10":
                return "amc10"
            elif args.lower() == "amc12":
                return "amc12"

        parsed_arg = await parse_args(args)

        tried = []

        def check_answer(reaction, user):
            return (
                user == ctx.message.author
                and reaction.emoji in reactions
                and user.id not in tried
            )

        if parsed_arg == "aime":
            while True:
                random_aime_id = random.choice(aime_id)
                aime_year = str(random.randint(2000, 2019))
                last_5 = str(random.randint(10, 15))
                await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AIME/{aime_year}/{random_aime_id}/{last_5}/statement.png"
                )
                await ctx.send(
                    f"<@{ctx.author.id}> Sorry, there is no solution file for this question yet, we are working hard to add more files."
                )
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        aime_attempted: firestore.Increment(aime_attempted_amount),
                    }
                )
                break
        elif parsed_arg == "usamo":
            while True:
                usamo_year = str(random.randint(1972, 2019))
                last_5 = str(random.randint(1, 5))
                await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAMO/{usamo_year}/{last_5}/statement.png"
                )
                await ctx.send(
                    f"<@{ctx.author.id}> Sorry, there is no solution file for this question yet, we are working hard to add more files."
                )
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        usamo_attempted: firestore.Increment(usamo_attempted_amount),
                    }
                )
                break
        elif parsed_arg == "usajmo":
            while True:
                usajmo_year = str(random.randint(2010, 2019))
                last_5 = str(random.randint(1, 5))
                await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAJMO/{usajmo_year}/{last_5}/statement.png"
                )
                await ctx.send(
                    f"<@{ctx.author.id}> Sorry, there is no solution file for this question yet, we are working hard to add more files."
                )
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        usajmo_attempted: firestore.Increment(usajmo_attempted_amount),
                    }
                )
                break
        elif parsed_arg == "amc10":
            while True:
                random_year = str(random.randint(2002, 2019))
                last_5 = str(random.randint(20, 25))
                random_contest = str(random.choice(amc10_id))

                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{random_contest}/{last_5}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{random_contest}/{last_5}/sol.txt"
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
                        f"<@{ctx.author.id}> Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{last_5}"
                    )
                    user_collection_ref.update(
                        {
                            questions_solved: firestore.Increment(
                                questions_solved_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc10_attempted: firestore.Increment(
                                amc10_attempted_amount
                            ),
                            amc10_points: firestore.Increment(
                                amc10_correct_amount_easy
                            ),
                            amc10_solved: firestore.Increment(amc10_solved_amount),
                        }
                    )
                    break
                elif reactions[reaction.emoji] == "quit":
                    await ctx.send(f"<@{ctx.author.id}> You quit.")
                    user_collection_ref.update(
                        {
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc10_attempted: firestore.Increment(
                                amc10_attempted_amount
                            ),
                        }
                    )
                    break
                else:
                    await ctx.send(
                        f"<@{ctx.author.id}> Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{last_5}"
                    )
                    user_collection_ref.update(
                        {
                            questions_failed: firestore.Increment(
                                questions_failed_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc10_attempted: firestore.Increment(
                                amc10_attempted_amount
                            ),
                            amc10_points: firestore.Increment(amc10_wrong_amount_easy),
                            amc10_failed: firestore.Increment(amc10_failed_amount),
                        }
                    )
                    break
        elif parsed_arg == "amc12":
            while True:
                random_year = str(random.randint(2002, 2019))
                last_5 = str(random.randint(20, 25))
                amc_id = str(random.choice(amc12_id))

                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{amc_id}/{last_5}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{amc_id}/{last_5}/sol.txt"
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
                        f"<@{ctx.author.id}> Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{amc_id}_Problems/Problem_{last_5}"
                    )
                    user_collection_ref.update(
                        {
                            questions_solved: firestore.Increment(
                                questions_solved_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc10_attempted: firestore.Increment(
                                amc12_attempted_amount
                            ),
                            amc10_points: firestore.Increment(
                                amc12_correct_amount_easy
                            ),
                            amc12_solved: firestore.Increment(amc12_solved_amount),
                        }
                    )
                    break
                elif reactions[reaction.emoji] == "quit":
                    await ctx.send(f"<@{ctx.author.id}> You quit.")
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
                        f"<@{ctx.author.id}> Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{amc_id}_Problems/Problem_{last_5}"
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

    @commands.command(aliases=["rnd"])
    async def random(self, ctx):
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

        while True:
            random_contest = str(random.choice(amc_id))
            random_year = str(random.randint(2002, 2019))
            random_problem = str(random.randint(1, 25))

            if random_contest == "10B" or random_contest == "10A":
                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{random_contest}/{random_problem}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{random_contest}/{random_problem}/sol.txt"
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
                        f"<@{ctx.author.id}> Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem}"
                    )
                    user_collection_ref.update(
                        {
                            questions_solved: firestore.Increment(
                                questions_solved_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc10_attempted: firestore.Increment(
                                amc10_attempted_amount
                            ),
                            amc10_points: firestore.Increment(
                                amc10_correct_amount_easy
                            ),
                            amc10_solved: firestore.Increment(amc10_solved_amount),
                        }
                    )
                    break
                elif reactions[reaction.emoji] == "quit":
                    await ctx.send(f"<@{ctx.author.id}> You quit.")
                    user_collection_ref.update(
                        {
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc10_attempted: firestore.Increment(
                                amc10_attempted_amount
                            ),
                        }
                    )
                    break
                else:
                    await ctx.send(
                        f"<@{ctx.author.id}> Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem}"
                    )
                    user_collection_ref.update(
                        {
                            questions_failed: firestore.Increment(
                                questions_failed_amount
                            ),
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            ),
                            amc10_attempted: firestore.Increment(
                                amc10_attempted_amount
                            ),
                            amc10_points: firestore.Increment(amc10_wrong_amount_easy),
                            amc10_failed: firestore.Increment(amc10_failed_amount),
                        }
                    )
                    break

            else:
                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{random_contest}/{random_problem}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{random_contest}/{random_problem}/sol.txt"
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
                        f"<@{ctx.author.id}> Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem}"
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
                    await ctx.send(f"<@{ctx.author.id}> You quit.")
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
                        f"<@{ctx.author.id}> Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem}"
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


def setup(bot):
    bot.add_cog(ContestProblems(bot))
