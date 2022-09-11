import discord
import random
import time
import pytz
import dict
import traceback as tb
from discord.errors import NotFound
from discord.ext import commands
from discord import DMChannel
from datetime import datetime as dt
from bot_sql import SQL_Server as db
import typing
from data import data, lists

#Declaring gateway intents, discord.py >= 2.0 feature
intent = discord.Intents().default()
intent.message_content = True

#Initalizing client object
client = commands.Bot(command_prefix = ".",  case_insensitive= True, help_command= None, intents=intent)

ban = "You are not allowed to use commands!"

#Say When Ready
@client.event
async def on_ready():
    print('I am ready')
    bot_channel = client.get_channel(data.get('dump_channel'))
    await bot_channel.send("I Am Ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone all the time"))

#Banned user check
async def banned_user(ctx):

    if ctx.author.id in db().banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return

#DMs specific user a message
@client.command(pass_context=True)
async def dm(ctx, user, *message):

    msg = ' '.join(message)

    await banned_user(ctx)

    if ctx.message.mentions:
        uid = str(ctx.message.raw_mentions[0])
        user = await client.fetch_user(uid)
        await DMChannel.send(user, msg)
        await ctx.send(embed=dict.dm_embed("Message sent!", ctx.message.mentions[0], msg))

    elif user in db().db_Name(): 
        uid = str(db().get_UserId(user))
        user = await client.fetch_user(uid)
        await DMChannel.send(user, msg)
        await ctx.send(embed=dict.dm_embed("Message sent!", user, msg))

    else:
        await ctx.send(embed=dict.cmd_error("User not found!"))
        return

#DMs user repeatedly the same message
@client.command(pass_context=True)
async def dmrep(ctx, user, arg3: typing.Optional[float] = 2, *message):

    await banned_user(ctx)

    msg = ' '.join(message)

    if msg == '':
        await ctx.send(embed=dict.cmd_error('Missing *message* argument.'))
        return

    if arg3 < 1:
        await ctx.send(embed=dict.cmd_error("Please enter a value more than 1, wait time interval has to be more than 1"))
        return

    if ctx.message.mentions:
        global on 
        on = True
        uid = str(ctx.message.raw_mentions[0])
        user = await client.fetch_user(uid)
        await ctx.send(embed=dict.dm_embed("Repeating Message!", ctx.message.mentions[0], msg))

        while on == True:
            time.sleep(arg3)
            await DMChannel.send(user, msg)
            if on == False:
                break

    elif user in db().db_Name():
        on = True
        uid = db().get_UserId(user)
        user = await client.fetch_user(uid)
        await ctx.send(embed=dict.dm_embed("Repeating Message!", user, msg))

        while on == True:
            time.sleep(arg3)
            await DMChannel.send(user, msg)
            if on == False:
                break

    else:
        await ctx.send(embed=dict.cmd_error("User not found!"))
        return

#Breaks while loop in dmrep function
@client.command(pass_context=True)
async def stop(ctx):

    await banned_user(ctx)

    global on
    on = False
    await ctx.send(embed=dict.embed_a("Stopped sending message!", random.choice(lists["stop_message"])))

#Adds the author's id to the database
@client.command(pass_context=True)
async def addme(ctx, name):

    usr = ctx.author.id

    await banned_user(ctx)

    if ctx.message.mentions:
        await ctx.send(embed=dict.cmd_error("Please type out your name, don't ping youself!"))
        return

    elif usr in db().db_UserId():
        await ctx.send(embed=dict.cmd_error("User is already in database!"))
        return

    else:
        db().insert_UserInfo(usr, name)
        await ctx.send(embed=dict.embed_a("Success!", f"{name} was added to the database successfully!"))

#Error handing specifically for addme command
@addme.error
async def addme_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(error)

    else:
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

#Adds the mentioned user's id to the database
@client.command(pass_context=True)
async def addusr(ctx, user, name):

    usr = ctx.message.raw_mentions[0]

    await banned_user(ctx)

    if usr in db().db_UserId(): 
        await ctx.send(embed=dict.cmd_error("User is already in database!"))
        return

    elif ctx.message.mentions:
        db().insert_UserInfo(usr, name)
        await ctx.send(embed=dict.embed_a("Success!", f"{name} was added to the database successfully!"))

    else:
        await ctx.send(embed=dict.cmd_error("Please mention the user you would like to add first!"))

#Error handing specifically for addusr command
@addusr.error
async def addusr_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(error)

    else: 
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

