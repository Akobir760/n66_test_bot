from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.user import Register
from keyboards.inline.user import languages
from loader import _

router = Router()

@router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    text = _("Assalomu alaykum, please select the language!")
    await message.answer(text=text, reply_markup=languages)
    await state.set_state(Register.language)