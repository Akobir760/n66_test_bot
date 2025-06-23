from asyncio import run
from aiogram import Bot, Dispatcher
from core.config import TOKEN
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.enums import ParseMode
from routers import common, register
from core.table_queries import initializing_table


async def startup():
    initializing_table()


async def shutdown():
    pass

async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)   
    dp = Dispatcher()
    dp.include_router(router=common.router)
    dp.include_router(router=register.router)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    await dp.start_polling(bot, polling_timeout=0)


if __name__ == "__main__":
    run(main())