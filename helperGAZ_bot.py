"""Умный помощник в телеграме (ботик) Г ГАЗ
что умеет: под запросы клиента предложит модели автомобилей
дерево решений прорисовано пока в Миро, не буду здесь четкие вопросы переписывать, пожалуйста
на вход от пользователя: клики в опросе
на выходе: предложение подходящих под запросы автомобилей"""

'''ПОДКЛЮЧЕНИЯ'''
import telebot
from telebot import types

bot = telebot.TeleBot('1809227380:AAHzeB6fcyiywzCX_x5NfmQrN-SmRU9rduc')

'''СТАРТ'''
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Привет! Меня зовут Олег, приятно познакомиться, {message.from_user.first_name}.')
    menu(message)

'''МЕНЮ'''
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_st1 = types.KeyboardButton('Красавчик, помоги')
    button_st2 = types.KeyboardButton('Перейти на сайт')
    button_st3 = types.KeyboardButton('Связаться с менеджером')
    keyboard.add(button_st1, button_st2, button_st3)
    bot.send_message(message.chat.id, 'Я умный помощник компании ГАЗ и с радостью помогу тебе с подбором автомобиля --'
                                      ' нажми для этого кнопку "Красавчик, помоги"', reply_markup=keyboard)
    bot.register_next_step_handler(message, get_start)
    # bot.register_next_step_handler(message, menu)


