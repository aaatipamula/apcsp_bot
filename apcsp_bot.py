# **Version 1.0.0**
# **Note dict and pyignore are required modules for this file to run. **
# **I will release the dict module on request as it is just functions and object definitions that crowd the main file, but for security reasons I will not release pyignore. **
# **Other required dependencies (modules) that do not come included with standard installations of python3 include, discord.py, mysql.connector, and *pytz. **
# *pytz does not come installed with some installations of python3 to check run your command for python in the terminal along with '-m pip install pytz'. If you have this dependency installed pip will indicate that you have it installed, otherwise it should install for you. *

from logging import error
import discord
import random
import time
from discord.errors import NotFound
from discord.utils import get
import pytz
import dict
import pyignore
from discord.ext import commands
from discord import DMChannel
import mysql.connector
from datetime import datetime as dt

client = commands.Bot(command_prefix = ".",  case_insensitive= True, help_command= None)

#Defining info to be pulled from MySQL database
#Pulling all values from the BannedUser table and compiling in a list 
def sqlserver():
    mydb = mysql.connector.connect(
    host= pyignore.host,
    user= pyignore.user,
    password= pyignore.password,
    database= pyignore.database
    )
    cursor = mydb.cursor()
    return mydb, cursor

def banned_user():
    mydb, cursor = sqlserver()
    list_a = []
    cursor.execute("select * from BannedUser")
    b = cursor.fetchall()

    for x in b:
        list_a.append(x[0])
    return list_a

#Pulling all values from the UserInfo table in the Name column and compiling in a list 
def db_Name():
    mydb, cursor = sqlserver()
    list_b = []
    cursor.execute("select Name from UserInfo")
    b = cursor.fetchall()

    for x in b:
        list_b.append(x[0])
    return list_b

#Pulling all values from the UserInfo table in the UserId column and compiling in a list
def db_UserId():
    mydb, cursor = sqlserver()
    list_c = []
    cursor.execute("select UserId from UserInfo")
    b = cursor.fetchall()

    for x in b:
        list_c.append(x[0])
    return list_c

#Pulling all values from the Busy table in the UserId column and compiling in a list
def db_Busy():
    mydb, cursor = sqlserver()
    list_d = []
    cursor.execute("select UserId from Busy")
    b = cursor.fetchall()

    for x in b:
        list_d.append(x[0])
    return list_d

#Pulling all values from the Working table in the UserId column and compiling in a list
def db_Working():
    mydb, cursor = sqlserver()
    list_e = []
    cursor.execute("select UserId from Working")
    b = cursor.fetchall()

    for x in b:
        list_e.append(x[0])
    return list_e

#Pulling UserId based on Name stored in database
def get_UserId(name):
    mydb, cursor = sqlserver()
    cursor.execute(f"select * from UserInfo where Name = '{name}'")
    b = cursor.fetchone()
    return b[0]

#Pulling Name based on UserId stored in database
def get_Name(Id):
    mydb, cursor = sqlserver()
    cursor.execute(f"select * from UserInfo where UserId = '{Id}'")
    b = cursor.fetchone()
    return b[1]

#Inserts info into UserInfo table
def insert_UserInfo(usr, arg):
    mydb, cursor = sqlserver()
    sql = "insert into UserInfo values (%s, %s)"
    val = (usr, arg)
    cursor.execute(sql, val)
    mydb.commit()

#Inserts info into BannedUser table
def insert_BannedUser(usr):
    mydb, cursor = sqlserver()
    sql = "insert into BannedUser values (%s)"
    val = (usr,)
    cursor.execute(sql, val)
    mydb.commit()

#Deletes info from BannedUser table
def delete_BannedUser(usr):
    mydb, cursor = sqlserver()
    sql = f"delete from BannedUser where UserId = {usr}"
    cursor.execute(sql)
    mydb.commit()

#Updates name in UserInfo table
def update_UserInfo(arg, usr):
    mydb, cursor = sqlserver()
    sql = "update UserInfo set Name = %s where UserId = %s"
    val = (arg, usr)
    cursor.execute(sql, val)
    mydb.commit()

#inserts info into Working table
def insert_Working(usr):
    mydb, cursor = sqlserver()
    sql = "insert into Working values (%s)"
    val = (usr,)
    cursor.execute(sql,val)
    mydb.commit()

