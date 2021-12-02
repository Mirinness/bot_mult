import requests
from bs4 import BeautifulSoup
import sqlite3
url = "https://multiplex.ua/soon"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

arr=[]

container = soup.select_one("div.soon_by_day")
days = container.find_all("div",{"class":"soon_el"})

for i in days:
    day = i.select_one("p.el_day_date").text
    fm = i.find_all("span")
    for j in fm:
        arr.append((day, (j).text))

conn = sqlite3.connect("multiplex.db")
cursor = conn.cursor()
cursor.executemany("INSERT INTO films VALUES (?,?)", arr)
conn.commit()
conn.close()