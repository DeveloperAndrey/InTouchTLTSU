import glob
from typing import Dict, Any

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton


from config import TOKEN
import sqlite3
from Function import *
from collections import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['add_admin'])
async def add_admin(message):
    if message.text.isdigit():
        add_admin1(message.text)
    else:
        await message.answer('Вы ввели неправильный id')


@dp.message_handler(commands=['delete_admin'])
async def delete_admin(message):
    if message.text.isdigit():
        if message.text in list_admin():
            del_admin(message.text)
    else:
        await message.answer('Вы ввели неправильный id')


@dp.message_handler(commands=['add_question'])
async def add_question(message):
    add_que(message.text)


@dp.message_handler(commands=['delete_question'])
async def delete_question(message):
    if message.text.isdigit():
        if message.text in list_que():
            del_que(message.text)
    else:
        await message.answer('Вы ввели неправильный id')


@dp.message_handler(commands=['question_connect_area'])
async def question_connect_area(message1, message2):
    if message1.text.isdigit() and message2.text.isdigit():
        if message2.text in list_area() and message1.text in list_que():
            add_que_area(message1.text, message2.text)
    else:
        await message1.answer('Вы ввели неправильный id')


@dp.message_handler(commands=['area_connect_area'])
async def area_connect_area(message):
    message1, message2 = message.text.split()
    if message1.text.isdigit() and message2.text.isdigit():
        if message1.text in list_area() and message2.text in list_area():
            add_area_area(message1.text, message2.text)
    else:
        await message.answer('Вы ввели неправильный id')


@dp.message_handler(commands=['area_connect'])
async def area_add(message):
    add_area(message.text)


@dp.message_handler(commands=['area_delete'])
async def area_delete(message):
    if message.text.isdigit():
        if message.text in list_area():
            del_area(message.text)
    else:
        await message.answer('Вы ввели неправильный id')


@dp.message_handler(commands=['delete_area_connect_area'])
async def delete_area_connect_area(message):
    message1, message2 = message.text.split()
    if message1.text.isdigit() and message2.text.isdigit():
        if [int(message1.text), int(message2.text)] in obl_con_obl_list():
            del_area_area(message1.text, message2.text)

    else:
        await message.answer('Вы ввели неправильный id')


@dp.message_handler(commands=['delete_question_connect_area'])
async def delete_question_connect_area(message):
    message1, message2 = message.text.split()
    if message1.text.isdigit() and message2.text.isdigit():
        if [int(message1.text), int(message2.text)] in obl_con_que_list():
            del_que_area(message1.text, message2.text)
    else:
        await message.answer('Вы ввели неправильный id')


"""
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Тестим тестим тестим")
"""


@dp.message_handler(commands=['find'])
async def test(msg: types.Message):
    inp = msg.text
    output = Counter(inp.split())
    qa_var1 = {}

    l = [[Counter(i.split()), qa_var1[i]] for i in qa_var1]

    max_s = -1
    ind = list()
    for j, i in enumerate(l):
        s = sum((output & l[j][0]).values())
        if s == max_s:
            ind.append(j)
        elif s > max_s:
            ind = [j]
            max_s = s
    if max_s == 0:
        await bot.send_message(msg.from_user.id, 'noobe')
    else:
        for i in ind:
            await bot.send_message(msg.from_user.id, l[i][1])


"""
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
 await message.reply("Тут пока ничего нету")
 """


@dp.message_handler(commands=['glob'])
async def test(msg: types.Message):
    inp = msg.text
    papapa = inp + "*.pdf"
    spisok = glob.glob(papapa)
    doc = open(spisok[0], "rb")
    await bot.send_document(msg.from_user.id, doc)
    await bot.send_document(msg.chat.id, "FILEID")


# Конец поиска файлов


# Кнопки

def obl():
    return cur.execute(""" SELECT idAreas, Name FROM Area;""")


def que():
    return cur.execute("""SELECT  idQuestions, Question FROM Question;""")


def obl_con_que_list():
    return cur.execute("""SELECT idAreas, idQuestions FROM Area_question;""")


def obl_con_obl_list():
    return cur.execute("""SELECT idParentArea, idChildArea FROM AreaArea;""")


main_obl_id = {1: obl_con_obl_list()[0]}
state_id = {1: obl_con_obl_list()[0]}


@dp.message_handler(commands=['start'])
async def show_main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_obl_list():
        if i[0] is None:
            continue

        if i[0] == main_obl_id[0]:
            buttons = [obl()[i][1]]
            keyboard.add(*buttons)
        elif i[1] == main_obl_id[0]:
            buttons = [obl()[i][0]]
            keyboard.add(*buttons)
        await message.answer("1")
    buttons = ["Вопросы по теме"]
    keyboard.add(*buttons)
    await message.answer("Основные категории", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "В начало")
async def show_main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_obl_list():
        if i[0] is None:
            continue

        if i[0] == main_obl_id[0]:
            buttons = [obl()[i][1]]
            keyboard.add(*buttons)
        elif i[1] == main_obl_id[0]:
            buttons = [obl()[i][0]]
            keyboard.add(*buttons)
    buttons = ["Вопросы по теме"]
    keyboard.add(*buttons)
    await message.answer("Основные категории", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in obl_names())
async def show_some_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    state_id[0] = list_area()[message.text]
    for i in obl_con_obl_list():
        if i[0] is None:
            continue

        if i[0] == id_obl(message.text):
            buttons = [list_area()[i][1]]
            keyboard.add(*buttons)
        elif i[1] == id_obl(message.text):
            buttons = [list_area()[i][0]]
            keyboard.add(*buttons)

    buttons1 = ["Вопросы по теме"]
    buttons2 = ["В начало"]
    keyboard.add(*buttons1, *buttons2)
    await message.answer(".", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Вернуться к теме")
async def show_some_menu_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_obl_list():
        if i[0] is None:
            continue

        if i[0] == state_id[0]:
            buttons = [obl()[i][1]]
            keyboard.add(*buttons)
        elif i[1] == state_id[0]:
            buttons = [obl()[i][0]]
            keyboard.add(*buttons)
    buttons1 = ["Вопросы по теме"]
    buttons2 = ["В начало"]
    keyboard.add(*buttons1, *buttons2)
    await message.answer(".", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Вопросы по теме")
async def show_que_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in obl_con_que_list():
        if i[0] == state_id[0]:
            buttons = [que()[i][1]]
            keyboard.add(*buttons)
    buttons = ["Вернуться к теме"]
    keyboard.add(*buttons)
    await message.answer("Вот:", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
