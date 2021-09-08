import discord
from pyston import PystonClient
from discord.ext import commands


# code help
code_help = {
    "name": "=runcode help info",
    "description_name": "Description",
    "description": "Execute code from a code block",
    "usage_name": "Usage",
    "usage_description": '`=run <language> <your code>`\nDo not put the language in the code block.\nIn addition for Java, declare a class.\n\n__Example__:\n=run python\n```def hello_world(n):\n    for i in range(n):\n        print("Hello, World")\n\nhello_world(5)```',
    "alias_name": "Aliases",
    "alias_description": "`run`, `code`, `program`",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}


class Code(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Code cog has been loaded sucessfully")

    @commands.command(aliases=["run", "code", "program"])
    async def runcode(self, ctx, lang=None, *, source=None):

        parsed_source = source.replace("```", "")

        language = lang

        if not source:
            raise commands.BadArgument("No source code found")

        client = PystonClient()
        output = await client.execute(language=f"{language}", code=f"{parsed_source}")

        response_output = output.output

        code_embed = discord.Embed(
            title=f"Execution of code called by {ctx.author}",
            description=f"**Output:**\n```{response_output}```",
            color=0xA4D0DA,
        )

        await ctx.send(embed=code_embed)


def setup(bot):
    bot.add_cog(Code(bot))
