import random
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup
from datetime import datetime, timedelta
from datetime import time
import pytz  # $ pip install pytz
import tzlocal  # $ pip install tzlocal

bot = telebot.TeleBot('5475765480:AAFr_N5Bj8ZAJQn1Po-8oHOuaw3sdjT1Ik8')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}! Я информационный бот компании Red Machine Games. Наша команда состоит из профессионалов, имеющих за своими плечами большой опыт создания игр.\n\nИнформация, которая может быть тебе полезна:\n\n'f'Наши проекты можно просмотреть на сайте, нажав -> /site. \n\nИнформацию об активных вакансиях можно просмотреть, нажав -> /job. А если ты не нашел вакансию по своему направлению, то всегда можешь написать нашей HR Юлии в телеграме, нажав -> /hr. \n\nМожешь узнать, где находится наш офис, нажав -> /adress.\n\nА если у тебя есть для нас крутое предложение, то незамедлительно пиши на почту! mail@redmachinegames.com </b>'

    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == "/adress":
        bot.send_message(message.chat.id, 'Москва, ул.Кожевническая 7 строение 1. Около 5-ти минут от метро "Павелецкая".', parse_mode='html')
        photo = open(f'1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == '/site':
        website(message)
    elif message.text == '/job':
        websitea(message)
    elif message.text == '/hr':
        bot.send_message(message.chat.id, '@juliesperanskaya', parse_mode='html')
    else:
        bot.send_message(message.chat.id,
                         'Пока что я так не умею, но ты можешь воспользоваться списком команд из приветственного сообщения! Если оно пропало, то нажим /start.',
                         parse_mode='html')


@bot.message_handler(commands=['site'])
def website(message):
    markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Red Machine Games', url="https://redmachinegames.com/"))
    bot.send_message(message.chat.id, 'Наши проекты', reply_markup=markup)


@bot.message_handler(command=['job'])
def websitea(message):
    markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('RMG HeadHunter', url="https://hh.ru/employer/1343803"))
    bot.send_message(message.chat.id, 'Активные вакансии', reply_markup=markup)


bot.polling(none_stop=True)
