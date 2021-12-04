import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot("5044535424:AAGn8WcUHezwEFLiDM4P00eLLVtd1-_zjqw")

def fm_days():
    sql_text = """SELECT DISTINCT date FROM films LIMIT 10"""
    conn = sqlite3.connect('multiplex.db')
    curs = conn.cursor()
    curs.execute(sql_text)
    res = curs.fetchall()
    conn.close()
    return res

# @bot.message_handler(commands=['start']) """так чомусь не працює"""
@bot.message_handler()
def send_welcome(message):
    bot.reply_to(message, 'Привіт! Обери день, коли маєш іти в кінотеатр', reply_markup=markup)

markup = types.ReplyKeyboardMarkup(row_width=2)
btn1 = types.KeyboardButton('a')
btn2 = types.KeyboardButton('v')
markup.add(btn1, btn2)

bot.infinity_polling()
