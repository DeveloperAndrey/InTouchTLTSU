import glob
import os
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
from parser import file

bot = Bot(token="2145085210:AAHzKokhuGOC62RpzUcmWTO90mQHtHvU8tQ")
# Диспетчер для бота
dp = Dispatcher(bot)
# Хэндлер на команду /test1
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("да начнётся секс!")


@dp.message_handler(commands=['start', 'help'])

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Тестим тестим тестим")

@dp.message_handler()
async def test(msg: types.Message):
    inp = (msg.text)+'('
    papapa = inp+"*.gif"
    spisok = glob.glob(papapa)
    doc = open(spisok[0], 'rb')
    await bot.send_document(msg.from_user.id, (doc, str))



@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)



"""
есть куча разных фалов .мне передают названия своих группы кафедры специаьности всё есть в названии файлов
я беру текест пользователя благордоря голбу какие названия файлов совпадают
он возвращает всегда список из разных файлов и я благодоря этим путям их возвращаю 
"""
















if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)











