from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


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
    return ['A? No', 'Смысл жизни? 42', '42? Нет', 'Я тебе покушать принёс? Отвали', 'Сколько тут тараканов? 128**128**128**128', 'qwe? йцу']

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
    buttons2 = ["Назад"]
    buttons3 = ["В начало"]
    keyboard.add(*buttons2, *buttons1, *buttons3)
    await message.answer("AAA", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Назад")
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
    buttons2 = ["Назад"]
    buttons3 = ["В начало"]
    keyboard.add(*buttons2, *buttons1, *buttons3)
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
    buttons2 = ["Назад"]
    buttons3 = ["В начало"]
    keyboard.add(*buttons2, *buttons1, *buttons3)
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
