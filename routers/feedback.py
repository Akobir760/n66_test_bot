from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext

from keyboards.default.user import back_user_menu_keyboard, user_main_keyboard
from states.user import Feedback
from core.config import DEVELOPER

router = Router()


@router.message(F.text == "Send feedback ✍️")
async def send_feedback_handler(message: types.Message, state: FSMContext):
    text = "Please enter your message in one text"
    await message.answer(text=text, reply_markup=back_user_menu_keyboard)

    await state.set_state(Feedback.feedback)


@router.message(Feedback.feedback)
async def get_feedback_handler(message: types.Message, state: FSMContext, bot: Bot):
    user = []
    feedback = f"""
User: {message.from_user.mention_html(f'{user[1]}')}
Feedback: {message.text}
    """
    await bot.send_message(text=feedback, chat_id=DEVELOPER)

    text = "Your feedback is sent to admins ✅"
    await message.answer(text=text, reply_markup=user_main_keyboard)
    await state.clear()

    await state.set_state(Feedback.feedback)