import os
import json
import sqlite3

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
            owner_id = int(owner_id)
            break
        
        except ValueError:
            print("\naPlease enter a valid channel id!\n")

    token = input("\nPlease input your bot token: ")

    connection = sqlite3.connect('./src/db.sqlite')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE AuthChannels(ChannelId bigint, Region varchar(3));")
    cursor.execute("CREATE TABLE BannedUser(UserId bigint);")
    cursor.execute("CREATE TABLE Busy(UserId bigint);")
    cursor.execute("CREATE TABLE Working(UserId bigint);")
    cursor.execute("CREATE TABLE UserInfo(UserId bigint,Name varchar(255));")

    connection.commit()
    connection.close() 
    
    x = {
        "token": token,
        "owner": owner_id,
        "dump_channel": dump_channel
    }

    with open('./src/data.json', 'w') as f:
        f.write(json.dumps(x, indent=4))
        
    print('''\nYour data is saved in ./src/data.json and can be edited if any of the previously input information is incorrect or needs to be updated!''')    

if __name__ == '__main__':
    directory = os.listdir()

    if 'src' in directory and 'scripts' in directory:
        try:
            main()
        except KeyboardInterrupt:
            print("Exited.\n")
    else:
        print("Please run this file in the root directory of the project!")

else:
    Exception("Please run this file as the main, do not import!")