#Adds user to blacklist
@client.command(pass_context=True)
async def cmdban(ctx, user):

    usr = ctx.message.raw_mentions[0]

    await banned_user(ctx)

    if usr in db().banned_user():
        await ctx.send(embed=dict.cmd_error("User is already banned from using commands!"))
        return

    else:
        db().insert_BannedUser(usr)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.mentions[0]} is banned from using commands!"))

#Error handing specifically for cmdban command
@cmdban.error
async def cmdban_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(error)

    else:
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

#Remove User from blacklist
@client.command(pass_context=True)
async def cmduban(ctx, user :str):

    usr = ctx.message.raw_mentions[0]

    await banned_user(ctx)

    if user.startswith('<@') == False:
        await ctx.send(embed=dict.cmd_error('Please mention the use you would like banned!'))

    if usr in db().banned_user():
        db().delete_BannedUser(usr)
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
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

#Sends the name of the user you mention
@client.command(pass_context=True)
async def info(ctx, user):

    usr = ctx.message.raw_mentions[0]

    await banned_user(ctx)

    if user.startswith('<@') == False:
        await ctx.send(embed=dict.cmd_error('Please mention the use you would like banned!'))

    if usr in db().db_UserId():
        await ctx.send(embed=dict.info_embed(ctx.message.mentions[0], db().get_Name(usr)))

    else:
        await ctx.send(embed=dict.cmd_error("User is not in database!"))

#Edits your name in the database
@client.command(pass_context=True)
async def editname(ctx, name):

    usr = ctx.message.author.id

    await banned_user(ctx)

    if ctx.message.author.id in db().banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return
        
    if ctx.message.mentions:
        await ctx.send(embed=dict.cmd_error("Please use this command on yourself, you cannot edit the names of other people!"))

    elif usr in db().db_UserId():
        name1 = db().get_Name(usr)
        db().update_UserInfo(name, usr)
        await ctx.send(embed=dict.embed_a("Success!", f"Your name was changed from {name1} to {name}"))

    else:
        await ctx.send(embed=dict.cmd_error("User is not in database!"))

#Sends Bot Ping
@client.command()
async def ping(ctx):

    await banned_user(ctx)

    await ctx.send(f"Pong {round(client.latency * 1000)}ms")
    time.sleep(1)

#Switch statement that defines if working or not
@client.command()
async def working(ctx):

    usr = ctx.author.id

    await banned_user(ctx)

    if usr in db().banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return

    elif usr in db().db_Working():
        db().delete_Working(usr)
        await ctx.send(embed=dict.embed_b("Not working! <a:yay:794447927820419082>"))

    else:
        db().insert_Working(usr)
        await ctx.send(embed=dict.work_embed(ctx.author))
        
#Switch statement that defines if working or not
@client.command()
async def busy(ctx):

    auth_id = ctx.author.id

    if auth_id in db().banned_user():
        await ctx.send(embed=dict.cmd_error(ban))
        return

    elif auth_id in db().db_Busy():
        db().delete_Busy(auth_id)
        await ctx.send(embed=dict.embed_b("Not busy! <a:yay:794447927820419082>"))

    else:
        db().insert_Busy(auth_id)
        await ctx.send(embed=dict.busy_embed(ctx.author))

#Sends compliment to user when command called
@client.command()
async def compliment(ctx):

    await banned_user(ctx)

    if ctx.message.mentions:
        await ctx.send(random.choice(lists["compliments"]))

    else:
        await ctx.send(random.choice(lists["compliments"]))

#Sends embed of commands that describe function of each command has optional arguments
@client.command()
async def help(ctx, opt="general"):

    await banned_user(ctx)

    await ctx.send(embed=dict.help_command(opt))

#Authorizes Channel for code updates
@client.command()
async def auth(ctx, arg1):

    l = ["cst", "est", "pst"]

    await banned_user(ctx)

    if ctx.message.channel.id in db().db_authChannels():
        await ctx.send(embed=dict.cmd_error("This channel is already authorized!"))
        return

    elif arg1.lower() in l:
        db().insert_authChannels(ctx.message.channel.id, arg1.lower())
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.channel.name} is now an authorized channel!\n\nYou have selected {arg1.upper()} as your timezone, to change this please use the command **authtz** in the authorized channel."))

    else: 
        await ctx.send(embed=dict.cmd_error("Please enter a valid region!\n\nCurrently supported regions are:\nCST (Central Standard Time *USA*)\nPST (Pacific Standard Time *USA*)\nEST (Eastern Standard Time *USA*)"))

#Error handing specifically for auth command
@auth.error
async def auth_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=dict.cmd_error("Please enter a valid region!\n\nCurrently supported regions are:\nCST (Central Standard Time *USA*)\nPST (Pacific Standard Time *USA*)\nEST (Eastern Standard Time *USA*)"))

    else:
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

