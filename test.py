import requests
from bs4 import BeautifulSoup
import sqlite3
url = "https://multiplex.ua/soon"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

container = soup.select_one("div.el_right")
post = container.find_all("span")

for th in post:
    a = th.text
    print(a)