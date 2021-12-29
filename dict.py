import discord

#List of Emotes
random_emote = ["<a:yay:794447927820419082>", 
"<:nabeelsmile:772290438345261116>", 
"<:PogYou:721074041053511800>", 
"<a:KirboExcite:809592083701694515>", 
"<:torchicy:780828666971029534>", 
"<:poyo:809155758075281458>", 
"<:oig:810974970440187904>", 
"<a:torchic:781329784621105172>", 
"<:rightkiss:797006910045814804>"]

#Defines who gets what randomized messages
user_msg_person1 = [ "You look nice!", "I like your shoes!", "You're doing great!", "Have a nice day!"]
user_msg_person2 = [ "Your hair is looking good today", "Your eyes look pretty", "I like your hair", "I love that color on your nails!"]
user_msg_person3 = [ "Do you like rasins? How about a Date?", "Are you French? Because Eiffel for you", "I'm learning about important dates in history. Want to be one of them?", "Life without you is like a broken pencil... pointless"]
general_compliment = [  "You look nice!", "I like your shoes!", "You're doing great!", "Have a nice day!", "Do you like rasins? How about a Date?", "Are you French? Because Eiffel for you", "I'm learning about important dates in history. Want to be one of them?", "Life without you is like a broken pencil... pointless"]

stop_msg = ["Aboose <:heh:796197098810769438>", "Maybe you should reconsider your life choices", "But why tho?", "<:pepelmao:721073981410508850>"]

#embed on command error
def cmd_error(value):
    a = discord.Embed(color=0xf2c4a7)
    a.add_field(name= "Error!", value= value)
    return a

#dm confirmation embed
def dm_embed(name, usr, msg):
    a = discord.Embed(color=0xf2c4a7)
    a.add_field(name= name, value= f"To: {usr}\n\nMessage: {msg}")
    return a

#name and value only embed
def embed_a(name, value):
    a = discord.Embed(color=0xf2c4a7)
    a.add_field(name= name, value= value)
    return a

#User info embed
def info_embd(usr, alias):
    a = discord.Embed(color=0xf2c4a7)
    a.add_field(name= "User Info", value= f"User Id: {usr}\n\nAlias: {alias}")
    return a

#Title only embed
def embed_b(title):
    a = discord.Embed(title= title, color=0xf2c4a7)
    return a

#Work Embed
def work_embed(auth):
    a = discord.Embed(title= f"{auth} is currently at work!", color=0xf2c4a7)
    a.add_field(name="They will respond ASAP or during his lunch break", value= "If you want them to see something please ping them", inline=False)
    a.add_field(name= "See ya soon!", value= "<a:wave:812383129608126484>", inline=False)
    return a

#Busy Embed
def busy_embed(auth):
    a = discord.Embed(title = f"{auth} is busy", color=0xf2c4a7)
    a.add_field(name= "<:poyo:809155758075281458>", value= "He'll probably get back to you a little later if you really want him to see something dm him", inline=False)
    a.set_footer(text= "Thank you for unerstanding")
    return a

#name and value only embed
def embed_c(title, name, value):
    a = discord.Embed(title= title, color=0xf2c4a7)
    a.add_field(name= name, value= value)
    return a

