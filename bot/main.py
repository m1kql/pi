import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# basic settings
load_dotenv()
token = os.getenv("token")
bot = commands.Bot(command_prefix="/", help_command=None)

cogs = [
    'commands.code.rextester',
    'commands.math.contestproblems',
]

for cog in cogs:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f'Could not load cog {cog}: {str(e)}')

@bot.event
async def on_ready():
    print('Bot is running')
    print(f'Logged in as {bot.user.name}')

# load and unload cogs for modularity purposes 
@bot.command()
@commands.is_owner()
async def loadcog(ctx, cogname=None):
    if cogname == None:
        return
    try:
        bot.load_extension(cogname)
    except Exception as e:
        print(f'Could not load cog {cogname}: {str(e)}')
        await ctx.send(f'Could not load cog {cogname}: {str(e)}')
    else: 
        print(f'Loaded cog: {cogname} sucessfully')
        await ctx.send(f'Loaded cog: {cogname} sucessfully')

@bot.command()
@commands.is_owner()
async def unloadcog(ctx, cogname=None):
    if cogname == None:
        return
    try:
        bot.unload_extension(cogname)
    except Exception as e:
        print(f'Could not unload cog {cogname}: {str(e)}')
        await ctx.send(f'Could not unload cog {cogname}: {str(e)}')
    else: 
        print(f'Unloaded cog: {cogname} sucessfully')
        await ctx.send(f'Unloaded cog: {cogname} sucessfully')

@bot.command(aliases=["killswitch", "kill"])
@commands.is_owner()
async def clearinstances(ctx):
    if ctx.message.author.id == int(os.getenv("myid")):
        print("called by owner, shutting down")
        await ctx.send("called by owner, shutting down")
        try: 
            await bot.logout()
            print("sucessfully disconnected")
        except:
            print("EnvironmentError")
            bot.clear()
    else:
        await ctx.send("you don't own this bot")

bot.run(token)