#Inserts info into Busy table
def insert_Busy(usr):
    mydb, cursor = sqlserver()
    sql = "insert into Busy values (%s)"
    val = (usr,)
    cursor.execute(sql,val)
    mydb.commit()

#Deletes info from Working table
def delete_Working(usr):
    mydb, cursor = sqlserver()
    sql = f"delete from Working where UserId = {usr}"
    cursor.execute(sql)
    mydb.commit()

#Deletes info from Working table
def delete_Busy(usr):
    mydb, cursor = sqlserver()
    sql = f"delete from Busy where UserId = {usr}"
    cursor.execute(sql)
    mydb.commit()

#Inserts into the Authorized Channels table
def insert_authChannels(id, region):
    mydb, cursor = sqlserver()
    sql = "insert into AuthChannels values (%s, %s)"
    val = (id, region)
    cursor.execute(sql,val)
    mydb.commit()

def delete_authChannels(id):
    mydb, cursor = sqlserver()
    sql = f"delete from AuthChannels where ChannelId = {id}"
    cursor.execute(sql)
    mydb.commit()

def update_authChannels(region, id):
    mydb, cursor = sqlserver()
    sql = "update AuthChannels set Region = %s where ChannelId = %s"
    val = (region, id)
    cursor.execute(sql, val)
    mydb.commit()

def get_authChannels_region(Id):
    mydb, cursor = sqlserver()
    cursor.execute(f"select * from AuthChannels where ChannelId = '{Id}'")
    b = cursor.fetchone()
    return b[1]

def db_authChannels():
    mydb, cursor = sqlserver()
    list_f = []
    cursor.execute("select ChannelId from AuthChannels")
    b = cursor.fetchall()

    for x in b:
        list_f.append(x[0])
    return list_f

def db_authChannels_byregion(region):
    mydb, cursor = sqlserver()
    list_f = []
    cursor.execute(f"select ChannelId from AuthChannels where Region = '{region}'")
    b = cursor.fetchall()

    for x in b:
        list_f.append(x[0])
    return list_f

#Defining the differnt ranomized messaged for different people and general compliments
def nice_message(userid):
    #person1
    if userid == 614188961216200752:
        return random.choice(dict.user_msg_person1)
    #person2
    elif userid == 756176803462119476:
        return random.choice(dict.user_msg_person2)
    #person3
    elif userid == 338375504405069824:
        return random.choice(dict.user_msg_person3)
    else:
        return random.choice(dict.general_compliment)

async def send_main_file(channel, version, date, notes ):
    await channel.send(f"```Version: {version}\nAuthor: Duren\nDate: {date}\n\nNotes: {notes}```")
    #, file=pyignore.mainFile

tz_central = pytz.timezone('US/Central')
tz_pacific = pytz.timezone('US/Pacific')
tz_eastern = pytz.timezone('US/Eastern')
central = dt.now(tz_central)
pacific = dt.now(tz_pacific)
eastern = dt.now(tz_eastern)

async def on_startup():
    answer = input("Would you like to send updated code? [y/n]: ")

    if answer.lower() == "y" or answer.lower() == "yes":
        version = input("What version is this?: ")
        notes = input("Any notes to add?: ")
    
        for x in db_authChannels_byregion("pst"):
            channel = client.get_channel(x)
            await channel.send(f"```Version: {version}\nAuthor: Duren\nDate: {eastern.strftime('%b-%d-%Y %I:%M:%S %p')}\n\nNotes: {notes}```")
            with open(pyignore.file, "rb") as f:
                await channel.send(file=discord.File(f, "apcsp_main.py"))
        
        for x in db_authChannels_byregion("cst"):
            channel = client.get_channel(x)
            await channel.send(f"```Version: {version}\nAuthor: Duren\nDate: {eastern.strftime('%b-%d-%Y %I:%M:%S %p')}\n\nNotes: {notes}```")
            with open(pyignore.file, "rb") as f:
                await channel.send(file=discord.File(f, "apcsp_main.py"))

        for x in db_authChannels_byregion("est"):
            channel = client.get_channel(x)
            await channel.send(f"```Version: {version}\nAuthor: Duren\nDate: {eastern.strftime('%b-%d-%Y %I:%M:%S %p')}\n\nNotes: {notes}```")
            with open(pyignore.file, "rb") as f:
                await channel.send(file=discord.File(f, "apcsp_main.py"))

    elif answer.lower() == "n" or answer.lower() == "n":
        return
    
    else:
        print("That is not a valid option please type out \"yes\"\\\"no\" or \"y\"\\\"n\"" )
        await on_startup()

