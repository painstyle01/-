# May the force be with you, Pain.
# 84 + 42 Errors. 31/08/18.

# REMINDER 11/09. Сделать чек статуса проще.
import telebot
import sqlite3
from telebot import types

# !! INIT PART !! #
bot = telebot.TeleBot('474080187:AAH2cJaOoNnVVujRqz1tTNQPTWAS15Aw9C4')# TEMP TOKEN! CHANGE!

main_db = sqlite3.connect("db/main.db", check_same_thread=False)
c_main_db = main_db.cursor()

constants_db = sqlite3.connect("db/constants.db", check_same_thread=False)
c_constants_db = constants_db.cursor()

derill_db = sqlite3.connect("db/derill.db", check_same_thread=False)
c_derill_db = derill_db.cursor()

crane_db = sqlite3.connect("db/crane.db", check_same_thread=False)
c_crane_db = crane_db.cursor()

dev_id = 357572186
# !! INIT PART END !! #

# Check one SQL - "SELECT * FROM derill WHERE id="+str(id[1])+" ORDER BY count DESC LIMIT 1"

# !! KEYBOARD SECTION !! #
# Register role
remove_keyboard = types.ReplyKeyboardRemove()

register_role = types.ReplyKeyboardMarkup(True)
register_role.row("Я клиент и хочу заказать спецтехнику", "Я владелец спецтехники, и хочу заработать")

main_customer = types.ReplyKeyboardMarkup(True)
main_customer.row("Автовышка","Автокран","Кран манипулятор")
main_customer.row("Экскаватор","Самосвал","Грузовик")
main_customer.row("Другая техника")

city_choice = types.ReplyKeyboardMarkup(True)
city_choice.row('Киев')

confirm = types.ReplyKeyboardMarkup(True)
confirm.row('Да')
confirm.row('Нет')

car_derric_1 = types.ReplyKeyboardMarkup(True)
car_derric_1.row('До 15 метров', 'До 18 метров', 'До 22 метров')
car_derric_1.row('До 24 метров', 'До 28 метров', 'До 34 метров')
car_derric_1.row('До 38 метров', 'До 40 метров', 'До 50 метров')

car_derric_2 = types.ReplyKeyboardMarkup(True)
car_derric_2.row("Реклама","Электромонтаж")
car_derric_2.row("Покраска","Обрезка деревьев")
car_derric_2.row("Другое")

car_derric_3 = types.ReplyKeyboardMarkup(True)
car_derric_3.row("Телескопическая")
car_derric_3.row('Локтевая')
car_derric_3.row('Любая')

car_derric_4 = types.ReplyKeyboardMarkup(True)
car_derric_4.row('Тип автовышки',"Высота автовышки")
car_derric_4.row('Вид работы',"Дата начала работ","Место работ")

autocrane_1 = types.ReplyKeyboardMarkup(True)
autocrane_1.row('До 16 мeтров', 'До 20 мeтров', 'До 22 мeтров')
autocrane_1.row('До 28 мeтров', 'До 32 мeтров')
autocrane_1.row('До 38 мeтров', 'До 40 мeтров', 'До 50 мeтров')

pay_type = types.ReplyKeyboardMarkup(True)
pay_type.row('Наличными')
pay_type.row('Карточкой')
pay_type.row('Безналичными')
# !! KEYBOARD SECTION END !! #


# !! MAIN FUNCS SECTION !! #
def register_customer(message):
    id = message.chat.id
    c_main_db.execute("INSERT INTO main(id,role,status) VALUES ('"+str(id)+"','1','1')")
    main_db.commit()


def register_executer(message):
    id = message.chat.id
    c_main_db.execute("INSERT INTO main(id,role,status) VALUES ('" + str(id) + "','2','1')")
    main_db.commit()


def save():
    main_db.commit()
    derill_db.commit()
    crane_db.commit()

# !! MAIN FUNCS SECTION END !! #

