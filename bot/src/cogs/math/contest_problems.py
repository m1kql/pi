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
    cmo_attempted,
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
import discord
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

# aime problems help
aime_help = {
    "name": "=aime help info",
    "description_name": "Description",
    "description": "Gives you a random AIME I or II question. \n**This command is unranked and will not give any points**",
    "usage_name": "Usage",
    "usage_description": "`=aime`",  # noqa E501
    "alias_name": "Aliases",
    "alias_description": "No aliases",
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
amc12_wrong_amount_easy = -4
amc12_correct_amount_med = 6
amc12_wrong_amount_med = -1.5
amc12_correct_amount_hard = 15
amc12_wrong_amount_hard = -0.5
amc12_attempted_amount = 1

amc10_correct_amount_easy = 2
amc10_wrong_amount_easy = -5  # push players to work for higher scores
amc10_correct_amount_med = 6
amc10_wrong_amount_med = -1.5
amc10_correct_amount_hard = 15
amc10_wrong_amount_hard = -0.5
amc10_attempted_amount = 1

aime_attempted_amount = 1
usamo_attempted_amount = 1
usajmo_attempted_amount = 1
cmo_attempted_amount = 1

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
    async def cmo(self, ctx):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id

        await open_user_db(user_guild_id, user_id)

        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        user_collection_ref.update(
            {
                questions_attempted: firestore.Increment(questions_attempted_amount),
                cmo_attempted: firestore.Increment(cmo_attempted_amount),
            }
        )

        cmo_year = random.randint(1969, 1973)
        cmo_question = random.randint(1, 9)
        requested_path = f"CMO/{cmo_year}/{cmo_question}"

        question_embed = discord.Embed(
            title=f"{cmo_year} CMO Problem {cmo_question}",
            description=f"<@{ctx.author.id}> There is no solution file for this question yet, we are working hard to add more files.",
            color=0xCF9FFF,
        ).set_image(
            url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/{requested_path}/statement.png"
        )

        await ctx.send(embed=question_embed)

    @commands.command()
    async def aime(self, ctx):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id

        await open_user_db(user_guild_id, user_id)

        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        user_collection_ref.update(
            {
                questions_attempted: firestore.Increment(questions_attempted_amount),
                aime_attempted: firestore.Increment(aime_attempted_amount),
            }
        )

        aime_year = random.randint(1983, 2019)
        aime_version = random.randint(1, 2)
        aime_question = random.randint(1, 15)
        requested_path = ""

        question_embed = discord.Embed(
            description=f"<@{ctx.author.id}> There is no solution file for this question yet, we are working hard to add more files.",
            color=0xCF9FFF,
        )

        if aime_year < 2000:
            requested_path = f"AIME/{aime_year}/{aime_question}"
            question_embed.title = f"{aime_year} AIME Problem {aime_question}"
        else:
            requested_path = f"AIME/{aime_year}/{aime_version}/{aime_question}"
            question_embed.title = (
                f"{aime_year} AIME {'I'*aime_version} Problem {aime_question}"
            )

        question_embed.set_image(
            url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/{requested_path}/statement.png"
        )

        await ctx.send(embed=question_embed)

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
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        aime_attempted: firestore.Increment(aime_attempted_amount),
                    }
                )
            elif "usamo" in args.lower():
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        usamo_attempted: firestore.Increment(usamo_attempted_amount),
                    }
                )
            elif "usajmo" in args.lower():
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        usajmo_attempted: firestore.Increment(usajmo_attempted_amount),
                    }
                )
            elif "cmo" in args.lower():
                user_collection_ref.update(
                    {
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        cmo_attempted: firestore.Increment(cmo_attempted_amount),
                    }
                )

        await parse_args(args)
        if args is not None:
            user_collection_ref = db.collection(str(user_guild_id)).document(
                str(user_id)
            )

            contest_data = args.upper().split()

            requested_path = args.upper().replace(" ", "/")

            tried = []

            question_embed = discord.Embed(
                title=f"{contest_data[1]} {contest_data[0]} {' '.join(contest_data[2:-1])+' '}Problem {contest_data[-1]}",
                color=0xCF9FFF,
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/{requested_path}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

            sol = str(
                (
                    requests.get(
                        f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/{requested_path}/sol.txt"
                    ).text
                ).strip()
            )

            if sol != "404: Not Found":
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
                    question_embed.description = f"<@{ctx.author.id}> Correct."
                    await question.edit(embed=question_embed)
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
                elif reactions[reaction.emoji] == "quit":
                    question_embed.description = f"<@{ctx.author.id}> You quit."
                    await question.edit(embed=question_embed)
                    user_collection_ref.update(
                        {
                            questions_attempted: firestore.Increment(
                                questions_attempted_amount
                            )
                        }
                    )
                else:
                    question_embed.description = f"<@{ctx.author.id}> Incorrect."
                    await question.edit(embed=question_embed)
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
            else:
                question_embed.description = f"<@{ctx.author.id}> There is no solution file for this question yet, we are working hard to add more files."
                await question.edit(embed=question_embed)

    @commands.command(aliases=["l5", "last5", "lfive"])
    async def lastfive(self, ctx, args):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id
        await open_user_db(user_guild_id, user_id)

        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        def parse_args(args):
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

        parsed_arg = parse_args(args)

        tried = []

        if parsed_arg == "aime":
            random_aime_id = random.choice(aime_id)
            aime_year = str(random.randint(2000, 2019))
            last_5 = str(random.randint(10, 15))

            question_embed = discord.Embed(
                title=f"{aime_year} AIME {'I'*random_aime_id} Problem {last_5}",
                description=f"<@{ctx.author.id}> There is no solution file for this question yet, we are working hard to add more files.",
                color=0xCF9FFF,
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AIME/{aime_year}/{random_aime_id}/{last_5}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

            user_collection_ref.update(
                {
                    questions_attempted: firestore.Increment(
                        questions_attempted_amount
                    ),
                    aime_attempted: firestore.Increment(aime_attempted_amount),
                }
            )

        elif parsed_arg == "usamo":
            usamo_year = str(random.randint(1972, 2019))
            last_5 = str(random.randint(1, 5))

            question_embed = discord.Embed(
                title=f"{usamo_year} USAMO Problem {last_5}",
                description=f"<@{ctx.author.id}> There is no solution file for this question yet, we are working hard to add more files.",
                color=0xCF9FFF,
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAJMO/{usamo_year}/{last_5}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

            user_collection_ref.update(
                {
                    questions_attempted: firestore.Increment(
                        questions_attempted_amount
                    ),
                    usamo_attempted: firestore.Increment(usamo_attempted_amount),
                }
            )

        elif parsed_arg == "usajmo":
            usajmo_year = str(random.randint(2010, 2019))
            last_5 = str(random.randint(1, 5))

            question_embed = discord.Embed(
                title=f"{usajmo_year} USAJMO Problem {last_5}",
                description=f"<@{ctx.author.id}> There is no solution file for this question yet, we are working hard to add more files.",
                color=0xCF9FFF,
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAJMO/{usajmo_year}/{last_5}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

            user_collection_ref.update(
                {
                    questions_attempted: firestore.Increment(
                        questions_attempted_amount
                    ),
                    usajmo_attempted: firestore.Increment(usajmo_attempted_amount),
                }
            )

        elif parsed_arg == "amc10":
            random_year = str(random.randint(2002, 2019))
            last_5 = str(random.randint(20, 25))
            amc_id = str(random.choice(amc10_id))

            question_embed = discord.Embed(
                title=f"{random_year} AMC {amc_id} Problem {last_5}",
                color=0xCF9FFF,
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{amc_id}/{last_5}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

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
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{amc_id}_Problems/Problem_{last_5})"
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
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{amc_id}_Problems/Problem_{last_5})"
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

        elif parsed_arg == "amc12":
            random_year = str(random.randint(2002, 2019))
            last_5 = str(random.randint(20, 25))
            amc_id = str(random.choice(amc12_id))

            question_embed = discord.Embed(
                title=f"{random_year} AMC {amc_id} Problem {last_5}",
                color=0xCF9FFF,
            ).set_image(
                url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{amc_id}/{last_5}/statement.png"
            )

            question = await ctx.send(embed=question_embed)

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
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{amc_id}_Problems/Problem_{last_5})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc10_attempted: firestore.Increment(amc12_attempted_amount),
                        amc10_points: firestore.Increment(amc12_correct_amount_easy),
                        amc12_solved: firestore.Increment(amc12_solved_amount),
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
                        amc12_attempted: firestore.Increment(amc12_attempted_amount),
                    }
                )

            else:
                question_embed.description = (
                    f"<@{ctx.author.id}> Incorrect. You may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{amc_id}_Problems/Problem_{last_5})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_failed: firestore.Increment(questions_failed_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc12_attempted: firestore.Increment(amc12_attempted_amount),
                        amc12_points: firestore.Increment(amc12_wrong_amount_easy),
                        amc12_failed: firestore.Increment(amc12_failed_amount),
                    }
                )

    @commands.command(aliases=["rnd"])
    async def random(self, ctx):
        user_guild_id = ctx.guild.id
        user_id = ctx.author.id
        await open_user_db(user_guild_id, user_id)

        user_collection_ref = db.collection(str(user_guild_id)).document(str(user_id))

        tried = []

        random_contest = str(random.choice(amc_id))
        random_year = str(random.randint(2002, 2019))
        random_problem = str(random.randint(1, 25))

        question_embed = discord.Embed(
            title=f"{random_year} AMC {random_contest} Problem {random_problem}",
            color=0x00BFFF,
        ).set_image(
            url=f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{random_year}/{random_contest}/{random_problem}/statement.png"
        )

        question = await ctx.send(embed=question_embed)

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

        if random_contest == "10B" or random_contest == "10A":
            if reactions[reaction.emoji] == sol:
                question_embed.description = (
                    f"<@{ctx.author.id}> Correct. However, you may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem})"
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
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem})"
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

        else:
            if reactions[reaction.emoji] == sol:
                question_embed.description = (
                    f"<@{ctx.author.id}> Correct. However, you may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_solved: firestore.Increment(questions_solved_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc12_attempted: firestore.Increment(amc12_attempted_amount),
                        amc12_points: firestore.Increment(amc12_correct_amount_easy),
                        amc12_solved: firestore.Increment(amc12_solved_amount),
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
                        amc12_attempted: firestore.Increment(amc12_attempted_amount),
                    }
                )

            else:
                question_embed.description = (
                    f"<@{ctx.author.id}> Incorrect. You may want to check against"
                    f" [this](https://artofproblemsolving.com/wiki/index.php?title={random_year}_AMC_{random_contest}_Problems/Problem_{random_problem})"
                    f" to get a better understanding."
                )
                await question.edit(embed=question_embed)
                user_collection_ref.update(
                    {
                        questions_failed: firestore.Increment(questions_failed_amount),
                        questions_attempted: firestore.Increment(
                            questions_attempted_amount
                        ),
                        amc12_attempted: firestore.Increment(amc12_attempted_amount),
                        amc12_points: firestore.Increment(amc12_wrong_amount_easy),
                        amc12_failed: firestore.Increment(amc12_failed_amount),
                    }
                )


def setup(bot):
    bot.add_cog(ContestProblems(bot))
