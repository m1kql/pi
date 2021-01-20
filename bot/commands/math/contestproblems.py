import random

import discord
from discord.ext import commands

class Contestproblems(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Contest Math cog has been loaded sucessfully')

    @commands.command()
    async def fetchamc(self, ctx, year=None, contest_id=None, problem_num=None):
        if year != None and problem_num != None and contest_id != None:
            requested_year = str(year)
            requested_id = str(contest_id.upper())
            requested_problem = str(problem_num)
            try:
                await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{requested_year}/{requested_id}/{requested_problem}/statement.png')
            except:
                await ctx.send("Sorry there was an error processing this command")
    
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
        contestid = ["10A", "10B", "12A", "12B"]
        lastfive = str(int(random.randint(20, 25)))
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(contestid))
        try:
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{lastfive}/statement.png')
        except:
            await ctx.send("Sorry there was an error processing this command")

    @commands.command()
    async def amc10(self, ctx, difficulty):
        amc10_id = ["10A", "10B"]
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(amc10_id))

        if difficulty == "easy" or difficulty == "e":
            easy= str(int(random.randint(1, 10)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/statement.png')
        elif difficulty == "med" or difficulty == "medium" or difficulty == "m":
            med = str(int(random.randint(11,16)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/statement.png')
        elif difficulty == "hard" or difficulty == "h":
            hard = str(int(random.randint(17, 25)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/statement.png')

    @commands.command()
    async def amc12(self, ctx, difficulty):
        amc12_id = ["12A", "12B"]
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(amc12_id))

        if difficulty == "easy" or difficulty == "e":
            easy= str(int(random.randint(1, 10)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/statement.png')
        elif difficulty == "med" or difficulty == "medium" or difficulty == "m":
            med = str(int(random.randint(11,16)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/statement.png')
        elif difficulty == "hard" or difficulty == "h":
            hard = str(int(random.randint(17, 25)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/statement.png')
    
    @commands.command()
    async def random(self, ctx, contest_type=None):
        if contest_type == 'amc' or contest_type == 'AMC':
            amc_id = ["10A", "12A", "12A", "12B"]
            randomcontestid = str(random.choice(amc_id))
            randomyear = str(int(random.randint(2002, 2019)))
            problem_num = str(int(random.randint(1, 25)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{problem_num}/statement.png')
        if contest_type == 'aime' or contest_type == 'AIME':
            randomyear = str(int(random.randint(2000, 2019)))
            contest_id = str(int(random.randint(1,2)))
            problem_num = str(int(random.randint(1, 15)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AIME/{randomyear}/{contest_id}/{problem_num}/statement.png')

def setup(bot):
    bot.add_cog(Contestproblems(bot))