#Say When Ready
@client.event
async def on_ready():
    await on_startup()
    print('I am ready')
    bot_channel = client.get_channel(914650069687492729)
    await bot_channel.send("I Am Ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone all the time"))

ban = "You are not allowed to use commands!"

#DMs specific user a message
@client.command(pass_context=True)
async def dm(ctx, arg1, arg2):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    if ctx.message.mentions:
        uid = str(ctx.message.raw_mentions[0])
        user = await client.fetch_user(uid)
        await DMChannel.send(user, arg2)
        await ctx.send(embed=dict.dm_embed("Message sent!", ctx.message.mentions[0], arg2))
    elif arg1 in db_Name(): 
        uid = str(get_UserId(arg1))
        user = await client.fetch_user(uid)
        await DMChannel.send(user, arg2)
        await ctx.send(embed=dict.dm_embed("Message sent!", arg1, arg2))
    else:
        await ctx.send(embed=dict.notfound)
        return

#Error handing specifically for dm command
@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if str(error).startswith("arg1"):
            msg = "```*user* is a required argument that is missing.```"
        elif str(error).startswith("arg2"):
            msg = "```*message* is a required argument that is missing.```"
        await ctx.send(msg)
    if isinstance(error, commands.ExpectedClosingQuoteError):
        await ctx.send("```Please enclose your message in quotes```")

#DMs user repeatedly the same message
@client.command(pass_context=True)
async def dmrep(ctx, arg1, arg2, arg3=2):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    if arg3 < 1:
        await ctx.send(embed=dict.cmd_error("Please enter a value more than 1, wait time interval has to be more than 1"))
    if ctx.message.mentions:
        global on 
        on = True
        uid = str(ctx.message.raw_mentions[0])
        user = await client.fetch_user(uid)
        await ctx.send(embed=dict.dm_embed("Repeating Message!", ctx.message.mentions[0], arg2))
        while on == True:
            time.sleep(arg3)
            await DMChannel.send(user, arg2)
            if on == False:
                break
    elif arg1 in db_Name():
        on = True
        uid = get_UserId(arg1)
        user = await client.fetch_user(uid)
        await ctx.send(embed=dict.dm_embed("Repeating Message!", arg1, arg2))
        while on == True:
            time.sleep(arg3)
            await DMChannel.send(user, arg2)
            if on == False:
                break
    else:
        await ctx.send(embed=dict.cmd_error("User not found!"))
        return

#Error handing specifically for dmrep command
@dmrep.error
async def dmrep_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if str(error).startswith("arg1"):
            msg = "```*user* is a required argument that is missing.```"
        elif str(error).startswith("arg2"):
            msg = "```*message* is a required argument that is missing.```"
        await ctx.send(msg)
    if isinstance(error, commands.ExpectedClosingQuoteError):
        await ctx.send("```Please enclose your message in quotes```")
    else:
        print(error)

#Breaks while loop in dmrep function
@client.command(pass_context=True)
async def stop(ctx):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    global on
    on = False
    await ctx.send(embed=dict.embed_a("Stopped sending message!", random.choice(dict.stop_msg)))

#Adds the author's id to the database
@client.command(pass_context=True)
async def addme(ctx, arg):
    usr = ctx.author.id
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    if ctx.message.mentions:
        await ctx.send(embed=dict.cmd_error("Please type out your name, don't ping youself!"))
        return
    elif usr in db_UserId():
        await ctx.send(embed=dict.cmd_error("User is already in database!"))
        return
    else:
        insert_UserInfo(usr, arg)
        await ctx.send(embed=dict.embed_a("Success!", f"{arg} was added to the database successfully!"))

#Error handing specifically for addme command
@addme.error
async def addme_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if str(error).startswith("arg"):
            msg = "```*name* is a required argument that is missing.```"
        await ctx.send(msg)

