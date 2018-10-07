# May the force be with you, Pain.
# 84 + 42 Errors. 31/08/18.

# REMINDER 11/09. Сделать чек статуса проще.
import telebot
import sqlite3
from telebot import types

# !! INIT PART !! #
bot = telebot.TeleBot('474080187:AAH2cJaOoNnVVujRqz1tTNQPTWAS15Aw9C4')# TEMP TOKEN! CHANGE!
upd = bot.get_updates()
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)
#telebot.TeleBot.threaded()
telebot.apihelper.CONNECT_TIMEOUT = 9999 # UNSTOPABLE!

main_db = sqlite3.connect("db/main.db", check_same_thread=False)
c_main_db = main_db.cursor()

executors_db = sqlite3.connect('db/executors.db', check_same_thread=False)
c_executors_db = executors_db.cursor()

constants_db = sqlite3.connect("db/constants.db", check_same_thread=False)
c_constants_db = constants_db.cursor()

derill_db = sqlite3.connect("db/derill.db", check_same_thread=False)
c_derill_db = derill_db.cursor()

crane_db = sqlite3.connect("db/crane.db", check_same_thread=False)
c_crane_db = crane_db.cursor()

crane_arm = sqlite3.connect('db/crane_arm.db', check_same_thread=False)
c_crane_arm = crane_arm.cursor()

excalator_db = sqlite3.connect('db/excalator.db', check_same_thread=False)
c_excalator_db = excalator_db.cursor()

dev_id = 357572186
derill_chat = 'https://t.me/joinchat/FVAeWlByBoChbPLF0M9bmg'
crane_chat = 'https://t.me/joinchat/FVAeWk2sv5YhUt07YeV1lA'
crane_arm_chat = 'https://t.me/joinchat/FVAeWkTwyfzqIWSeK7r3iQ'
excalator_chat = 'https://t.me/joinchat/FVAeWk7bLVRaNlidJqUl-g'
samosval_chat = 'https://t.me/joinchat/FVAeWkw0jAhgr1DGB6BpcA'
truck_chat = 'https://t.me/joinchat/FVAeWlBy7gH6UJVlmNJRJA'
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

city_choice = types.ReplyKeyboardMarkup(True)
city_choice.row('Киев')

confirm = types.ReplyKeyboardMarkup(True)
confirm.row('Да')
confirm.row('Нет')

executors_1 = types.ReplyKeyboardMarkup(True)
executors_1.row("Автoвышка","Автoкран","Кран манипулятoр")
executors_1.row("Экскаватoр","Самoсвал","Грузoвик")

executors_2 = types.ReplyKeyboardMarkup(True)
executors_2.row('Профиль')
executors_2.row('Активный заказ')

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

crane_arm_1 = types.ReplyKeyboardMarkup(True)
crane_arm_1.row("ЖБК","Кирпич на паллетах","Газоблок")
crane_arm_1.row("Вагончик","Кольца","Другое")

excalator_1 = types.ReplyKeyboardMarkup(True)
excalator_1.row('JCB 3','JCB 4','Полноповоротник колесный')
excalator_1.row('Полноповоротник гусеничный','Другой')

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
    crane_arm.commit()
    excalator_db.commit()
    executors_db.commit()

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
            bot.send_message(message.chat.id, 'ПРОФИЛЬ.')
    except:
        bot.send_message(message.chat.id, 'Приветствуем Вас в сервисе обмена заказами СПЕЦРЕНТ.\nВыберите роль', reply_markup=register_role)

@bot.message_handler(commands=['a_chats'])
def a_chats(message):
    bot.send_message(message.chat.id, 'ЧАТЫ'
                                      '\n[Автовышка]('+str(derill_chat)+')'
                                      '\n[Автокран]('+str(crane_chat)+')'
                                      '\n[Кран манипулятор]('+str(crane_arm_chat)+')'
                                      '\n[Самосвал]('+str(samosval_chat)+')'
                                      '\n[Грузовик]('+str(truck_chat)+')'
                                      '\n[Экскаватор]('+str(excalator_chat)+')', parse_mode='Markdown')

