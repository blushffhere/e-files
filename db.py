import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # default XAMPP user
        password="",       # default XAMPP password is empty unless changed
        database="testdb"  # replace with your actual DB name
    )
