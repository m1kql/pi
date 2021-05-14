import json
import random

import discord
import requests
from discord.ext import commands

amc10weight = 0.3
amc12weight = 0.7
amc10_id = ["10A", "10B"]
amc12_id = ["12A", "12B"]
amc_id = ["10A", "10B", "12A", "12B"]
aime_id = ["1", "2"]
emojis = {"🇦": "a", "🇧": "b", "🇨": "c", "🇩": "d", "🇪": "e", "❎": "quit"}
# aime_last5 = str(random.randint(10, 15)); usamo_last5 = str(random.randint(10, 15)); aime_contestid = str(random.choice(aime_id))

###################################################################################################################
# Basic Functions to return data
###################################################################################################################
async def open_account(self, user):
    users = await get_points_data(self)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}

    # points
    users[str(user.id)]["amc10 points"] = 0
    users[str(user.id)]["amc12 points"] = 0

    # questions
    users[str(user.id)]["amc10 questions solved"] = 0
    users[str(user.id)]["amc10 questions failed"] = 0
    users[str(user.id)]["amc12 questions solved"] = 0
    users[str(user.id)]["amc12 questions failed"] = 0
    users[str(user.id)]["amc10 questions"] = 0
    users[str(user.id)]["amc12 questions"] = 0
    users[str(user.id)]["aime questions"] = 0
    users[str(user.id)]["usamo questions"] = 0
    users[str(user.id)]["usajmo questions"] = 0
    users[str(user.id)]["questions failed"] = 0
    users[str(user.id)]["questions solved"] = 0
    users[str(user.id)]["questions done"] = 0

    with open("mathpoints.json", "w") as f:
        json.dump(users, f)
    return True


async def get_points_data(self):
    with open("mathpoints.json", "r") as f:
        users = json.load(f)
    return users