@bot.message_handler(content_types=['new_chat_members'])
def chat_rules(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!'
                                      '\n\n'
                                      'В этом чате вы можете получить заказы, а так же общатся с другими владельцами техники.'
                                      '\n'
                                      'Для того что б общение было приятным, существует ряд правил:\n'
                                      '1) Запрещено оскорбление в сторону других людей | Наказание: Режим "только чтение" на 24 часа.'
                                      '\n2) Запрещено публиковать рекламные ссылки. | Наказание: Режим "только чтение" на 2 часа.'
                                      '\n3) Запрещено злоупотреблять ненормативной лексикой. | Наказание: Режим "только чтение" на 1 час.'
                                      '\n'
                                      '\nПриятного общения!')

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
            #bot.send_message(id_new[1], 'Вы добавлены в администраторы. Доступные команды - /ahelp')
            c_main_db.execute("UPDATE main SET role = 3 WHERE id="+str(id_new[1]))
            main_db.commit()
        else:
            bot.send_message(message.chat.id, 'Недостаточно прав на использование команды.')
    except Exception as e:
        bot.send_message(dev_id, e)
        bot.send_message(message.chat.id, 'Не удалось повысить права. Пользователь не зарегестрирован.')

@bot.message_handler(content_types=['contact'])
def contact_get(message):
    phone = message.contact.phone_number
    print(phone)
    c_main_db.execute('UPDATE main SET status = 501 WHERE id='+str(message.chat.id))
    c_executors_db.execute("UPDATE executors SET phone ='"+str(phone)+"' WHERE id="+str(message.chat.id))
    save()
    bot.send_message(message.chat.id, 'Замечательно. Пожалуйста, укажите ваш тип техники из списка ниже',reply_markup=executors_1)

