import mysql.connector
import os
import json

if __name__ != '__main__':

    os.chdir(__file__.strip('bot_mysql.py'))
    data = json.load(open('ignore.json'))

    #Defining info to be pulled from MySQL database
    #Pulling all values from the BannedUser table and compiling in a list 
    class MySQL_Server():

        def __init__(self,):

            self.mydb = mysql.connector.connect(
            host= data.get('host'),
            user= data.get('user'),
            password= data.get('password'),
            database= data.get('database')
            )

            self.cursor = self.mydb.cursor()

        def banned_user(self):
            list_a = []
            self.cursor.execute("select * from BannedUser")
            b = self.cursor.fetchall()

            for x in b:
                list_a.append(x[0])
            return list_a

        #Pulling all values from the UserInfo table in the Name column and compiling in a list 
        def db_Name(self):
            list_b = []
            self.cursor.execute("select Name from UserInfo")
            b = self.cursor.fetchall()

            for x in b:
                list_b.append(x[0])
            return list_b

        #Pulling all values from the UserInfo table in the UserId column and compiling in a list
        def db_UserId(self):
            
            list_c = []
            self.cursor.execute("select UserId from UserInfo")
            b = self.cursor.fetchall()

            for x in b:
                list_c.append(x[0])
            return list_c

        #Pulling all values from the Busy table in the UserId column and compiling in a list
        def db_Busy(self):
            
            list_d = []
            self.cursor.execute("select UserId from Busy")
            b = self.cursor.fetchall()

            for x in b:
                list_d.append(x[0])
            return list_d

        #Pulling all values from the Working table in the UserId column and compiling in a list
        def db_Working(self):
            
            list_e = []
            self.cursor.execute("select UserId from Working")
            b = self.cursor.fetchall()

            for x in b:
                list_e.append(x[0])
            return list_e

        #Pulling UserId based on Name stored in database
        def get_UserId(self, name):
            self.cursor.execute(f"select * from UserInfo where Name = '{name}'")
            b = self.cursor.fetchone()
            return b[0]

        #Pulling Name based on UserId stored in database
        def get_Name(self, Id):
            self.cursor.execute(f"select * from UserInfo where UserId = '{Id}'")
            b = self.cursor.fetchone()
            return b[1]

        #Inserts info into UserInfo table
        def insert_UserInfo(self, usr, arg):
            sql = "insert into UserInfo values (%s, %s)"
            val = (usr, arg)
            self.cursor.execute(sql, val)
            self.mydb.commit()

        #Inserts info into BannedUser table
        def insert_BannedUser(self, usr):
            sql = "insert into BannedUser values (%s)"
            val = (usr,)
            self.cursor.execute(sql, val)
            self.mydb.commit()

        #Deletes info from BannedUser table
        def delete_BannedUser(self, usr):
            sql = f"delete from BannedUser where UserId = {usr}"
            self.cursor.execute(sql)
            self.mydb.commit()

        #Updates name in UserInfo table
        def update_UserInfo(self, arg, usr):
            sql = "update UserInfo set Name = %s where UserId = %s"
            val = (arg, usr)
            self.cursor.execute(sql, val)
            self.mydb.commit()

        #inserts info into Working table
        def insert_Working(self, usr):
            sql = "insert into Working values (%s)"
            val = (usr,)
            self.cursor.execute(sql,val)
            self.mydb.commit()

        #Inserts info into Busy table
        def insert_Busy(self, usr):
            sql = "insert into Busy values (%s)"
            val = (usr,)
            self.cursor.execute(sql,val)
            self.mydb.commit()

        #Deletes info from Working table
        def delete_Working(self, usr):
            sql = f"delete from Working where UserId = {usr}"
            self.cursor.execute(sql)
            self.mydb.commit()

        #Deletes info from Working table
        def delete_Busy(self, usr):
            sql = f"delete from Busy where UserId = {usr}"
            self.cursor.execute(sql)
            self.mydb.commit()

        #Inserts into the Authorized Channels table
        def insert_authChannels(self, id, region):
            sql = "insert into AuthChannels values (%s, %s)"
            val = (id, region)
            self.cursor.execute(sql,val)
            self.mydb.commit()

        def delete_authChannels(self, id):
            sql = f"delete from AuthChannels where ChannelId = {id}"
            self.cursor.execute(sql)
            self.mydb.commit()

        def update_authChannels(self, region, id):
            sql = "update AuthChannels set Region = %s where ChannelId = %s"
            val = (region, id)
            self.cursor.execute(sql, val)
            self.mydb.commit()

        def get_authChannels_region(self, Id):
            self.cursor.execute(f"select * from AuthChannels where ChannelId = '{Id}'")
            b = self.cursor.fetchone()
            return b[1]

        def db_authChannels(self):
            list_f = []
            self.cursor.execute("select ChannelId from AuthChannels")
            b = self.cursor.fetchall()

            for x in b:
                list_f.append(x[0])
            return list_f

        def db_authChannels_byregion(self, region):
            list_f = []
            self.cursor.execute(f"select ChannelId from AuthChannels where Region = '{region}'")
            b = self.cursor.fetchall()

            for x in b:
                list_f.append(x[0])
            return list_f
            
else:
    print('You cannot run this file!\nPlease run the apcsp_bot.py file!')
    exit()