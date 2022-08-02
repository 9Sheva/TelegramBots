import random
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup
from datetime import datetime, timedelta
from datetime import time
import pytz     # $ pip install pytz
import tzlocal  # $ pip install tzlocal
from notifiers import get_notifier
import time
bot = telebot.TeleBot('5515600539:AAGdW-tqItg-mhdIBrnTDeNfKcZvnUOCLoQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, я бот компании Red Machine Games! А ты, видимо, <b>{message.from_user.first_name} ? Ого, наслышан о тебе, гуру геймдэва! Тебе доступен следующий функционал:\n\n' f'Можешь узнать, во сколько окончится твой рабочий день, нажав на  /time. \n\nМожешь узнать, какой кот ты сегодня, нажав на  /mood. Если же тебе выпала собака, то это определенно твой день - шансы на нее крайне малы. Искать собаку можно раз в день, не чаще! Так будет интереснее. \n\nТакже ты можешь перейти на новостной портал, нажав на /news. \n\nА если ты каждое утро за чашечкой чая мониторишь курсы валют, то тебе сюда /course. \n\nПриятного пользования!</b>'

    bot.send_message(message.chat.id, mess, parse_mode='html')

local_timezone = tzlocal.get_localzone()  # pytz-timezone

future_in_half_hour = datetime.now(pytz.utc) + timedelta(hours=9)
local_time = future_in_half_hour.astimezone(local_timezone)
formatted_local_time = local_time.strftime("%H:%M:%S")


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == '/mood':
        photo_number = random.randint(1, 37)
        photo = open(f'{photo_number}.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == '/time':
        bot.send_message(message.chat.id, f'Сегодня твой рабочий день окончится в {formatted_local_time}' , parse_mode='html')
    elif message.text == '/news':
        websites(message)
    elif message.text == '/course':
        website(message)
    else:
        bot.send_message(message.chat.id, 'Пока что я так не умею, но ты всегда можешь воспользоваться командами, которые имеются в приветственном сообщении. Если ты его потерял, то нажми /start.', parse_mode='html')


@bot.message_handler(commands=['news'])
def websites(message):
    markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Все о мире видеоигр', url="https://dtf.ru/s/gamedevnews"))
    bot.send_message(message.chat.id, 'Читать новости', reply_markup=markup)

@bot.message_handler(command=['course'])
def website(message):
    markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Курсы валют в Москве', url="https://www.banki.ru/products/currency/cash/moskva/"))
    bot.send_message(message.chat.id, 'Узнать курс', reply_markup=markup)


#while True:
 #   what = input('O chrm napomnit?\nДля выхода отправьте \'exit\'\n')
  #  if what == 'exit':
   #     break
    #else:
     #   t = input('Через сколько минут напомнить?\n')
      #  t = int(t) * 60
       # time.sleep(t)
        #telegram = get_notifier('telegram')
        #telegram.notify(token='5515600539:AAGdW-tqItg-mhdIBrnTDeNfKcZvnUOCLoQ', chat_id=623440723, message=what)

bot.polling(none_stop=True)
