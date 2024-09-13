from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '____________'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())  



@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    print('Введена команда /start')


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('У вас новое сообщение')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


