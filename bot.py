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

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1", "Кнопка 2"]
    buttons_2 = ["Кнопка 3", "Кнопка 4"]
    keyboard.add(*buttons_1, *buttons_2)
    await message.answer("Вопрос", reply_markup=keyboard)

main_obl_id=0
@dp.message_handler(lambda message: message.text == "Кнопка 1")
async def show_buttons_1(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   for i in obl_con_obl_list():
      if (i[0] == None):
         main_obl_id = i[1]
   for i in obl_con_obl_list():
      if i[0] == None:
         continue
      if (i[0] == main_obl_id and i[1] == main_obl_id):
         #await message.answer(i[1] and i[0], reply_markup=keyboard)
         buttons = [i[0], i[1]]
      elif (i[0] == main_obl_id):
         #await message.answer(i[1], reply_markup=keyboard)
         buttons = [i[1]]
      elif (i[1] == main_obl_id):
         #await message.answer(i[0], reply_markup=keyboard)
         buttons = [i[0]]
      keyboard.add(*buttons)
      await message.answer("Область 1", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Кнопка 2")
async def show_buttons_2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 2", "Кнопка 2 2"]
    buttons_2 = ["Кнопка 3 2", "Кнопка 4 2"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 2", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Кнопка 3")
async def show_buttons_3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 3", "Кнопка 2 3"]
    buttons_2 = ["Кнопка 3 3", "Кнопка 4 3"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 3", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Кнопка 4")
async def show_buttons_4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 4", "Кнопка 2 4"]
    buttons_2 = ["Кнопка 3 4", "Кнопка 4 4"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 4", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Назад")
async def show_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1", "Кнопка 2"]
    buttons_2 = ["Кнопка 3", "Кнопка 4"]
    keyboard.add(*buttons_1, *buttons_2)
    await message.answer("Вопрос", reply_markup=keyboard)

if __name__ == '__main__':
   executor.start_polling(dp)
