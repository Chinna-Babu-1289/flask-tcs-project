# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd = "123123",
# )

# my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE posts")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)
import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv('DBUSER')
print(user)
