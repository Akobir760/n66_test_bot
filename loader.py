from aiogram.utils.i18n import I18n
from core.config import I18N_DOMAIN, LOCALES_DIR
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from core.config import TOKEN

i18n = I18n(path=LOCALES_DIR, default_locale="en", domain=I18N_DOMAIN)
_=i18n.gettext  

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
