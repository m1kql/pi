import json
import random

import discord
import requests
from discord.ext import commands

amc10weight=0.2
amc12weight=0.3
last5weight=0.3
randomweight=0.2

class Contestproblems(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Contest Math cog has been loaded sucessfully')



    # All Math Commands
    @commands.command()
    async def fetchamc(self, ctx, year=None, contest_id=None, problem_num=None):

        if year != None and problem_num != None and contest_id != None:
            requested_year = str(year)
            requested_id = str(contest_id.upper())
            requested_problem = str(problem_num)
            emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e", "❎":"quit"}

            tried = []

            def check(reaction, user):
                return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{requested_year}/{requested_id}/{requested_problem}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{requested_year}/{requested_id}/{requested_problem}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={requested_year}_AMC_{requested_id}_Problems/Problem_{requested_problem}')
                    break    
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={requested_year}_AMC_{requested_id}_Problems/Problem_{requested_problem}')
                    break
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={requested_year}_AMC_{requested_id}_Problems/Problem_{requested_problem}')
                    break
    
    @commands.command()
    async def fetchaime(self, ctx, year=None, problem_num=None):
        if year!=None and problem_num !=None:
            requested_year = str(year)
            requested_problem = str(problem_num)
            try:
                await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AIME/{requested_year}/{requested_problem}/statement.png')
            except:
                await ctx.send("Sorry there was an error processing this command")

    @commands.command()
    async def fetchusamo(self, ctx, year=None, problem_num=None):
        if year!=None and problem_num!=None:
            requested_year = str(year)
            requested_problem = str(problem_num)
            try:
                await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAMO/{requested_year}/{requested_problem}/statement.png')
            except:
                await ctx.send("Sorry there was an error processing this command")
    
    @commands.command()
    async def fetchusajmo(self, ctx, year=None, problem_num=None):
        if year!=None and problem_num!=None:
            requested_year = str(year)
            requested_problem = str(problem_num)
            try:
                await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAJMO/{requested_year}/{requested_problem}/statement.png')
            except:
                await ctx.send("Sorry there was an error processing this command")

    @commands.command()
    async def last5(self, ctx):

        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author

        contestid = ["10A", "12B"]
        lastfive = str(int(random.randint(20, 25)))
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(contestid))
        emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e"}

        tried = []

        def check(reaction, user):
            return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried

        while True:
            url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{lastfive}/sol.txt'
            page = requests.get(url)
            sol = str((str(page.text).strip()))
            question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{lastfive}/statement.png')

            for i in emojis:
                await question.add_reaction(i)

            reaction, user = await self.bot.wait_for('reaction_add', check=check)

            if randomcontestid == "10A":

                if emojis[reaction.emoji] == sol:
                    users[str(user.id)]["last5"] += 6
                    users[str(user.id)]["questions"]+=1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                    break
                
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                    break 

                else:
                    tried.append(user.id)
                    users[str(user.id)]["last5"] -= 0
                    users[str(user.id)]["questions"]+=1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                    break
            else:
                if emojis[reaction.emoji] == sol:
                    users[str(user.id)]["last5"] += 6
                    users[str(user.id)]["questions"]+=1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                    break

                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                    break 

                else:
                    tried.append(user.id)
                    users[str(user.id)]["last5"] -= 0
                    users[str(user.id)]["questions"]+=1
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                    break

    @commands.command()
    async def amc10(self, ctx, difficulty):

        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author


        amc10_id = ["10A", "10B"]
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(amc10_id))
        emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e", "❎":"quit"}

        tried = []

        def check(reaction, user):
            return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried


        if difficulty == "easy" or difficulty == "e":
            easy= str(int(random.randint(1, 10)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:

                    users[str(user.id)]["amc10 points"] += 1
                    users[str(user.id)]["amc10 questions solved"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions solved"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break
                
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break 

                else:

                    users[str(user.id)]["amc10 points"] -= 2
                    users[str(user.id)]["amc10 questions failed"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions failed"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break    


        elif difficulty == "med" or difficulty == "medium" or difficulty == "m":
            med = str(int(random.randint(11,16)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:

                    users[str(user.id)]["amc10 points"] += 4
                    users[str(user.id)]["amc10 questions solved"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions solved"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break
                
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break 

                else:

                    users[str(user.id)]["amc10 points"] -= 1.5
                    users[str(user.id)]["amc10 questions failed"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions failed"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break



        elif difficulty == "hard" or difficulty == "h":
            hard = str(int(random.randint(17, 25)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    
                    users[str(user.id)]["amc10 points"] += 6
                    users[str(user.id)]["amc10 questions solved"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions solved"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break

                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break 

                else:
                    
                    users[str(user.id)]["amc10 points"] -= 0.5
                    users[str(user.id)]["amc10 questions failed"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions failed"]+=1
                    
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break

    @commands.command()
    async def amc12(self, ctx, difficulty):

        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author

        amc12_id = ["12A", "12B"]
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(amc12_id))

        emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e", "❎":"quit"}

        tried = []

        def check(reaction, user):
            return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried

        if difficulty == "easy" or difficulty == "e":
            easy= str(int(random.randint(1, 10)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:

                    users[str(user.id)]["amc12 points"] += 4
                    users[str(user.id)]["amc12 questions solved"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions solved"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break
                
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break 

                else:

                    users[str(user.id)]["amc12 points"] -= 1.5
                    users[str(user.id)]["amc12 questions failed"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions failed"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break


        elif difficulty == "med" or difficulty == "medium" or difficulty == "m":
            med = str(int(random.randint(11,16)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    
                    users[str(user.id)]["amc12 points"] += 5.5
                    users[str(user.id)]["amc12 questions solved"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions solved"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break

                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break    
                
                else:

                    users[str(user.id)]["amc12 points"] -= 0.5
                    users[str(user.id)]["amc12 questions failed"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions failed"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break

        elif difficulty == "hard" or difficulty == "h":
            hard = str(int(random.randint(17, 25)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    
                    users[str(user.id)]["amc12 points"] += 6
                    users[str(user.id)]["amc12 questions solved"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions solved"]+=1

                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break
                
                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break

                else:
                    users[str(user.id)]["amc12 points"] -= 0.5
                    users[str(user.id)]["amc12 questions failed"]+=1
                    users[str(user.id)]["questions done"]+=1
                    users[str(user.id)]["questions failed"]+=1
                    
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break
    

    @commands.command()
    async def random(self, ctx, contest_type=None):

        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author

        emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e", "❎":"quit"}

        if contest_type == 'amc' or contest_type == 'AMC':
            
            tried = []

            def check(reaction, user):
                return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried

            while True:
                amc_id = ["10A", "12A", "10B", "12B"]
                randomcontestid = str(random.choice(amc_id))
                randomyear = str(int(random.randint(2002, 2019)))
                problem_num = str(int(random.randint(13, 25)))

                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{problem_num}/sol.txt'
                page = requests.get(url)
                sol = str((str(page.text).strip()))

                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{problem_num}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if randomcontestid == "10A" or randomcontestid == "10B":
                    if emojis[reaction.emoji] == sol:

                        users[str(user.id)]["random question points"] += 5.5
                        users[str(user.id)]["amc10 questions solved"] += 1
                        users[str(user.id)]["questions done"]+=1
                        users[str(user.id)]["questions solved"]+=1

                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        await ctx.send("Correct. You may want to check against this to get a better understanding")
                        await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{problem_num}')
                        break
                    
                    elif emojis[reaction.emoji] == "quit":
                        await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                        await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{problem_num}')
                        break

                    else:

                        users[str(user.id)]["random question points"] -= 0.5
                        users[str(user.id)]["amc10 questions failed"]+=1
                        users[str(user.id)]["questions failed"]+=1
                        users[str(user.id)]["questions done"]+=1

                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        tried.append(user.id)
                        await ctx.send("Wrong. You may want to check against this go get a better understanding")
                        await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{problem_num}')
                        break


                elif emojis[reaction.emoji] == "quit":
                    await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{problem_num}')
                    break


                else:
                    if emojis[reaction.emoji] == sol:

                        users[str(user.id)]["random question points"] += 5.5
                        users[str(user.id)]["amc12 questions solved"]+=1
                        users[str(user.id)]["questions done"]+=1
                        users[str(user.id)]["questions solved"]+=1

                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        await ctx.send("Correct. You may want to check against this to get a better understanding")
                        await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{problem_num}')
                        break

                    elif emojis[reaction.emoji] == "quit":
                        await ctx.send("Sorry to see you go. Perhaps try taking a look at this question.")
                        await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{problem_num}')
                        break

                    else:

                        users[str(user.id)]["random question points"] -= 0.5
                        users[str(user.id)]["amc12 questions failed"]+=1
                        users[str(user.id)]["questions failed"]+=1
                        users[str(user.id)]["questions done"]+=1

                        with open("mathpoints.json", "w") as f:
                            json.dump(users, f)
                        tried.append(user.id)
                        await ctx.send("Wrong. You may want to check against this go get a better understanding")
                        await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{problem_num}')
                        break

    # Ranked Question Answering
    @commands.command()
    async def stats(self, ctx):

        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author

        last5_weighted = round((last5weight*(int(users[str(user.id)]["last5 points"])))/(int(users[str(user.id)]["questions done"])), 2)
        amc10_weighted = round((amc10weight*(int(users[str(user.id)]["amc10 points"])))/(int(users[str(user.id)]["questions done"])), 2)
        amc12_weighted = round((amc12weight*(int(users[str(user.id)]["amc12 points"])))/int(users[str(user.id)]["questions done"]), 2)
        random_weighted = round((randomweight*(int(users[str(user.id)]["random question points"]))/(int(users[str(user.id)]["questions done"]))), 2)

        amc10_solved = int(users[str(user.id)]["amc10 questions solved"])
        amc10_failed = int(users[str(user.id)]["amc10 questions failed"])
        amc12_solved = int(users[str(user.id)]["amc12 questions solved"])
        amc12_failed = int(users[str(user.id)]["amc12 questions failed"])
        amc10_questions = int(users[str(user.id)]["amc10 questions"])
        amc12_questions = int(users[str(user.id)]["amc12 questions"])
        aime_questions = int(users[str(user.id)]["aime questions"])
        usamo_questions = int(users[str(user.id)]["usamo questions"])
        usajmo_questions = int(users[str(user.id)]["usajmo questions"])
        total_questions_fetched = int(users[str(user.id)]["questions done"])
        total_questions_solved = int(users[str(user.id)]["questions solved"])
        total_questions_failed = int(users[str(user.id)]["questions failed"])

        total_weighted_score = last5_weighted+amc10_weighted+amc12_weighted+random_weighted
        final_score = round(total_weighted_score, 2)

        emb = discord.Embed(title=f"{ctx.author.name}'s points", color=discord.Color.blue())
        emb.add_field(name="Problems Solved", value=f"AMC 10:`{amc10_solved}`\nAMC 12:`{amc12_solved}`\nTotal Solved:`{total_questions_solved}`")
        emb.add_field(name="Problems Fetched", value=f"AMC 10:`{amc10_questions}`\nAMC 12:`{amc12_questions}`\nAIME:`{aime_questions}`\nUSAMO:`{usamo_questions}`\nUSAJMO:`{usajmo_questions}`\n\nTotal:`{total_questions_fetched}`")
        emb.add_field(name="Problems Failed", value=f"AMC 10:`{amc10_failed}`\nAMC 12:`{amc12_failed}`\nTotal Failed:`{total_questions_failed}`")
        emb.add_field(name="Score", value=f"AMC 10:`{amc10_weighted}`\nAMC 12:`{amc12_weighted}`\n\nTotal Score:`{final_score}`")
        emb.add_field(name="Rank", value="Not a feature yet")
        await ctx.send(embed=emb)

async def open_account(self, user):
    users = await get_points_data(self)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}

        # points
        users[str(user.id)]["last5 points"] = 0
        users[str(user.id)]["amc10 points"] = 0
        users[str(user.id)]["amc12 points"] = 0
        users[str(user.id)]["random question points"] = 0

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
        users[str(user.id)]["questions done"] = 1

    with open("mathpoints.json", "w") as f:
        json.dump(users, f)

    return True

async def get_points_data(self):
    with open("mathpoints.json", "r") as f:
        users = json.load(f)
    
    return users







def setup(bot):
    bot.add_cog(Contestproblems(bot))
