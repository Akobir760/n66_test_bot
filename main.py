from asyncio import run
from aiogram import Bot, Dispatcher
from core.config import  DEVELOPER, TOKEN
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.enums import ParseMode
from routers import common, register
from core.table_queries import initializing_table

# TOKEN = "8099267684:AAEIOZGBnGK5yNy1f1IMsuu9SzH5_-BqNKA"

async def startup():
    initializing_table()


import logging

from middlewares.db_settings import DbSessionMiddleware
from routers import start, register, feedback, backs
from utils.commands import set_my_commands


async def startup(bot: Bot):
    await set_my_commands(bot)
    await bot.send_message(text="Bot start to work", chat_id=DEVELOPER)


async def shutdown(bot: Bot):
    await bot.send_message(text="Bot stopped", chat_id=DEVELOPER)


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_router(router=start.router)
    dp.include_router(router=register.router)
    dp.include_router(router=feedback.router)
    dp.include_router(router=backs.router)

    dp.message.middleware.register(DbSessionMiddleware())

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot, polling_timeout=0)


if __name__ == '__main__':
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    run(main())
async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)   
    dp = Dispatcher()
    dp.include_router(router=common.router)
    dp.include_router(router=register.router)

    dp.startup.register(startup)
    await dp.start_polling(bot, polling_timeout=0)


if __name__ == "__main__":
    run(main())