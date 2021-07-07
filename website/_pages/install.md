---
layout: page
title: Installation and Contributing
include_in_header: true
---

### ToC
- <a href="#getting-started" target="_self">Getting Started</a>
- <a href="#contributing" target="_self">Contributing</a>
- <a href="#license" target="_self">License</a>

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
- [The bot](https://github.com/yak-fumblepack/pi/tree/master/bot)


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

## Contributing

Features, bugfixes, issues are all greatly appreciated. Please, if you do encounter a bug, report it to us by opening an issue or even better, fix it yourself and make a pull request! 

Please open a pull request or an issue on the `dev` branch.

## License
This project is licensed under the [GNU AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.txt) license.

<hr>

<button class="button is-large"><a href="{{ site.base_url }}/">Go back</a></button>