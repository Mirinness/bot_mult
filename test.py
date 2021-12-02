# import requests
# from bs4 import BeautifulSoup
# import sqlite3
# url = "https://multiplex.ua/soon"
#
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
#
# container = soup.select_one("div.el_right")
# post = container.find_all("span")
#
# for th in post:
#     a = th.text
#     print(a)


""" тут виводиться один елемент і записується в масив"""
# import requests
# from bs4 import BeautifulSoup
# import sqlite3
# url = "https://multiplex.ua/soon"
#
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
#
# # container = soup.select_one("div.soon_by_day")
# arr=[]
# container = soup.select_one("div.soon_el")
# day = container.select_one("p.el_day_name").text[4:]
# fm = container.find_all("span")
# for i in fm:
#     arr.append((day, (i).text))
# print(arr)

"""Тут спробуємо інший варіант"""
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