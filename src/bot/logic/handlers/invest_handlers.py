import asyncio

from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery, Message, ReplyKeyboardRemove,
)
from aiogram import F, Router

from src.bot.structures.fsm.register import RegisterGroup, RegisterMessage
from src.bot.structures.keyboards.registration_kb import application
from src.bot.structures.text.text import info_text
from src.configuration import conf

invest_router = Router(name = 'invest_router')

WHO_PARTNER = 'AgACAgIAAxkBAAIDsWXuJKeydI7nhzcJ3F7yjJ5J4IdbAAKi2TEbRVZwS4IKS5ivRinFAQADAgADeQADNAQ'
HOW_WORK = 'AgACAgIAAxkBAAIDs2XuJU0zS475Z36e26Kuw0AcQoELAAKj2TEbRVZwS2TNjB05rvXJAQADAgADeQADNAQ'
PR = 'AgACAgIAAxkBAAIDtWXuJaDHNLTjF-njKX1pDD04KPMMAAKl2TEbRVZwS3E06ptv9ZdnAQADAgADeQADNAQ'
CHAT_ID = '-1002008269761'


@invest_router.message(F.text == 'Инвестирование (ипотечное кредитование) 💸', RegisterGroup.select)
async def invest_without_callback_button(message: Message, state: FSMContext):
    await message.answer_photo(photo = WHO_PARTNER, caption = info_text)
    await message.answer_photo(photo = HOW_WORK)
    await message.answer_photo(photo = PR, reply_markup = application)


@invest_router.message(F.text == 'Инвестирование собственных средств 💵', RegisterGroup.select)
async def invest_with_callback_button(message: Message, state: FSMContext
                                      ):
    await message.answer(text = f"Ты можешь стать куратором и приводить людей\n"
                                         f"Оставляй заявку и мы свяжемся с тобой, чтобы рассказть подробные условия\n"
                                  , reply_markup = application)


@invest_router.message(F.text == 'partner_with')
async def invest_with_callback_button(message: Message, state: FSMContext):
    await message.answer(text = "", reply_markup = application)


@invest_router.message(F.text == "Оставить заявку для сотрудничества 📝")
async def invest_application(message: Message, state: FSMContext):
    await message.answer(text = f"Ответным сообщением напиши, как можно с тобой связаться? \n"
                                f"Интересующий вопрос?\n")
    await state.set_state(RegisterMessage.text_message)


@invest_router.message(RegisterMessage.text_message)
async def invest_message_handler(message: Message, state: FSMContext):
    await message.answer(text = message.text, reply_markup = ReplyKeyboardRemove())
    await state.update_data(messageSend = message.text)
    await message.answer(text = f"Обращения, я зарегистрировал.\n"
                                          f"Скоро мы свяжемся с тобой")
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)
    message_data = await state.get_data()
    message_send = message_data.get('messageSend')
    chat_message_text = (
        f"Пользователь {username} (ID: {user_id}) успешно зарегистрирован.\n"
        f"ФИО: {reg_name}\n"
        f"Cообщение: {message_send}\n"
    )
    await message.bot.send_message(CHAT_ID, chat_message_text)
