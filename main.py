import telebot
import yaml
from telebot import types
from yaml.loader import SafeLoader
from datetime import datetime
data = {}
now = datetime.now()
current_time = now.strftime("%H:%M")
str1= "Текущее время :"
str2 = str1 + current_time

bot = telebot.TeleBot("5246042835:AAFY86NskjMBb3xToabKheCIKqsaC4OO8rU")

with open('Test1.txt', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, indent=4, default_flow_style=False, allow_unicode=True)

with open('Test1.yml', encoding='utf-8') as file:
    documents = yaml.load(file, Loader=SafeLoader)
    alola = " ".join(map(str, documents))
    strings = []
    for key, item in documents.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    result = "; ".join(strings)
    S = "\n".join(result.split("-"))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Расписание')
    item2 = types.KeyboardButton('ДЗ и дедлайны')
    item3 = types.KeyboardButton('Лекции')
    item4 = types.KeyboardButton('Раписание экзаменов')
    item5 = types.KeyboardButton('Полезные ссылки')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Доброго времени суток, {0.first_name}!'.format(message.from_user),
                     reply_markup=markup)
    bot.send_message(message.chat.id,str2)



@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Расписание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Показать действующее')
            item2 = types.KeyboardButton('Добавить')
            item3 = types.KeyboardButton('Изменить')
            item4 = types.KeyboardButton('Удалить')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Расписание', reply_markup=markup)

        elif message.text == 'Показать действующее':
            bot.send_message(message.chat.id, S)




        elif message.text == 'ДЗ и дедлайны':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Действующее ДЗ')
            item2 = types.KeyboardButton('Добавить')
            item3 = types.KeyboardButton('Изменить')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'ДЗ и дедлайны', reply_markup=markup)
        elif message.text == 'Действующее ДЗ':
            bot.send_message(message.chat.id, 'Досдать 2 лабу\n'
                                              'Подготовиться к коллоку по матану и ангему\n'
                                              'Записать видос на пп\n')




        elif message.text == 'Лекции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Действующие лекции')
            item2 = types.KeyboardButton('Добавить')
            item3 = types.KeyboardButton('Изменить')
            item4 = types.KeyboardButton('Удалить')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Лекции', reply_markup=markup)

        elif message.text == 'Действующие лекции':
            bot.send_message(message.chat.id, '...\n')





        elif message.text == 'Раписание экзаменов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Действующие экзамены')
            item2 = types.KeyboardButton('Добавить')
            item3 = types.KeyboardButton('Изменить')
            item4 = types.KeyboardButton('Удалить')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Раписание экзаменов', reply_markup=markup)

        elif message.text == 'Действующие экзамены':
            bot.send_message(message.chat.id, 'Пока не знаем!¯\_(ツ)_/¯\n'
                                              'Где то в мае скажут\n')



        elif message.text == 'Полезные ссылки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Ссылки')
            item2 = types.KeyboardButton('Добавить')
            item3 = types.KeyboardButton('Изменить')
            item4 = types.KeyboardButton('Удалить')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Полезные ссылки', reply_markup=markup)
        elif message.text == 'Ссылки':
            bot.send_message(message.chat.id,
                             '1. Физика: https://potatohd.notion.site/c16df808f57f46858156e98ba7e06d29\n'
                             '2. Физика: https://drive.google.com/drive/folders/1BA5NRNSTnX9azVnpklmVYM3ncbIuO30m\n'
                             '3.Notion по 2 сему:https://potatohd.notion.site/2-2021-f5eafffde8b844ef9b8420d68c6a669c\n')

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Расписание')
            item2 = types.KeyboardButton('ДЗ и дедлайны')
            item3 = types.KeyboardButton('Лекции')
            item4 = types.KeyboardButton('Раписание экзаменов')
            item5 = types.KeyboardButton('Полезные ссылки')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


bot.polling(none_stop=True)