dm_values = ["dm (*user*, *message*)","\nThis command DM's a specific user a message of your choice.", "This command excepts two arguments, *user* and *message*.\n\n*user* can either be a mention of the user, or the users name, if they are already added to the dictionary.\n\n*message* has to be put in quotation marks if more than one word, emotes can be used if the bot is in the same server as the emotes origin."]
dmrep_values = ["dmrep (*user*, *message*)","Similar to the dm command except it repeats the message to the user until stopped with stop command.", "\nThis command excepts two arguments, *user* and *message*.\n\n*user* can either be a mention of the user, or the users name, if they are already added to the dictionary.\n\n*message* has to be put in quotation marks if more than one word, emotes can be used if the bot is in the same server as the emotes origin."]
stop_values = ["stop","Stops the repeated messages to user from the *dmrep* command."]
addme_values = ["addme (*name*)","If user is not defined in dictionary, this command can be used by a user to add them to the dictionary.", "\nThis command accepts one argument, *name*\n\n*name* is the name you would like to be stored as in the dictionary."]
addusr_values = ["addusr (*user* *name*)","If user who is now you is not defined in dictionary, this command can be used by user to add to dictionary", "\nThis command accepts two arguments, *user* and *name*\n\n*user* is the mention of the user you would like to add\n\n*name* is the name you would like the user to be to be stored as in the database."]
ping_values = ["ping","Sends 'pong' along with the bot's ping in milliseconds."]
working_values = ["working","Are you working or not? (switch statement)", "If you are working it will add you to the database and if you are pinged it will send a message letting the person who pinged you know that you are working."]
busy_values = ["busy","Are you busy or not? (switch statement)", "If you are busy it will add you to the database and if you are pinged it will send a message letting the person who pinged you know that you are busy."]
compliment_values = ["compliment","Sends a nice message to user based on user id."]
cmdban_values = ["cmdban (*user*)","Bans *user* from using bot commands.", "This command accepts one argument, *user*\n\n*user* is the mention of the user you would like to ban from using commands."]
cmduban_values = ["cmduban (*user*)","Unbans *user* from using bot commands.", "\nThis command accepts one argument, *user*\n\n*user* is the mention of the user you would like to unban from using commands."]
info_values = ["info (*user*)","Sends the info of the mentioned user that has been stored in the database", "\nThis command accepts one argument, *user*\n\n*user* is the mention of the user you would like to get the name for."]
editname_values = ["editname (*name*)","Changes the current name for the user in the database to *name*.\n\nThis command only works for the user who uses the command, you are not allowed to change another users name.", "\nThis command accepts one argument, *name*\n\n*name* is the name you would like to be put in the database under your profile."]
update_values = ["update", "Sends the updated code to a list of channels that it is authorized to send to, can only be used by the author of the bot."]
auth_values = ["auth (*region*)", "Use this command in a channel you would like to authorize so code updates will be sent periodically by the author.", "\nThis command accepts one argument, *region*\n\n*region* is the region you are located in so updates will send with the correct timestamp, the only regions that are currently supported are CST, PST, and EST."]
authtz_values = ["authtz (*region*)", "This command changes the region of an authorized channel.\nThis command can only be used on channels that have been authorized.", "\nThis command accepts one argument, *region*\n\n*region* is the region you are located in so updates will send with the correct timestamp, the only regions that are currently supported are CST, PST, and EST."]
rmauth_values = ["rmauth", "This command removes authorization from an authorized channel.\nThis command can only be used on a previously authorized channel, it had no additional arguments."]

commands_list = (
    dm_values, 
    dmrep_values, 
    stop_values, 
    addme_values, 
    addusr_values, 
    ping_values, 
    working_values, 
    busy_values, 
    compliment_values, 
    cmdban_values, 
    cmduban_values, 
    editname_values,
    update_values,
    auth_values,
    authtz_values,
    rmauth_values,
    )

#Commands Embed
cmdEmbed = discord.Embed(title = "Command List", color=0xf2c4a7)
for x in commands_list:
    cmdEmbed.add_field(name=x[0], value = "\u200b", inline=False)
cmdEmbed.set_footer(text= "Bot Command Prefix = '.'")

dmEmbed= embed_c(dm_values[0], dm_values[1], dm_values[2])
dmrepEmbed= embed_c(dmrep_values[0], dmrep_values[1], dmrep_values[2])
stopEmbed= embed_c(stop_values[0], stop_values[1], "\u200b")
addmeEmbed= embed_c(addme_values[0], addme_values[1], addme_values[2])
addusrEmbed= embed_c(addusr_values[0], addusr_values[1], addusr_values[2])
workingEmbed= embed_c(working_values[0], working_values[1], working_values[2])
busyEmbed= embed_c(busy_values[0], busy_values[1], busy_values[2])
cmdbanEmbed= embed_c(cmdban_values[0], cmdban_values[1], cmdban_values[2]),
cmdubanEmbed= embed_c(cmduban_values[0], cmduban_values[1], cmduban_values[2])
infoEmbed= embed_c(info_values[0], info_values[1], info_values[2])
editnameEmbed= embed_c(editname_values[0], editname_values[1], editname_values[2])
pingEmbed= embed_c(ping_values[0], ping_values[1], "\u200b")
complimentEmbed= embed_c(compliment_values[0], compliment_values[1], "\u200b")
updateEmbed= embed_c(update_values[0], update_values[1], "\u200b")
authEmbed= embed_c(auth_values[0], auth_values[1], auth_values[2])
authtzEmbed= embed_c(authtz_values[0], authtz_values[1], authtz_values[2])
rmauthEmbed= embed_c(rmauth_values[0], rmauth_values[1], "\u200b")

key = {
    "general": cmdEmbed,
    "dm": dmEmbed,
    "dmrep": dmrepEmbed,
    "stop": stopEmbed,
    "addme": addmeEmbed,
    "addusr": addusrEmbed,
    "working": workingEmbed,
    "busy": busyEmbed,
    "cmdban": cmdbanEmbed,
    "cmduban": cmdubanEmbed,
    "info": infoEmbed,
    "editname": editnameEmbed,
    "ping": pingEmbed,
    "compliment": complimentEmbed,
    "update": updateEmbed,
    "auth": authEmbed,
    "authtz": authtzEmbed,
    "rmauth": rmauthEmbed,
}

def help_cmd(arg):
    if arg in key:
        return key[arg]