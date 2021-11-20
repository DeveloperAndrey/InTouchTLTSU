from collections import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("да начнётся секс!")


@dp.message_handler(commands=['start', 'help'])

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Тестим тестим тестим")





@dp.message_handler()
async def test(msg: types.Message):
        inp = (msg.text)
        output = Counter(inp.split())
        qa_var1 = {'когда обед':'в обед','расписание': 'будет', 'путин':'Путин вор', 'знаешь': 'ну незнаю', 'кто такой криштал': 'Не заню ходят легенды что это путин'}

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
        if max_s==0:
            await bot.send_message(msg.from_user.id,'noobe')
        else:
            for i in ind:
                await bot.send_message(msg.from_user.id, l[i][1])



@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

