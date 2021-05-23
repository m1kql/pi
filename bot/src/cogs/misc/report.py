from PIL.Image import Image
import discord
from discord.ext import commands
from captcha.image import ImageCaptcha
import random
import os
from dotenv import load_dotenv

# suggest_help
suggest_help = {
    "name": "=suggest help info",
    "description_name": "Description",
    "description": "Suggest a feature or more contests we should add",
    "usage_name": "Usage",
    "usage_description": "`=suggest <your suggestion>`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

# report_help
report_help = {
    "name": "=report help info",
    "description_name": "Description",
    "description": "Get the report link",
    "usage_name": "Usage",
    "usage_description": "`=report <an issue with this bot>`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

captchas = [
    "hello17world",
    "126discord",
    "Erp21J",
    "0Odqrs",
    "28Hf0S",
    "02jdm",
    "02mciUD7",
    "9Dkru72Q",
    "81JdiU7W",
    "edjewUE",
    "932JDE",
    "9999o",
    "01LOdem",
    "e9DJem3S",
    "ZZxts9W73",
    "dxZIW3x",
]

load_dotenv()
bug_channel = int(os.getenv("bug_channel"))
feature_channel = int(os.getenv("feature_channel"))


class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Report cog has been loaded sucessfully")

    @commands.command()
    async def suggest(self, ctx, *, message):
        random_captcha = random.randint(0, 17)
        image_dimensions = ImageCaptcha(width=280, height=90)
        data = image_dimensions.generate(captchas[random_captcha])
        image_dimensions.write(
            str(captchas[random_captcha]), "bot/src/cogs/misc/captcha.png"
        )
        captcha_answer = str(captchas[random_captcha])
        await ctx.send(file=discord.File("bot/src/cogs/misc/captcha.png"))

        async def check_answer(answer):
            if answer.content == captcha_answer and answer.author == ctx.author:
                return True
            else:
                return False

        answer = await self.bot.wait_for("message", check=check_answer)
        channel = await self.bot.fetch_channel(feature_channel)
        await ctx.send("Correct CAPTCHA submission.")
        await channel.send(
            f"Suggestion from: `{ctx.author.name}` with id: `{ctx.author.id}`\nMessage:\n```{message}```"
        )
        await ctx.send("Successfully sent your suggestion! Have a nice day.")

    @commands.command()
    async def report(self, ctx, *, message):
        random_captcha = random.randint(0, 17)
        image_dimensions = ImageCaptcha(width=280, height=90)
        data = image_dimensions.generate(captchas[random_captcha])
        image_dimensions.write(
            str(captchas[random_captcha]), "bot/src/cogs/misc/captcha.png"
        )
        captcha_answer = str(captchas[random_captcha])
        await ctx.send(file=discord.File("bot/src/cogs/misc/captcha.png"))

        async def check_answer(answer):
            if answer.content == captcha_answer and answer.author == ctx.author:
                return True
            else:
                return False

        answer = await self.bot.wait_for("message", check=check_answer)
        channel = await self.bot.fetch_channel(bug_channel)
        await ctx.send("Correct CAPTCHA submission.")
        await channel.send(
            f"Bug report from: `{ctx.author.name}` with id: `{ctx.author.id}`\nMessage:\n```{message}```"
        )
        await ctx.send("Successfully sent your report! Have a nice day.")


def setup(bot):
    bot.add_cog(Report(bot))
