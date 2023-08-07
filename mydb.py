
import pymysql.connections
import pymysql.cursors
import MySQLdb

dataBase = pymysql.connections.Connection(
    host = 'localhost',
    user = 'root',
    passwd = '04052002'
)

#prepare a cursor object

cursorObject = dataBase.cursor()

#create the DB
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")

