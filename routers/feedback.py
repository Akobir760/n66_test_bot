from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext

from keyboards.default.user import back_user_menu_keyboard, user_main_keyboard_keyboard
from states.user import Feedback
from core.config import DEVELOPER
from loader import _

router = Router()


@router.message(F.text.in_(["Send feedback ✍️", "Отправить отзыв ✍️", "Izoh yuborish ✍️"]))
async def send_feedback_handler(message: types.Message, state: FSMContext):
    text = _("Please enter your message in one text")
    await message.answer(text=text, reply_markup=await back_user_menu_keyboard())

    await state.set_state(Feedback.feedback)


@router.message(Feedback.feedback)
async def get_feedback_handler(message: types.Message, state: FSMContext, bot: Bot):
    user = []
    feedback = f"""
User: {message.from_user.mention_html(f'{user[1]}')}
Feedback: {message.text}
    """
    await bot.send_message(text=feedback, chat_id=DEVELOPER)

    text = _("Your feedback is sent to admins ✅")
    await message.answer(text=text, reply_markup=await user_main_keyboard_keyboard())
    await state.clear()

    await state.set_state(Feedback.feedback)