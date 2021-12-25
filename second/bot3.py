import sqlite3
import requests
from bs4 import BeautifulSoup

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.utils import executor


TOKEN = "5044535424:AAGn8WcUHezwEFLiDM4P00eLLVtd1-_zjqw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

kbd1 = ['фільм', 'кінотеатр', 'unknown']
kbd2 = []
kbd3 = []

film = ''
time = ''
date = ''

db = {}

level1 = 1
level2 = 2
level3 = 3
level4 = 4

"""-------------------виводить клавіатуру з кінотеатрів-------------------"""
def show_cinemas():
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

"""-------------------виводить клавіатуру з фільмів-------------------"""
def show_films():
    sql_text = """SELECT DISTINCT film FROM films2 LIMIT 10"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text)
    res = curs.fetchall()
    conn.close()
    s = []
    kb_films = ReplyKeyboardMarkup()
    for i in res:
        s.append(KeyboardButton(i[0]))
        print(i[0])
    kb_films.add(*s)
    return kb_films

"""-------------------виводить дату конкретного фільма-------------------"""
def date_film(film):
    sql_text = """SELECT DISTINCT date FROM films2 WHERE film = ?"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text, (film,))
    res = curs.fetchall()
    conn.close()
    s = []
    kb_films = ReplyKeyboardMarkup()
    for i in res:
        s.append(KeyboardButton(i[0]))
        print(i[0])
    kb_films.add(*s)
    return kb_films

"""-------------------виводить години конкретного фільма-------------------"""
def time_film(film, date):
    sql_text = """SELECT time FROM films2 WHERE film = ? AND date = ?"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text, (film, date))
    res = curs.fetchall()
    conn.close()
    s = []
    kb_films = ReplyKeyboardMarkup()
    for i in res:
        s.append(KeyboardButton(i[0]))
        print(i[0])
    kb_films.add(*s)
    return kb_films

"""-------------------генерує посилання-------------------"""
def get_film_link(film, date, time):
    sql_text = """SELECT link FROM films2 WHERE film = ? AND date = ? AND time = ?"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text, (film, date, time))
    res = curs.fetchall()
    temp = res[0][0]
    arr = temp.split("-")
    link1 = arr[0]
    link2 = arr[1]
    link = "https://new.multiplex.ua/order/cinema/" + link1 + "/session/" + link2
    urlkb = InlineKeyboardMarkup(row_width=1)
    urlButton = InlineKeyboardMarkup(text="Посилання", url=link)
    urlkb.add(urlButton)
    return urlkb


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

def is_date_film(date):
    sql_text = """SELECT date FROM films2 WHERE film = ?"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text, (date,)) # передаємо date як параметр в sql текст
    res = curs.fetchall()
    conn.close()
    if len(res) > 0:
        return True
    else:
        return False

def is_film_time(time):
    # sql_text = """SELECT time FROM films2 WHERE date = ?"""
    # conn = sqlite3.connect("multiplex.db")
    # curs = conn.cursor()
    # curs.execute(sql_text, (time,))
    # res = curs.fetchall()
    # conn.close()
    # if len(res) > 0:
    #     return True
    # else:
    #     return False
    return True

async def on_startup(_):
    print('Бот в онлайні')


"""-------------------користувач почав спілкування з ботом-------------------"""
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привіт. Обери опції пошуку', reply_markup=kb_client)

"""-------------------користувач обрав фільм і виводиться список фільмів-------------------"""
@dp.message_handler(lambda message: message.text == 'фільм')
async def film_open_command(message: types.Message):
    c = show_films() #---------------------------------------------------виводиться список фільмів
    db[message.chat.id] = level2
    print("1")
    await bot.send_message(message.from_user.id, 'Обери фільм', reply_markup=c)

"""-------------------виведення дати фільму-------------------"""
@dp.message_handler(lambda message: is_date_film(message.text) and db.get(message.chat.id, 1) == level2)
async def place_command(message: types.Message):
    global film
    film = message.text
    c = date_film(message.text) #-----------------------------------------виводяться дати фільма
    db[message.chat.id] = level3
    print("2")
    await bot.send_message(message.from_user.id, 'Ви обрали фільм ' + message.text + '. Тепер оберіть дату', reply_markup=c)

"""-------------------виведення часу фільму-------------------"""
@dp.message_handler(lambda message: is_film_time(message.text) and db.get(message.chat.id, 1) == level3)
async def place_command(message: types.Message):
    global date
    date = message.text
    c = time_film(film, message.text)
    db[message.chat.id] = level4
    print("3")
    await bot.send_message(message.from_user.id, 'Ви обрали фільм ' + film + ' дата якого ' + message.text + '. Тепер оберіть час', reply_markup=c)

"""-------------------перенесення користувача на сторінку сайту по вибору квитка (місця в залі)-------------------"""
@dp.message_handler(lambda message: is_film_time(message.text) and db.get(message.chat.id, 1) == level4)
async def place_command(message: types.Message):
    global time
    time = message.text
    c = get_film_link(film, date, message.text) # тут message.text це час
    print("4")
    await bot.send_message(message.from_user.id, 'Натисніть на кнопку і Вас буде перенаправлено на сторінку купівлі квитка', reply_markup=c)

"""-------------------користувач обрав кінотеатр і виводиться список кінотеатрів-------------------"""
@dp.message_handler(lambda message: message.text == 'кінотеатр')
async def cinema_place_command(message: types.Message):
    c = show_cinemas()
    await bot.send_message(message.from_user.id, 'Обери кінотеатр', reply_markup=c)











kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(*kbd1)
executor.start_polling(dp, skip_updates=False, on_startup=on_startup)