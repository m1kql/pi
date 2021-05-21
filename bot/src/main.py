import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="=")

load_dotenv()
token = os.getenv("token")


@bot.event
async def on_ready():
    print("Hello World!")
    print(f"Username: {bot.user.name} | Logged in successfully")
    activity = discord.Activity(
        type=discord.ActivityType.playing, name="Type =help for usage"
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, World!")

bot.run(token)
