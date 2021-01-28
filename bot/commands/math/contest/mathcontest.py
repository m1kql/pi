import json
import random

import discord
import requests
from discord.ext import commands

amc10weight = 0.3
amc12weight = 0.7

emojis = {"🇦": "a", "🇧": "b", "🇨": "c", "🇩": "d", "🇪": "e", "❎": "quit"}


class MathContest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Contest Math cog has been loaded sucessfully')

    # basic functions to return data

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
        users[str(user.id)]["questions done"] = 1

        with open("mathpoints.json", "w") as f:
            json.dump(users, f)

        return True

    async def get_points_data(self):
        with open("mathpoints.json", "r") as f:
            users = json.load(f)
        return users

    # send stuff function
    async def send_correct(self, requested_year, requested_id, requested_problem):
        correct_msg = "Correct. You may want to check against this to get a better understanding"
        correct_problem = f'https://artofproblemsolving.com/wiki/index.php?title={requested_year}_AMC_{requested_id}_Problems/Problem_{requested_problem}'
        return correct_msg and correct_problem

    async def send_wrong(self, requested_year, requested_id, requested_problem):
        wrong_msg = "Wrong. You may want to check against this go get a better understanding"
        wrong_problem = f'https://artofproblemsolving.com/wiki/index.php?title={requested_year}_AMC_{requested_id}_Problems/Problem_{requested_problem}'
        return wrong_msg and wrong_problem

    # Main math commands
    @commands.command()
    async def fetch(self, ctx, *, argspath=None):
        if argspath != None:
            requested_path = argspath.replace(" ", "/")
            await ctx.send()

def setup(bot):
    bot.add_cog(MathContest(bot))
