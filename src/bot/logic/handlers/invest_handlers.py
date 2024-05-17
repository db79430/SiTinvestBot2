from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import (Message, ReplyKeyboardRemove)
from aiogram import F, Router
from src.bot.structures.fsm.state import RegisterGroup, UserSelect
from src.bot.structures.keyboards.buttons import contact_us, contact_us_buy_home, contact_us_sale_home, \
    contact_us_w_money, \
    contact_us_wo_money, \
    contact_us_work, invest_categories_kb, menu_kb
from src.configuration import conf

invest_router = Router(name = 'invest_router')

TEXT_1 = 'AgACAgIAAxkBAAP2Zjjsib2ACRknaZNojNERu92HsqYAAsPfMRvIrslJolbGchFQ928BAAMCAAN5AAM1BA'
TEXT_2 = 'AgACAgIAAxkBAAP4Zjjstls7zBYmNMGOTmu0TwHRhSAAAsXfMRvIrslJCvmEW8an1dQBAAMCAAN5AAM1BA'
WHO_SEARCH = 'AgACAgIAAxkBAAP-ZjjtDta3omaz_UmkKgidP5X_CAoAAsnfMRvIrslJmH1ChaZGcrYBAAMCAAN5AAM1BA'
PARTNER_IMG = 'AgACAgIAAxkBAAIBAmY48QG9zsPzWpVn5nAawNAPUbDyAALW3zEbyK7JSSQohXvRYCP6AQADAgADeQADNQQ'
INVEST_IMG = 'AgACAgIAAxkBAAIDX2ZEacgEPTP7AAHcaafsWBrjgGxv3gACqtYxGw6PIUq2Gbrd4boCCwEAAwIAA3kAAzUE'
CONCEPT_IMG_1 = 'AgACAgIAAxkBAAP6Zjjs1tp3mc4JQ7iffSLS_U_rjq0AAsffMRvIrslJC9sGB7TeQHsBAAMCAAN5AAM1BA'
CONCEPT_IMG_2 = 'AgACAgIAAxkBAAIBDWY48faJMkhzb1_tBLt2f7dfgoI1AALI3zEbyK7JSUB6NItOu5JgAQADAgADeQADNQQ'
BY_HOME_LIFE = 'AgACAgIAAxkBAAIEM2ZEnZIlpaWmlSU_KcqHQmYGCMWjAAL21zEbDo8hSnqNcK6JWSTPAQADAgADeQADNQQ'
BY_HOME_SALE = 'AgACAgIAAxkBAAIBBGY48UxqNNmIFtZSvheqx-BnlSkeAALY3zEbyK7JSb3ZfxB7YdqtAQADAgADeQADNQQ'
CHAT_ID = '-1002008269761'
INVEST_MONEY_IMG = 'AgACAgIAAxkBAAIDbmZEai3L1RastxUXyAE4kNo01lWdAAKu1jEbDo8hSo7IJfHsuxHtAQADAgADeQADNQQ'

DOCUMENT_ID_KOPNINO = 'BQACAgIAAxkBAAIGAAFmRN22lhLX4kTu_iyFzLOomKfKEgACe08AAg6PIUqhcRblCqmU4jUE'
DOCUMENT_ID_VILLAGE = 'BQACAgIAAxkBAAIGAmZE3ynz7F2EV2jnmIUx9WEc8FB8AAKeTwACDo8hSpq_hs_pCx_gNQQ'
DOCUMENT_ID_BELAVINO = 'BQACAgIAAxkBAAIGDmZE4evSQ-6OIOKvFVzn0OU2U6w5AALITwACDo8hSgwbMiLa273iNQQ'

text_contact = (f"Жаждешь подробностей? Просто нажми кнопку внизу 👇🏻\n"
                f"Оставь заявку, и мы отправим тебе всю информацию\n"
                f"и ответим на все твои вопросы.")


