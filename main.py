import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('5177178571:AAF7OJmJMdnvpm4ic-KXRaxR4hRUwc380Vk')

URL = "https://auto.drom.ru/"

transmission=""
bodyStyle=""
wheelDrive=""
price=""
fuelType=""
steeringWheelType=""
color=""
milage=""
horsepowerLowerBound=""
horsepowerUpperBound=""
UrlResult=""


transmissionAvito=""
bodyStyleAvito=""
wheelDriveAvito=""
priceAvito=""
UrlResultAvito=""



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
    global transmission
    global transmission_autoRu
    global bodyStyle
    global bodystyle_autoRu
    global wheelDrive
    global wheelDrive_autoRu
    global price
    global price_autoRu
    global price
    global fuelType
    global fuelType_autoRu
    global steeringWheelType
    global steeringWheelType_autoRu
    global color
    global color_autoRu
    global milage
    global milage_autoRu
    global horsepowerLowerBound
    global horsepowerLowerBound_autoRu
    global horsepowerUpperBound
    global horsepowerUpperBound_autoRu
    global UrlResult
    global UrlResult_autoRu


    if (message.text == "Автоподбор"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        automatic = types.KeyboardButton("Автомат")
        manual = types.KeyboardButton("Механика")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(automatic, manual, back)
        bot.send_message(message.chat.id, text="Выберите тип коробки передач", reply_markup=markup)


    elif (message.text == "Автомат" or message.text == "Механика"):
        if message.text == "Автомат":
            transmission = "&transmission[]=2&transmission[]=3&transmission[]=4&transmission[]=5&transmission[]=-1"
            transmission_autoRu = "&transmission=ROBOT&transmission=AUTOMATIC&transmission=VARIATOR&transmission=AUTO"
        else:
            transmission = "&transmission[]=1"
            transmission_autoRu = "&transmission=MECHANICAL"
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
            bodyStyle = "sedan/all?"
            bodyStyleAvito="sedan/"
            bodystyle_autoRu = "body-sedan/?"
        elif message.text == "Купе":
            bodyStyle = "coupe/all/?"
            bodystyle_autoRu = "body-coupe/?"
        elif message.text == "Универсал":
            bodyStyle = "wagon/all/?"
            bodystyle_autoRu = "body-wagon/?"
        elif message.text == "Внедорожник":
            bodyStyle = "suv/all/?"
            bodystyle_autoRu = "body-allroad/?"
        elif message.text == "Минивен":
            bodyStyle = "van/all/?"
            bodystyle_autoRu = "body-minivan/?"
        elif message.text == "Пикап":
            bodyStyle = "pickup/all/?"
            bodystyle_autoRu = "body-pickup/?"
        elif message.text == "Кабриолет":
            bodyStyle = "open/all/?"
            bodystyle_autoRu = "body-cabrio/?"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        front = types.KeyboardButton("Передний")
        rear = types.KeyboardButton("Задний")
        awd = types.KeyboardButton("Полный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(front, rear, awd, back)
        bot.send_message(message.chat.id, text="Выберите тип привода", reply_markup=markup)


    elif message.text == "Передний" or message.text == "Задний" or message.text == "Полный":
        if message.text == "Передний":
            wheelDrive = "&privod=1"
            wheelDrive_autoRu = "&gear_type=FORWARD_CONTROL"
        elif message.text == "Задний":
            wheelDrive = "&privod=2"
            wheelDrive_autoRu = "&gear_type=REAR_DRIVE"
        elif message.text == "Полный":
            wheelDrive = "&privod=3"
            wheelDrive_autoRu = "&gear_type=ALL_WHEEL_DRIVE"

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
            price = "maxprice=100000"
            price_autoRu = "&price_to=100000"
        elif message.text == "300 000 руб":
            price = "maxprice=300000"
            price_autoRu = "&price_to=300000"
        elif message.text == "500 000 руб":
            price = "maxprice=500000"
            price_autoRu = "&price_to=500000"
            priceAvito="do-500000-rubley-ASgCAgECAUXGmgwWeyJmcm9tIjowLCJ0byI6NTAwMDAwfQ"
        elif message.text == "1 000 000 руб":
            price = "maxprice=1000000"
            price_autoRu = "&price_to=1000000"
        elif message.text == "1 500 000 руб":
            price = "maxprice=1500000"
            price_autoRu = "&price_to=1500000"
        elif message.text == "2 000 000 руб":
            price = "maxprice=2000000"
            price_autoRu = "&price_to=2000000"
        elif message.text == "3 000 000 руб":
            price = "maxprice=3000000"
            price_autoRu = "&price_to=3000000"
        elif message.text == "5 000 000 руб":
            price = "maxprice=5000000"
            price_autoRu = "&price_to=5000000"
        elif message.text == "10 000 000 руб":
            price = "maxprice=10000000"
            price_autoRu = "&price_to=10000000"
        elif message.text == "20 000 000 руб":
            price = "maxprice=20000000"
            price_autoRu = "&price_to=20000000"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Бензин")
        button2 = types.KeyboardButton("Дизель")
        button3 = types.KeyboardButton("Электро")
        button4 = types.KeyboardButton("Гибрид")
        button5 = types.KeyboardButton("ГБО")
        button6 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, text="Выберите тип топлива", reply_markup=markup)

        #UrlResult = URL + bodyStyle + transmission + wheelDrive + price
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #button1 = types.KeyboardButton("Автоподбор")
        #button2 = types.KeyboardButton("Описание авто")
        #button3 = types.KeyboardButton("Подобрать авто!")
        #markup.add(button1, button2, button3)
        #bot.send_message(message.chat.id, text="Подбираем вам авто", reply_markup=markup)



        #UrlResultAvito = "https://auto.ru/moskva/cars/opel/all/"
        #requestAvito = requests.get(UrlResultAvito)
        #bsAvito = BeautifulSoup(requestAvito.text, "html.parser")
        #all_linksAvito = bsAvito.find_all('a')#, {'class': 'Link ListingItemTitle__link'})
        #bot.send_message(message.chat.id, text="Вот, что я подобрал специально для тебя на авто ru")

        #for link in all_linksAvito:
            #bot.send_message(message.chat.id, text="Купил опель - молодец. Засунь в жопу огурец")
            #bot.send_message(message.chat.id, text=link["href"])

    elif message.text=="Бензин" or message.text=="Дизель" or message.text=="Электро"or message.text=="Гибрид"or message.text=="ГБО":
        if message.text=="Бензин":
            fuelType="&fueltype=1"
            fuelType_autoRu = "&engine_group=GASOLINE"
        elif message.text=="Дизель":
            fuelType="&fueltype=2"
            fuelType_autoRu = "&engine_group=DIESEL"
        elif message.text=="Электро":
            fuelType="&fueltype=3"
            fuelType_autoRu = "&engine_group=ELECTRO"
        elif message.text=="Гибрид":
            fuelType="&fueltype=4"
            fuelType_autoRu = "&engine_group=HYBRID"
        elif message.text=="ГБО":
            fuelType="&fueltype=5"
            fuelType_autoRu = "&engine_group=LPG"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Любое расположение")
        button2 = types.KeyboardButton("Левый")
        button3 = types.KeyboardButton("Правый")
        button4 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text="Выберите расположение руля", reply_markup=markup)


    elif message.text=="Любое расположение" or message.text=="Левый" or message.text=="Правый":
        if message.text=="Любое расположение":
            steeringWheelType=""
            steeringWheelType_autoRu = ""
        elif message.text=="Левый":
            steeringWheelType="&w=2"
            steeringWheelType_autoRu = "&steering_wheel=LEFT"
        elif message.text=="Правый":
            steeringWheelType="&w=1"
            steeringWheelType_autoRu = "&steering_wheel=RIGHT"

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
            color=""
            color_autoRu = ""
        elif message.text=="Белый":
            color="&colorid[]=12"
            color_autoRu = "&color=FAFBFB"
        elif message.text=="Черный":
            color="&colorid[]=1"
            color_autoRu = "&color=040001"
        elif message.text=="Коричневый":
            color="&colorid[]=7"
            color_autoRu = "&color=97948F"
        elif message.text=="Зеленый":
            color="&colorid[]=9"
            color_autoRu = "&color=007F00"
        elif message.text=="Фиолетовый":
            color="&colorid[]=2"
            color_autoRu = "&color=4A2197"
        elif message.text=="Серый/Серебристый":
            color="&colorid[]=4&colorid[]=16"
            color_autoRu = "&color=97948F&color=CACECB"
        elif message.text=="Синий/Голубой":
            color="&colorid[]=3&colorid[]=14"
            color_autoRu = "&color=0000CC&color=22A0F8"
        elif message.text=="Бежевый/Желтый/Золотистый":
            color="&colorid[]=13&colorid[]=10&colorid[]=8"
            color_autoRu = "&color=C49648&color=DEA522&color=FFD600"
        elif message.text=="Красный/Бордовый/Оранжевый/Розовый":
            color="&colorid[]=6&colorid[]=11&colorid[]=5&colorid[]=15"
            color_autoRu = "&color=EE1D19&color=660099&color=FF8649&color=FFC0CB"


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
            horsepowerLowerBound="&minpower=1"
            horsepowerUpperBound = "&maxpower=70"
            horsepowerLowerBound_autoRu = ""
            horsepowerUpperBound_autoRu = "&power_to=70"
        if message.text == "71-100 лс":
            horsepowerLowerBound = "&minpower=71"
            horsepowerUpperBound = "&maxpower=100"
            horsepowerLowerBound_autoRu = "&power_from=71"
            horsepowerUpperBound_autoRu = "&power_to=100"
        if message.text == "101-150 лс":
            horsepowerLowerBound = "&minpower=101"
            horsepowerUpperBound = "&maxpower=150"
            horsepowerLowerBound_autoRu = "&power_from=101"
            horsepowerUpperBound_autoRu = "&power_to=150"
        if message.text == "151-200 лс":
            horsepowerLowerBound = "&minpower=151"
            horsepowerUpperBound = "&maxpower=200"
            horsepowerLowerBound_autoRu = "&power_from=151"
            horsepowerUpperBound_autoRu = "&power_to=200"
        if message.text == "201-249 лс":
            horsepowerLowerBound = "&minpower=201"
            horsepowerUpperBound = "&maxpower=249"
            horsepowerLowerBound_autoRu = "&power_from=201"
            horsepowerUpperBound_autoRu = "&power_to=249"
        if message.text == "Более 250 лс":
            horsepowerLowerBound = "&minpower=251"
            horsepowerUpperBound = "&maxpower=10000"
            horsepowerLowerBound_autoRu = "&power_from=250"
            horsepowerUpperBound_autoRu = ""


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

        #UrlResultDrom = "https://auto.drom.ru/" + bodyStyle + price + transmission + wheelDrive
        #request = requests.get(UrlResultDrom)
        #bs = BeautifulSoup(request.text, "html.parser")
        #all_links = bs.find_all('a', {'class': 'css-1ctbluq ewrty961'})
        #bot.send_message(message.chat.id, text="Вот, что я подобрал специально для тебя")

        #for link in all_links:
            #bot.send_message(message.chat.id, text=link["href"])


    elif message.text=="Любой пробег" or message.text=="До 10 000 км" or message.text=="До 30 000 км" or message.text=="До 50 000 км" or message.text=="До 80 000 км" or message.text=="До 100 000 км" or message.text=="До 150 000 км" or message.text=="До 200 000 км" or message.text=="До 300 000 км":
        if message.text=="Любой пробег":
            milage=""
        if message.text=="До 10 000 км":
            milage="&maxprobeg=10000"
            milage_autoRu="km_age_to=10000"
        if message.text == "До 30 000 км":
            milage = "&maxprobeg=30000"
            milage_autoRu = "km_age_to=30000"
        if message.text == "До 50 000 км":
            milage = "&maxprobeg=50000"
            milage_autoRu = "km_age_to=50000"
        if message.text == "До 80 000 км":
            milage = "&maxprobeg=80000"
            milage_autoRu = "km_age_to=80000"
        if message.text == "До 100 000 км":
            milage = "&maxprobeg=100000"
            milage_autoRu = "km_age_to=100000"
        if message.text == "До 150 000 км":
            milage = "&maxprobeg=150000"
            milage_autoRu = "km_age_to=150000"
        if message.text == "До 200 000 км":
            milage = "&maxprobeg=200000"
            milage_autoRu = "km_age_to=200000"
        if message.text == "До 300 000 км":
            milage = "&maxprobeg=300000"
            milage_autoRu = "km_age_to=300000"
        if message.text == "Более 300 000 км":
            milage = "&minprobeg=300000"
            milage_autoRu = "km_age_from=300000"


        UrlResultDrom = "https://auto.drom.ru/" + bodyStyle + price + transmission + fuelType + wheelDrive + color + steeringWheelType + horsepowerLowerBound+horsepowerUpperBound + milage
        request = requests.get(UrlResultDrom)
        bs = BeautifulSoup(request.text, "html.parser")
        all_links = bs.find_all('a', {'class': 'css-eii4kh ewrty961'})[:5]
        bot.send_message(message.chat.id, text="Вот, что я подобрал специально для тебя на drom.ru")
        for link in all_links:
            bot.send_message(message.chat.id, text=link["href"])


        UrlResult_autoRu="https://auto.ru/moskva/cars/all/" + bodystyle_autoRu + transmission_autoRu + fuelType_autoRu + wheelDrive_autoRu + price_autoRu + horsepowerLowerBound_autoRu + horsepowerUpperBound_autoRu + steeringWheelType_autoRu + milage_autoRu + color_autoRu
        request_autoRu = requests.get(UrlResult_autoRu)
        bs_autoRu = BeautifulSoup(request_autoRu.text, "html.parser")
        all_links_autoRu = bs_autoRu('a')
        bot.send_message(message.chat.id, text="Вот, что я подобрал специально для тебя на auto.ru "+str(len(all_links_autoRu)))
        bot.send_message(message.chat.id, text=UrlResult_autoRu)
        for link in all_links_autoRu:
            bot.send_message(message.chat.id, text=link["href"])


        UrlResultAvito="https://www.avito.ru/rossiya/avtomobili"

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
