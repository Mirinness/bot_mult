import sqlite3

conn = sqlite3.connect("multiplex.db")
sql = "CREATE TABLE films2 (film TEXT, date TEXT, time TEXT, status TEXT, build TEXT, geo TEXT)"
cursor = conn.cursor()
cursor.execute(sql)
conn.close()