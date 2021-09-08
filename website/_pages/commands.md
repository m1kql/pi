---
layout: page
title: Commands
include_in_header: true
---

## Commands

Prefix: `=`

<u>Basic Commands</u>
<br>

| Command  | Has Arguments | Arguments             | Expected Output                                                                          |
| -------- | ------------- | --------------------- | ---------------------------------------------------------------------------------------- |
| `=hello` | No            |                       | `Hello, World!`                                                                          |
| `=help`  | Yes           | `bot`, `math`, `misc` | An embed showing the arguments you can pass to it to learn more about the other commands |

<u>Bot</u>
<br>

| Command   | Has Arguments | Arguments | Expected Output                                                  |
| --------- | ------------- | --------- | ---------------------------------------------------------------- |
| `=invite` | No            |           | Gives invite links to the support server and for the bot         |
| `=info`   | No            |           | Gives info about this bot and other other techinical information |

<u>Math</u>
<br>

| Command        | Has Arguments | Arguments                                                 | Expected Output                                                                                               |
| -------------- | ------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `=statistics`  | Yes           | `@user`, `user_id`                                        | Gives an embed showing your statistics (if you leave the arguments blank) or someone else's statistics        |
| `=tex`         | Yes           | `tex statement`                                           | Returns a rendered LaTeX statement                                                                            |
| `=amc10`       | Yes           | `easy`, `medium`, `hard`                                  | Gives an AMC10 problem of the selected difficulty                                                             |
| `=amc12`       | Yes           | `easy`, `medium`, `hard`                                  | Gives an AMC12 problem of the selected difficulty                                                             |
| `=fetch`       | Yes           | `contest_name year [contest id, optional] problem_number` | Fetches a problem from the specified path                                                                     |
| `=last5`       | Yes           | `contest_name`                                            | Returns the last 5 questions from a specified contest                                                         |
| `=random`      | No            |                                                           | Returns a random problem                                                                                      |
| `=leaderboard` | Yes           | `amount of users`                                         | Shows the leaderboard for the server with a specified amount of users. If it is not given, the default is 10. |

<u>Miscellaneous</u>
<br>

| Command    | Has Arguments | Arguments         | Expected Output                                                                            |
| ---------- | ------------- | ----------------- | ------------------------------------------------------------------------------------------ |
| `=suggest` | Yes           | `your message`    | Allows you to make a feature suggestion or any suggestion. Needs you to complete a captcha |
| `=report`  | Yes           | `your message`    | Allows you to make a bug report or any report on an issue. Needs you to complete a captcha |
| `=runcode` | Yes           | `language` `code` | Runs code from different languages.                                                        |

<br>
<br>
<hr>

<button class="button is-large"><a href="{{ site.base_url }}/">Go back</a></button>