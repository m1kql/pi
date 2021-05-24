<div align="center">
  <img src="./Pi.png" alt="" width="256">
  <br>
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/yak-fumblepack/pi/Build?style=plastic">
  <img src="https://img.shields.io/github/license/yak-fumblepack/pi?style=plastic" alt="">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=plastic" alt="">
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
- [Getting Started](#getting-started)
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

Have fun!

### Docker

Prerequisites:
- Docker
- Docker Compose

To run both the bot:

```shell
$ sudo docker pull yakfumblepack/pi
$ sudo docker-compose up --build
```

Running it from the git repo:

```shell
$ sudo docker-compose up --build pi-bot
```

To run them invididually using separate images, refer to their respective readmes:
- [The bot](https://github.com/yak-fumblepack/pi/tree/rewrite/bot)

## Commands

Default prefix: `=`

<u>Basic Commands</u>
<br>
| Command | Has parameters | Expected Output |
| --- | --- | --- | 
| `=hello` | No | `Hello, World!` |

## Contributing

Features, bugfixes, issues are all greatly appreciated. Please, if you do encounter a bug report it to us by opening an issue or even better, fix it yourself and make a pull request!

Note: Since we are undergoing a rewrite, please make pull requests against the `rewrite` branch of this repo.

## License
This project is licensed under the [GNU AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.txt) license.