#Adds the mentioned user's id to the database
@client.command(pass_context=True)
async def addusr(ctx, arg1, arg2):
    usr = ctx.message.raw_mentions[0]
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    elif usr in db_UserId(): 
        await ctx.send(embed=dict.cmd_error("User is already in database!"))
        return
    elif ctx.message.mentions:
        insert_UserInfo(usr, arg2)
        await ctx.send(embed=dict.embed_a("Success!", f"{arg2} was added to the database successfully!"))
    else:
        await ctx.send(embed=dict.cmd_error("Please mention the user you would like to add first!"))

#Error handing specifically for addusr command
@addusr.error
async def addusr_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if str(error).startswith("arg1"):
            msg = "```*user* is a required argument that is missing.```"
        elif str(error).startswith("arg2"):
            msg = "```*name* is a required argument that is missing.```"
        await ctx.send(msg)

#Adds user to blacklist
@client.command(pass_context=True)
async def cmdban(ctx, arg):
    usr = ctx.message.raw_mentions[0]
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    elif usr in banned_user():
        await ctx.send(embed=dict.cmd_error("User is already banned from using commands!"))
        return
    else:
        insert_BannedUser(usr)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.mentions[0]} is banned from using commands!"))

#Error handing specifically for cmdban command
@cmdban.error
async def cmdban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if str(error).startswith("arg"):
            msg = "```*user* is a required argument that is missing.```"
        await ctx.send(msg)
    else:
        await ctx.send(f"```{error}```")

#Remove User from blacklist
@client.command(pass_context=True)
async def cmduban(ctx, arg):
    usr = ctx.message.raw_mentions[0]
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    elif usr in banned_user():
        delete_BannedUser(usr)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.mentions[0]} is unbanned from using commands!"))
    else:
        await ctx.send(embed=dict.cmd_error("User is not banned from using commands!"))
        return

#Error handing specifically for cdmuban command
@cmduban.error
async def cmduban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if str(error).startswith("arg"):
            msg = "```*user* is a required argument that is missing.```"
        await ctx.send(msg)
    else:
        await ctx.send(f"```{error}```")

#Sends the name of the user you mention
@client.command(pass_context=True)
async def info(ctx, arg):
    usr = ctx.message.raw_mentions[0]
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    elif usr in db_UserId():
        await ctx.send(embed=dict.info_embd(ctx.message.mentions[0], get_Name(usr)))
    else:
        await ctx.send(embed=dict.cmd_error("User is not in database!"))

#Edits your name in the database
@client.command(pass_context=True)
async def editname(ctx, arg):
    usr = ctx.message.author.id
    if ctx.message.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    if ctx.message.mentions:
        await ctx.send(embed=dict.cmd_error("Please use this command on yourself, you cannot edit the names of other people!"))
    elif usr in db_UserId():
        name1 = get_Name(usr)
        update_UserInfo(arg, usr)
        await ctx.send(embed=dict.embed_a("Success!", f"Your name was changed from {name1} to {arg}"))
    else:
        await ctx.send(embed=dict.cmd_error("User is not in database!"))

#Sends Bot Ping
@client.command()
async def ping(ctx):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    else:
        await ctx.send(f"Pong {round(client.latency * 1000)}ms")
        time.sleep(1)

#Switch statement that defines if working or not
@client.command()
async def working(ctx):
    auth_id = ctx.author.id
    if auth_id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    elif auth_id in db_Working():
        delete_Working(auth_id)
        await ctx.send(embed=dict.embed_b("Not working! <a:yay:794447927820419082>"))
    else:
        insert_Working(auth_id)
        await ctx.send(embed=dict.work_embed(ctx.author))
        
#Switch statement that defines if working or not
@client.command()
async def busy(ctx):
    auth_id = ctx.author.id
    if auth_id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    elif auth_id in db_Busy():
        delete_Busy(auth_id)
        await ctx.send(embed=dict.embed_b("Not busy! <a:yay:794447927820419082>"))
    else:
        insert_Busy(auth_id)
        await ctx.send(embed=dict.busy_embed(ctx.author))

#Sends compliment to user when command called
@client.command()
async def compliment(ctx):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
    elif ctx.message.mentions:
        await ctx.send(nice_message(ctx.message.mentions[0]))
    else:
        await ctx.send(nice_message(ctx.author.id))

