import telebot
from telebot import types
bot = telebot.TeleBot('5721746834:AAHtUP6-BGNignxPBkwmcLACaeGBz0hSHMI')
midterm= ''
endterm= ''
@bot.message_handler(commands=['start'])
def start(message):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Final")
    item2 = types.KeyboardButton("Courses")
    markup.add(item1,item2)
    bot.send_message(message.chat.id,f'Hello, {message.from_user.first_name} {message.from_user.last_name}  /aboutbot  /help',reply_markup=markup)


@bot.message_handler(commands=['aboutbot'])
def aboutbot(message):
    mess2 = 'The Final Project of Daulet , Azamat , Adiya , Damir cs-2120.      The bot that can do all usefull calculations and information'
    bot.send_message(message.chat.id,mess2)


@bot.message_handler(content_types=['text'])
def button(message):
    if message.text == "Final":
        bot.send_message(message.chat.id,'Введи оценку за первую аттестацию(midterm)')
    elif message.text =="Courses": 
        markup =types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("DBMS",callback_data='GOOD')
        item2 = types.InlineKeyboardButton("PYTHON",callback_data='BAD')
        markup.add(item1,item2)
        bot.send_message(message.chat.id,'Выбери урок',reply_markup=markup)



@bot.message_handler(commands=['aboutbot'])
def aboutbot(message):
    mess2 = 'The Final Project of Daulet , Azamat , Adiya , Damir cs-2120.      The bot that can do all usefull calculations and information'
    bot.send_message(message.chat.id,mess2)




bot.polling(none_stop=True)





