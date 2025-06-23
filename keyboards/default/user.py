from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share phone number ☎️", request_contact=True)]
    ], 
    resize_keyboard=True, one_time_keyboard=True
)
location_share = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share phone location 📍", request_location=True)]
    ], 
    resize_keyboard=True, one_time_keyboard=True
)


user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menu 📕")],
        [KeyboardButton(text="my orders 🥄")],
        [KeyboardButton(text="basket 🧺"), KeyboardButton(text="call ☎️")],
        [KeyboardButton(text="send message 📧"), KeyboardButton(text="settings ⚙️")],
    ],
    resize_keyboard=True,
    is_persistent=True
)

