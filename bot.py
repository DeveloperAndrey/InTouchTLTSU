from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from tkinter import *

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

root = Tk()
def hi(i):
    print(i)

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

obl_name = [""]

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1", "Кнопка 2"]
    buttons_2 = ["Кнопка 3", "Кнопка 4"]
    keyboard.add(*buttons_1, *buttons_2)
    await message.answer("Вопрос", reply_markup=keyboard)

"""
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("help")


    for i in obl_con_obl_list():
        if (i[0]==None):
            obl_name = obl_id(i[1])

    k=0
    for i in obl_con_obl_list():
        for j in range(2):
            if (i[j] == obl_name):
                # buttons = [obl_con_que_list(i[j])]
                Button(text=str(i), command=lambda i=i: hi(i)).pack()
                k+=1
    # keyboard.add(*buttons)
    root.mainloop()
    await message.answer("Область 1:", reply_markup=keyboard)
"""


@dp.message_handler(lambda message: message.text == "Кнопка 1")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 1", "Кнопка 2 1"]
    buttons_2 = ["Кнопка 3 1", "Кнопка 4 1"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 1", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Кнопка 2")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 2", "Кнопка 2 2"]
    buttons_2 = ["Кнопка 3 2", "Кнопка 4 2"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 2", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Кнопка 3")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 3", "Кнопка 2 3"]
    buttons_2 = ["Кнопка 3 3", "Кнопка 4 3"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 3", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Кнопка 4")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 4", "Кнопка 2 4"]
    buttons_2 = ["Кнопка 3 4", "Кнопка 4 4"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 4", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Назад")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1", "Кнопка 2"]
    buttons_2 = ["Кнопка 3", "Кнопка 4"]
    keyboard.add(*buttons_1, *buttons_2)
    await message.answer("Вопрос", reply_markup=keyboard)

if __name__ == '__main__':
   executor.start_polling(dp)
