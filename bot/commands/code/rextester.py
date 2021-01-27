import json
import urllib.error
import urllib.parse
import urllib.request

import discord
from discord.ext import commands


class Code(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print('Code runner cog has been loaded sucessfully')

    @commands.command(aliases=["run"])
    async def runcode(self, ctx, lang=None, *, args=None):
        author = ctx.message.author

        # C++ (gcc)
        if lang == 'c++' and args != None:

            # sends data to rextester.com
            # rextester requires it to be formatted this way more info -> (https://rextester.com/main)
            api_url = 'https://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': 7,
                'Program': args,
                'Input': "",
                'CompilerArgs': "-o a.out source_file.cpp",
            })

            # supplying values
            pdbytes = str.encode(postdata)
            request = urllib.request.Request(api_url, pdbytes)
            response = urllib.request.urlopen(request)
            output = response.read()

            # decode json strings
            response_decoded = json.loads(output)
            comp_warnings = response_decoded["Warnings"]
            comp_errors = response_decoded["Errors"]
            comp_results = response_decoded["Result"]
            comp_status = response_decoded["Stats"]

            # displays the status of the compilation
            emb = discord.Embed(title="Running code", color=0x6b0080)
            emb.add_field(name="Called by: ", value="{}".format(author))
            emb.add_field(name="Compilation Warnings: ",
                          value="```{}```".format(comp_warnings), inline=False)
            emb.add_field(name="Compilation Errors: ",
                          value="```{}```".format(comp_errors), inline=False)
            emb.add_field(name="Compilation Status: ",
                          value="```{}```".format(comp_status), inline=False)
            emb.add_field(name="Compilation Results: ",
                          value="```{}```".format(comp_results), inline=False)
            emb.set_footer(text="Running using the rextester api")

            try:
                await ctx.send(embed=emb)
            except:
                await ctx.send("Sorry there was an error processing this command")

        # Haskell
        elif lang == 'haskell' and args != None:
            # sends data to rextester.com
            # rextester requires it to be formatted this way more info -> (https://rextester.com/main)
            api_url = 'https://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': 11,
                'Program': args,
                'Input': "",
                'CompilerArgs': "-o a.out source_file.hs",
            })

            # supplying values
            pdbytes = str.encode(postdata)
            request = urllib.request.Request(api_url, pdbytes)
            response = urllib.request.urlopen(request)
            output = response.read()

            # decode json strings
            response_decoded = json.loads(output)
            comp_warnings = response_decoded["Warnings"]
            comp_errors = response_decoded["Errors"]
            comp_results = response_decoded["Result"]
            comp_status = response_decoded["Stats"]

            # displays the status of the compilation
            emb = discord.Embed(title="Running code", color=0x6b0080)
            emb.add_field(name="Called by: ", value="{}".format(author))
            emb.add_field(name="Compilation Warnings: ",
                          value="```{}```".format(comp_warnings), inline=False)
            emb.add_field(name="Compilation Errors: ",
                          value="```{}```".format(comp_errors), inline=False)
            emb.add_field(name="Compilation Status: ",
                          value="```{}```".format(comp_status), inline=False)
            emb.add_field(name="Compilation Results: ",
                          value="```{}```".format(comp_results), inline=False)
            emb.set_footer(text="Running using the rextester api")

            try:
                await ctx.send(embed=emb)
            except:
                await ctx.send("Sorry there was an error processing this command")

        # Go
        elif lang == 'go' and args != None:
            # sends data to rextester.com
            # rextester requires it to be formatted this way more info -> (https://rextester.com/main)
            api_url = 'https://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': 20,
                'Program': args,
                'Input': "",
                'CompilerArgs': "-o a.out source_file.go",
            })

            # supplying values
            pdbytes = str.encode(postdata)
            request = urllib.request.Request(api_url, pdbytes)
            response = urllib.request.urlopen(request)
            output = response.read()

            # decode json strings
            response_decoded = json.loads(output)
            comp_warnings = response_decoded["Warnings"]
            comp_errors = response_decoded["Errors"]
            comp_results = response_decoded["Result"]
            comp_status = response_decoded["Stats"]

            # displays the status of the compilation
            emb = discord.Embed(title="Running code", color=0x6b0080)
            emb.add_field(name="Called by: ", value="{}".format(author))
            emb.add_field(name="Compilation Warnings: ",
                          value="```{}```".format(comp_warnings), inline=False)
            emb.add_field(name="Compilation Errors: ",
                          value="```{}```".format(comp_errors), inline=False)
            emb.add_field(name="Compilation Status: ",
                          value="```{}```".format(comp_status), inline=False)
            emb.add_field(name="Compilation Results: ",
                          value="```{}```".format(comp_results), inline=False)
            emb.set_footer(text="Running using the rextester api")

            try:
                await ctx.send(embed=emb)
            except:
                await ctx.send("Sorry there was an error processing this command")

        # C (gcc)
        elif lang == 'c' and args != None:
            # sends data to rextester.com
            # rextester requires it to be formatted this way more info -> (https://rextester.com/main)
            api_url = 'https://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': 6,
                'Program': args,
                'Input': "",
                'CompilerArgs': "-o a.out source_file.c",
            })

            # supplying values
            pdbytes = str.encode(postdata)
            request = urllib.request.Request(api_url, pdbytes)
            response = urllib.request.urlopen(request)
            output = response.read()

            # decode json strings
            response_decoded = json.loads(output)
            comp_warnings = response_decoded["Warnings"]
            comp_errors = response_decoded["Errors"]
            comp_results = response_decoded["Result"]
            comp_status = response_decoded["Stats"]

            # displays the status of the compilation
            emb = discord.Embed(title="Running code", color=0x6b0080)
            emb.add_field(name="Called by: ", value="{}".format(author))
            emb.add_field(name="Compilation Warnings: ",
                          value="```{}```".format(comp_warnings), inline=False)
            emb.add_field(name="Compilation Errors: ",
                          value="```{}```".format(comp_errors), inline=False)
            emb.add_field(name="Compilation Status: ",
                          value="```{}```".format(comp_status), inline=False)
            emb.add_field(name="Compilation Results: ",
                          value="```{}```".format(comp_results), inline=False)
            emb.set_footer(text="Running using the rextester api")

            try:
                await ctx.send(embed=emb)
            except:
                await ctx.send("Sorry there was an error processing this command")

        # D
        elif lang == 'd' and args != None:
            # sends data to rextester.com
            # rextester requires it to be formatted this way more info -> (https://rextester.com/main)
            api_url = 'https://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': 30,
                'Program': args,
                'Input': "",
                'CompilerArgs': "source_file.d -ofa.out",
            })

            # supplying values
            pdbytes = str.encode(postdata)
            request = urllib.request.Request(api_url, pdbytes)
            response = urllib.request.urlopen(request)
            output = response.read()

            # decode json strings
            response_decoded = json.loads(output)
            comp_warnings = response_decoded["Warnings"]
            comp_errors = response_decoded["Errors"]
            comp_results = response_decoded["Result"]
            comp_status = response_decoded["Stats"]

            # displays the status of the compilation
            emb = discord.Embed(title="Running code", color=0x6b0080)
            emb.add_field(name="Called by: ", value="{}".format(author))
            emb.add_field(name="Compilation Warnings: ",
                          value="```{}```".format(comp_warnings), inline=False)
            emb.add_field(name="Compilation Errors: ",
                          value="```{}```".format(comp_errors), inline=False)
            emb.add_field(name="Compilation Status: ",
                          value="```{}```".format(comp_status), inline=False)
            emb.add_field(name="Compilation Results: ",
                          value="```{}```".format(comp_results), inline=False)
            emb.set_footer(text="Running using the rextester api")

            try:
                await ctx.send(embed=emb)
            except:
                await ctx.send("Sorry there was an error processing this command")

        elif (lang == 'ada' or lang == 'assembly' or lang == 'bash' or lang == 'c#' or lang == 'clojure' or lang == 'lisp' or lang == 'elixir' or lang == 'erlang' or lang == 'f#' or lang == 'fortran' or lang == 'java' or lang == 'javascript' or lang == 'kotlin' or lang == 'lua' or lang == 'ocaml' or lang == 'octave' or lang == 'perl' or lang == 'php' or lang == 'prolog' or lang == 'python' or lang == 'python3' or lang == 'rust' or lang == 'r' or lang == 'ruby' or lang == 'scala' or lang == 'scheme' or lang == 'swift' or lang == 'tcl' or lang == 'vb') and args != None:
            # sends data to rextester.com
            # rextester requires it to be formatted this way more info -> (https://rextester.com/main)
            api_url = 'https://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': lang,
                'Program': args,
                'Input': "",
                'CompilerArgs': "",
            })

            # supplying values
            pdbytes = str.encode(postdata)
            request = urllib.request.Request(api_url, pdbytes)
            response = urllib.request.urlopen(request)
            output = response.read()

            # decode json strings
            response_decoded = json.loads(output)
            comp_warnings = response_decoded["Warnings"]
            comp_errors = response_decoded["Errors"]
            comp_results = response_decoded["Result"]
            comp_status = response_decoded["Stats"]

            # displays the status of the compilation
            emb = discord.Embed(title="Running code", color=0x6b0080)
            emb.add_field(name="Called by: ", value="{}".format(author))
            emb.add_field(name="Compilation Warnings: ",
                          value="```{}```".format(comp_warnings), inline=False)
            emb.add_field(name="Compilation Errors: ",
                          value="```{}```".format(comp_errors), inline=False)
            emb.add_field(name="Compilation Status: ",
                          value="```{}```".format(comp_status), inline=False)
            emb.add_field(name="Compilation Results: ",
                          value="```{}```".format(comp_results), inline=False)
            emb.set_footer(text="Running using the rextester api")

            try:
                await ctx.send(embed=emb)
            except:
                await ctx.send("Sorry there was an error processing this command")


def setup(bot):
    bot.add_cog(Code(bot))
