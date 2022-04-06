import os
import json
from tokenize import tabsize

os.chdir(__file__.strip('setup.py'))

def main():
    while True:
        dump_channel = input("Please input the channel id you would like to send bot-message-dumps: ")

        try:
            dump_channel = int(dump_channel)
            break

        except ValueError:
            print("\naPlease enter a valid channel id!\n")

    while True:
        owner_id = input("\nPlease input your Discord user-id: ")

        try:
            owner_id = int(dump_channel)
            break
        
        except ValueError:
            print("\naPlease enter a valid channel id!\n")

    host = input("\nPlease input a hostname for the MySQL server.\nIf you want the default hit enter to continue: ") or 'bot-mysql'
    user = input("\nPlease input a user for the MySQL server.\nIf you want the default hit enter to continue: ") or 'python'
    password = input("\nPlease input a password for the MySQL server.\nIf you want the default hit enter to continue: ") or'Chb4ug8h#d'

    token = input("\nPlease input your bot token: ")

    x = {
        "host": host,
        "user": user,
        "password": password,
        "database": 'Discord',
        "token": token,
        "owner": owner_id,
        "dump_channel": dump_channel
    }

    with open('data.json', 'w') as f:
        f.write(json.dumps(x, indent=4))

if __name__ == '__main__':
    main()

else:
    Exception("Please run this file as the main, do not import!")