#Removes authorization from a channel for code updates
@client.command()
async def rmauth(ctx):

    usr = ctx.author.id

    await banned_user(ctx)

    if ctx.message.channel.id in db().db_authChannels():
        db().delete_authChannels(ctx.message.channel.id)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.channel.name} has been unauthorized!"))

    else: 
        await ctx.send(embed=dict.cmd_error("This channel was not previously authorized!"))

#Changes the region of an authorized channel 
@client.command()
async def authtz(ctx, arg1):

    l = ["cst", "est", "pst"]

    await banned_user(ctx)

    if arg1.lower() == db().get_authChannels_region(ctx.message.channel.id):
        await ctx.send(embed=dict.cmd_error(f"This authorized channel has already been set to {arg1.lower()} region!"))
        return

    elif ctx.message.channel.id in db().db_authChannels() and arg1.lower() in l:
        db().update_authChannels(arg1.lower(), ctx.message.channel.id)
        await ctx.send(embed=dict.embed_a("Success!", f"{ctx.message.channel.name}'s region has been changed from {db().get_authChannels_region(ctx.message.channel.id)} to {arg1.lower()}"))

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
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

@client.command()
async def update(ctx, version, notes):

    if ctx.author.id != data.get('owner'):
        await ctx.send(embed=dict.cmd_error('You are not authorized to use this command!'))

    tz_central = pytz.timezone('US/Central')
    tz_pacific = pytz.timezone('US/Pacific')
    tz_eastern = pytz.timezone('US/Eastern')
    central = dt.now(tz_central)
    pacific = dt.now(tz_pacific)
    eastern = dt.now(tz_eastern)

    for x in db().db_authChannels_byregion("pst"):
        channel = client.get_channel(x)
        await channel.send(f"```Version: {version}\nAuthor: Duren\nDate: {pacific.strftime('%b-%d-%Y %I:%M:%S %p')}\n\nNotes: {notes}```")
        with open(__file__, "rb") as f:
            await channel.send(file=discord.File(f, "apcsp_bot.py"))

    for x in db().db_authChannels_byregion("cst"):
        channel = client.get_channel(x)
        await channel.send(f"```Version: {version}\nAuthor: Duren\nDate: {central.strftime('%b-%d-%Y %I:%M:%S %p')}\n\nNotes: {notes}```")
        with open(__file__, "rb") as f:
            await channel.send(file=discord.File(f, "apcsp_bot.py"))

    for x in db().db_authChannels_byregion("est"):
        channel = client.get_channel(x)
        await channel.send(f"```Version: {version}\nAuthor: Duren\nDate: {eastern.strftime('%b-%d-%Y %I:%M:%S %p')}\n\nNotes: {notes}```")
        with open(__file__, "rb") as f:
            await channel.send(file=discord.File(f, "apcsp_bot.py"))

#Error handing specifically for authtz command
@update.error
async def update_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        if str(error).startswith('version'):
            msg = '```Please enter what version you are sending out!```'

        elif str(error).startswith('version'):
            msg = '```Please enter what notes you are putting in!```'
        
        await ctx.send(msg)

    else:
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

@client.command()
async def poke(ctx):
    await ctx.send(random.choice(lists["emoticon"]))

#General error handling on commands
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, NotFound):
        ctx.send(embed=dict.cmd_error("This is not a command!"))

    else:
        print(error)
        err = client.get_channel(data.get("dump_channel"))
        await err.send(f"```Error: {error}\nMessage: {ctx.message.content}\nAuthor: {ctx.author}\nServer: {ctx.message.guild}\nLink: {ctx.message.jump_url}\nTraceback: {''.join(tb.format_exception(None, error, error.__traceback__))}```")

#On every message sent to server the following actions occur
@client.event
async def on_message(message):
    
    #Ignores if user is client (self)
    if message.author == client.user:
        return

    #checks if user is 'busy' or 'working' and sends message if true
    if message.mentions:
        try:
            if message.raw_mentions[0] in db().db_Busy():
                await message.channel.send(embed=dict.busy_embed(message.mentions[0]))

            elif message.raw_mentions[0] in db().db_Working():
                await message.channel.send(embed=dict.work_embed(message.mentions[0]))

        except AttributeError:
            return

    #Sends a happy birthday message if "happy birthday" is in message
    elif "happy birthday" in message.content.lower():
        await message.channel.send(f"happy birthday!! {random.choice(lists['emotes'])}")
        
    #process any commands before on message event is processed
    await client.process_commands(message)

client.run(data.get('token'))
