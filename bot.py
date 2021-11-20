from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text




from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("help")

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1", "Кнопка 2"]
    buttons_2 = ["Кнопка 3", "Кнопка 4"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос", reply_markup=keyboard)



@dp.message_handler(Text(equals="Кнопка 1"))
async def with_puree(message: types.Message):
    await message.reply("Ответ на кнопку 1")



@dp.message_handler(Text(equals="Кнопка 2"))
async def with_puree(message: types.Message):
    await message.reply("Ответ на кнопку 2")

@dp.message_handler(Text(equals="Кнопка 3"))
async def with_puree(message: types.Message):
    await message.reply("Ответ на кнопку 3")

@dp.message_handler(Text(equals="Кнопка 4"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1 1", "Кнопка 2 2"]
    buttons_2 = ["Кнопка 3 3", "Кнопка 4 4"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос 1", reply_markup=keyboard)

    @dp.message_handler(commands="Назад")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = ["Кнопка 1", "Кнопка 2"]
    buttons_2 = ["Кнопка 3", "Кнопка 4"]
    button_back = ["Назад"]
    keyboard.add(*buttons_1, *buttons_2, *button_back)
    await message.answer("Вопрос", reply_markup=keyboard)


if __name__ == '__main__':
   executor.start_polling(dp)
