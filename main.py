from asyncio import run
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

async def start_handler(message: types.Message, bot: Bot):
    print(message.from_user.full_name)
    await bot.send_message(chat_id=message.chat.id, text = "Salom")
    await message.answer(text=message.text)


async def main():
    bot = Bot(token="8099267684:AAEIOZGBnGK5yNy1f1IMsuu9SzH5_-BqNKA")
    dp = Dispatcher()
    dp.message.register(start_handler, Command('start'))

    await dp.start_polling(bot, polling_timeout=0)

if __name__ == "__main__":
    run(main())