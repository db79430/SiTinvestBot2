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
    await state.update_data(
        phone_number = message.contact.phone_number,
        user_id = message.contact.user_id,
    )
    chat_message = (
        f"Зарегистрировался новый пользователь (поделился контактом)\n"
        f"Пользователь @{username} (ID: {user_id}) успешно зарегистрирован.\n"
        f"ФИО: {reg_name}\n"
        f"Телефон: {phone_number}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message)


async def send_reg_data_tg_user_chat(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    user_id = message.from_user.id
    username = message.from_user.username
    chat_message = (
        f"Зарегистрировался новый пользователь (через никнейм тг)\n"
        f"Пользователь @{username} (ID: {user_id}) успешно зарегистрирован.\n"
        f"ФИО: {reg_name}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message)


async def send_message_chat_partner_handler(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_id = reg_data.get('user_id')
    reg_name = reg_data.get('regTgName')
    reg_phone = reg_data['phone_number']
    reg_name = reg_data.get('regFullName')
    username = str(message.from_user.username)
    chat_message_text = (
        f"Пользователь @{username} (ID: {reg_id}) отправил запрос связаться с ним\n"
        f"ФИО: {reg_name}\n"
        f"Телeфон: {reg_phone}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message_text)



