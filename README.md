<div align="center">
  <img src="./Pi.png" alt="" width="256">
  <br>
  <br>
</div>

<div>
<img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/yak-fumblepack/pi/Build?logo=github&logoColor=lightgrey&style=plastic"> 
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/yak-fumblepack/pi?style=plastic">
<img alt="GitHub" src="https://img.shields.io/github/license/yak-fumblepack/pi?style=plastic">
<a href="https://discord.com/api/oauth2/authorize?client_id=842500814625832990&permissions=0&scope=bot"><img src="https://img.shields.io/badge/Invite-7289DA?style=plastic&logo=discord&logoColor=white" alt="Invite the bot to your discord server"></a>
</div>

## Overview

Pi is a discord bot for those interested in contest math to practice their skills while engaging in a casual conversation with their fellow mathematicians or friends. 

Some features include: 

- Ability to fetch problems from USAMO, USAJMO, AIME, AMC 10 & 12
- Fully rendered problems (using LaTeX) with solution links
- Robust points system to promote healthy competition
- Extensible core module, simply make a pull request with your cog and we can add it in without a problem!

Note: It would be preferred if you do not host your own instance of this bot

### Table of contents
- [Overview](#overview)
  - [Table of contents](#table-of-contents)
- [Getting Started](#getting-started)
  - [Python venv](#python-venv)
  - [Docker](#docker)
  - [Setup](#setup)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Python venv

Make a virtual environment

```shell
$ mkdir bot && cd bot
$ python -m venv venv
$ source venv/bin/activate
```

Clone the repo

```shell
$ git clone https://github.com/yak-fumblepack/pi.git
$ cd pi
$ pip install -U -r requirements.txt
```

Add your token to the environmental variable file (`.env`). Make sure you are in the project's root directory.

```shell
$ echo "token=<your token without spaces and without the arrow brackets>" > .env
```

Change directory and run the bot.

```shell
$ cd bot/src/
$ python main.py
```

### Docker

Prerequisites:
- Docker
- Docker Compose

To run the bot:

```shell
$ git clone https://github.com/yak-fumblepack/pi.git
$ sudo docker-compose up --build
```

Or if you don't have docker compose, build the image and run it. For more info, refer to their respective readmes:
- [The bot](https://github.com/yak-fumblepack/pi/tree/rewrite/bot)


### Setup 

This bot uses firebase as the database service. 

Set up the `.env` like so (if you would like to run it using firebase):

```
token=<your token>
bug_channel=<channel id>
feature_channel=<channel id>
firebase_type=
firebase_project_id=
firebase_private_key_id=
firebase_private_key=
firebase_client_email=
firebase_client_id=
firebase_auth_uri=
firebase_token_uri=
firebase_auth_provider_x509_cert_url=
firebase_client_x509_cert_url=
```

Rememeber to omit the < >. There is no space as well.

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
| `=cmo`         | No            |                                                           | Gives you a random CMO problem.                                                                               |
| `=aime`        | No            |                                                           | Gives you a random AIME I or II problem.                                                                      |
| `=fetch`       | Yes           | `contest_name year [contest id, optional] problem_number` | Fetches a problem from the specified path                                                                     |
| `=last5`       | Yes           | `contest_name`                                            | Returns the last 5 questions from a specified contest                                                         |
| `=random`      | No            |                                                           | Returns a random problem                                                                                      |
| `=leaderboard` | Yes           | `amount of users`                                         | Shows the leaderboard for the server with a specified amount of users. If it is not given, the default is 10. |

<u>Miscellaneous</u>
<br>
| Command    | Has Arguments | Arguments                          | Expected Output                                                                            |
| ---------- | ------------- | ---------------------------------- | ------------------------------------------------------------------------------------------ |
| `=suggest` | Yes           | `your message`                     | Allows you to make a feature suggestion or any suggestion. Needs you to complete a captcha |
| `=report`  | Yes           | `your message`                     | Allows you to make a bug report or any report on an issue. Needs you to complete a captcha |
| `=runcode` | Yes           | `language` `code` `file extension` | Runs code from different languages.                                                        |

## Contributing

Features, bugfixes, issues are all greatly appreciated. Please, if you do encounter a bug, report it to us by opening an issue or even better, fix it yourself and make a pull request! 

Please open a pull request or an issue on the `dev` branch.

## License
This project is licensed under the [GNU AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.txt) license.