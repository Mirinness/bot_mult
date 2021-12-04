import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot("5044535424:AAGn8WcUHezwEFLiDM4P00eLLVtd1-_zjqw")

res=[]

def fm_days():
    sql_text = """SELECT DISTINCT date FROM films LIMIT 10"""
    conn = sqlite3.connect('multiplex.db')
    curs = conn.cursor()
    curs.execute(sql_text)
    global res(curs.fetchall())
    conn.close()
    return res

@bot.message_handler()
def send_welcome(message):
    bot.reply_to(message, 'Привіт! Обери день, коли маєш іти в кінотеатр', reply_markup=markup)


# markup = types.ReplyKeyboardMarkup(row_width=2)
# btn1 = types.KeyboardButton(fm_days[0])
# btn2 = types.KeyboardButton(fm_days[1])
# btn3 = types.KeyboardButton(fm_days[2])
# btn4 = types.KeyboardButton(fm_days[3])
# btn5 = types.KeyboardButton(fm_days[4])
# btn6 = types.KeyboardButton(fm_days[5])
# btn7 = types.KeyboardButton(fm_days[6])
# btn8 = types.KeyboardButton(fm_days[7])
# btn9 = types.KeyboardButton(fm_days[8])
# btn10 = types.KeyboardButton(fm_days[9])
# markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, )

print(res)

bot.infinity_polling()