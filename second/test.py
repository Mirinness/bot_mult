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


a = [('one',), ('two',), ('three',)]

for i in range(3):
    a[i] = a[i][0]

print(type(a))