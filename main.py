
import telebot as t
import pymysql 
from config import host, user, password, db_name

bot = t.TeleBot('6123660359:AAG0bKCMhK8bEiKELcdoHzwUHbyJ-hFnPVw')

try:
     connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
     cursor = connection.cursor()
     print('successfully connected...')


     @bot.message_handler(commands=['start'])
     def start_message(message):
          markup = t.types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = t.types.KeyboardButton('Просмотр')
          btn2 = t.types.KeyboardButton('Редактировать')
          markup.add(btn1, btn2)
          bot.send_message(message.chat.id, 'Что хотите сделать?', reply_markup=markup)

     @bot.message_handler(func=lambda message: message.text==['Просмотр'])
     def view_tables(message):
          cursor.execute('SHOW TABLES')
          tables = cursor.fetchall()

          table_names = [table[0] for table in tables]

          markup = t.types.ReplyKeyboardMarkup(resize_keyboard=True)
          buttons = [t.types.KeyboardButton(table_name) for table_name in table_names]
          markup.add(buttons)
          bot.send_message(message.chat.id, 'Какую таблицу желаете посмотреть?', reply_markup=markup)     
     bot.infinity_polling()     
except Exception as ex:
     print('Connection refused')
     print(ex)

