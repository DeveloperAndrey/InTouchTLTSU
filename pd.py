import glob
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token="12345678:AaBbCcDdEeFfGgHh")
# Диспетчер для бота
dp = Dispatcher(bot)
# Хэндлер на команду /test1
@dp.message_handler(commands="старт")
async def cmd_test1(message: types.Message):
    await message['text']
    glob.glob('*.pdf')

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

