import discord

code_help="""
            ```
            \n

            Code:
            -------
            Supported Languages: ada, assembly, bash, c#, c++, c, clojure, common lisp, d, elixir, erlang, f#, fortran, go, haskell, java, javascript, kotlin, lua, node.js, ocaml, octave, obj-c, pascal, perl, php, prolog, python, python3, R, rust, ruby, scala, scheme, swift, tcl, visual basic

            run <language> <your program> (e.g run rust fn main() {let sum = 5+10; println!("{}", sum);})

            ```
            """


default_help="""
            ```
            \n

            help commands
            -------
            Categories: math, code, music
            Prefix: ^

            help <category> (e.g help math)

            ```
            """


math_help="""
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
            """


goback="would you like to go back?"

invite="https://discord.com/api/oauth2/authorize?client_id=799423483968618566&permissions=0&scope=bot"
