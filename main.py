from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

file = open("admins.txt", "r")

def is_admin():
    call.from_user.id
    if call.from_user.id in mylist:
        return 1
    else:
        return 0

#is_admin()


@dp.message_handler(commands=['add_admin'])
async def add_admin(id):
    add_admin(" ")

@dp.message_handler(commands=['delete_admin'])
async def delete_admin(id):
    delete_admin(" ")

@dp.message_handler(commands=['add_question'])
async def add_question(id):
    add_question(" ")

@dp.message_handler(commands=['delete_question'])
async def delete_question(id):
    delete_question(" ")

@dp.message_handler(commands=['question_connect_area'])
async def question_connect_area(id):
    question_connect_area(" ")

@dp.message_handler(commands=['area_connect_area'])
async def area_connect_area(id):
    area_connect_area(" ")


async def select_name():
    return [[1,'we'], [2,'yu']]



