import re
from aiogram import Bot, F
from aiogram.enums import ContentType, ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, Update
from src.bot.structures.fsm.register import (
    RegisterGroup, )
from src.configuration import conf
from ...send_message import send_message
from ...structures.keyboards.invest_kb import invest_categories_kb
from .router import register_router
from ...structures.keyboards.registration_kb import contacts_btn
from ...structures.text.text import register_btn_text

CATEGORIES_IMG = 'AgACAgIAAxkBAAIDm2XuGgRJg3X8YU6hqBSKIssbdjG8AAKH2TEbRVZwS7nkLuVLMxOGAQADAgADeQADNAQ'
CHAT_ID = '-1002008269761'


@register_router.callback_query(F.data == 'register', RegisterGroup.confirmation)
async def register_confirmation(call: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterGroup.regFullName)
    return await call.message.answer(' 📝Введите ваше ФИО на русском языке:',
                                     reply_markup = ReplyKeyboardRemove())


@register_router.message(RegisterGroup.regFullName)
async def register_full_name(message: Message, state: FSMContext):
    # await state.clear()
    if re.findall('^[а-яА-Я ]+$', message.text):
        await message.reply(
            'Супер 🙂! Имя я записал\n'
            '📱Теперь нужно нажать на кнопку внизу, чтобы подделиться контактом\n',
            reply_markup = contacts_btn
        )
        await state.update_data(regFullName = message.text)
        await state.set_state(RegisterGroup.regContacts)
        print("Value of FullName:", message.text)
    else:
        await message.reply('Неккоректное имя')
        return await message.answer(' 📝Введите ваше ФИО на русском языке:')


@register_router.message(F.contact)
async def handle_contact(message: Message, state: FSMContext):
    global phone_number
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    phone_number = str(message.contact.phone_number)
    user_id = str(message.contact.user_id)
    username = str(message.from_user.username)
    await state.update_data(
        phone_number = message.contact.phone_number,
        user_id = message.contact.user_id
    )
    await state.set_state(RegisterGroup.regContacts)

    msg = (
        f'✅ Вы успешно зарегистрированы!\n'
        f'👇🏻Ниже представлены категории инвестирования.\n'
    )
    await message.answer(text = msg, reply_markup = ReplyKeyboardRemove())
    info = (
        # f'\n Ниже представлены категории инвестирования.\n'
        f'Выберите интересующий Вас раздел.\n'
    )
    await state.set_state(RegisterGroup.select)
    await message.answer_photo(photo = CATEGORIES_IMG, caption = info, reply_markup = invest_categories_kb)

    # Create a formatted message to send to the chat
    chat_message = (
        f"Пользователь {username} (ID: {user_id}) успешно зарегистрирован.\n"
        f"ФИО: {reg_name}\n"
        f"Телефон: {phone_number}\n"
    )
    await message.bot.send_message(CHAT_ID, chat_message)

# @register_router.message(RegisterGroup.regContacts)
# async def successful_registration(message: Message, state: FSMContext):
#     await state.clear()
#     await state.set_state(RegisterGroup.regContacts)
#     msg = (
#         f'✅ Вы успешно зарегистрированы!\n'
#         # f'Мы сохранили Вашу информацию и скоро свяжемся с Вами.\n'
#     )
#     await message.answer(text = msg, reply_markup = ReplyKeyboardRemove())
#     info = (
#         f'\n Ниже представлены категории инвестирования.\n'
#         f'Выберите интересующий Вас рездел.\n'
#     )
#     await state.set_state(RegisterGroup.select)
#     print("Value of Info:", RegisterGroup.select)
#     full_name = message.from_user.first_name
#     contact = message.from_user.contact
#     username = message.from_user.username
#     await message.send_message(CHAT_ID, f'fИмя пользователя{username}, контакт{contact}, ФИО{full_name}')
#     print("Value of Message:", full_name, contact, username)
#     await message.answer_photo(photo = CATEGORIES_IMG, caption = info, reply_markup = invest_categories_kb)
#     await send_message(message.from_user, message.text)
