import logging
from asyncio import run

from aiogram import Bot
# from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
# from aiohttp import web

from middlewares.db_settings import DbSessionMiddleware
from middlewares.language import LanguageMiddleware
from middlewares.subscription import SubscribeMiddleware
from routers import start, register, feedback, backs, user_menu
from utils.commands import set_my_commands
from core.config import DEVELOPER
from loader import bot, dp, i18n

# # bind localhost only to prevent any external access
# WEB_SERVER_HOST = "127.0.0.1"
# # Port for incoming request from reverse proxy. Should be any available port
# WEB_SERVER_PORT = 8080

# # Path to webhook route, on which Telegram will send requests
# WEBHOOK_PATH = "/webhook"
# # Secret key to validate requests from Telegram (optional)
# WEBHOOK_SECRET = "SECRET"


async def startup(bot: Bot):
    # await bot.set_webhook(
    #     url=f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",
    #     secret_token=WEBHOOK_SECRET,
    #     drop_pending_updates=True
    # )
    await set_my_commands(bot)
    await bot.send_message(text="Bot start to work", chat_id=DEVELOPER)


async def shutdown(bot: Bot):
    await bot.send_message(text="Bot stopped", chat_id=DEVELOPER)


async def main():
    dp.include_router(router=start.router)
    dp.include_router(router=register.router)
    dp.include_router(router=feedback.router)
    dp.include_router(router=backs.router)
    dp.include_router(router=user_menu.router)

    dp.message.middleware.register(DbSessionMiddleware())
    dp.message.middleware.register(LanguageMiddleware(i18n=i18n))
    dp.message.middleware.register(SubscribeMiddleware())

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    
    await dp.start_polling(bot, polling_timeout=0)


    # app = web.Application()

    # webhook_requests_handler = SimpleRequestHandler(
    #     dispatcher=dp,
    #     bot=bot,
    #     secret_token=WEBHOOK_SECRET,
    # )
    # webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # setup_application(app, dp, bot=bot)

    # web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == '__main__':
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.ERROR
    )
    logging.getLogger("aiogram.event").setLevel(logging.ERROR)
    run(main())