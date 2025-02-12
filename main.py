import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Задание 1: Обработка /start и кнопок
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Выберите действие:", reply_markup=kb.start_keyboard)

@dp.message(F.text == "Привет")
async def hello_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def bye_handler(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Обработка /links
@dp.message(Command("links"))
async def links_command(message: Message):
    await message.answer("Полезные ссылки:", reply_markup=kb.links_keyboard)

# Задание 3: Обработка /dynamic и callback-ов
@dp.message(Command("dynamic"))
async def dynamic_command(message: Message):
    await message.answer("Нажмите чтобы показать опции:", reply_markup=kb.get_dynamic_keyboard())

@dp.callback_query(F.data == "show_more")
async def show_more_handler(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=kb.get_dynamic_keyboard(show_more=True))
    await callback.answer()

@dp.callback_query(F.data.startswith("option_"))
async def option_handler(callback: CallbackQuery):
    option = callback.data.split("_")[1]
    await callback.message.answer(f"Выбрана опция {option}")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())