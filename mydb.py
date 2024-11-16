import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="11341149Tedo!",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All Done!")
