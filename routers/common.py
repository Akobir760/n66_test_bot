from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start_handler(message: types.Message):
    text = "Assalomu alaykum"
    await message.answer(text=text)