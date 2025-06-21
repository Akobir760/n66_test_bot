from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.user import Register

router = Router()

@router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    text = "Assalomu alaykum"
    await message.answer(text=text)
    await state.set_state(Register.language)