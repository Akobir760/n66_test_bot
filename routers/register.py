from aiogram import Router, types, F
from states.user import Register
from aiogram.fsm.context import FSMContext
from keyboards.default.user import phone_number_share_keyboard, location_share_keyboard, user_main_keyboard_keyboard
from loader import _

router = Router()

@router.callback_query(Register.language)
async def get_user_language_handler(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=call.data)
    text = _("Please enter your full name", locale=call.data)
    await call.message.answer(text=text)
    await state.set_state(Register.full_name)



@router.message(Register.full_name)
async def get_user_full_name_handler(message: types.Message, state:FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    language = data.get('language')

    await message.answer(text=_("Please share your phone number", locale=language), reply_markup=await phone_number_share_keyboard())
    await state.set_state(Register.phone_number)


@router.message(Register.phone_number, F.contact)
async def get_user_phone_number_handler(message: types.Message, state:FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)

    data = await state.get_data()
    language = data.get('language')


    await message.answer(text=_("Please share your location", locale=language), reply_markup=await location_share_keyboard())
    await state.set_state(Register.location)


@router.message(Register.location, F.location)
async def get_user_location_handler(message: types.Message, state:FSMContext):
    await state.update_data(longitude=message.location.longitude, latitude=message.location.latitude)

    data = await state.get_data()
    language = data.get('language')


    await message.answer(text=_("You have successfully registered!", locale=language), reply_markup=await user_main_keyboard_keyboard())
    await state.clear()





