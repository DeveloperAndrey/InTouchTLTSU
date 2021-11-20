from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



#is_admin()


@dp.message_handler(commands=['add_admin'])
async def add_admin(message):
   if(message.text.isdigit()):
        add_admin1(message.text)
   else:
       print('Вы ввели неправильный id')






@dp.message_handler(commands=['delete_admin'])
async def delete_admin(message):
    if (message.text.isdigit()):
         if message.text in list_admin():
          del_admin(message.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['add_question'])
async def add_question(message):

    add_que(message.text)

@dp.message_handler(commands=['delete_question'])
async def delete_question(message):
    if (message.text.isdigit()):
        if message.text in list_que():
          del_que(message.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['question_connect_area'])
async def question_connect_area(message1, message2):
    if (message1.text.isdigit() and message2.text.isdigit()):
        if message2.text in list_area() and message1.text in list_que():
          add_que_area(message1.text, message2.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['area_connect_area'])
async def area_connect_area(message):
    message1, message2 = message.text.split()
    if (message1.text.isdigit() and message2.text.isdigit()):
        if message1.text in list_area() and message2.text in list_area():
          add_area_area(message1.text, message2.text)
    else:
        print('Вы ввели неправильный id')


@dp.message_handler(commands=['area_connect'])
async def area_add(message):
         add_area(message.text)

@dp.message_handler(commands=['area_delete'])
async def area_delete(message):
    if (message.text.isdigit()):
        if message.text in list_area():
          del_area(message.text)
    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['delete_area_connect_area'])
async def delete_area_connect_area(message):
    message1, message2 = message.text.split()
    if (message1.text.isdigit() and message2.text.isdigit()):
        if [int(message1.text),int(message2.text)] in obl_con_obl_list():
          delete_add_area_area(message1.text, message2.text)

    else:
        print('Вы ввели неправильный id')

@dp.message_handler(commands=['delete_question_connect_area'])
async def delete_question_connect_area(message1, message2):
    message1, message2 = message.text.split()
    if (message1.text.isdigit() and message2.text.isdigit()):
        if [int(message1.text),int(message2.text)] in obl_con_que_list():
          delete_add_que_area(message1.text, message2.text)
    else:
        print('Вы ввели неправильный id')









async def select_name():
    return [[1,'we'], [2,'yu']]







def add_admin1(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    return 'ok'


def list_admin():
    return [123, 432, 6343]


def del_admin(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    return 'ok'


def add_que(id_):
    if not isinstance(id_, str):
        raise Warning('ne int')
    return 543


def list_que():
    return [65456, 543, 5344]


def del_que(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    return 'ok'


def add_area(id_):
    if not isinstance(id_, str):
        raise Warning('ne int')
    return 123


def list_area():
    return [123, 432, 6343]


def del_area(id_):
    if not isinstance(id_, int):
        raise Warning('ne int')
    return 'ok'


def add_que_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    return 'ok'


def list_que_area():
    return [1, 2, 3]


def del_que_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    return 'ok'


def add_area_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    return 'ok'


def list_area_area():
    return [796, 234, 756]


def del_area_area(id_, id_1):
    if not isinstance(id_, int) or not isinstance(id_1, int):
        raise Warning('ne int')
    return 'ok'







