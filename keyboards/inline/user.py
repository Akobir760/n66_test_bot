from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


languages = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Uzbek", callback_data="uz"),
        InlineKeyboardButton(text="Russian", callback_data="ru"),
        InlineKeyboardButton(text="English", callback_data="en"),
    ]]
)