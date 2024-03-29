import asyncio

from aiogram.enums import ContentType, ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery, Message, ReplyKeyboardRemove,
)
from aiogram import F, Router

from src.bot.logic.register.successfully_register import send_message_chat_partner_handler
from src.bot.structures.keyboards.invest_kb import contact_us, invest_categories_kb, menu_kb
from src.bot.structures.keyboards.registration_kb import contacts_btn
from src.configuration import conf

invest_router = Router(name = 'invest_router')

WHO_PARTNER = 'AgACAgIAAxkBAAIDsWXuJKeydI7nhzcJ3F7yjJ5J4IdbAAKi2TEbRVZwS4IKS5ivRinFAQADAgADeQADNAQ'
HOW_WORK = 'AgACAgIAAxkBAAIDs2XuJU0zS475Z36e26Kuw0AcQoELAAKj2TEbRVZwS2TNjB05rvXJAQADAgADeQADNAQ'
PR = 'AgACAgIAAxkBAAIDtWXuJaDHNLTjF-njKX1pDD04KPMMAAKl2TEbRVZwS3E06ptv9ZdnAQADAgADeQADNAQ'
PARTNER_IMG = 'AgACAgIAAxkBAAIJbWYCZULeAAHT0-MC4mtK2AmUCphewgACiOAxG5AnEUhtxe7U2KM0iAEAAwIAA3kAAzQE'
INVEST_IMG = 'AgACAgIAAxkBAAIJqGYD4PYDqP-LgyR5uqyWbUL31nHNAAKU2TEbYNAhSMlV-inL_zzpAQADAgADeQADNAQ'
CHAT_ID = '-1002008269761'


@invest_router.message(F.text == 'Инвестирование (ипотечное кредитование) 💸')
async def invest_without_callback_button(message: Message, state: FSMContext):
    await message.answer_photo(photo = WHO_PARTNER)
    await message.answer_photo(photo = HOW_WORK)
    await message.answer_photo(photo = PR, reply_markup = contact_us)
    await message.answer(text = f"Для подробной информации, нажимай кнопку 👇🏻\n "
                                f" 💬Связаться со мной",
                         reply_markup = contact_us)


@invest_router.message(F.text == 'Инвестирование собственных средств 💵')
async def invest_with_callback_button(message: Message, state: FSMContext):
    await message.answer_photo(photo = INVEST_IMG, reply_markup = contact_us)
    await message.answer(text = f"Для подробной информации, нажимай кнопку 👇🏻\n "
                                f" 💬Связаться со мной",
                         reply_markup = contact_us)


@invest_router.message(F.text == 'Стать нашим партнером 💼')
async def invest_with_callback_button(message: Message, state: FSMContext):
    await message.answer_photo(photo = PARTNER_IMG)
    await message.answer(text = f"Для подробной информации, нажимай кнопку 👇🏻\n "
                                f"💬Связаться со мной",
                         reply_markup = contact_us)


@invest_router.message(F.text == 'Связаться со мной 💬')
async def invest_contact_application(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_name = reg_data.get('regTgName')
    reg_phone = reg_data['phone_number']
    # if (reg_name and not reg_phone) or (reg_phone and not reg_name):
    await message.answer(text = "✅Запрос принят. Скоро мы свяжемся с тобой",
                             reply_markup = menu_kb)
    await send_message_chat_partner_handler(message, state)
    # else:
    #     await message.answer(text = f"⚠️🤖 Я не увидел Ваших контактов.\n"
    #                                 f"\n   Пожалуйста поделитесь контактом, чтобы я обработал сообщение",
    #                          reply_markup = contacts_btn)


@invest_router.message(F.text == "Меню 💼")
async def handle_click_menu(message: Message, state: FSMContext):
    await message.answer(text = "Выбери инетересующую категорию 👇🏻",
                         reply_markup = invest_categories_kb)


# @invest_router.message(F.text == "Оставить заявку 📝")
# async def invest_application(message: Message, state: FSMContext):
#     await message.answer(text = f"Ответным сообщением напиши, как можно с тобой связаться? \n"
#                                 f"Интересующий вопрос?\n")
#     await state.set_state(RegisterMessage.text_message)


class CantParseEntities:
    pass


@invest_router.message(lambda message: not message.text.startswith("/"))
async def send_message_user(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_id = str(message.from_user.id)
    reg_name = reg_data.get('regTgName') or None
    reg_phone = reg_data.get('phone_number') or None
    reg_name = reg_data.get('regFullName')
    username = str(message.from_user.username)
    send_message_text_user = (
        f"Пользователь @{username} (ID: {reg_id}) отправил сообщение в чат\n"
        f"ФИО: {reg_name}\n"
        f"Телефон: {reg_phone}\n"
        f"Cообщение пользователя: {message.text}\n"
    )
    try:
        if isinstance(message.text, str):
            await message.bot.send_message(conf.chat.chat_id, send_message_text_user, parse_mode = ParseMode.HTML)
    except CantParseEntities:
        await message.bot.send_message(conf.chat.chat_id, send_message_text_user, parse_mode = ParseMode.HTML)