class MathContest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Contest Math cog has been loaded sucessfully")

    @commands.command()
    async def fetch(self, ctx, *, argspath=None):
        if argspath != None:

            await open_account(self, ctx.author)
            users = await get_points_data(self)
            user = ctx.author
            tried = []

            def check_reactions(reaction, user):
                return (
                    user == ctx.message.author
                    and reaction.emoji in emojis
                    and user.id not in tried
                )

            requested_path = argspath.upper().replace(" ", "/")
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
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct.")
                    users[str(user.id)]["questions solved"] += 1
                    users[str(user.id)]["questions done"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    users[str(user.id)]["questions done"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                else:
                    await ctx.send("Wrong.")
                    tried.append(user.id)
                    users[str(user.id)]["questions failed"] += 1
                    users[str(user.id)]["questions done"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break

    ###################################################################################################################
    # American Contests
    ###################################################################################################################
    @commands.command()
    async def amc10(self, ctx, difficulty):
        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author
        tried = []

        def check_reactions(reaction, user):
            return (
                user == ctx.message.author
                and reaction.emoji in emojis
                and user.id not in tried
            )

        if difficulty == "easy" or difficulty == "e":
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_easy = str(random.randint(1, 10))
                amc10_contestid = str(random.choice(amc10_id))
                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_easy}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_easy}/sol.txt"
                        ).text
                    ).strip()
                )
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_easy}"
                    )
                    users[str(user.id)]["questions solved"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions solved"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    users[str(user.id)]["amc10 points"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_easy}"
                    )
                    tried.append(user.id)
                    users[str(user.id)]["questions failed"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions failed"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    users[str(user.id)]["amc10 points"] -= 2
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
        if difficulty == "med" or difficulty == "m":
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_med = str(random.randint(11, 16))
                amc10_contestid = str(random.choice(amc10_id))
                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_med}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_med}/sol.txt"
                        ).text
                    ).strip()
                )
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_med}"
                    )
                    users[str(user.id)]["questions solved"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions solved"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    users[str(user.id)]["amc10 points"] += 4
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_med}"
                    )
                    tried.append(user.id)
                    users[str(user.id)]["questions failed"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions failed"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    users[str(user.id)]["amc10 points"] -= 1.5
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
        if difficulty == "hard" or difficulty == "h":
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_hard = str(random.randint(17, 25))
                amc10_contestid = str(random.choice(amc10_id))
                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_hard}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{amc10_contestid}/{amc_hard}/sol.txt"
                        ).text
                    ).strip()
                )
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_hard}"
                    )
                    users[str(user.id)]["questions solved"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions solved"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    users[str(user.id)]["amc10 points"] += 6
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc10_contestid}_Problems/Problem_{amc_hard}"
                    )
                    tried.append(user.id)
                    users[str(user.id)]["questions failed"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions failed"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    users[str(user.id)]["amc10 points"] -= 0.5
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break

    # Random AMC 12 problem based on difficulty
    @commands.command()
    async def amc12(self, ctx, difficulty):
        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author
        tried = []

        def check_reactions(reaction, user):
            return (
                user == ctx.message.author
                and reaction.emoji in emojis
                and user.id not in tried
            )

        if difficulty == "easy" or difficulty == "e":
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
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_easy}"
                    )
                    users[str(user.id)]["questions solved"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc12 questions solved"] += 1
                    users[str(user.id)]["amc12 questions"] += 1
                    users[str(user.id)]["amc12 points"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_easy}"
                    )
                    tried.append(user.id)
                    users[str(user.id)]["questions failed"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc12 questions failed"] += 1
                    users[str(user.id)]["amc12 questions"] += 1
                    users[str(user.id)]["amc12 points"] -= 2
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
        if difficulty == "med" or difficulty == "m":
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
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_med}"
                    )
                    users[str(user.id)]["questions solved"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc12 questions solved"] += 1
                    users[str(user.id)]["amc12 questions"] += 1
                    users[str(user.id)]["amc12 points"] += 4
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_med}"
                    )
                    tried.append(user.id)
                    users[str(user.id)]["questions failed"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc12 questions failed"] += 1
                    users[str(user.id)]["amc12 questions"] += 1
                    users[str(user.id)]["amc12 points"] -= 1.5
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
        if difficulty == "hard" or difficulty == "h":
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
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_hard}"
                    )
                    users[str(user.id)]["questions solved"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc12 questions solved"] += 1
                    users[str(user.id)]["amc12 questions"] += 1
                    users[str(user.id)]["amc12 points"] += 6
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("You quit.")
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc10 questions"] += 1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{amc12_contestid}_Problems/Problem_{amc_hard}"
                    )
                    tried.append(user.id)
                    users[str(user.id)]["questions failed"] += 1
                    users[str(user.id)]["questions done"] += 1
                    users[str(user.id)]["amc12 questions failed"] += 1
                    users[str(user.id)]["amc12 questions"] += 1
                    users[str(user.id)]["amc12 points"] -= 0.5
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    break

    # Any last 5 questions from the AMC 10 or 12 (Ranked)
    @commands.command()
    async def last5(self, ctx, contest_type=None):
        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author
        tried = []

        def check_reactions(reaction, user):
            return (
                user == ctx.message.author
                and reaction.emoji in emojis
                and user.id not in tried
            )

        if contest_type != None:
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_hard = str(random.randint(17, 25))
                random_contestid = str(random.choice(amc_id))
                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{random_contestid}/{amc_hard}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{random_contestid}/{amc_hard}/sol.txt"
                        ).text
                    ).strip()
                )
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{random_contestid}_Problems/Problem_{amc_hard}"
                    )
                    if amc_id == "10A" or amc_id == "10B":
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc10 questions solved"] += 1
                        users[str(user.id)]["amc10 questions"] += 1
                        users[str(user.id)]["amc10 points"] += 6
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                    else:
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc12 questions solved"] += 1
                        users[str(user.id)]["amc12 questions"] += 1
                        users[str(user.id)]["amc12 points"] += 6
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                elif emojis[reaction.emoji] == "quit":
                    if amc_id == "10A" or amc_id == "10B":
                        await ctx.send("You quit.")
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc10 questions"] += 1
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                    else:
                        await ctx.send("You quit.")
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc12 questions"] += 1
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{random_contestid}_Problems/Problem_{amc_hard}"
                    )
                    if amc_id == "10A" or amc_id == "10B":
                        tried.append(user.id)
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc10 questions failed"] += 1
                        users[str(user.id)]["amc10 questions"] += 1
                        users[str(user.id)]["amc10 points"] -= 0.5
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                    else:
                        tried.append(user.id)
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc12 questions failed"] += 1
                        users[str(user.id)]["amc12 questions"] += 1
                        users[str(user.id)]["amc12 points"] -= 0.5
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break

    # A random question from the AMC10 or 12 (Ranked)
    @commands.command()
    async def random(self, ctx, contest_type):
        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author
        tried = []

        def check_reactions(reaction, user):
            return (
                user == ctx.message.author
                and reaction.emoji in emojis
                and user.id not in tried
            )

        if contest_type == "amc":
            while True:
                randomyear = str(random.randint(2002, 2019))
                amc_random = str(random.randint(1, 25))
                random_contestid = str(random.choice(amc_id))
                question = await ctx.send(
                    f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{random_contestid}/{amc_random}/statement.png"
                )
                sol = str(
                    (
                        requests.get(
                            f"https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{random_contestid}/{amc_random}/sol.txt"
                        ).text
                    ).strip()
                )
                for i in emojis:
                    await question.add_reaction(i)
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check_reactions
                )
                if emojis[reaction.emoji] == sol:
                    await ctx.send(
                        "Correct. However, you may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{random_contestid}_Problems/Problem_{amc_random}"
                    )
                    if amc_id == "10A" or amc_id == "10B":
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc10 questions solved"] += 1
                        users[str(user.id)]["amc10 questions"] += 1
                        users[str(user.id)]["amc10 points"] += 3
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                    else:
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc12 questions solved"] += 1
                        users[str(user.id)]["amc12 questions"] += 1
                        users[str(user.id)]["amc12 points"] += 3
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                elif emojis[reaction.emoji] == "quit":
                    if amc_id == "10A" or amc_id == "10B":
                        await ctx.send("You quit.")
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc10 questions"] += 1
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                    else:
                        await ctx.send("You quit.")
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc12 questions"] += 1
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                else:
                    await ctx.send(
                        "Wrong. You may want to check against this get a better understanding"
                    )
                    await ctx.send(
                        f"https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{random_contestid}_Problems/Problem_{amc_random}"
                    )
                    if amc_id == "10A" or amc_id == "10B":
                        tried.append(user.id)
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc10 questions failed"] += 1
                        users[str(user.id)]["amc10 questions"] += 1
                        users[str(user.id)]["amc10 points"] -= 1
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break
                    else:
                        tried.append(user.id)
                        users[str(user.id)]["questions solved"] += 1
                        users[str(user.id)]["questions done"] += 1
                        users[str(user.id)]["amc12 questions failed"] += 1
                        users[str(user.id)]["amc12 questions"] += 1
                        users[str(user.id)]["amc12 points"] -= 1
                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        break

    ###################################################################################################################
    # Canadian Contests
    ###################################################################################################################

    # TODO

    ###################################################################################################################
    # Statistics command
    ###################################################################################################################
    @commands.command()
    async def stats(self, ctx):

        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author

        amc10_weighted = amc10weight * (int(users[str(user.id)]["amc10 points"]))
        amc12_weighted = amc12weight * (int(users[str(user.id)]["amc12 points"]))
        questions_done = users[str(user.id)]["questions done"]
        questions_solved = users[str(user.id)]["questions solved"]
        questions_failed = users[str(user.id)]["questions failed"]
        amc10_solved = users[str(user.id)]["amc10 questions solved"]
        amc12_solved = users[str(user.id)]["amc12 questions solved"]
        amc10_failed = users[str(user.id)]["amc10 questions failed"]
        amc12_failed = users[str(user.id)]["amc12 questions failed"]
        amc10_done = users[str(user.id)]["amc10 questions"]
        amc12_done = users[str(user.id)]["amc12 questions"]
        aime_done = users[str(user.id)]["aime questions"]
        usamo_done = users[str(user.id)]["usamo questions"]
        usajmo_done = users[str(user.id)]["usajmo questions"]

        total_weighted = round((amc10_weighted + amc12_weighted), 2)
        total_unweighted = round(
            (users[str(user.id)]["amc10 points"] + users[str(user.id)]["amc12 points"]),
            2,
        )

        statistics_emb = discord.Embed(
            title=f"{ctx.author.name}'s statistics", color=discord.Color.blue()
        )
        statistics_emb.add_field(
            name="Problems Solved",
            value=f"AMC 10: `{amc10_solved}`\nAMC 12: `{amc12_solved}`\nTotal Solved: `{questions_solved}`",
        )
        statistics_emb.add_field(
            name="Problems Fetched",
            value=f"AMC 10: `{amc10_done}`\nAMC 12: `{amc12_done}`\nAIME: `{aime_done}`\nUSAMO: `{usamo_done}`\nUSAJMO: `{usajmo_done}`\nTotal Fetched: `{questions_done}`",
        )
        statistics_emb.add_field(
            name="Problems Failed",
            value=f"AMC 10: `{amc10_failed}`\nAMC 12: `{amc12_failed}`\nTotal Failed: `{questions_failed}`",
        )
        statistics_emb.add_field(
            name="Points and Score",
            value=f"Weights: `amc10: 30%, amc12: 70%`\nAMC 10: `{amc10_weighted}`\nAMC 12: `{amc12_weighted}`\nTotal Score: `{total_weighted}`\nTotal Unweighted: `{total_unweighted}`",
        )

        await ctx.send(embed=statistics_emb)


def setup(bot):
    bot.add_cog(MathContest(bot))
