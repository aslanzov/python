"""Умный помощник в телеграме (ботик) Г ГАЗ

что умеет: под запросы клиента предложит модели автомобилей

дерево решений прорисовано пока в Миро, не буду здесь четкие вопросы переписывать, пожалуйста

на вход от пользователя: клики в опросе
на выходе: предложение подходящих под запросы автомобилей"""

"""Библиотеки: PyTelegramBotAPI, json, telegram.ext"""
import telebot
from telebot import types

bot = telebot.TeleBot('1809227380:AAHzeB6fcyiywzCX_x5NfmQrN-SmRU9rduc')

# запустить сервер с ботом, подгрузить базу вопросов и решений
# принять сигнал с кнопки 'start' бота
# приветственное сообщение об умном помощнике - выводится само

"""ДОП КНОПКИ в меню:
*связаться с менеджером
*перейти в шоурум
*help
"""


@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_st1 = types.KeyboardButton('Красавчик помоги')
        button_st2 = types.KeyboardButton('Перейти на сайт')
        button_st3 = types.KeyboardButton('Связаться с менеджером')
        button_st4 = types.KeyboardButton('Помощь')
        keyboard.add(button_st1, button_st2, button_st3, button_st4)
        bot.send_message(message.chat.id,
                         f'Привет! Меня зовут Олег, приятно познакомиться, {message.from_user.first_name}. '
                         f'Я умный помощник компании ГАЗ и с радостью помогу тебе с подбором автомобиля - нажми для '
                         f'этого кнопку "Красавчик помоги"',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, get_start)
    else:
        bot.send_message(message.from_user.id, 'Error')


# 1ая итерация - общий вопрос дерева
# считать сигнал кнопки - получение ответа от пользователя в опросе

@bot.message_handler(content_types=['text'])
def get_start(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'azgaz.ru')
    elif message.text == 'Связаться с менеджером':
        bot.send_message(message.chat.id, '@arslanzov')
    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, 'Помоги себе сам')
    elif message.text == 'Красавчик помоги':
        bot.register_next_step_handler(message, get_helper)
        return get_helper(message)
    else:
        bot.send_message(message.from_user.id, 'Error1')


def get_helper(message):
    if message.text == 'Красавчик помоги':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_auto1 = types.KeyboardButton('Перевозка людей')
        button_auto2 = types.KeyboardButton('Перевозка грузов')
        button_auto3 = types.KeyboardButton('Решения для бизнеса')
        button_auto4 = types.KeyboardButton('Коммунальные службы')
        keyboard.add(button_auto1, button_auto2, button_auto3, button_auto4)
        bot.send_message(message.chat.id, 'Для чего вам нужен автомобиль?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_type)
        return get_type(message)
    else:
        bot.send_message(message.from_user.id, 'Error2')


def get_type(message):
    if message.text == 'Перевозка людей':
        bot.send_message(message.chat.id, 'В разработке')
        return get_type(message)
    elif message.text == 'Перевозка грузов':
        bot.send_message(message.chat.id, 'В разработке')
        return get_type(message)
    elif message.text == 'Решения для бизнеса':
        bot.send_message(message.chat.id, 'В разработке')
        return get_type(message)
    elif message.text == 'Комунальные службы':
        bot.register_next_step_handler(message, get_kom)
        return get_kom(message)
    else:
        bot.send_message(message.from_user.id, 'Error3')


def get_kom(message):
    if message.text == 'Коммунальные службы':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_kom1 = types.KeyboardButton('Уборка снега')
        button_kom2 = types.KeyboardButton('Подъём и перенос грузов')
        button_kom3 = types.KeyboardButton('Выкачивание жидкости')
        button_kom4 = types.KeyboardButton('Транспортировка отходов')
        button_kom5 = types.KeyboardButton('Дорожная техника')
        keyboard.add(button_kom1, button_kom2, button_kom3, button_kom4, button_kom5)
        bot.send_message(message.chat.id, 'Уточните, какую задачу предстоит решать?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_kom_dop)
        return get_kom_dop(message)
    else:
        bot.send_message(message.from_user.id, 'Error4')


def get_kom_dop(message):
    if message.text == 'Уборка снега':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Снегоуборщик.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для уборки снега вам подойдёт Комбинированная дорожная машина ГАЗон Next.')
        bot.send_message(message.chat.id, 'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре.')
    elif message.text == 'Подъём и перенос грузов':
        bot.send_message(message.chat.id, 'Ищу')
        #bot.send_photo(message.chat.id, open('C:\Users\rusab\Documents\Python_RUDN\lab1\Снегоуборщик.jpg', 'rb'))
        #bot.send_message(message.chat.id,
        #                     'Для уборки снега вам подойдёт Комбинированная дорожная машина ГАЗон Next.')
        #bot.send_message(message.chat.id,
        #                     'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре.')
    elif message.text == 'Выкачивание жидкостей':
        bot.send_message(message.chat.id, 'Ищу')
        # bot.send_photo(message.chat.id, open('C:\Users\rusab\Documents\Python_RUDN\lab1\Снегоуборщик.jpg', 'rb'))
        # bot.send_message(message.chat.id,
        #                     'Для уборки снега вам подойдёт Комбинированная дорожная машина ГАЗон Next.')
        # bot.send_message(message.chat.id,
        #                     'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре.')
    elif message.text == 'Транспортировка отходов':
        bot.send_message(message.chat.id, 'Ищу')
        # bot.send_photo(message.chat.id, open('C:\Users\rusab\Documents\Python_RUDN\lab1\Снегоуборщик.jpg', 'rb'))
        # bot.send_message(message.chat.id,
        #                     'Для уборки снега вам подойдёт Комбинированная дорожная машина ГАЗон Next.')
        # bot.send_message(message.chat.id,
        #                     'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре.')
    elif message.text == 'Дорожная техника':
        bot.send_message(message.chat.id, 'Ищу')
        # bot.send_photo(message.chat.id, open('C:\Users\rusab\Documents\Python_RUDN\lab1\Снегоуборщик.jpg', 'rb'))
        # bot.send_message(message.chat.id,
        #                     'Для уборки снега вам подойдёт Комбинированная дорожная машина ГАЗон Next.')
        # bot.send_message(message.chat.id,
        #                     'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре.')
    else:
        bot.send_message(message.from_user.id, 'Error5')

def get_othod(message):
    bot.send_message(message.from_user.id, 'PAMAGIIITII')

# 2ая итерация - пошли по ветке, зависит от ответа пользователя
# считать сигнал кнопки - получение ответа от пользователя в опросе

# .
# .
# .

# напомнить о себе, если не дошел пользователь до решения

# .
# .
# .

# nая итареция - получили ответ на последний вопрос ветки (всего их от 3ех до 5ти в зависимости от ветки)
# считать сигнал кнопки - получение ответа от пользователя в опросе

# отправить пользователю фотографии подходящих моделей автомобилей + характеристики и ссылка на сайте

# отправить сообщение о возможностях шоурума на сайте

# отправить сообщение и опрос с обратной связью/оценкой удовлетворенностью
# считать обратную связь

bot.polling(none_stop=True)
