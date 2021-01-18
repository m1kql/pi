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
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/pi/master/bot/{requested_contest}/{requested_year}/{contest_id}/{requested_problem}/statement.png')
        except:
            await ctx.send("Sorry there was an error processing this command")

def setup(bot):
    bot.add_cog(Contestproblems(bot))