# APCSP Bot

A bot that does a lot of useless stuff in Discord. 

## Project Info

**Author**: Aniketh Aatipamula <br>
**Project Start Date**: October 30, 2021 <br>
**Contributors**: N/A <br> <br>

**Project Origin**: This project originated as something to submit to my digital portfoliio for AP Computer Science Principles. I have continued to work on and add to the project as I have come up with improvements and increased my knowledge of python. <br> <br> 

**Project Description**: This is a Discord bot that can be added to any number servers. The bot mostly carries out commands that are called by the user using a specific prefix trigger character followed by the command. In the case of the bot the trigger `prefix = '.'`  The commands include sending personal messages to specified users, sending automated messages if a user is definied as "busy" or "working" and is pinged, and a host of commands that deal with information handling in the database.  

## Project Notes

**Module Dependencies**: This project requires that a handful of non-standard python modules be installed. <br>
This includes:
- discord.py
- pytz
- mysql-connector-python



## Running This Project 

I have no problems with people running this project. It is easily self hosted with docker containers!

**Inital Setup** <br> 
Make sure you have Docker installed on your host, you can install it [here](https://docs.docker.com/get-docker/). <br><br>
Assuming you have [**git**](https://git-scm.com/) installed on your client, clone the repo by running the following command in your terminal:

```
git clone https://github.com/aaatipamula/apcsp_bot
``` 

This will create a folder named `apcsp_bot` in your working directory. Navigate into that directory in your terminal and run `python3 ./src/setup.py` This will ask you for a handful of items including a Discord channel in a server that you would not mind the bot dumping messages in, your Discord user id, information on the MySQL server, and the bot token. <br><br>

If you don't know how to get channel and user id's refer to [this](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) discord faq. <br><br>

If you don't have a MySQL server you would rather use, would rather use a docker container MySQL server, or don't know how to set a MySQL server up go ahead and skip inputting all those values by hitting `Enter`.<br><br>

You can create a bot token by going to https://discord.com/developers/applications signing in, hitting `New Application` and typing in what you want the bot to be named. From there go to the `Bot` tab and hit `Add Bot` and hit `Yes`. If your token is displayed copy that and put it into the required field. If not you can reset your token and copy it in. The token only appears once before you cannot see it again so make sure to copy it down somewhere. <br><br>

If you're hosting this bot on a Linux machine, or even OSX, you can run the configuration file located in `./scripts/dockerstart.sh` to create the images and run them. Use the following command to do so:

```
sudo /bin/sh -c './scripts/dockerstart.sh'
```

You will have to manually set up the MySQL container by putting in a few commands, start by running the following command:

```
sudo docker exec -it bot-mysql bash
```

You will be given the bash prompt for the container, run the following command to set up the SQL database. The password for the MySQL image is defaulted to `Chb4ug8h#d`:

```
mysql -uroot -p < /home/sql_script/setup_database.sql
```

You can exit the container by hitting `CTRL+D` or just typing `exit` into the Pesudo-TTY.

Finally you can start the bot up by running the following command:

```
sudo docker exec -it -d bot python3 apcsp_bot/src/apcsp_bot.py &
```