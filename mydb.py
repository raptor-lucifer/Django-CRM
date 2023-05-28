import mysql.connector

#create database object
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
)
#create cursor object  
cursorObject=dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE scorpio")

print("all done")