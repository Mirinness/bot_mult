# import sqlite3
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# from aiogram.utils import executor
#
# sql_text = """SELECT DISTINCT film FROM films2 LIMIT 10"""
# conn = sqlite3.connect("multiplex.db")
# curs = conn.cursor()
# curs.execute(sql_text)
# res = curs.fetchall()
# conn.close()
# kb_film = ReplyKeyboardMarkup
# for i in res:
#     kb_film.row(KeyboardButton(i))
# return res


# a = [('one',), ('two',), ('three',)]
# b = ['1', '2', '3']
#
# print(*b)
# print(b)
"""---------------------------------------------"""

# import requests
# from bs4 import BeautifulSoup
#
# def link(date, film, time):
#     test={}
#     # date="25122021"
#     # film="Співай 2"
#     # time="13:40"
#     r = requests.get("https://multiplex.ua/cinema/kyiv/tsum")
#     soup = BeautifulSoup(r.text, 'lxml')
#     lvl1 = soup.find('div', attrs={'data-date': date})
#     lvl2 = lvl1.find_all('div', attrs={'data-name': film})
#     for i in lvl2:
#         test.update(
#             {
#                 i.find('p', class_='time').text :
#                 i.get('data-id')
#             }
#         )
#
#     arr = test[time].split("-")
#
#     link1 = arr[0]
#     link2 = arr[1]
#     link = "https://new.multiplex.ua/order/cinema/" + link1 + "/session/" + link2
#     return link
#
# print(link("26122021", "Співай 2", "11:40"))
# print(test)
# print(test[time])
"""------------ще одне повторення РЕАЛЬНО РОБОЧА ФУНКЦІЯ----------------"""
# import requests
# from bs4 import BeautifulSoup
#
# def link_pay(date, film, time):
#     test = {}
#     r = requests.get("https://multiplex.ua/cinema/kyiv/tsum") # ТАКОЖ ЗМІНИТИ ПОСИЛАННЯ ДЛЯ КОЖНОГО ФІЛЬМУ ВІДПОВІДНО
#     soup = BeautifulSoup(r.text, 'lxml')
#     lvl1 = soup.find('div', attrs={'data-date': date})
#     lvl2 = lvl1.find_all('div', attrs={'data-name': film})
#     for i in lvl2:
#         test.update(
#             {
#                 i.find('p', class_='time').text :
#                 i.get('data-id')
#             }
#         )
#     arr = test[time].split("-")
#     link1 = arr[0]
#     link2 = arr[1]
#     link = "https://new.multiplex.ua/order/cinema/" + link1 + "/session/" + link2
#     return link


"""---------------------------------------------"""
# test = "0000000031-21489"
#
# arr = test.split("-")
# link1 = arr[0]
# link2 = arr[1]
# print(link1)
# print(link2)

#h = soup.select_one('div', class_="ns locked")
# arr = soup.find_all('div', attrs={'data-name': 'Людина-павук: Додому шляху нема '})
# for i in arr:
#     test.append(i.find('p', class_='time').text)
#s = h.get("time")

# my_st = "синий,оранжевый,красный"
# print(my_st.split(","))

# arr = soup.find_all('p', class_="time")
# for i in arr:
#     b = i.text
#     print(b)
#print(arr)
"""test"""
# a = "Лавіна"
# kin_th = (
#     'Multiplex',
#     {
#         'Цум' : 'https://multiplex.ua/cinema/kyiv/tsum',
#         'Лавіна' : 'https://multiplex.ua/cinema/kyiv/lavina',
#         'Республіка' : 'https://multiplex.ua/cinema/kyiv/respublika',
#         'Проспект' : 'https://multiplex.ua/cinema/kyiv/prospect',
#         'Комод' : 'https://multiplex.ua/cinema/kyiv/komod',
#         'Атмосфера' : 'https://multiplex.ua/cinema/kyiv/atmosphera',
#         'Краван': 'https://multiplex.ua/cinema/kyiv/karavan',
#         'Ретровіль': 'https://multiplex.ua/cinema/kyiv/retroville'
#     }
# )
# print(kin_th[1][a])
#-------------------------------------------------------------------
# import sqlite3
#
# def time_film(film):
#     sql_text = """SELECT time FROM films2 WHERE film = ?"""
#     conn = sqlite3.connect("multiplex.db")
#     curs = conn.cursor()
#     curs.execute(sql_text, (film,))
#     res = curs.fetchall()
#     conn.close()
#     s = []
#     # kb_films = ReplyKeyboardMarkup()
#     for i in res:
#         s.append(i[0])
#         print(i[0])
#     return
#
# a = "Лускунчик"
# print(time_film(a))
import sqlite3

def time_film(film):
    sql_text = """SELECT time, date FROM films2 WHERE film = ? AND date = 24122021 AND build = 'ЦУМ'"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text, (film,))
    res = curs.fetchall()
    conn.close()
    print(res)

time_film("Співай 2")