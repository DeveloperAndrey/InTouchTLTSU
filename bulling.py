from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



#is_admin()


@dp.message_handler(commands=['add_admin'])
async def add_admin(id):
    id = "28212"
    print(id.isdigit())

    id = "123214124"
    print(id.isdigit())
    add_admin(" ")


@dp.message_handler(commands=['delete_admin'])
async def delete_admin(id):
    id = "28212"
    print(id.isdigit())

    id = "123214124"
    print(id.isdigit())
    delete_admin(" ")

@dp.message_handler(commands=['add_question'])
async def add_question(id):
    id = "28212"
    print(id.isdigit())

    id = "123214124"
    print(id.isdigit())
    add_question(" ")

@dp.message_handler(commands=['delete_question'])
async def delete_question(id):
    id = "28212"
    print(id.isdigit())

    delete_question = "123214124"
    print(id.isdigit())
    delete_question(" ")

@dp.message_handler(commands=['question_connect_area'])
async def question_connect_area(id):
    id = "28212"
    print(id.isdigit())

    id = "123214124"
    print(id.isdigit())
    question_connect_area(" ")

@dp.message_handler(commands=['area_connect_area'])
async def area_connect_area(id):
    id = "28212"
    print(id.isdigit())

    id = "123214124"
    print(id.isdigit())
    area_connect_area(" ")


async def select_name():
    return [[1,'we'], [2,'yu']]



