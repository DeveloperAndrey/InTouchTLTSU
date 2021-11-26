import 
import os
from aiogram.types import
from aiogram import Bot, Dispatcher, executor, types
 
bot = Bot(token="2145085210:AAHzKokhuGOC62RpzUcmWTO90mQHtHvU8tQ")
# Диспетчер для бота
dp = Dispatcher(bot)
# Хэндлер на команду /test1
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
 await message.reply("будь здоров!")
 
 
@dp.message_handler(commands=['start', 'help'])
 
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
 await message.reply("памагитеее")
 
@dp.message_handler()
 async deftest(msg: types.Message):
 inp = (msg.text)
    papapa = inp+"*.pdf"
    spisok = glob.glob(papapa)
    doc = open(spisok[0],"rb")
    await bot.send_document(msg.from_user.id, doc)
    await bot.send_document(msg.chat.id, "FILEID")
 
 
 
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
