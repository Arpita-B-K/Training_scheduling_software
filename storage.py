import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host = "localhost")
    if connection.is_connected():

except Error as e:
    print("!!!!! error while connecting !!!!!")

finally:
    if(connection.is_connected()):
        