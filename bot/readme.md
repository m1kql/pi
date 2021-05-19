## Building with docker

This is for building the bot **only**:

```shell
$ sudo docker pull yakfumblepack/pi
$ sudo docker run --env token=<your token without spaces and without the arrow brackets> --detach yakfumblepack/pi:latest
```
Your bot should be online and ready to respond to commands.