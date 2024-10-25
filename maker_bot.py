import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from buttons import menu

API_TOKEN = '7642306739:AAGsD41ZOrf5LLAh3J8L5sthU0ZWCrBvG8s'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage =   MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    fullname = State()
    phone = State()
    web_site = State()
    email = State()
    finish = State()
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await UserState.fullname.set()
    await message.reply("Assalomu aleykum!", reply_markup=menu)


@dp.message_handler(state=UserState.fullname)
async def get_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text
    await message.answer("Ism-Familyangizni kiriting:")
    await UserState.next()
    await UserState.phone.set()

@dp.message_handler(state=UserState.phone)
async def get_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer("Telefon raqamingizni kiriting:")
    await UserState.next()
    await UserState.web_site.set()

@dp.message_handler(state=UserState.web_site)
async def get_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['web_site'] = message.text
    await message.answer("Web Site manzilini kiriting:")
    await UserState.next()
    await UserState.email.set()

@dp.message_handler(state=UserState.email)
async def get_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await message.answer("Elektron pochtangizni kiriting:")
    await UserState.next()
    await UserState.finish.set()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)