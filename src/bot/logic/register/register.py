import re
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from src.bot.structures.fsm.state import RegisterGroup
from src.configuration import conf
from .successfully_register import send_reg_data_tg_user_chat, send_reg_data_user_chat
from ...structures.keyboards.invest_kb import invest_categories_kb
from .router import register_router
from ...structures.keyboards.registration_kb import contacts_btn, phone_numbers_btn

CATEGORIES_IMG = 'AgACAgIAAxkBAAIMzWYHEA3Ksq-HvEmDemrtXT0LwMZNAAJ02TEb9jw4SMCxC-4t-DnyAQADAgADeQADNAQ'
info = 'Выбери интересующий раздел 👇🏻.\n'


@register_router.callback_query(F.data == 'register', RegisterGroup.confirmation)
async def register_confirmation(call: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterGroup.regFullName)
    return await call.message.answer(' 📝Введите ваше ФИО на русском языке:',
                                     reply_markup = ReplyKeyboardRemove())


@register_router.message(RegisterGroup.regFullName)
async def register_full_name(message: Message, state: FSMContext):
    if re.findall('^[а-яА-Я ]+$', message.text):
        await message.reply(
            'Супер 🙂! Имя я записал'
            '\n 📱Теперь нужно нажать на кнопку внизу, чтобы подделиться контактом или никнеймом tg\n',
            reply_markup = contacts_btn
        )
        await state.update_data(regFullName = message.text)
        await state.set_state(RegisterGroup.regPhone)
    else:
        await message.reply('Неккоректное имя')
        return await message.answer(' 📝Введите ваше ФИО на русском языке:')


@register_router.message(F.text == "🔔 Поделиться именем тг")
async def register_tg_name(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    await state.set_state(RegisterGroup.regTgName)
    reg_tg_name = reg_data.get('regTgName')
    msg = (
        f'\n✅ Твой никнейм: @{message.from_user.username}\n'
        f'\n✅ Твое ФИО: {reg_name}\n'
        f'\n🤗 Регистрация прошла успешно!\n'
        f'\n👇🏻 Ниже представлены категории инвестирования.\n'
    )
    if reg_tg_name is None:
        print(reg_tg_name)
        await message.answer(text = f"🥺 Упппс твой тг никнейм скрыт.\n "
                                    f"\n Нажми кнопку, пожалуйста, 📞 Поделиться контактом\n"
                                    f"\n Чтобы продолжить взаимодействие с ботом",
                             reply_markup = phone_numbers_btn)
    else:
        await message.answer(text = msg, reply_markup = ReplyKeyboardRemove())
        await send_reg_data_tg_user_chat(message, state)
        await send_sit_photo(message, state)


@register_router.message(F.contact)
async def register_phone(message: Message, state: FSMContext):
    await state.set_state(RegisterGroup.regPhone)
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    phone_number = str(message.contact.phone_number)
    await state.update_data(regTgName = message.from_user.username)
    msg = (
        f'\n✅ Твой никнейм: @{message.from_user.username}\n'
        f'\n✅ Твой телефон: {phone_number}\n'
        f'\n✅ Твое ФИО: {reg_name}\n'
        f'\n🤗 Регистрация прошла успешно!\n'
        f'\n👇🏻Ниже представлены категории инвестирования.\n'
    )
    await message.answer(text = msg, reply_markup = ReplyKeyboardRemove())
    await send_reg_data_user_chat(message, state)
    await send_sit_photo(message, state)


async def send_sit_photo(message: Message, state: FSMContext):
    await message.answer_photo(photo = CATEGORIES_IMG, caption = info, reply_markup = invest_categories_kb)




