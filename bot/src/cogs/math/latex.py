import urllib.request
import discord
from discord.ext import commands


class LaTeX(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("LaTeX cog has been loaded sucessfully")

    @commands.command(aliases=["tex", "LaTeX", "latexify", "totex"])
    async def latex(self, ctx, *, tex=None,):
        if tex != None:
            formatted_tex = tex.strip().replace(' ','%20')
            target_url = (
                f"https://latex.codecogs.com/png.latex?\\dpi{{300}}\\bg_black%20{formatted_tex}"
            )
            urllib.request.urlretrieve(target_url, "latex.png")
            await ctx.send(file=discord.File("latex.png"))
        else:
            pass


def setup(bot):
    bot.add_cog(LaTeX(bot))
