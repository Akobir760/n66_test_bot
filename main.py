from asyncio import run
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Setlar")],
        [KeyboardButton(text="Lavash"), KeyboardButton(text="Shaurma")],
        [KeyboardButton(text="Burger"), KeyboardButton(text="Hot-Dog")],
        [KeyboardButton(text="Ichimliklar")],
        [KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    is_persistent=True
)

async def start_handler(message: types.Message, bot: Bot):
    await bot.send_message(chat_id=message.chat.id, text = "🛒 Asosiy Menyu\n Marhamat buyurtma berishingiz mumkin!", reply_markup=user_main_keyboard)

async def menu_handler(message: types.Message):
    text = "Tanlang:"
    await message.answer(text=text, reply_markup=menu_keyboard)

async def my_orders_handler(message: types.Message):
    text = "Asosiy menu bosildi"
    await message.answer(text=text)

async def main():
    bot = Bot(token="8099267684:AAEIOZGBnGK5yNy1f1IMsuu9SzH5_-BqNKA")
    dp = Dispatcher()
    dp.message.register(start_handler, Command('start'))
    dp.message.register(menu_handler, F.text == "Menyu")
    dp.message.register(start_handler, F.text == "Orqaga")
    dp.message.register(my_orders_handler, F.text == "Savat")
    dp.message.register(my_orders_handler, F.text == "Mening buyurtmalarim")
    dp.message.register(my_orders_handler, F.text == "Aloqa")
    dp.message.register(my_orders_handler, F.text == "Xabar yuborish")
    dp.message.register(my_orders_handler, F.text == "Sozlamalar")

    await dp.start_polling(bot, polling_timeout=0)

if __name__ == "__main__":
    run(main())