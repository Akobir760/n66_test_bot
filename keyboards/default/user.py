from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=_("Share phone number ☎️"), request_contact=True)]
    ], 
    resize_keyboard=True, one_time_keyboard=True
)
location_share = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=_("Share phone location 📍"), request_location=True)]
    ], 
    resize_keyboard=True, one_time_keyboard=True
)


user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=_("Menu 📕"))],
        [KeyboardButton(text=_("my orders 🥄"))],
        [KeyboardButton(text=_("basket 🧺")), KeyboardButton(text=_("call ☎️"))],
        [KeyboardButton(text=_("Send feedback ✍️")), KeyboardButton(text=_("settings ⚙️"))],
    ],
    resize_keyboard=True,
    is_persistent=True
)


async def back_user_menu_keyboard():
    ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Back")
        ]], resize_keyboard=True
    )