async def get_user_data(state: FSMContext, message: Message):
    data = await state.get_data()
    phone_number = None
    if message.contact:
        phone_number = message.contact.phone_number
    return {
        'reg_id': data.get('user_id'),
        'reg_name': str(message.from_user.username) or None,
        'reg_phone': data.get('phone_number'),
        'full_name': data.get('regFullName'),
        'phone_number': data.get('phone_number') or None,
        'username': str(message.from_user.username),
        'link_name': data.get('link_name')
    }


@invest_router.message(F.text == '💸 Инвестирование без вложений')
async def invest_without_callback_button(message: Message, state: FSMContext):
    await state.set_state(UserSelect.wo_money)
    await message.answer_photo(photo = INVEST_IMG)
    await message.answer_photo(photo = TEXT_1)
    await message.answer_photo(photo = TEXT_2)
    await message.answer_photo(photo = CONCEPT_IMG_1)
    await message.answer_photo(photo = CONCEPT_IMG_2)
    await message.answer_photo(photo = WHO_SEARCH)
    await message.answer(text = text_contact,
                         reply_markup = contact_us_wo_money)


@invest_router.message(F.text == '💬Заявка: инвестирование без вложений')
async def invest_application(message: Message, state: FSMContext):
    user_data = await get_user_data(state, message)
    chat_message_text = (
        f"Пользователь @{user_data['username']} (ID: {user_data['reg_id']}) "
        f"отправил запрос связаться с ним (ипотечное)\n"
        f"Имя: {user_data['full_name']}\n"
        f"Телефон: {user_data['phone_number']}\n"
        f"Никнейм: @{user_data['reg_name']}\n"
        f"Пользователь перешел по ссылке: {user_data['link_name']}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message_text, reply_markup=ReplyKeyboardRemove())


@invest_router.message(F.text == '💵 Инвестирование собственных средств')
async def invest_with_callback_button(message: Message, state: FSMContext):
    await state.set_state(UserSelect.w_money)
    await message.answer_photo(photo = INVEST_MONEY_IMG)
    await message.answer(text = text_contact,
                         reply_markup = contact_us_w_money)


@invest_router.message(F.text == '💬Заявка: инвестирование средств')
async def invest_application(message: Message, state: FSMContext):
    user_data = await get_user_data(state, message)
    chat_message_text = (
        f"Пользователь @{user_data['username']} (ID: {user_data['reg_id']}) "
        f"отправил запрос связаться с ним (инвест.собственных средств)\n"
        f"Имя: {user_data['full_name']}\n"
        f"Телефон: {user_data['phone_number']}\n"
        f"Никнейм: @{user_data['reg_name']}\n"
        f"Пользователь перешел по ссылке: {user_data['link_name']}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message_text, reply_markup=ReplyKeyboardRemove())


@invest_router.message(F.text == '🏡 Покупка дома для жилья')
async def invest_with_callback_button(message: Message, state: FSMContext):
    await state.set_state(UserSelect.buy_house)
    await message.answer_photo(photo = BY_HOME_LIFE)
    await message.answer_document(document = DOCUMENT_ID_KOPNINO)
    await message.answer_document(document = DOCUMENT_ID_VILLAGE)
    await message.answer_document(document = DOCUMENT_ID_BELAVINO)
    await message.answer(text = text_contact,
                         reply_markup = contact_us_buy_home)


@invest_router.message(F.text == '💬Заявка: покупка дома для жилья')
async def invest_application(message: Message, state: FSMContext):
    user_data = await get_user_data(state, message)
    chat_message_text = (
        f"Пользователь @{user_data['username']} (ID: {user_data['reg_id']}) "
        f"отправил запрос связаться с ним (покупка дома)\n"
        f"Имя: {user_data['full_name']}\n"
        f"Телефон: {user_data['phone_number']}\n"
        f"Никнейм: @{user_data['reg_name']}\n"
        f"Пользователь перешел по ссылке: {user_data['link_name']}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message_text, reply_markup=ReplyKeyboardRemove())


@invest_router.message(F.text == '🏘 Покупка дома для дальнейшей перепродажи')
async def invest_with_callback_button(message: Message, state: FSMContext):
    await message.answer_photo(photo = BY_HOME_SALE)
    await message.answer_document(document = DOCUMENT_ID_KOPNINO)
    await message.answer_document(document = DOCUMENT_ID_VILLAGE)
    await message.answer_document(document = DOCUMENT_ID_BELAVINO)
    await message.answer(text = text_contact,
                         reply_markup = contact_us_sale_home)


@invest_router.message(F.text == '💬Заявка: покупка дома для перепродажи')
async def invest_application(message: Message, state: FSMContext):
    user_data = await get_user_data(state, message)
    chat_message_text = (
        f"Пользователь @{user_data['username']} (ID: {user_data['reg_id']}) "
        f"отправил запрос связаться с ним (перепродажа дома)\n"
        f"Имя: {user_data['full_name']}\n"
        f"Телефон: {user_data['phone_number']}\n"
        f"Никнейм: @{user_data['reg_name']}\n"
        f"Пользователь перешел по ссылке: {user_data['link_name']}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message_text, reply_markup=ReplyKeyboardRemove())


@invest_router.message(F.text == '👨🏻‍💻 Работать с нами')
async def invest_with_callback_button(message: Message, state: FSMContext):
    await state.set_state(UserSelect.work)
    await message.answer_photo(photo = PARTNER_IMG)
    await message.answer(text = text_contact,
                         reply_markup = contact_us_work)


@invest_router.message(F.text == '💬Заявка: работать с нами')
async def invest_application(message: Message, state: FSMContext):
    user_data = await get_user_data(state, message)
    chat_message_text = (
        f"Пользователь @{user_data['username']} (ID: {user_data['reg_id']}) "
        f"отправил запрос связаться с ним (работать с нами)\n"
        f"Имя: {user_data['full_name']}\n"
        f"Телефон: {user_data['phone_number']}\n"
        f"Никнейм: @{user_data['reg_name']}\n"
        f"Пользователь перешел по ссылке: {user_data['link_name']}\n"
    )
    await message.bot.send_message(conf.chat.chat_id, chat_message_text, reply_markup=ReplyKeyboardRemove())


@invest_router.message(F.text == '💬 Задать вопрос')
async def invest_with_callback_button(message: Message, state: FSMContext):
    if not message.text.startswith('/'):
        await message.answer(text = "Мы всегда на связи, напиши нам. 🤗")
        await message.answer("https://t.me/SiT_investment", link_preview = False)
        # await state.set_state(RegisterGroup.question)


# @invest_router.message(RegisterGroup.question)
# async def handle_question(message: Message, state: FSMContext):
#     if not message.text.startswith('/'):
#         await message.answer(text = "Мы получили ваше сообщение, скоро свяжемся")
#     reg_data = await state.get_data()
#     reg_id = str(message.from_user.id)
#     reg_name = reg_data.get('regTgName') or None
#     reg_phone = reg_data.get('phone_number') or None
#     reg_name = reg_data.get('regFullName')
#     username = str(message.from_user.username)
#     send_message_text_user = (
#         f"Пользователь @{username} (ID: {reg_id}) отправил сообщение в чат\n"
#         f"ФИО: {reg_name}\n"
#         f"Телефон: {reg_phone}\n"
#         f"Никнейм: @{username}\n"
#         f"Cообщение пользователя: {message.text}\n"
#     )
#     await message.bot.send_message(conf.chat.chat_id, send_message_text_user)


@invest_router.message(F.text == '💼 Меню')
async def handle_click_menu(message: Message, state: FSMContext):
    await message.answer(text = "Выбери инетересующую категорию 👇🏻",
                         reply_markup = invest_categories_kb)


@invest_router.message()
async def message_user(message: Message, state: FSMContext):
    if not message.text.startswith('/'):
        await message.reply(text = "Oй, я такого не знаю. Нажми кнопку меню и выбери из что-нибудь из списка!", reply_markup=menu_kb)
