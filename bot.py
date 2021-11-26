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

def obl_con_que_list():
    return [[23, 6], [76, 1], [6, 5], [123, 4], [6, 4], [23, 3], [76, 2], [76, 3]]


@dp.message_handler(commands="start", "В начало")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_start = ["Да"]
    keyboard.add(*button_start)
    await message.answer("Хотите начать?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Да")
async def show_buttons_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_obl_id = 0
    for i in obl_con_obl_list():
        if (i[0] == None):
            main_obl_id = i[1]

    for i in obl_con_que_list():
        if (i[0] == main_obl_id):
            #await message.answer(que_id(i[1]), reply_markup=keyboard)
            buttons = [que_id(i[1])]
            keyboard.add(*buttons)

        elif (i[1] == main_obl_id):
            #await message.answer(que_id(i[0]), reply_markup=keyboard)
            buttons = [que_id(i[0])]
            keyboard.add(*buttons)

    for i in obl_con_obl_list():
        if i[0] == None:
            continue

        if (i[0] == main_obl_id):
            #await message.answer(obl_id(i[1]), reply_markup=keyboard)
            buttons = [obl_id(i[1])]
            keyboard.add(*buttons)
        elif (i[1] == main_obl_id):
            #await message.answer(obl_id(i[0]), reply_markup=keyboard)
            buttons = [obl_id(i[0])]
            keyboard.add(*buttons)
    #button_back = ["Назад"]
    #keyboard.add(*button_back)
    await message.answer("Типа область 1", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "42? Нет")
async def show_buttons_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await message.answer("А вот и да!", reply_markup=keyboard)


if __name__ == '__main__':
   executor.start_polling(dp)
