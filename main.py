import telebot
from telebot import types
import wikipedia
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('5177178571:AAF7OJmJMdnvpm4ic-KXRaxR4hRUwc380Vk')

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")

URL = "https://auto.ru/moskva/cars/"

transmission=""
bodyStyle=""
wheelDrive=""
price=""

UrlResult=""


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    selection = types.KeyboardButton("Автоподбор")
    description = types.KeyboardButton("Описание авто")
    test = types.KeyboardButton("Тест")
    markup.add(selection, description, test)
    bot.send_message(message.chat.id,
                     'Привет, я Автобот. Помогу тебе подобрать машину под твои параметры, а также могу рассказать много интересного про любое авто. Список команд открывается командой /help',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    global transmission
    global bodyStyle
    global wheelDrive
    global price
    global UrlResult

    if (message.text == "Автоподбор"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        automatic = types.KeyboardButton("Автомат")
        manual = types.KeyboardButton("Механика")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(automatic, manual, back)
        bot.send_message(message.chat.id, text="Выберите тип коробки передач", reply_markup=markup)


    elif (message.text == "Автомат" or message.text == "Механика"):
        if message.text == "Автомат":
            transmission = ""
        else:
            transmission = ""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sedan = types.KeyboardButton("Седан")
        coupe = types.KeyboardButton("Купе")
        wagon = types.KeyboardButton("Универсал")
        suv = types.KeyboardButton("Внедорожник")
        minivan = types.KeyboardButton("Минивен")
        pickup = types.KeyboardButton("Пикап")
        convertible = types.KeyboardButton("Кабриолет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(sedan, coupe, wagon, suv, minivan, pickup, convertible, back)
        bot.send_message(message.chat.id, text="Выберите тип кузова", reply_markup=markup)

    elif (message.text == "Седан" or message.text == "Купе" or message.text == "Универсал" or message.text == "Внедорожник" or message.text == "Минивен" or message.text == "Пикап" or message.text == "Кабриолет"):
        if message.text == "Седан":
            bodyStyle = "body-sedan/"
        elif message.text == "Купе":
            bodyStyle = "body-coupe/"
        elif message.text == "Универсал":
            bodyStyle = "body-wagon/"
        elif message.text == "Внедорожник":
            bodyStyle = "body-allroad/"
        elif message.text == "Минивен":
            bodyStyle = "body-minivan/"
        elif message.text == "Пикап":
            bodyStyle = "body-pickup/"
        elif message.text == "Кабриолет":
            bodyStyle = "body-cabrio/"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        front = types.KeyboardButton("Передний")
        rear = types.KeyboardButton("Задний")
        awd = types.KeyboardButton("Полный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(front, rear, awd, back)
        bot.send_message(message.chat.id, text="Выберите тип привода", reply_markup=markup)


    elif message.text == "Передний" or message.text == "Задний" or message.text == "Полный":
        if message.text == "Передний":
            wheelDrive = "&gear_type=FORWARD_CONTROL"
        elif message.text == "Задний":
            wheelDrive = "&gear_type=REAR_DRIVE"
        elif message.text == "Полный":
            wheelDrive = "&gear_type=ALL_WHEEL_DRIVE"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        price100000 = types.KeyboardButton("100 000 руб")
        price300000 = types.KeyboardButton("300 000 руб")
        price500000 = types.KeyboardButton("500 000 руб")
        price1000000 = types.KeyboardButton("1 000 000 руб")
        price1500000 = types.KeyboardButton("1 500 000 руб")
        price2000000 = types.KeyboardButton("2 000 000 руб")
        price3000000 = types.KeyboardButton("3 000 000 руб")
        price5000000 = types.KeyboardButton("5 000 000 руб")
        price10000000 = types.KeyboardButton("10 000 000 руб")
        price20000000 = types.KeyboardButton("20 000 000 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(price100000, price300000, price500000, price1000000, price1500000, price2000000, price3000000,
                   price5000000, price10000000, price20000000, back)
        bot.send_message(message.chat.id, text="Выберите ценовую категорию", reply_markup=markup)


    elif message.text == "100 000 руб" or message.text == "300 000 руб" or message.text == "500 000 руб" or message.text == "1 000 000 руб" or message.text == "1 500 000 руб" or message.text == "2 000 000 руб" or message.text == "3 000 000 руб" or message.text == "5 000 000 руб" or message.text == "10 000 000 руб" or message.text == "20 000 000 руб":
        if message.text == "100 000 руб":
            price = "&price_to=100000"
        elif message.text == "300 000 руб":
            price = "&price_to=300000"
        elif message.text == "500 000 руб":
            price = "&price_to=500000"
        elif message.text == "1 000 000 руб":
            price = "&price_to=1000000"
        elif message.text == "1 500 000 руб":
            price = "&price_to=1500000"
        elif message.text == "2 000 000 руб":
            price = "&price_to=2000000"
        elif message.text == "5 000 000 руб":
            price = "&price_to=5000000"
        elif message.text == "10 000 000 руб":
            price = "&price_to=10000000"
        elif message.text == "20 000 000 руб":
            price = "&price_to=20000000"

        UrlResult = URL + bodyStyle + transmission + wheelDrive + price
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Автоподбор")
        button2 = types.KeyboardButton("Описание авто")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Подбираем вам авто", reply_markup=markup)


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Автоподбор")
        button2 = types.KeyboardButton("Описание авто")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


@bot.message_handler(commands=["search"])
def search(message):
    UrlResult = "https://www.avito.ru/rossiya/avtomobili"
    request = requests.get(UrlResult)
    bs = BeautifulSoup(request.text, "html.parser")
    all_links = bs.find('a', {'class':'link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH'})

    for link in all_links:
        bot.send_message(message.chat.id, text="https://www.avito.ru"+link["href"])

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, text="/start - запуск бота, /search - поиск")

# Получение сообщений от юзера
# Запускаем бота
bot.polling(none_stop=True, interval=0)