@bot.message_handler(content_types=['photo'])
def photo_get(message):
    photo = message.photo[-1].file_id
    print(photo)
    c_executors_db.execute("UPDATE executors SET photo_id='"+str(photo)+"' WHERE id="+str(message.chat.id))
    c_main_db.execute("UPDATE main SET status = 504 WHERE id="+str(message.chat.id))
    save()
    bot.send_message(message.chat.id, 'Хорошо. Пожалуйста, введите гос. номер техники.')

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
    if message.text == 'Профиль':
        c_executors_db.execute('SELECT * FROM executors WHERE id='+str(message.chat.id))
        parse = c_executors_db.fetchone()
        print(parse)
        tech_type = 'None'
        if parse[1] == 1:
            tech_type = 'Автовышка'
        if parse[1] == 2:
            tech_type = "Автокран"
        if parse[1] == 3:
            tech_type = "Кран манипулятор"
        if parse[1] == 4:
            tech_type = "Экскаватор"
        if parse[1] == 5:
            tech_type = "Самосвал"
        if parse[1] == 6:
            tech_type = "Грузовик"
        bot.send_message(message.chat.id, 'ПРОФИЛЬ'
                         '\n\n'
                         'Имя: '+str(parse[7])+''
                         '\n'
                         'ID: '+str(parse[0])+''
                         '\n'
                         'Тип техники: '+str(tech_type)+''
                         '\n'
                         'Гос. номер: '+str(parse[2])+''
                         '\n'
                         'Номер телефона: '+str(parse[5])+''
                         '\n')
        bot.send_photo(message.chat.id, parse[3])
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
    if message.text == 'Я владелец спецтехники, и хочу заработать':
        c_main_db.execute("INSERT INTO main(id,role,status) VALUES ('" + str(message.chat.id) + "','2','1')")
        save()
        c_main_db.execute("UPDATE main SET status = 500 WHERE id = " + str(message.chat.id))
        c_executors_db.execute("INSERT INTO executors(id) VALUES ('" + str(message.chat.id) + "')")
        save()
        bot.send_message(message.chat.id,
                         'Нужно пройти регистрацию в боте. После регистрации и подтверждения у вас будет доступ ко всем возможностям.')
        bot.send_message(message.chat.id, 'Представьтесь, пожалуйста.',reply_markup=remove_keyboard)
    else:
        id = message.chat.id
        c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
        fetch = c_main_db.fetchone()
        status = fetch[0]
        if status == 500:
            name = message.text
            c_executors_db.execute("UPDATE executors SET name ='"+str(name)+"' WHERE id="+str(message.chat.id))
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
            keyboard.add(button_phone)
            bot.send_message(message.chat.id,
                             "Очень приятно. Пожалуйста, отправьте мне ваш телефон с помощью кнопки ниже.",
                             reply_markup=keyboard)
        if status == 501:
            c_main_db.execute("UPDATE main SET status = 502 WHERE id="+str(message.chat.id))
            tech_type = 'None'
            """
            excalator_1.row("Автовышка","Автокран","Кран манипулятор")
            executors_1.row("Экскаватор","Самосвал","Грузовик")
            """
            if message.text == "Автoвышка":
                tech_type = 1
            if message.text == "Автoкран":
                tech_type = 2
            if message.text == "Кран манипулятoр":
                tech_type = 3
            if message.text == "Экскаватoр":
                tech_type = 4
            if message.text == "Самoсвал":
                tech_type = 5
            if message.text == "Грузoвик":
                tech_type = 6
            c_executors_db.execute("UPDATE executors SET tech_type="+str(tech_type)+" WHERE id="+str(message.chat.id))
            save()
            bot.send_message(message.chat.id, 'Пожалуйста, отправьте фото вашего ТС что б пользователи могли его увидеть.',reply_markup=remove_keyboard)
        if status == 504:
            c_main_db.execute("UPDATE main SET status=505 WHERE id="+str(message.chat.id))
            c_executors_db.execute("UPDATE executors SET gov_num='"+str(message.text)+"' WHERE id="+str(message.chat.id))
            save()
            bot.send_message(message.chat.id, 'Хорошо. Ваша автотехника успешно зарегестрирована. Необходимо ввести номер банковской карты для получения оплаты за работу.'
                                              '\nНе волнуйтесь за свои данные! Все они зашифрованы и будут показаны только тем людям которым вы предложите свои услуги.')
        if status == 505:
            text = message.text
            card = len(text)
            if card == 16:
                c_main_db.execute("UPDATE main SET status=508 WHERE id="+str(message.chat.id))
                c_executors_db.execute("UPDATE executors SET card='"+str(message.text)+"' WHERE id="+str(message.chat.id))
                save()
                c_executors_db.execute("SELECT tech_type FROM executors WHERE id="+str(message.chat.id))
                parse = c_executors_db.fetchone()
                chat_link = 'None'
                if parse[0] == 1:
                    chat_link = derill_chat
                if parse[0] == 2:
                    chat_link == crane_chat
                if parse[0] == 3:
                    chat_link = crane_arm_chat
                if parse[0] == 4:
                    chat_link = excalator_chat
                if parse[0] == 5:
                    chat_link = samosval_chat
                if parse[0] == 6:
                    chat_link = truck_chat
                bot.send_message(message.chat.id, "Вы успешно зарегестрировались! Для получения заказов вам необходимо ждать их в чате вашей техники."
                                                  "\nПожалуйста, перед предложением помощи убедитесь что ваши параметры совпадают с требуемыми!"
                                                  "\n\n[Ссылка на чат]("+str(chat_link)+")", parse_mode='Markdown', reply_markup=executors_2)
            else:
                bot.send_message(message.chat.id, 'Убедитесь в правильности ввода данных.\n'
                                                  'Пример: 1234567890123456')
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
            day = int(data[8])
            month = int(data[7])
            print(data)
            bot.send_message(message.chat.id, 'Давайте убедимся в правильности заказа.\n'
                                                  'Вам требуется: Автокран до ' + str(data[2]) + ' для '+str(data[6])+'\n'
                                                                                                                        'Начало работ: '+str(day)+'.'+str(month)+'.2018 в '+str(data[9])+' в городе '+str(data[10])+' по адресу '
                                                                                                                                                                                                                                ''+str(data[11])+', всё верно?',reply_markup=confirm)
        if status == 23:
            if message.text == 'Да':
                bot.send_message(message.chat.id, 'Каким способом Вам удобно рассчитаться?', reply_markup=pay_type)
                c_main_db.execute("UPDATE main SET status = 24 WHERE id = "+str(message.chat.id))
                main_db.commit()
            if message.text == 'Нет':
                bot.send_message(message.chat.id, 'Вы уверены что хотите отменить заказ? Все данные придется вводить сначала.')
                c_main_db.execute("UPDATE main SET status = 241 WHERE id ="+str(message.chat.id))
        if status == 241:
            if message.text == 'Да':
                bot.send_message(message.chat.id, "Заказ удален. Начнем сначала?", reply_markup=main_customer)
                c_main_db.execute("UPDATE main SET status=1 WHERE id="+str(message.chat.id))
            if message.text == 'Нет':
                bot.send_message(message.chat.id, 'С какого моменнта вы хотите изменить ваш заказ?')
        if status == 24:
            if message.text == 'Наличными':
                bot.send_message(message.chat.id, 'Спасибо! Ваш запрос принят! Ожидайте ответа!\n'
                                                  'Возможно Вам понадобится что-то ещё?', reply_markup=main_customer)
                c_main_db.execute("UPDATE main SET status = 1 WHERE id = "+str(message.chat.id))
                c_derill_db.execute("UPDATE crane SET pay_type = 'наличными.' WHERE id="+str(message.chat.id))
                save()
                c_derill_db.execute("SELECT * FROM crane WHERE id ="+str(message.chat.id))
                parse = c_crane_db.fetchone()
                print(parse)
                #bot.send_message(crane_id,"НОВЫЙ ЗАКАЗ #")
            if message.text == 'Карточкой':
                bot.send_message(message.chat.id, 'Спасибо! Ваш запрос принят! Ожидайте ответа!\nВозможно Вам понадобится что-то ещё?', reply_markup=main_customer)
                c_main_db.execute("UPDATE main SET status = 1 WHERE id = "+str(message.chat.id))
                c_crane_db.execute("UPDATE crane SET pay_type = 'картой.' WHERE id="+str(message.chat.id))
                save()
                c_crane_db.execute("SELECT * FROM crane WHERE id ="+str(message.chat.id))
                parse = c_crane_db.fetchone()
                print(parse)
            if message.text == 'Безналичными':
                bot.send_message(message.chat.id, 'Спасибо! Ваш запрос принят! Ожидайте ответа!\nВозможно Вам понадобится что-то ещё?', reply_markup=main_customer)
                c_main_db.execute("UPDATE main SET status = 1 WHERE id = "+str(message.chat.id))
                c_crane_db.execute("UPDATE crane SET pay_type = 'безналичными.' WHERE id="+str(message.chat.id))
                save()
                c_crane_db.execute("SELECT * FROM crane WHERE id ="+str(message.chat.id))
                parse = c_crane_db.fetchone()
                print(parse)
        if message.text == 'Кран манипулятор':
            bot.send_message(message.chat.id, 'Хорошо. Нам понадобятся некоторые данные. Пожалуйста, выберите Ваши требования к спецтехнике из клавиатуры ниже.')
            bot.send_message(message.chat.id, 'Что планируете перевозить?',reply_markup=crane_arm)
            c_main_db.execute("UPDATE main SET status=25 WHERE id="+str(message.chat.id))
            save()
        else:
            id = message.chat.id
            c_main_db.execute("SELECT status FROM main WHERE id=" + str(id))
            fetch = c_main_db.fetchone()
            status = fetch[0]
            if status == 25:
                bot.send_message(message.chat.id,'Опишите задачу крана своими словами.',reply_markup=remove_keyboard)
                c_crane_arm.execute("INSERT INTO crane_arm(id,item_type) VALUES ('"+str(message.chat.id)+"','"+str(message.text)+"')")
                c_main_db.execute('UPDATE main SET status=26 WHERE id='+str(message.chat.id))
                save()
            if status == 26:
                bot.send_message(message.chat.id,'Укажите размер груза.')
                c_crane_arm.execute("UPDATE crame_arm SET item_task='"+str(message.text)+"' WHERE id ="+str(message.chat.id))
                c_main_db.execute('UPDATE main SET status=27 WHERE id='+str(message.chat.id))
                save()
            if status == 27:
                bot.send_message(message.chat.id,'Укажите количество груза.')
                c_crane_arm.execute("UPDATE crame_arm SET item_parameters='"+str(message.text)+"' WHERE id ="+str(message.chat.id))
                c_main_db.execute('UPDATE main SET status=27 WHERE id='+str(message.chat.id))
                save()
            if status == 28:
                bot.send_message(message.chat.id, 'Введите число месяца работ.')
                c_crane_db.execute("UPDATE crane SET item_task='" + str(message.text) + "' WHERE id=" + str(message.chat.id))
                c_main_db.execute("UPDATE main SET status=29 WHERE id=" + str(message.chat.id))
                save()
            if status == 29:
                text = message.text
                month = text.split(' ')
                print(month[0])
                try:
                    if int(month[0]) <= 12:
                        c_crane_db.execute("UPDATE crane_arm SET month =" + str(month[0]) + " WHERE id=" + str(message.chat.id))
                        c_main_db.execute("UPDATE main SET status = 30 WHERE id=" + str(message.chat.id))
                        bot.send_message(message.chat.id, "Укажите день работ.")
                        save()
                    else:
                        bot.send_message(message.chat.id, "Ошибка. Укажите верное число месяца.")
                except:
                    bot.send_message(dev_id, 'Твой косяк, ламер. Исправь.')
            if status == 30:
                text = message.text
                day = text.split(' ')
                print(day[0])
                try:
                    if int(day[0]) <= 31:
                        c_crane_db.execute("UPDATE crane_arm SET day =" + str(day[0]) + " WHERE id=" + str(message.chat.id))
                        c_main_db.execute("UPDATE main SET status = 31 WHERE id=" + str(message.chat.id))
                        bot.send_message(message.chat.id, "Укажите время работ.")
                        save()
                    else:
                        bot.send_message(message.chat.id, 'Убедитесь в правильности дня.')
                except:
                    bot.send_message(dev_id, 'Опять костыль')
            if status == 31:
                c_crane_db.execute(
                    "UPDATE crane_arm SET begin_time = '" + str(message.text) + "' WHERE id=" + str(message.chat.id))
                c_main_db.execute("UPDATE main SET status = 32 WHERE id=" + str(message.chat.id))
                save()
                bot.send_message(message.chat.id,
                                 "Выбирите город или область в котором вы планируете проводить работы.",
                                 reply_markup=city_choice)
            if status == 32:
                if message.text == "Киев":
                    c_crane_db.execute("UPDATE crane_arm SET city = 'Киев' WHERE id =" + str(message.chat.id))
                    c_main_db.execute("UPDATE main SET status = 33 WHERE id=" + str(message.chat.id))
                    save()
                    bot.send_message(message.chat.id, 'Введите адрес проведения работ.', reply_markup=remove_keyboard)
                else:
                    bot.send_message(message.chat.id, 'Вашего города пока что нету в списке.')
            if status == 33:
                c_crane_db.execute(
                    "UPDATE crane_arm SET adress ='" + str(message.text) + "' WHERE id =" + str(message.chat.id))
                c_crane_db.execute("SELECT * FROM crane WHERE id=" + str(message.chat.id))
                c_main_db.execute("UPDATE main SET status = 34 WHERE id=" + str(message.chat.id))
                save()
                data = c_crane_db.fetchone()
                day = int(data[8])
                month = int(data[7])
                print(data)
                """bot.send_message(message.chat.id, 'Давайте убедимся в правильности заказа.\n'
                                                  'Вам требуется: Кран манипулятор до ' + str(data[2]) + ' для ' + str(
                    data[6]) + '\n'
                               'Начало работ: ' + str(day) + '.' + str(month) + '.2018 в ' + str(
                    data[9]) + ' в городе ' + str(data[10]) + ' по адресу '
                                                              '' + str(data[11]) + ', всё верно?', reply_markup=confirm)"""
            if status == 34:
                if message.text == 'Да':
                    bot.send_message(message.chat.id, 'Каким способом Вам удобно рассчитаться?', reply_markup=pay_type)
                    c_main_db.execute("UPDATE main SET status = 35 WHERE id = " + str(message.chat.id))
                    main_db.commit()
                if message.text == 'Нет':
                    bot.send_message(message.chat.id,
                                     'Вы уверены что хотите отменить заказ? Все данные придется вводить сначала.')
                    c_main_db.execute("UPDATE main SET status = 341 WHERE id =" + str(message.chat.id))
            if status == 341:
                if message.text == 'Да':
                    bot.send_message(message.chat.id, "Заказ удален. Начнем сначала?", reply_markup=main_customer)
                    c_main_db.execute("UPDATE main SET status=1 WHERE id=" + str(message.chat.id))
                if message.text == 'Нет':
                    bot.send_message(message.chat.id, 'С какого моменнта вы хотите изменить ваш заказ?')
            if status == 35:
                if message.text == 'Наличными':
                    bot.send_message(message.chat.id, 'Спасибо! Ваш запрос принят! Ожидайте ответа!\n'
                                                      'Возможно Вам понадобится что-то ещё?',
                                     reply_markup=main_customer)
                    c_main_db.execute("UPDATE main SET status = 1 WHERE id = " + str(message.chat.id))
                    c_derill_db.execute("UPDATE crane SET pay_type = 'наличными.' WHERE id=" + str(message.chat.id))
                    save()
                    c_derill_db.execute("SELECT * FROM crane WHERE id =" + str(message.chat.id))
                    parse = c_crane_db.fetchone()
                    print(parse)
                    #bot.send_message(arm_crane_id,"НОВЫЙ ЗАКАЗ #")
                if message.text == 'Карточкой':
                    bot.send_message(message.chat.id,
                                     'Спасибо! Ваш запрос принят! Ожидайте ответа!\nВозможно Вам понадобится что-то ещё?',
                                     reply_markup=main_customer)
                    c_main_db.execute("UPDATE main SET status = 1 WHERE id = " + str(message.chat.id))
                    c_crane_db.execute("UPDATE crane SET pay_type = 'картой.' WHERE id=" + str(message.chat.id))
                    save()
                    c_crane_db.execute("SELECT * FROM crane WHERE id =" + str(message.chat.id))
                    parse = c_crane_db.fetchone()
                    print(parse)
                if message.text == 'Безналичными':
                    bot.send_message(message.chat.id,
                                     'Спасибо! Ваш запрос принят! Ожидайте ответа!\nВозможно Вам понадобится что-то ещё?',
                                     reply_markup=main_customer)
                    c_main_db.execute("UPDATE main SET status = 1 WHERE id = " + str(message.chat.id))
                    c_crane_db.execute("UPDATE crane SET pay_type = 'безналичными.' WHERE id=" + str(message.chat.id))
                    save()
                    c_crane_db.execute("SELECT * FROM crane WHERE id =" + str(message.chat.id))
                    parse = c_crane_db.fetchone()
                    print(parse)








# !! DECORATORS SECTION END !! #


# !! END PART !! #
if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass
