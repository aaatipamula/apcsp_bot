# APCSP Bot

A bot that does a lot of useless stuff in Discord. 

## Project Info

**Author**: Aniketh Aatipamula <br>
**Project Start Date**: October 30 2021 <br>
**Contributors**: N/A <br> <br>

**Project Origin**: This project originated as something to submit to my digital portfoliio for AP Computer Science Principles. I have continued to work on and add to the project as I have come up with improvements and increased my knowledge of python. <br> <br> 

**Project Description**: This is a Discord bot that can be added to any number servers. The bot mostly carries out commands that are called by the user using a specific prefix trigger character followed by the command. In the case of the bot the trigger `prefix = '.'`  The commands include sending personal messages to specified users, sending automated messages if a user is definied as "busy" or "working" and is pinged, and a host of commands that deal with information handling in the database.  

## Project Notes

**Module Dependencies**: This project requires that a handful of non-standard python modules be installed. <br>
This includes:
- discord.py
- *pytz
- *mysql.connector

*While some installations of python3 come standard with these modules other installations may not. Use the pip python package manager to install these dependencies if you do not have them or are not sure you have them. The package manager will indicate if you have them installed or not. For more information on how to use pip to install depenencies use the python [pip docs](https://pip.pypa.io/en/stable/cli/pip_install/).

## Running This Project 

I have no problems with people running this project. However, I am still working on the ability to easily run the project. For now the only way to run the project is to run is with slight modifications to the main file, the addition of a pyignore.py file, and by starting a MySQL server on the machine you intend to run the project on. 


**Modifications to the Main File**: 
- *Changing the command invoke prefix `client = commands.Bot(command_prefix = ".",  case_insensitive= True, help_command= None)`
- Change UserId's in the  `nice_message` function 
- Change the Bot Channel in `on_ready` function/event
- Change the Error channel in the `on_command_error` function
- *Changing the predefined compliment messages in the *dict.py* module <br> <br>

*These changes are optional and not required for the bot to operate properly.

**Setting up the MySQL server**:
I am working on creating a sql execute file that will create all the tables and databases necessary, however for now you have to make these tables yourself. <br> <br>

I highly suggest creating a fresh database for this project named **Discord** (case sensitive). You will need to create the following tables. The tables and column names are case sensitive. 

- Create the Authchannels table with two columns named ChannelId and Region, ChannelId should contain the bigInt datatype and Region should contain the varchar datatype with a minimum of 3 characters.
- Create the BannedUser table with one column named UserId, UserId should contain the bigInt data type.
- Create the Busy table with one column named UserId, UserId should contain the bigInt data type.
- Create the Working table with one column named UserId, UserId should contain the bigInt data type.
- Create the UserInfo table with two columns named UserId and Name, UserId should contain the bigInt datatype and Name should contain the varchar datatype with as many characters as you would like to allow. <br> <br> 

I could not find a good all-around source that would provide a comprehensive user guide to installing and setting up databases and tables in MySQL however I will link the [W3Schools.com](https://www.w3schools.com/mysql/default.asp) guide for MySQL as a place to get started. <br><br> 

**Creating the pyignore.py File**:
There are a handful of variables that you need to define in this file. They are listed below.
- *file* This is the filepath of the main document you want to be uploaded when the update option is selected on startup of the program. 
- *host* This is the ip of the MySQL server, if the server is being hosted on the same machine, set this variable to "localhost".
- *user* This is the user you want the program to access the MySQL database as.
- *password* This is the password for the previously defined user.
- *database* This is the name of the database that you have made for the bot to use. 
- *token* This is the token string for the bot that you get when 

As for how to get a token and create your own discord bot there is a [video](https://www.youtube.com/watch?v=nW8c7vT6Hl4) I reccomend that goes through all the inital stages of creating the developer application, getting your client token, and adding the bot to servers. Although the video is long and somewhat lenthy it goes over everything you would need to get started in depth. 
