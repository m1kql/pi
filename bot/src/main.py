import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="=", intents=intents, help_command=None)

load_dotenv()
token = os.getenv("token")

cogs = [
    "cogs.math.latex",
    "cogs.math.contest_problems",
    "cogs.math.stats",
    "cogs.misc.help",
    "cogs.misc.info",
    "cogs.misc.report",
]


@bot.event
async def on_ready():
    print("Hello World!")
    print(f"Username: {bot.user.name} | Logged in successfully")
    activity = discord.Activity(
        type=discord.ActivityType.playing, name="Type =help for usage"
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)


for cog in cogs:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f"Could not load cog {cog}: {str(e)}")

# load and unload cogs for modularity purposes
@bot.command()
@commands.is_owner()
async def loadcog(ctx, cogname=None):
    if cogname == None:
        return
    try:
        bot.load_extension(cogname)
    except Exception as e:
        print(f"Could not load cog {cogname}: {str(e)}")
        await ctx.send(f"Could not load cog {cogname}: {str(e)}")
    else:
        print(f"Loaded cog: {cogname} sucessfully")
        await ctx.send(f"Loaded cog: {cogname} sucessfully")


@bot.command()
@commands.is_owner()
async def unloadcog(ctx, cogname=None):
    if cogname == None:
        return
    try:
        bot.unload_extension(cogname)
    except Exception as e:
        print(f"Could not unload cog {cogname}: {str(e)}")
        await ctx.send(f"Could not unload cog {cogname}: {str(e)}")
    else:
        print(f"Unloaded cog: {cogname} sucessfully")
        await ctx.send(f"Unloaded cog: {cogname} sucessfully")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, World!")


bot.run(token)
