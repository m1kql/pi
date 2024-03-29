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
    "description": "Report a bug, or something that's not going right with the bot.",
    "usage_name": "Usage",
    "usage_description": "`=report <an issue with this bot>`",
    "alias_name": "Aliases",
    "alias_description": "No aliases",
    "usage_syntax_name": "Usage syntax",
    "usage_syntax": "<required> [optional]",
    "footer": "Remember to omit < > and [ ] when giving commands",
}

captchas = [
    "qr8g",
    "rg9q",
    "rg3q",
    "ga2q",
    "rg4h",
]

load_dotenv()
bug_channel = os.getenv("bug_channel")
feature_channel = os.getenv("feature_channel")


class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print("Report cog has been loaded sucessfully")

    @commands.command()
    @commands.cooldown(2, 43200, commands.BucketType.user)
    async def suggest(self, ctx, *, message):
        random_captcha = random.randint(0, 5)
        image_dimensions = ImageCaptcha(width=280, height=90)
        data = image_dimensions.generate(captchas[random_captcha])  # noqa F841
        image_dimensions.write(
            str(captchas[random_captcha]), "bot/src/cogs/misc/captcha.png"
        )
        captcha_answer = str(captchas[random_captcha])
        await ctx.send(file=discord.File("bot/src/cogs/misc/captcha.png"))

        answer = await self.bot.wait_for(  # noqa F841
            "message",
            check=(
                lambda answer: answer.content == captcha_answer
                and answer.author == ctx.author
            ),
        )
        channel = await self.bot.fetch_channel(feature_channel)
        await ctx.send("Correct CAPTCHA submission.")
        await channel.send(
            f"Suggestion from: `{ctx.author.name}` with id: `{ctx.author.id}`\nMessage:\n```{message}```"  # noqa E501
        )
        await ctx.send("Successfully sent your suggestion! Have a nice day.")

    @commands.command()
    @commands.cooldown(2, 43200, commands.BucketType.user)
    async def report(self, ctx, *, message):
        random_captcha = random.randint(0, 5)
        image_dimensions = ImageCaptcha(width=280, height=90)
        data = image_dimensions.generate(captchas[random_captcha])  # noqa F841
        image_dimensions.write(
            str(captchas[random_captcha]), "bot/src/cogs/misc/captcha.png"
        )
        captcha_answer = str(captchas[random_captcha])
        await ctx.send(file=discord.File("bot/src/cogs/misc/captcha.png"))
        answer = await self.bot.wait_for(  # noqa F841
            "message",
            check=(
                lambda answer: answer.content == captcha_answer
                and answer.author == ctx.author
            ),
        )
        channel = await self.bot.fetch_channel(bug_channel)
        await ctx.send("Correct CAPTCHA submission.")
        await channel.send(
            f"Bug report from: `{ctx.author.name}` with id: `{ctx.author.id}`\nMessage:\n```{message}```"  # noqa E501
        )
        await ctx.send("Successfully sent your report! Have a nice day.")

    @report.error
    async def report_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                "Slow down there bud, there can't be that many problems with this bot! Maybe tell us about it 12 hours later eh?"
            )

    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                "Slow down there bud, we'd love to hear your suggestions, but we're a bit pre-occupied at the moment. Come back at another time eh? Perhaps 12 hours later?"
            )


def setup(bot):
    bot.add_cog(Report(bot))
