import sqlite3

conn = sqlite3.connect("multiplex.db")
sql = "CREATE TABLE films (date TEXT, film TEXT)"
cursor = conn.cursor()
cursor.execute(sql)
conn.close()