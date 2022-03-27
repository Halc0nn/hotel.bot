import telebot
import sqlite3
from telebot import types
bot = telebot.TeleBot('')
conn = sqlite3.connect("db.db", check_same_thread = False)
kb = types.ReplyKeyboardMarkup(True,False)
kb.add("Где мой номер?", "О гостинице")
kb.add("Услуги гостиницы", "Обратная связь")
cursor = conn.cursor()
@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, text='Выберите интересующую вас услугу', reply_markup = kb)

@bot.message_handler(regexp="О гостинице")
def about(message):
    cursor.execute('SELECT `info`,`photo` FROM `about` WHERE id = 1')
    rows = cursor.fetchall()
    photo = open(rows[0][1], 'rb')
    bot.send_photo(message.from_user.id, photo, caption = rows[0][0], reply_markup=types.ReplyKeyboardRemove())
    bot.send_photo(message.from_user.id, "FILEID")
    bot.register_next_step_handler(message, start)

if __name__ == '__main__':
    bot.polling(none_stop=True,interval=0)
