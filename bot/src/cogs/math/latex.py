import urllib.request
import discord
from discord.ext import commands


# latex help
latex_help = {
    "name": "=latex help info",
    "description_name": "Description",
    "description": "Render a LaTeX equation. Only inline math is supported at the moment.",
    "usage_name": "Usage",
    "usage_description": "`=latex <your equation>`",
    "alias_name": "Aliases",
    "alias_description": "`tex`, `LaTeX`, `latexify`, `totex`",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}


class LaTeX(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("LaTeX cog has been loaded sucessfully")

    @commands.command(aliases=["tex", "LaTeX", "latexify", "totex"])
    async def latex(
        self,
        ctx,
        *,
        tex=None,
    ):
        if tex is not None:
            formatted_tex = tex.strip().replace(" ", "%20")
            target_url = f"https://latex.codecogs.com/png.latex?\\dpi{{300}}\\bg_black%20{formatted_tex}"
            urllib.request.urlretrieve(target_url, "latex.png")
            await ctx.send(file=discord.File("latex.png"))
        else:
            pass


def setup(bot):
    bot.add_cog(LaTeX(bot))
