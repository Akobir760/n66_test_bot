from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.user import user_main_keyboard
from states.user import Feedback
from loader import _

router = Router()


@router.message(Feedback.feedback, F.text == "Back ⬅️")
async def back_user_main_menu(message: types.Message, state: FSMContext):
    text = _("Main menu")
    await message.answer(text=text, reply_markup=user_main_keyboard)
    await state.clear()