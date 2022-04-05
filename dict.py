import discord
import json
import os
import random

if __name__ != '__main__':

    os.chdir(__file__.strip('dict.py'))
    commands = json.load(open('commands.json'))

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

    #Defines compliments
    general_compliment = [ "You look nice!", "I like your shoes!", "You're doing great!", "Have a nice day!", "Do you like rasins? How about a Date?", "Are you French? Because Eiffel for you", "I'm learning about important dates in history. Want to be one of them?", "Life without you is like a broken pencil... pointless"]

    #list of random messages to sent when using stop command
    stop_msg = ["Aboose <:heh:796197098810769438>", "Maybe you should reconsider your life choices", "But why tho?", "<:pepelmao:721073981410508850>"]

    #title only embed
    def embed_b(title):
        a = discord.Embed(title= title, color=0xf2c4a7)
        return a

    #name and value only embed
    def embed_a(name, value):
        a = discord.Embed(color=0xf2c4a7)
        a.add_field(name= name, value= value)
        return a

    #title name and value embed
    def embed_c(title, name, value):
        a = discord.Embed(title= title, color=0xf2c4a7)
        a.add_field(name= name, value= value)
        return a

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

    #User info embed
    def info_embed(usr, alias):
        a = discord.Embed(color=0xf2c4a7)
        a.add_field(name= "User Info", value= f"User Id: {usr}\n\nAlias: {alias}")
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


    #help command, scalable through the commands.json file
    def help_command(opt):

        opts = ["Help Has Arrived!", "At Your Service!", "HI!"]

        if opt == 'general':
            cmdEmbed = discord.Embed(title=random.choice(opts), color=0xf2c4a7)
            cmdEmbed.add_field(name="About Me!", value="I am a bot that was made for a CS project!\n\nBelow are some commands you can use with me. For any extra information on a command type the *help* command again along with the name of the command.")
            for x in commands:
                cmdEmbed.add_field(name=f"*{x}*", value="\u200b", inline=False)
            cmdEmbed.set_footer(text= "Bot Command Prefix = '.'")
            return cmdEmbed

        elif opt not in commands:
            return cmd_error("Not a valid option.")

        elif opt in commands:
            cmd = commands.get(opt)
            return embed_c(f"{opt} {cmd[0]}", cmd[1], cmd[2])

else:
    print('You cannot run this file!\nPlease run the apcsp_bot.py file!')