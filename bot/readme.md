## Building with docker

This is for building the bot **only**:

```shell
$ git clone git@github.com:yak-fumblepack/pi.git
$ cd bot/src/
$ sudo docker run -e token=<your bot token here with no spaces> -d pi-bot:latest 
```
Your bot should be online and ready to respond to commands.