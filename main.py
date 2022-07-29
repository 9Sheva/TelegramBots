import telebot
from telebot import types
token='5405357107:AAEu1oBK9fSfUv5XCEnaOEl2g7lQ0w_L7Mw'
bot=telebot.TeleBot(token)
#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id,'Привет, тебе нужно нажать сюда, чтобы увидеть дополнительную информацию /button.')
@bot.message_handler(commands=['start'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Активные вакансии")
    item2 = types.KeyboardButton('Наши проекты')
    item3=types.KeyboardButton('Наш офис')
    item4=types.KeyboardButton('Сотрудничество')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'Привет! Я информационный бот компании Red Machine Games! Использую кнопки, расположенные в меню чата, чтобы найти нужную информацию:)',reply_markup=markup)

@bot.message_handler(content_types=['text'], func=lambda message: message.text =='Активные вакансии')
def func(message):
    markup = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url='https://hh.ru/employer/1343803', text='RMG HeadHunter')
    markup.add(url_btn)
    bot.send_message(message.chat.id, 'Перейди по ссылке', reply_markup=markup)

@bot.message_handler(content_types=['text'], func=lambda message: message.text =='Наши проекты')
def func1(message):
    markup = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url='https://www.redmachinegames.com/', text='RedMachineGames')
    markup.add(url_btn)
    bot.send_message(message.chat.id, 'Мы создали множество успешных игр, часть из которых ты найдешь нанашем сайте', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=='Наши проекты':
        bot.send_message(message.chat.id,'Мы создали множество успешных игр, часть из которых можно найти на нашем сайте https://www.redmachinegames.com/')
    elif message.text=='Наш офис':
        bot.send_message(message.chat.id,'Мы находимся по адресу: г.Москва, ул.Кожевническая, 7/1. Недалеко от метро "Павелецкая. Всегда рады гостям!".',  parse_mode='html')
        photo = open(f'1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text=='Сотрудничество':
        bot.send_message(message.chat.id,'Если у тебя есть крутые идеи и предложения-не стесняйся, пиши на аншу почту! mail@redmachinegames.com')




bot.polling(none_stop=True)
