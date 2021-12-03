from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton
from config import TOKEN
import sqlite3 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db =   sqlite3.connect('db/database.db')#cursor
cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS AreaArea( id INTEGER PRIMARY KEY , idParentArea INTEGER, idChildArea INTEGER)""")
db.commit()


cursor.execute(""" CREATE TABLE IF NOT EXISTS  ADMINS ( id INTEGER PRIMARY KEY ,  idtelegram INTEGER  )""")
db.commit()



def obl_con_obl_list():
    return [[None, 23], [23, 6], [23, 76], [6, 123], [23, 123]]
#is_admin()

def obl_con_que_list():
    return [[23, 6], [76, 1], [6, 5], [123, 4], [6, 4], [23, 3], [76, 2], [76, 3]]

@dp.message_handler(commands=['add_admin'])
async def add_admin(message):
   if(message.text.isdigit()):
        add_admin1(message.text)
   else:
       print('Вы ввели неправильный id')






@dp.message_handler(commands=['delete_admin'])
async def delete_admin(message):
    if (message.text.isdigit()):
         if message.text in list_admin():
          del_admin(message.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['add_question'])
async def add_question(message):

    add_que(message.text)

@dp.message_handler(commands=['delete_question'])
async def delete_question(message):
    if (message.text.isdigit()):
        if message.text in list_que():
          del_que(message.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['question_connect_area'])
async def question_connect_area(message1, message2):
    if (message1.text.isdigit() and message2.text.isdigit()):
        if message2.text in list_area() and message1.text in list_que():
          add_que_area(message1.text, message2.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['area_connect_area'])
async def area_connect_area(message):
    message1, message2 = message.text.split()
    if (message1.text.isdigit() and message2.text.isdigit()):
        if message1.text in list_area() and message2.text in list_area():
          add_area_area(message1.text, message2.text)
    else:
        print('Вы ввели неправильный id')


@dp.message_handler(commands=['area_connect'])
async def area_add(message):
         add_area(message.text)

@dp.message_handler(commands=['area_delete'])
async def area_delete(message):
    if (message.text.isdigit()):
        if message.text in list_area():
          del_area(message.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['delete_area_connect_area'])
async def delete_area_connect_area(message):
    message1, message2 = message.text.split()
    if (message1.text.isdigit() and message2.text.isdigit()):
        if [int(message1.text),int(message2.text)] in obl_con_obl_list():
          del_area_area(message1.text, message2.text)

    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['delete_question_connect_area'])
async def delete_question_connect_area(message):
    message1, message2 = message.text.split()
    if (message1.text.isdigit() and message2.text.isdigit()):
        if [int(message1.text),int(message2.text)] in obl_con_que_list():
          del_que_area(message1.text, message2.text)
    else:
        print('Вы ввели неправильный id')









async def select_name():
    return [[1,'we'], [2,'yu']]







def add_admin1(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    else:    
     cursor.execute("INSERT INTO ADMINS VALUES (NULL,  ?)", (id_, ))
     db.commit()


def list_admin():
    select_all_rows = "SELECT * FROM ADMINS "
    cursor.execute(select_all_rows)
    rows = cursor.fetchall()
    return rows


def del_admin(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    else:
     cursor.execute(""" DELETE FROM ADMINS WHERE idtelegram = ? """, (id_,))
     db.commit()


def add_que(id_):
    if not isinstance(id_, str):
        raise Warning('ne int')
    return 543


def list_que():
    return [65456, 543, 5344]


def del_que(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    return 'ok'


def add_area(id_):
    if not isinstance(id_, str):
        raise Warning('ne int')
    else: 
     cursor.execute(""" CREATE TABLE IF NOT EXISTS  Area ( id INTEGER PRIMARY KEY ,  idtelegram TEXT  )""")
     db.commit()


def list_area():
    return [123, 432, 6343]


def del_area(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    else: 
     cursor.execute(""" DROP TABLE IF EXISTS Area ( id INTEGER PRIMARY KEY ,  idtelegram INTEGER  )""")
     db.commit()

# Нужен человек работающий с ОбластьВопрос
def add_que_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    return 'ok'

# Нужен человек работающий с ОбластьВопрос
def list_que_area():
    select_all_rows = "SELECT * FROM AreaQuestion "
    cursor.execute(select_all_rows)
    rows = cursor.fetchall()
    return rows

# Нужен человек работающий с ОбластьВопрос
def del_que_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    return 'ok'


def add_area_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    else:
     cursor.execute("INSERT INTO AreaArea VALUES (NULL, ? , ? )", ( id_, id_1))
     db.commit()


def list_area_area():
    select_all_rows = "SELECT * FROM AreaArea "
    cursor.execute(select_all_rows)
    rows = cursor.fetchall()
    return rows

def del_area_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    else:
     cursor.execute(""" DELETE FROM AreaArea WHERE id = ? """, (id,))
     db.commit()


      
      
      
      
def obl_id(id_):
    d = {
        123: 'havka',
        23: 'qwe',
        6: 'obshaga',
        76: 'profkom'
    }
    return d[id_]


def id_obl(id_):
    d = {
        'havka': 123,
        'qwe': 23,
        'obshaga': 6,
        'profkom': 76,
    }
    return d[id_]


def obl_names():
    return ['havka', 'qwe', 'obshaga', 'profkom']


def obl_con_obl_list():
    return [[None, 23], [23, 6], [23, 76], [6, 123], [23, 123]]


def que_id(id_):
    d = {
        1: 'A? No',
        2: 'Смысл жизни? 42',
        3: '42? Нет',
        4: 'Я тебе покушать принёс? Отвали',
        5: 'Сколько тут тараканов? 128**128**128**128',
        6: 'qwe? йцу',
    }
    return d[id_]


def que_list():
    return ['A? No', 'Смысл жизни? 42', '42? Нет', 'Я тебе покушать принёс? Отвали',
            'Сколько тут тараканов? 128**128**128**128', 'qwe? йцу']


def obl_con_que_list():
    return [[23, 6], [76, 1], [6, 5], [123, 4], [6, 4], [23, 3], [76, 2], [76, 3]]


main_obl_id = {'0': None}
for i in obl_con_obl_list():
    if (i[0] == None):
        main_obl_id[0] = i[1]

state_id = {'0': None}
state_id[0] = main_obl_id[0]


@dp.message_handler(commands="start")
async def show_main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_obl_list():
        if i[0] == None:
            continue

        if (i[0] == main_obl_id[0]):
            buttons = [obl_id(i[1])]
            keyboard.add(*buttons)
        elif (i[1] == main_obl_id[0]):
            buttons = [obl_id(i[0])]
            keyboard.add(*buttons)
    buttons = ["Вопросы по теме"]
    keyboard.add(*buttons)
    await message.answer("Основные категории", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "В начало")
async def show_main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_obl_list():
        if i[0] == None:
            continue

        if (i[0] == main_obl_id[0]):
            buttons = [obl_id(i[1])]
            keyboard.add(*buttons)
        elif (i[1] == main_obl_id[0]):
            buttons = [obl_id(i[0])]
            keyboard.add(*buttons)
    buttons = ["Вопросы по теме"]
    keyboard.add(*buttons)
    await message.answer("Основные категории", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in obl_names())
async def show_some_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    state_id[0] = id_obl(message.text)
    for i in obl_con_obl_list():
        if i[0] == None:
            continue

        if (i[0] == id_obl(message.text)):
            buttons = [obl_id(i[1])]
            keyboard.add(*buttons)
        elif (i[1] == id_obl(message.text)):
            buttons = [obl_id(i[0])]
            keyboard.add(*buttons)

    buttons1 = ["Вопросы по теме"]
    buttons2 = ["В начало"]
    keyboard.add(*buttons1, *buttons2)
    await message.answer("AAA", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Вернуться к теме")
async def show_some_menu_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_obl_list():
        if i[0] == None:
            continue

        if (i[0] == state_id[0]):
            buttons = [obl_id(i[1])]
            keyboard.add(*buttons)
        elif (i[1] == state_id[0]):
            buttons = [obl_id(i[0])]
            keyboard.add(*buttons)
    buttons1 = ["Вопросы по теме"]
    buttons2 = ["В начало"]
    keyboard.add(*buttons1, *buttons2)
    await message.answer("AAA", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Вопросы по теме")
async def show_que_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_que_list():
        if (i[0] == state_id[0]):
            buttons = [que_id(i[1])]
            keyboard.add(*buttons)
    buttons = ["Вернуться к теме"]
    keyboard.add(*buttons)
    await message.answer("Вот:", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