# !! DECORATORS SECTION !! #
@bot.message_handler(commands=['start'])
def start(message):
    try:
        c_main_db.execute("SELECT role FROM main WHERE id ="+str(message.chat.id))
        parse = c_main_db.fetchone()
        print(parse[0])
        if parse[0] == 1:
            bot.send_message(message.chat.id, "Здравствуйте. Какой вид спецтехники вам требуется?", reply_markup=main_customer)
        if parse[0] == 2:
            bot.send_message(message.chat.id, 'Executer_message_1. Replying executer keyboard.')
    except:
        bot.send_message(message.chat.id, 'Welcome_text.py. Replying keyboard...', reply_markup=register_role)

@bot.message_handler(commands=['check_last'])
def check_last_order(message):
    text = message.text
    id = text.split(' ')
    c_derill_db.execute("SELECT * FROM derill WHERE id="+str(id[1])+" ORDER BY count DESC LIMIT 1")
    fetch = c_derill_db.fetchone()
    print(fetch)
    bot.send_message(message.from_user.id, ' FETCH - ' +str(fetch))

@bot.message_handler(commands=['id'])
def id_print(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, "Ваш ID - "+str(user_id))

@bot.message_handler(commands=['chat_id'])
def chat_id_print(message):
    bot.send_message(message.chat.id, 'ID чата - '+str(message.chat.id))

@bot.message_handler(commands=['add_admin'])
def add_admin(message):
    text = message.text
    id_new = text.split(' ')
    try:
        c_main_db.execute("SELECT role FROM main WHERE id ="+str(message.from_user.id))
        parse = c_main_db.fetchone()
        if parse[0] == 3:
            bot.send_message(message.chat.id, 'Пользователь с ID '+str(id_new[1])+' успешно добавлен.')
            #bot.send_message(id_new[1], 'Вы добавлены в администраторы. Доступные команды - /help')
            c_main_db.execute("UPDATE main SET role = 3 WHERE id="+str(id_new[1]))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, 'Недостаточно прав на использование команды.')
    except Exception as e:
        bot.send_message(dev_id, e)
        bot.send_message(message.chat.id, 'Не удалось повысить права. Пользователь не зарегестрирован.')



