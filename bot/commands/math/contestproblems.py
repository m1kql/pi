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
    async def fetch(self, ctx, contest_type=None, year=None, contest_id=None, problem_num=None):
        if contest_type != None:
            requested_contest = str(contest_type.upper())
        if year != None:
            requested_year = str(year)
        if contest_id != None:
            requested_id = str(contest_id.upper())
        if problem_num != None:
            requested_problem = str(problem_num)
        try:
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/pi/master/bot/{requested_contest}/{requested_year}/{requested_id}/{requested_problem}/statement.png')
        except:
            await ctx.send("Sorry there was an error processing this command")

    @commands.command()
    async def last5(self, ctx):
        contestid = ["10A", "10B", "12A", "12B"]
        lastfive = str(int(random.randint(20, 25)))
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(contestid))
        try:
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/pi/master/bot/AMC/{randomyear}/{randomcontestid}/{lastfive}/statement.png')
        except:
            await ctx.send("Sorry there was an error processing this command")

    @commands.command()
    async def amc10(self, ctx, difficulty):
        amc10_id = ["10A", "10B"]
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(amc10_id))

        if difficulty == "easy" or difficulty == "e":
            easy= str(int(random.randint(1, 10)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/pi/master/bot/AMC/{randomyear}/{randomcontestid}/{easy}/statement.png')
        elif difficulty == "med" or difficulty == "medium" or difficulty == "m":
            med = str(int(random.randint(11,16)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/pi/master/bot/AMC/{randomyear}/{randomcontestid}/{med}/statement.png')
        elif difficulty == "hard" or difficulty == "h":
            hard = str(int(random.randint(17, 25)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/pi/master/bot/AMC/{randomyear}/{randomcontestid}/{hard}/statement.png')
            

def setup(bot):
    bot.add_cog(Contestproblems(bot))
