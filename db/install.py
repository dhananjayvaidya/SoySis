import sqlite3 

connection = sqlite3.connect("../app.db")
c = connection.cursor()

def createTables():
    c.execute("CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY AUTOINCREMENT, key_name TEXT, val TEXT)")
    c.close()
createTables()