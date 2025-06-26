from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _

admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("Products ")),
            KeyboardButton(text=_("Categories ")),
        ],
        [
            KeyboardButton(text=_("Users ")),
            KeyboardButton(text=_("Orders "))
        ],
        [
            KeyboardButton(text=_("Statistics ")),
            KeyboardButton(text=_("Settings ")),
        ]
    ], resize_keyboard=True
)