# !! THIS IS THE LAST DECORATOR. !! #
@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == 'Я клиент и хочу заказать спецтехнику':
        try:
            register_customer(message)
            bot.send_message(message.chat.id, "Отлично. Вот что мы можем вам предложить.", reply_markup=main_customer)
        except:
            bot.send_message(message.chat.id, 'Приветствую. Какой вид спецтехники вам требуется??', reply_markup=main_customer)
    if message.text == 'Автовышка':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 1:
            bot.send_message(message.chat.id, 'Хорошо. Нам понадобятся некоторые данные. Пожалуйста, выберите Ваши требования к спецтехнике из клавиатуры ниже.')
            bot.send_message(message.chat.id, 'Какая Вам нужна автовышка?',reply_markup=car_derric_3)
            c_main_db.execute("UPDATE main SET status=2 WHERE id="+str(message.chat.id)+"")
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Телескопическая':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 2:
            bot.send_message(message.chat.id, 'На какой высоте планируются проводиться работы?', reply_markup=car_derric_1)
            c_derill_db.execute("INSERT INTO derill(id,tech_type,tech_meters,tech_usage,tech_usage_comms,month,day,city,pay_type) VALUES ('"+str(message.chat.id)+"','телескопическая ','0','0','0','0','0','0','0')")
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 3 WHERE id=' + str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Локтевая':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 2:
            bot.send_message(message.chat.id, 'На какой высоте планируются проводиться работы?', reply_markup=car_derric_1)
            c_derill_db.execute("INSERT INTO derill(id,tech_type,tech_meters,tech_usage,tech_usage_comms,month,day,city,pay_type) VALUES ('"+str(message.chat.id)+"','локтевая ','0','0','0','0','0','0','0')")
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 3 WHERE id=' + str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Любая':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 2:
            bot.send_message(message.chat.id, 'На какой высоте планируются проводиться работы?', reply_markup=car_derric_1)
            c_derill_db.execute("INSERT INTO derill(id,tech_type,tech_meters,tech_usage,tech_usage_comms,month,day,city,pay_type) VALUES ('" + str(message.chat.id) + "','','0','0','0','0','0','0','0')")
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 3 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 15 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 15 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 18 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 18 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 22 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 22 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 24 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 24 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 28 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 28 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 34 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 34 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 38 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 38 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 40 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 40 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'До 50 метров':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 3:
            bot.send_message(message.chat.id, 'Для каких работ необходима вышка??', reply_markup=car_derric_2)
            c_derill_db.execute("UPDATE derill SET tech_meters = 50 WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 4 WHERE id='+str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Реклама':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 4:
            bot.send_message(message.chat.id, 'Укажите число месяца начала работ.',reply_markup=remove_keyboard)
            c_derill_db.execute("UPDATE derill SET tech_usage = 'рекламы.' WHERE id=" + str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 6 WHERE id=' + str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Электромонтаж':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 4:
            bot.send_message(message.chat.id, 'Укажите число месяца начала работ.',reply_markup=remove_keyboard)
            c_derill_db.execute("UPDATE derill SET tech_usage = 'электромонтажа.' WHERE id=" + str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 6 WHERE id=' + str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Покраска':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 4:
            bot.send_message(message.chat.id, 'Укажите число месяца начала работ.',reply_markup=remove_keyboard)
            c_derill_db.execute("UPDATE derill SET tech_usage = 'покраски.' WHERE id=" + str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 6 WHERE id=' + str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Обрезка деревьев':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 4:
            bot.send_message(message.chat.id, 'Укажите число месяца начала работ.',reply_markup=remove_keyboard)
            c_derill_db.execute("UPDATE derill SET tech_usage = 'обрезки деревьев.' WHERE id=" + str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 6 WHERE id=' + str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    if message.text == 'Другое':
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 4:
            bot.send_message(message.chat.id, 'Опишите  для каких работ вам необходима автовышка.',reply_markup=remove_keyboard)
            c_derill_db.execute("UPDATE derill SET tech_usage = 5 WHERE id=" + str(message.chat.id))
            derill_db.commit()
            c_main_db.execute('UPDATE main SET status = 41 WHERE id=' + str(message.chat.id))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    else:
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 41:
            comm = message.text
            bot.send_message(message.chat.id,"Укажите число месяца начала работ.", reply_markup=remove_keyboard)
            c_main_db.execute("UPDATE main SET status = 6 WHERE id="+str(message.chat.id))
            main_db.commit()
            c_derill_db.execute("UPDATE derill SET tech_usage_comms = '"+str(comm)+"' WHERE id="+str(message.chat.id))
            derill_db.commit()
        if status == 6:
            text = message.text
            month = text.split(' ')
            print(month[0])
            try:
                if int(month[0]) <= 12:
                    c_derill_db.execute("UPDATE derill SET month ="+str(month[0])+" WHERE id="+str(message.chat.id))
                    derill_db.commit()
                    c_main_db.execute("UPDATE main SET status = 7 WHERE id="+str(message.chat.id))
                    main_db.commit()
                    bot.send_message(message.chat.id, "Укажите день работ.")
                else:
                    bot.send_message(message.chat.id, "Ошибка. Укажите верное число месяца.")
            except:
                bot.send_message(dev_id,'Твой косяк, ламер. Исправь.')
        if status == 7:
            text = message.text
            day = text.split(' ')
            print(day[0])
            try:
                if int(day[0]) <= 31:
                    c_derill_db.execute("UPDATE derill SET day =" + str(day[0]) + " WHERE id=" + str(message.chat.id))
                    derill_db.commit()
                    c_main_db.execute("UPDATE main SET status = 8 WHERE id=" + str(message.chat.id))
                    main_db.commit()
                    bot.send_message(message.chat.id, "Укажите время работ.")
                else:
                    bot.send_message(message.chat.id, 'Убедитесь в правильности дня.')
            except:
                bot.send_message(dev_id, 'Опять костыль')
        if status == 8:
            c_derill_db.execute("UPDATE derill SET time = '"+str(message.text)+"' WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_main_db.execute("UPDATE main SET status = 9 WHERE id="+str(message.chat.id))
            main_db.commit()
            bot.send_message(message.chat.id, "Выбирите город или область в котором вы планируете проводить работы.",reply_markup=city_choice)
        if status == 9:
            if message.text == "Киев":
                c_derill_db.execute("UPDATE derill SET city = 'Киев' WHERE id ="+str(message.chat.id))
                derill_db.commit()
                c_main_db.execute("UPDATE main SET status = 10 WHERE id="+str(message.chat.id))
                main_db.commit()
                bot.send_message(message.chat.id, 'Введите адрес проведения работ.', reply_markup=remove_keyboard)
            else:
                bot.send_message(message.chat.id, 'Вашего города пока что нету в списке.')
        if status == 10:
            c_derill_db.execute("UPDATE derill SET adress ='"+str(message.text)+"' WHERE id ="+str(message.chat.id) )
            c_derill_db.execute("SELECT * FROM derill WHERE id="+str(message.chat.id) )
            derill_db.commit()
            c_main_db.execute("UPDATE main SET status = 11 WHERE id="+str(message.chat.id))
            main_db.commit()
            data = c_derill_db.fetchone()
            print(data)
            if data[5] == 5:
                bot.send_message(message.chat.id, 'Давайте убедимся в прваильности заказа.\n'
                                                  'Вам требуется: Автовышка ')
            else:
                day = int(data[7])
                month = int(data[6])
                bot.send_message(message.chat.id, 'Давайте убедимся в правильности заказа.\n'
                                                  'Вам требуется: Автовышка '+str(data[2])+'до ' + str(data[3]) + ' метров для '+str(data[4])+'\n'
                                                                                                                                     'Начало работ: '+str(day)+'.'+str(month)+'.2018 в '+str(data[8])+' в городе '+str(data[9])+' по адресу '
                                                                                                                                                                                                                                ''+str(data[10])+', всё верно?',reply_markup=confirm)
        if status == 11:
            if message.text == 'Да':
                bot.send_message(message.chat.id, 'Каким способом Вам удобно рассчитаться?', reply_markup=pay_type)
                c_main_db.execute("UPDATE main SET status = 12 WHERE id = "+str(message.chat.id))
                main_db.commit()
            if message.text == 'Нет':
                bot.send_message(message.chat.id, 'Вы уверены что хотите отменить заказ? Все данные придется вводить сначала.')
                c_main_db.execute("UPDATE main SET status = 13 WHERE id ="+str(message.chat.id))
        if status == 12:

            bot.send_message(message.chat.id, 'Спасибо! Ваш запрос принят! Ожидайте ответа!\n'
                                              'Возможно Вам понадобится что-то ещё?', reply_markup=main_customer)
            c_main_db.execute("UPDATE main SET status = 1 WHERE id = "+str(message.chat.id))
            main_db.commit()
            c_derill_db.execute("UPDATE derill SET pay_type = 'наличными.' WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_derill_db.execute("SELECT * FROM derill WHERE id ="+str(message.chat.id))
            parse = c_derill_db.fetchone()
            print(parse)
            bot.send_message(-310186468, "НОВЫЙ ЗАКАЗ №"+str(parse[0])+ "\n"
                                                                        "Дата: "+str(parse[7])+'.'+str(parse[6])+'.2018. Время: '+str(parse[8])+'\n'
                                                                                                                                               'Автовышка '+str(parse[2])+' до '+str(parse[3])+' метров для '+str(parse[4])+'\n'
                                                                                                                                                                                                                            'Адрес: '+str(parse[9])+', '+str(parse[10])+'.\n'
                                                                                                                                                                                                                                                                        'Оплата: '+str(parse[11])+'')
    if message.text == "Автокран":
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 1:
            bot.send_message(message.chat.id,'Хорошо. Нам понадобятся некоторые данные. Пожалуйста, выберите Ваши требования к спецтехнике из клавиатуры ниже.')
            bot.send_message(message.chat.id,'Укажите высоту подьема.', reply_markup=autocrane_1)
            c_crane_db.execute("INSERT INTO crane(id) VALUES ('"+str(message.chat.id)+"')")
            c_main_db.execute("UPDATE main SET status=13 WHERE id=" + str(message.chat.id))
            save()
        else:
            bot.send_message(message.chat.id, "К сожалению, я вас не понимаю. Выберите вариант из клавиатуры.")
    id = message.chat.id
    c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
    fetch = c_main_db.fetchone()
    status = fetch[0]
    if status == 13:
        if message.text == "До 16 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
        if message.text == "До 20 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
        if message.text == "До 22 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
        if message.text == "До 28 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
        if message.text == "До 32 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
        if message.text == "До 38 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
        if message.text == "До 40 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
        if message.text == "До 50 мeтров":
            c_crane_db.execute("UPDATE crane SET meters = '50 метров' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=25 WHERE id=" + str(message.chat.id))
            bot.send_message(message.chat.id, 'Опишите груз своими словами.', reply_markup=remove_keyboard)
            save()
    else:
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 25:
            bot.send_message(message.chat.id, 'Укажите размеры груза.')
            c_crane_db.execute("UPDATE crane SET luggage_type='"+str(message.text)+"' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=14 WHERE id="+str(message.chat.id))
            save()
        if status == 14:
            bot.send_message(message.chat.id, 'Укажите количество груза.')
            c_crane_db.execute("UPDATE crane SET luggage_parameters='"+str(message.text)+"' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=15 WHERE id="+str(message.chat.id))
            save()
        if status == 15:
            bot.send_message(message.chat.id, 'Опишите задачу своими словами.')
            c_crane_db.execute("UPDATE crane SET luggage_count='"+str(message.text)+"' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=16 WHERE id="+str(message.chat.id))
            save()
        if status == 16:
            bot.send_message(message.chat.id, 'Введите число месяца работ.')
            c_crane_db.execute("UPDATE crane SET task='"+str(message.text)+"' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status=17 WHERE id="+str(message.chat.id))
            save()
        if status == 17:
            text = message.text
            month = text.split(' ')
            print(month[0])
            try:
                if int(month[0]) <= 12:
                    c_crane_db.execute("UPDATE crane SET month ="+str(month[0])+" WHERE id="+str(message.chat.id))
                    c_main_db.execute("UPDATE main SET status = 18 WHERE id="+str(message.chat.id))
                    bot.send_message(message.chat.id, "Укажите день работ.")
                    save()
                else:
                    bot.send_message(message.chat.id, "Ошибка. Укажите верное число месяца.")
            except:
                bot.send_message(dev_id,'Твой косяк, ламер. Исправь.')
        if status == 18:
            text = message.text
            day = text.split(' ')
            print(day[0])
            try:
                if int(day[0]) <= 31:
                    c_crane_db.execute("UPDATE crane SET date =" + str(day[0]) + " WHERE id=" + str(message.chat.id))
                    c_main_db.execute("UPDATE main SET status = 19 WHERE id=" + str(message.chat.id))
                    bot.send_message(message.chat.id, "Укажите время работ.")
                    save()
                else:
                    bot.send_message(message.chat.id, 'Убедитесь в правильности дня.')
            except:
                bot.send_message(dev_id, 'Опять костыль')
        if status == 19:
            c_crane_db.execute("UPDATE crane SET begin_time = '"+str(message.text)+"' WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status = 21 WHERE id="+str(message.chat.id))
            save()
            bot.send_message(message.chat.id, "Выбирите город или область в котором вы планируете проводить работы.",reply_markup=city_choice)
        if status == 21:
            if message.text == "Киев":
                c_crane_db.execute("UPDATE crane SET city = 'Киев' WHERE id ="+str(message.chat.id))
                c_main_db.execute("UPDATE main SET status = 22 WHERE id="+str(message.chat.id))
                save()
                bot.send_message(message.chat.id, 'Введите адрес проведения работ.', reply_markup=remove_keyboard)
            else:
                bot.send_message(message.chat.id, 'Вашего города пока что нету в списке.')
        if status == 22:
            c_crane_db.execute("UPDATE crane SET adress ='"+str(message.text)+"' WHERE id ="+str(message.chat.id) )
            c_crane_db.execute("SELECT * FROM crane WHERE id="+str(message.chat.id))
            c_main_db.execute("UPDATE main SET status = 23 WHERE id="+str(message.chat.id))
            save()
            data = c_crane_db.fetchone()
            #day = int(data[7])
            #month = int(data[6])
            print(data)
            bot.send_message(message.chat.id, 'Давайте убедимся в правильности заказа.\n'
                                                  'Вам требуется: Автокран до ' + str(data[2]) + ' метров для '+str(data[4])+'\n'
                                                                                                                                     'Начало работ: '+str(day)+'.'+str(month)+'.2018 в '+str(data[8])+' в городе '+str(data[9])+' по адресу '
                                                                                                                                                                                                                                ''+str(data[10])+', всё верно?',reply_markup=confirm)
        if status == 11:
            if message.text == 'Да':
                bot.send_message(message.chat.id, 'Каким способом Вам удобно рассчитаться?', reply_markup=pay_type)
                c_main_db.execute("UPDATE main SET status = 12 WHERE id = "+str(message.chat.id))
                main_db.commit()
            if message.text == 'Нет':
                bot.send_message(message.chat.id, 'Вы уверены что хотите отменить заказ? Все данные придется вводить сначала.')
                c_main_db.execute("UPDATE main SET status = 13 WHERE id ="+str(message.chat.id))
        if status == 12:

            bot.send_message(message.chat.id, 'Спасибо! Ваш запрос принят! Ожидайте ответа!\n'
                                              'Возможно Вам понадобится что-то ещё?', reply_markup=main_customer)
            c_main_db.execute("UPDATE main SET status = 1 WHERE id = "+str(message.chat.id))
            main_db.commit()
            c_derill_db.execute("UPDATE derill SET pay_type = 'наличными.' WHERE id="+str(message.chat.id))
            derill_db.commit()
            c_derill_db.execute("SELECT * FROM derill WHERE id ="+str(message.chat.id))
            parse = c_derill_db.fetchone()
            print(parse)
            bot.send_message(-310186468, "НОВЫЙ ЗАКАЗ №"+str(parse[0])+ "\n"
                                                                        "Дата: "+str(parse[7])+'.'+str(parse[6])+'.2018. Время: '+str(parse[8])+'\n'
                                                                                                                                               'Автовышка '+str(parse[2])+' до '+str(parse[3])+' метров для '+str(parse[4])+'\n'
                                                                                                                                                                                                                            'Адрес: '+str(parse[9])+', '+str(parse[10])+'.\n'
                                                                                                                                                                                                                                                                        'Оплата: '+str(parse[11])+'')
        if status == 13:
            if message.text == 'Да':
                bot.send_message(message.chat.id, 'Ваш заказ удален. Начнем с начала?', reply_markup=main_customer)
                c_main_db.execute("UPDATE main SET status = 1 WHERE id = "+str(message.chat.id))
                main_db.commit()
            if message.text == 'Нет':
                bot.send_message(message.chat.id, 'Edit_data.func()',reply_markup=car_derric_4)





# !! DECORATORS SECTION END !! #


# !! END PART !! #
if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        bot.send_message(dev_id, "!!!ERROR!!!\n"
                                 "Exception code:\n"+ str(e))
