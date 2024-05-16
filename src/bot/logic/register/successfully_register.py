import urllib

from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.configuration import conf


async def send_reg_data_user_chat(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    phone_number = str(message.contact.phone_number)
    user_id = str(message.contact.user_id)
    username = str(message.from_user.username)
    link_name = reg_data.get('link_name')
    print(link_name)

    await state.update_data(
        link_name = link_name,
        phone_number = phone_number,
        user_id = user_id,
    )

    chat_message_contact = (
        f"Зарегистрировался новый пользователь (поделился контактом)\n"
        f"Пользователь @{username} (ID: {user_id}) успешно зарегистрирован.\n"
        f"ИМЯ: {reg_name}\n"
        f"Телефон: {phone_number}\n"
        f"Пользователь перешел для регистрации по ссылке: {link_name}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message_contact)


async def send_reg_data_tg_user_chat(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    user_id = message.from_user.id
    username = message.from_user.username
    link_type = reg_data.get('link_name')
    reg_tg_name = message.from_user.username
    chat_message = (
        f"Зарегистрировался новый пользователь (через никнейм тг)\n"
        f"Пользователь @{username} (ID: {user_id}) успешно зарегистрирован.\n"
        f"ИМЯ: {reg_name}\n"
        f"Никнейм: @{reg_tg_name}\n"
        f"Пользователь перешел для регистрации по ссылке: {link_type}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, text = chat_message)
