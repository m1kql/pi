import os

from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="$")

load_dotenv()
token = os.getenv("token")


@bot.event
async def on_ready():
    print("Hello World!")


@bot.command()
async def sudo(ctx):
    await ctx.send("sudo dnf -y update")


bot.run(token)
