import sqlite3
connection = sqlite3.connect("addressbook.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
connection.execute("create table Address (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")
print("Table created successfully")
connection.close()   
