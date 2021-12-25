import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor

import os

TOKEN = "5044535424:AAGn8WcUHezwEFLiDM4P00eLLVtd1-_zjqw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

kbd1 = ['фільм', 'кінотеатр', 'unknown']
kbd2 = []
kbd3 = []

db = {}

level1 = 1
level2 = 2
level3 = 3

def search_cinema():
    sql_text = """SELECT DISTINCT build FROM films2 LIMIT 10"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text)
    res = curs.fetchall()
    conn.close()
    s = []
    kb_cinema = ReplyKeyboardMarkup()
    for i in res:
        s.append(KeyboardButton(i[0]))
        print(i[0])
    kb_cinema.add(*s)
    return kb_cinema

def search_film():
    sql_text = """SELECT time FROM films2 WHERE film = ?"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text)
    res = curs.fetchall()
    conn.close()
    s = []
    kb_time = ReplyKeyboardMarkup()
    for i in res:
        s.append(KeyboardButton(i[0]))
        print(i[0])
    kb_time.add(*s)
    return kb_time

def is_film(film):
    sql_text = """SELECT film FROM films2 WHERE film = ?"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text, (film,)) # передаємо film як параметр в sql текст
    res = curs.fetchall()
    conn.close()
    if len(res) > 0:
        return True
    else:
        return False

def is_film_time(time):
    sql_text = """SELECT time FROM films2 WHERE film = ?"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text, (time,))
    res = curs.fetchall()
    conn.close()
    if len(res) > 0:
        return True
    else:
        return False

async def on_startup(_):
    print('Бот в онлайні')



@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привіт. Обери опції пошуку', reply_markup=kb_client)


@dp.message_handler(lambda message: message.text == 'фільм')
async def film_open_command(message: types.Message):
    sql_text = """SELECT DISTINCT film FROM films2 LIMIT 10"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text)
    res = curs.fetchall()
    conn.close()

    kb_film = ReplyKeyboardMarkup()
    for i in res:
        kbd2.append(KeyboardButton(i[0]))
    kb_film.add(*kbd2)
    db[message.chat.id] = level2
    for j in range(10):
        res[j] = res[j][0]
    await bot.send_message(message.from_user.id, 'Обери фільм', reply_markup=kb_film)

@dp.message_handler(lambda message: is_film(message.text) and db.get(message.chat.id, 1) == level2)
async def place_command(message: types.Message):
    print(message.text)
    # await message.answer('Ви обрали фільм ' + message.text + '. Тепер оберіть час')
    # c = search_film(message.text)
    # await bot.send_message(message.from_user.id, 'Обери час', reply_markup=c)


@dp.message_handler(lambda message: message.text == 'кінотеатр')
async def cinema_place_command(message: types.Message):
    c = search_cinema()
    await bot.send_message(message.from_user.id, 'Обери кінотеатр', reply_markup=c)





kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(*kbd1)



executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

