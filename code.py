import sqlite3
import requests
from bs4 import BeautifulSoup as BS

def create_db():
    # sql_text = """CREATE TABLE film (film_now TEXT NO NULL, date NUMBER REAL NOT NULL)"""
    sql_text = """CREATE TABLE film (film_now TEXT NO NULL)"""
    conn = sqlite3.connect('film.db')
    curs = conn.cursor()
    curs.execute(sql_text)
    conn.close()

def insert_data(film_now):
    sql_text = """INSERT INTO film VALUES (?)"""
    conn = sqlite3.connect("film.db")
    curs = conn.cursor()
    curs.execute(sql_text, (film_now))
    conn.commit()
    conn.close()

data = []

r = requests.get("https://multiplex.ua/soon")
html = BS(r.content, 'html.parser')

for el in html.select(".soon_el > .el_right"):
    title = el.select(".soon_fm_name")
    data.append(title[0].text)

for item in data:
    insert_data(item)

