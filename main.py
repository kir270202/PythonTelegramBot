import self as self
import telebot
from Car import Car
from telebot import types
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('5177178571:AAF7OJmJMdnvpm4ic-KXRaxR4hRUwc380Vk')

URL = "https://auto.drom.ru/"

car = Car()

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):

    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    selection = types.KeyboardButton("Автоподбор")
    description = types.KeyboardButton("Автоновости")


    markup.add(selection, description)
    bot.send_message(message.chat.id,
                     'Привет, я Автобот. Помогу тебе подобрать машину под твои параметры, а также могу рассказать много интересного про любое авто. Список команд открывается командой /help',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):

    if (message.text == "Автоподбор"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        automatic = types.KeyboardButton("Автомат")
        manual = types.KeyboardButton("Механика")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(automatic, manual, back)
        bot.send_message(message.chat.id, text="Выберите тип коробки передач", reply_markup=markup)


    elif (message.text == "Автомат" or message.text == "Механика"):
        if message.text == "Автомат":
            car.setTransmission("&transmission[]=2&transmission[]=3&transmission[]=4&transmission[]=5&transmission[]=-1")
        else:
            car.setTransmission("&transmission[]=1")

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
            car.setBodyStyle("sedan/all?")
        elif message.text == "Купе":
            car.setBodyStyle("coupe/all/?")
        elif message.text == "Универсал":
            car.setBodyStyle("wagon/all/?")
        elif message.text == "Внедорожник":
            car.setBodyStyle("suv/all/?")
        elif message.text == "Минивен":
            car.setBodyStyle("van/all/?")
        elif message.text == "Пикап":
            car.setBodyStyle("pickup/all/?")
        elif message.text == "Кабриолет":
            car.setBodyStyle("open/all/?")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        front = types.KeyboardButton("Передний")
        rear = types.KeyboardButton("Задний")
        awd = types.KeyboardButton("Полный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(front, rear, awd, back)
        bot.send_message(message.chat.id, text="Выберите тип привода", reply_markup=markup)


    elif message.text == "Передний" or message.text == "Задний" or message.text == "Полный":
        if message.text == "Передний":
            car.setWheelDrive("&privod=1")
        elif message.text == "Задний":
            car.setWheelDrive("&privod=2")
        elif message.text == "Полный":
            car.setWheelDrive("&privod=3")

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
            car.setPrice("maxprice=100000")
        elif message.text == "300 000 руб":
            car.setPrice("maxprice=300000")
        elif message.text == "500 000 руб":
            car.setPrice("maxprice=500000")
        elif message.text == "1 000 000 руб":
            car.setPrice("maxprice=1000000")
        elif message.text == "1 500 000 руб":
            car.setPrice("maxprice=1500000")
        elif message.text == "2 000 000 руб":
            car.setPrice("maxprice=2000000")
        elif message.text == "3 000 000 руб":
            car.setPrice("maxprice=3000000")
        elif message.text == "5 000 000 руб":
            car.setPrice("maxprice=5000000")
        elif message.text == "10 000 000 руб":
            car.setPrice("maxprice=10000000")
        elif message.text == "20 000 000 руб":
            car.setPrice("maxprice=20000000")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Бензин")
        button2 = types.KeyboardButton("Дизель")
        button3 = types.KeyboardButton("Электро")
        button4 = types.KeyboardButton("Гибрид")
        button5 = types.KeyboardButton("ГБО")
        button6 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, text="Выберите тип топлива", reply_markup=markup)


    elif message.text=="Бензин" or message.text=="Дизель" or message.text=="Электро"or message.text=="Гибрид"or message.text=="ГБО":
        if message.text=="Бензин":
            car.setFuelType("&fueltype=1")
        elif message.text=="Дизель":
            car.setFuelType("&fueltype=2")
        elif message.text=="Электро":
            car.setFuelType("&fueltype=3")
        elif message.text=="Гибрид":
            car.setFuelType("&fueltype=4")
        elif message.text=="ГБО":
            car.setFuelType("&fueltype=5")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Любое расположение")
        button2 = types.KeyboardButton("Левый")
        button3 = types.KeyboardButton("Правый")
        button4 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text="Выберите расположение руля", reply_markup=markup)


    elif message.text=="Любое расположение" or message.text=="Левый" or message.text=="Правый":
        if message.text=="Любое расположение":
            car.setSteeringWheelType("")
        elif message.text=="Левый":
            car.setSteeringWheelType("&w=2")
        elif message.text=="Правый":
            car.setSteeringWheelType("&w=1")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Любой цвет")
        button2 = types.KeyboardButton("Белый")
        button3 = types.KeyboardButton("Коричневый")
        button4 = types.KeyboardButton("Зеленый")
        button5 = types.KeyboardButton("Фиолетовый")
        button6 = types.KeyboardButton("Серый/Серебристый")
        button7 = types.KeyboardButton("Синий/Голубой")
        button8 = types.KeyboardButton("Бежевый/Желтый/Золотистый")
        button9 = types.KeyboardButton("Красный/Бордовый/Оранжевый/Розовый")
        button10 = types.KeyboardButton("Любой")
        button11 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button7, button8, button9, button10, button11)
        bot.send_message(message.chat.id, text="Выберите цвет", reply_markup=markup)


    elif message.text=="Белый" or message.text=="Черный" or message.text=="Коричневый" or message.text=="Зеленый" or message.text=="Фиолетовый" or message.text=="Серый/Серебристый" or message.text=="Синий/Голубой" or message.text=="Бежевый/Желтый/Золотистый" or message.text=="Красный/Бордовый/Оранжевый/Розовый" or message.text=="Любой цвет":

        if message.text=="Любой цвет":
            car.setColor("")
        elif message.text=="Белый":
            car.setColor("&colorid[]=12")
        elif message.text=="Черный":
            car.setColor("&colorid[]=1")
        elif message.text=="Коричневый":
            car.setColor("&colorid[]=7")
        elif message.text=="Зеленый":
            car.setColor("&colorid[]=9")
        elif message.text=="Фиолетовый":
            car.setColor("&colorid[]=2")
        elif message.text=="Серый/Серебристый":
            car.setColor("&colorid[]=4&colorid[]=16")
        elif message.text=="Синий/Голубой":
            car.setColor("&colorid[]=3&colorid[]=14")
        elif message.text=="Бежевый/Желтый/Золотистый":
            car.setColor("&colorid[]=13&colorid[]=10&colorid[]=8")
        elif message.text=="Красный/Бордовый/Оранжевый/Розовый":
            car.setColor("&colorid[]=6&colorid[]=11&colorid[]=5&colorid[]=15")


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("До 70 лс")
        button2 = types.KeyboardButton("71-100 лс")
        button3 = types.KeyboardButton("101-150 лс")
        button4 = types.KeyboardButton("151-200 лс")
        button5 = types.KeyboardButton("201-249 лс")
        button6 = types.KeyboardButton("Более 250 лс")
        button7 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, text="Укажите мощность", reply_markup=markup)


    elif message.text=="До 70 лс" or message.text=="71-100 лс" or message.text=="101-150 лс" or message.text=="151-200 лс" or message.text=="201-249 лс" or message.text=="Более 250 лс":
        if message.text == "До 70 лс":
            car.setHorsepowerLowerBound("&minpower=1")
            car.setHorsepowerUpperBound("&maxpower=70")
        if message.text == "71-100 лс":
            car.setHorsepowerLowerBound("&minpower=71")
            car.setHorsepowerUpperBound("&maxpower=100")
        if message.text == "101-150 лс":
            car.setHorsepowerLowerBound("&minpower=101")
            car.setHorsepowerUpperBound("&maxpower=150")
        if message.text == "151-200 лс":
            car.setHorsepowerLowerBound("&minpower=151")
            car.setHorsepowerUpperBound("&maxpower=200")
        if message.text == "201-249 лс":
            car.setHorsepowerLowerBound("&minpower=201")
            car.setHorsepowerUpperBound("&maxpower=249")
        if message.text == "Более 250 лс":
            car.setHorsepowerLowerBound("&minpower=251")
            car.setHorsepowerUpperBound("&maxpower=10000")


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Любой пробег")
        button2 = types.KeyboardButton("До 10 000 км")
        button3 = types.KeyboardButton("До 30 000 км")
        button4 = types.KeyboardButton("До 50 000 км")
        button5 = types.KeyboardButton("До 80 000 км")
        button6 = types.KeyboardButton("До 100 000 км")
        button7 = types.KeyboardButton("До 150 000 км")
        button8 = types.KeyboardButton("До 200 000 км")
        button9 = types.KeyboardButton("До 300 000 км")
        button10 = types.KeyboardButton("Более 300 000 км")
        button11 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
        bot.send_message(message.chat.id, text="Укажите пробег", reply_markup=markup)


    elif message.text=="Любой пробег" or message.text=="До 10 000 км" or message.text=="До 30 000 км" or message.text=="До 50 000 км" or message.text=="До 80 000 км" or message.text=="До 100 000 км" or message.text=="До 150 000 км" or message.text=="До 200 000 км" or message.text=="До 300 000 км":
        if message.text=="Любой пробег":
            car.setMilage("")
        if message.text=="До 10 000 км":
            car.setMilage("&maxprobeg=10000")
        if message.text == "До 30 000 км":
            car.setMilage("&maxprobeg=30000")
        if message.text == "До 50 000 км":
            car.setMilage("&maxprobeg=50000")
        if message.text == "До 80 000 км":
            car.setMilage("&maxprobeg=80000")
        if message.text == "До 100 000 км":
            car.setMilage("&maxprobeg=100000")
        if message.text == "До 150 000 км":
            car.setMilage("&maxprobeg=150000")
        if message.text == "До 200 000 км":
            car.setMilage("&maxprobeg=200000")
        if message.text == "До 300 000 км":
            car.setMilage("&maxprobeg=300000")
        if message.text == "Более 300 000 км":
            car.setMilage("&minprobeg=300000")


        UrlResultDrom = "https://auto.drom.ru/" + car.getBodyStyle() + car.getPrice() + car.getTransmission() + car.getFuelType() + car.getWheelDrive() + car.getColor() + car.getSteeringWheelType() + car.getHorsepowerLowerBound()+car.getHorsepowerUpperBound() + car.getMilage()

        request = requests.get(UrlResultDrom)
        bs = BeautifulSoup(request.text, "html.parser")
        all_links = bs.find_all('a', {'class': 'css-5l099z ewrty961'})[:8]
        bot.send_message(message.chat.id, text="Результаты с портала drom.ru")
        for link in all_links:
            bot.send_message(message.chat.id, text=link["href"])

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Автоподбор")
        button2 = types.KeyboardButton("Автоновости")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Автоподбор")
        button2 = types.KeyboardButton("Автоновости")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "Автоновости"):
        UrlNews = "https://news.drom.ru"
        request2 = requests.get(UrlNews)
        bs2 = BeautifulSoup(request2.text, "html.parser")
        all_links_news = bs2.find_all('a', {'class': 'b-info-block__cont b-info-block__cont_state_reviews'})[:3]
        bot.send_message(message.chat.id, text="Свежие новости с drom.ru специально для тебя!")

        for link in all_links_news:
                bot.send_message(message.chat.id, text=link["href"])


        UrlNewsAutoRu = "https://mag.auto.ru/theme/news/"
        requestNewsAutoRu = requests.get(UrlNewsAutoRu)
        bsNewsAutoRu = BeautifulSoup(requestNewsAutoRu.text, "html.parser")
        all_links_newsAutoRu = bsNewsAutoRu.find_all('a', {'class': 'MagLink MagLink_color_black'})[:3]
        bot.send_message(message.chat.id, text="Свежие новости с auto.ru специально для тебя!")

        for link in all_links_newsAutoRu:
                bot.send_message(message.chat.id, text=link["href"])


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, text="/start - запуск бота, /search - поиск")

bot.polling(none_stop=True, interval=0)
