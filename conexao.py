import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Sistema_Biblioteca"
    )
    return mydb