#Sends embed of commands that describe function of each command has optional arguments
@client.command()
async def help(ctx, arg1="general"):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
    if arg1 in dict.key:
        await ctx.send(embed=dict.help_cmd(arg1))
    else:
        await ctx.send(embed=dict.cmd_error("Please enter a valid command to view more information about it!"))

#Authorizes Channel for code updates
@client.command()
async def auth(ctx, arg1):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
    if ctx.message.channel.id in db_authChannels():
        await ctx.send(embed=dict.cmd_error("This channel is already authorized!"))
        return
    l = ["cst", "est", "pst"]
    if arg1.lower() in l:
        insert_authChannels(ctx.message.channel.id, arg1)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.channel.name} is now an authorized channel!\n\nYou have selected {arg1.upper()} as your timezone, to change this please use the command **authtz** in the authorized channel."))
    else: 
        await ctx.send(embed=dict.cmd_error("Please enter a valid region!\n\nCurrently supported regions are:\nCST (Central Standard Time *USA*)\nPST (Pacific Standard Time *USA*)\nEST (Eastern Standard Time *USA*)"))

#Error handing specifically for auth command
@auth.error
async def auth_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=dict.cmd_error("Please enter a valid region!\n\nCurrently supported regions are:\nCST (Central Standard Time *USA*)\nPST (Pacific Standard Time *USA*)\nEST (Eastern Standard Time *USA*)"))
    else:
        await ctx.send(f"```{error}```")

#Removes authorization from a channel for code updates
@client.command()
async def rmauth(ctx):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
    if ctx.message.channel.id in db_authChannels():
        delete_authChannels(ctx.message.channel.id)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.channel.name} has been unauthorized!"))
    else: 
        await ctx.send(embed=dict.cmd_error("This channel was not previously authorized!"))

#Changes the region of an authorized channel 
@client.command()
async def authtz(ctx, arg1):
    if ctx.author.id in banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
    l = ["cst", "est", "pst"]
    if arg1 == get_authChannels_region(ctx.message.channel.id):
        await ctx.send(embed=dict.cmd_error(f"This authorized channel has already been set to {arg1} region!"))
        return
    elif ctx.message.channel.id in db_authChannels() and arg1.lower() in l:
        update_authChannels(arg1, ctx.message.channel.id)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.channel.name}'s region has been changed from {get_authChannels_region(ctx.message.channel.id)} to {arg1}"))
    elif arg1.lower() in l is False:
        await ctx.send(embed=dict.cmd_error(""))
    else: 
        await ctx.send(embed=dict.cmd_error("Please enter a valid region!\n\nCurrently supported regions are:\nCST (Central Standard Time *USA*)\nPST (Pacific Standard Time *USA*)\nEST (Eastern Standard Time *USA*)"))

#Error handing specifically for authtz command
@authtz.error
async def authtz_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=dict.cmd_error("Please enter a valid region!\n\nCurrently supported regions are:\nCST (Central Standard Time *USA*)\nPST (Pacific Standard Time *USA*)\nEST (Eastern Standard Time *USA*)"))
    else:
        await ctx.send(f"```{error}```")

#General error handling on commands
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, NotFound):
        ctx.send(embed=dict.cmd_error("This is not a command!"))
    else:
        print(error)
        err = client.get_channel(914649594531553300)
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}```")

#On every message sent to server the following actions occur
@client.event
async def on_message(message):
    
    #Ignores if user is client (self)
    if message.author == client.user:
        return

    #checks if user is 'busy' or 'working' and sends message if true
    if message.mentions:
        try:
            if message.raw_mentions[0] in db_Busy():
                await message.channel.send(embed=dict.busy_embed(message.mentions[0]))
            elif message.raw_mentions[0] in db_Working():
                await message.channel.send(embed=dict.work_embed(message.mentions[0]))
        except AttributeError:
            return

    #Sends a happy birthday message if "happy birthday" is in message
    elif "happy birthday" in message.content.lower():
        await message.channel.send(f"happy birthday!! {random.choice(dict.random_emote)}")
        
    #process any commands before on message event is processed
    await client.process_commands(message)

client.run(pyignore.token)