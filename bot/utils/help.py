import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog has been loaded sucessfully')

    @commands.command()
    async def help(self, ctx, arg=None):
        if arg is None:
            await ctx.send("""
            ```
            \n

            help commands
            -------
            Categories: math, code, music
            Prefix: ^

            help <category> (e.g help math)

            ```
            """)

        elif arg == 'code':
            await ctx.send("""
            ```
            \n

            Code:
            -------
            Supported Languages: ada, assembly, bash, c#, c++, c, clojure, common lisp, d, elixir, erlang, f#, fortran, go, haskell, java, javascript, kotlin, lua, node.js, ocaml, octave, obj-c, pascal, perl, php, prolog, python, python3, R, rust, ruby, scala, scheme, swift, tcl, visual basic

            run <language> <your program> (e.g run rust fn main() {let sum = 5+10; println!("{}", sum);})

            ```
            """)
            await ctx.send("would you like to go back?")
            def check(m):
                return m.author.id == ctx.author.id
            returnmsg = await self.bot.wait_for('message',check=check)
            if returnmsg.content == 'yes' or returnmsg.content=='ye' or returnmsg.content=='yee':
                await ctx.send("""
                ```
                \n
                help commands
                -------
                Categories: math, code, music
                Prefix: ^

                help <category> (e.g help math)

                ```
                """)
            else:
                await ctx.send("ok")

        elif arg == 'math':
            await ctx.send("""
            ```
            \n

            Math:
            -------
            Supported contests: AMC, AIME, USAMO, USAJMO

            fetch<contest type> <year> <id or no id> <problem number> (e.g fetchamc 2013 10a 12) - fetches a specific problem
            random <contest type> (e.g random usamo) - returns any problem from a specified contest
            last5 - returns the last 5 question of any AMC contest
            amc10 <difficulty> (e.g amc10 med) - returns an amc10 question of that difficulty 
            amc12 <difficulty> (e.g amc12 e) - returns an amc12 question of that difficulty

            ```
            """)
            await ctx.send("would you like to go back?")
            def check(m):
                return m.author.id == ctx.author.id
            returnmsg = await self.bot.wait_for('message',check=check)
            if returnmsg.content == 'yes' or returnmsg.content=='ye' or returnmsg.content=='yee':
                await ctx.send("""
                ```
                \n
                help commands
                -------
                Categories: math, code, music
                Prefix: ^

                help <category> (e.g help math)

                ```
                """)
            else:
                await ctx.send("ok")
    
def setup(bot):
    bot.add_cog(Help(bot))
