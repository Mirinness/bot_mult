import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor

import os

TOKEN = "5044535424:AAGn8WcUHezwEFLiDM4P00eLLVtd1-_zjqw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def search_film():
    sql_text = """SELECT DISTINCT film FROM films2 LIMIT 10"""
    conn = sqlite3.connect("multiplex.db")
    curs = conn.cursor()
    curs.execute(sql_text)
    res = curs.fetchall()
    conn.close()
    # ---------------Тут має бути код, який видаляє попередню клавіатуру kb_client
    kb_film = ReplyKeyboardMarkup
    for i in res:
        kb_film.row(KeyboardButton(i))
    return res

async def on_startup(_):
    print('Бот в онлайні')



@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привіт. Обери опції пошуку', reply_markup=kb_client)


@dp.message_handler(commands=['фільм'])
async def pizza_open_command(message: types.Message):

    await bot.send_message(message.from_user.id, 'Обери фільм', reply_markup=kb_film) # ----------------тут у відповідь клієнту має відображатися інша клавіатура kb_film, яка попередньо створена у функції search_film


@dp.message_handler(commands=['кінотеатр'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Повідомлення 3')

button1 = KeyboardButton('/фільм')
button2 = KeyboardButton('/кінотеатр')
button3 = KeyboardButton('3')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(button1, button2, button3)




# @dp.message_handler(commands=['Меню'])
# async def pizza_menu_command(message: types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')


'''*******************************АДМИНСКАЯ ЧАСТЬ*******************************************'''

'''*********************************ОБЩАЯ ЧАСТЬ*********************************************'''


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет!')


# await message.reply(message.text)
# await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