@bot.message_handler(content_types=['text'])
def get_start(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'azgaz.ru')
        menu(message)
    elif message.text == 'Связаться с менеджером':
        bot.send_message(message.chat.id, '@arslanzov')
        menu(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_auto1 = types.KeyboardButton('Перевозка людей')
        button_auto2 = types.KeyboardButton('Перевозка грузов')
        button_auto3 = types.KeyboardButton('Решения для бизнеса')
        button_auto4 = types.KeyboardButton('Коммунальные службы')
        keyboard.add(button_auto1, button_auto2, button_auto3, button_auto4)
        bot.send_message(message.chat.id, 'Для чего вам нужен автомобиль?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_type)


def get_type(message):
    if message.text == 'Перевозка людей':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_ludi1 = types.KeyboardButton('Д')
        button_ludi2 = types.KeyboardButton('Д1')
        button_ludi3 = types.KeyboardButton('Б/Б1')
        button_ludi4 = types.KeyboardButton('Любая')
        keyboard.add(button_ludi1, button_ludi2, button_ludi3, button_ludi4)
        bot.send_message(message.chat.id, 'Какая категория прав водителя подразумевается?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_ludi)
    elif message.text == 'Перевозка грузов':
        bot.send_message(message.chat.id, 'В разработке')
        get_start(message)
    elif message.text == 'Решения для бизнеса':
        bot.send_message(message.chat.id, 'В разработке')
        get_start(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_kom1 = types.KeyboardButton('Уборка снега')
        button_kom2 = types.KeyboardButton('Подъём и перенос грузов')
        button_kom3 = types.KeyboardButton('Выкачивание жидкости')
        button_kom4 = types.KeyboardButton('Транспортировка отходов')
        button_kom5 = types.KeyboardButton('Дорожная техника')
        keyboard.add(button_kom1, button_kom2, button_kom3, button_kom4, button_kom5)
        bot.send_message(message.chat.id, 'Уточните, какую задачу предстоит решать?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_kom)

'''АВТОБУСЫ'''

def get_ludi(message):
    if message.text == 'Д':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_pass1 = types.KeyboardButton('18-30 человек')
        button_pass2 = types.KeyboardButton('Более 30 человек')
        keyboard.add(button_pass1, button_pass2)
        bot.send_message(message.chat.id, 'Сколько людей вы планируете перевозить?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_D_pass)
    elif message.text == 'Д1':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_d1_deti_1 = types.KeyboardButton('Да')
        button_d1_deti_2 = types.KeyboardButton('Нет')
        keyboard.add(button_d1_deti_1, button_d1_deti_2)
        bot.send_message(message.chat.id, 'Вы планируете перевозить 10-17 человек. Планируете ли вы перевозить детей?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_passD1_deti)
    elif message.text == 'Б/Б1':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_B_pass_1 = types.KeyboardButton('До 10 человек')
        button_B_pass_2 = types.KeyboardButton('10-17 человек')
        keyboard.add(button_B_pass_1, button_B_pass_2)
        bot.send_message(message.chat.id, 'Сколько людей вы планируете перевозить?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, get_B_pass)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_any_1 = types.KeyboardButton('До 10 человек')
        button_any_2 = types.KeyboardButton('10-17 человек')
        button_any_3 = types.KeyboardButton('18-30 человек')
        button_any_4 = types.KeyboardButton('Более 30 человек')
        keyboard.add(button_any_1,  button_any_2,  button_any_3,  button_any_4)
        bot.send_message(message.chat.id, 'Сколько людей вы планируете перевозить?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, get_any)

def get_any(message):
    if message.text == 'До 10 человек':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_any10_1 = types.KeyboardButton('Да')
        button_any10_2 = types.KeyboardButton('Нет')
        keyboard.add(button_any10_1, button_any10_2)
        bot.send_message(message.chat.id, 'Планируете ли вы перевозить детей?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_B_deti)
    if message.text == '10-17 человек':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_any17_1 = types.KeyboardButton('Да')
        button_any17_2 = types.KeyboardButton('Нет')
        keyboard.add(button_any17_1, button_any17_2)
        bot.send_message(message.chat.id, 'Планируете ли вы перевозить детей?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, get_passD1_deti)
    elif message.text == '18-20 человек' or 'Более 30 человек':
        get_D_pass(message)

def get_B_pass(message):
    if message.text == 'До 10 человек':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_B_deti_1 = types.KeyboardButton('Да')
        button_B_deti_2 = types.KeyboardButton('Нет')
        keyboard.add(button_B_deti_1, button_B_deti_2)
        bot.send_message(message.chat.id, 'Планируете ли вы перевозить детей?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_B_deti)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_d1_deti_1 = types.KeyboardButton('Да')
        button_d1_deti_2 = types.KeyboardButton('Нет')
        keyboard.add(button_d1_deti_1, button_d1_deti_2)
        bot.send_message(message.chat.id, 'Планируете ли вы перевозить детей?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, get_passD1_deti)

def get_B_deti(message):
    if message.text == 'Да':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Школьный.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для пеервозки детей (до 10 человек) с категорией прав Б/Б1 вам подойдёт Школьный автобус малого класса Соболь Бизнес.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    else:
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/10Б1.jpg', 'rb'))
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/10Б2.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для пеервозки до 10 человек с категорией прав Б/Б1  вам подойдёт Микро Автобус на базе ГАЗель Некст или ГАЗель Соболь.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)

def get_D_pass(message):
    if message.text == '18-30 человек':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_pass18_deti_1 = types.KeyboardButton('Да')
        button_pass18_deti_2 = types.KeyboardButton('Нет')
        keyboard.add(button_pass18_deti_1, button_pass18_deti_2)
        bot.send_message(message.chat.id, 'Планируете ли вы перевозить детей?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_pass18D_deti)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_pass30_deti_1 = types.KeyboardButton('Да')
        button_pass30_deti_2 = types.KeyboardButton('Нет')
        keyboard.add(button_pass30_deti_1, button_pass30_deti_2)
        bot.send_message(message.chat.id, 'Планируете ли вы перевозить детей??', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_pass30D_deti)

def get_pass18D_deti(message):
    if message.text == 'Да':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Школьный.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для пеервозки детей (18-30 человек) с категорией прав Д вам подойдёт Школьный автобус малого класса Соболь Бизнес.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    else:
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/МиниАвтобус.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для пеервозки 18-30 человек с категорией прав Д вам подойдёт Микро Автобус на базе ГАЗель Некст или ГАЗель Соболь.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)

def get_pass30D_deti(message):
    if message.text == 'Да':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Автобус КАВ3.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для пеервозки детей (более 30 человек) с категорией прав Д вам подойдёт Школьный автобус КАВЗ-4235/4238.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_city30_1 = types.KeyboardButton('Междугородние и туристические поездки')
        button_city30_2 = types.KeyboardButton('Городские и пригородные поездки')
        keyboard.add(button_city30_1, button_city30_2)
        bot.send_message(message.chat.id, 'Дальность поездок?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_pass30D_city)

def get_pass30D_city(message):
    if message.text == 'Междугородние и туристические поездки':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/ЛИАЗ ВОЯЖ 525110.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для междугородних поездок вам подойдёт автобус ЛИАЗ ВОЯЖ 525110.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, отавьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    else:
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/ЛИАЗ-5292 РЕСТАЙЛИНГ.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для перевозок по городу вам подойдёт автобус ЛИАЗ-5292 РЕСТАЙЛИНГ.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, отавьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)

def get_passD1_deti(message):
    if message.text == 'Да':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Дети Некст.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для первозки детей (10-17 человек) с категорией прав Д1 вам подойдёт Школьный микроавтобус на базе ГАЗель НЕКТ.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    else:
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/сити.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для первозки пассажиров (10-17 человек) с категорией прав Д1 вам подойдёт пригородный и городской автобус на базе ГАЗЕЛЬ Сити.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)

'''КОММУНАЛЬНАЯ ТЕХНИКА'''

def get_kom(message):
    if message.text == 'Уборка снега':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Снегоуборщик.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Для уборки снега вам подойдёт Комбинированная дорожная машина ГАЗон Next.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, отавьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    elif message.text == 'Подъём и перенос грузов':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/КМУ.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для подъёма и переноса грузов вам подойдёт Кран-манипулятор ГАЗОН NEXT с КМУ UNIC или Садко-Некст бортовой с кму Hyva 27.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, отавьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    elif message.text == 'Выкачивание жидкостей':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Ассенизатор.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для выкачивания жидкостей вам подойдёт ассенизатор Вакуумная машина ГАЗ-САЗ- 39014-12 на шасси ГАЗон НЕКСТ.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
        bot.send_message(message.chat.id, 'Пожалуйста, отавьте обратну связь по моей работе.')
        bot.register_next_step_handler(message, get_obratka)
    elif message.text == 'Транспортировка отходов':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_othod1 = types.KeyboardButton('Твердые отходы')
        button_othod2 = types.KeyboardButton('Перевоз бытовых отходов (сбор из мусорных баков)')
        keyboard.add(button_othod1, button_othod2)
        bot.send_message(message.chat.id, 'Какие отходы вы будете трансопртирвоать?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_othod)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_road1 = types.KeyboardButton('Работа на жд путях')
        button_road2 = types.KeyboardButton('Разметка дорожного полотна')
        keyboard.add(button_road1, button_road2)
        bot.send_message(message.chat.id, 'Уточните задачу, которую предстоит решать?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_road)


def get_othod(message):
    if message.text == 'Твердые отходы':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Самосвал.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для транспортировки твердых отходов вам подойдёт самосвал ГАЗ-САЗ-35125 на шасси Газели-Некст.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
    else:
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Мусоровоз.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для сбора из мусорных баков и перевозки бытовых отходов вам подойдёт Мусоровоз с задней загрузкой KBR-P6N на базе ГАЗ C-41R.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
    bot.send_message(message.chat.id, 'Пожалуйста, отавьте обратну связь по моей работе.')
    bot.register_next_step_handler(message, get_obratka)


def get_road(message):
    if message.text == 'Работа на жд путях':
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/ЖД.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для очищения, ремонта или замены железных путей вам подойдёт путеуборочная или подметально-уборочная машина на базе ГАЗ C-41R.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')
    else:
        bot.send_photo(message.chat.id, open('C:/Users/rusab/Documents/Python_RUDN/lab1/Дорога.jpg', 'rb'))
        bot.send_message(message.chat.id,
                         'Для разметки дорожного полотна вам подойдёт дорожно-разметочная машина на базе ГАЗон НЕКСТ.')
        bot.send_message(message.chat.id,
                         'Свяжитесь с менеджером, чтобы узнать о наличии подходящего автомобиля в дилерском центре: @arslanzov')

    bot.send_message(message.chat.id, 'Пожалуйста, отавьте обратну связь по моей работе.')
    bot.register_next_step_handler(message, get_obratka)

'''СБОР ОБРАТНОЙ СВЯЗИ'''

def get_obratka(message):
    global name
    name = message.text
    doc = open("Obratka.txt", 'a')
    doc.write('{} \n'.format(name))
    doc.close()
    bot.send_message(message.chat.id, 'Спасибо за обратную связь! Давайте вернемся в меню.')
    menu(message)


bot.polling(none_stop=True)
