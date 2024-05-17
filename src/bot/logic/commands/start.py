"""This file represents a start logic."""
import urllib

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.bot.structures.fsm.state import RegisterGroup
from src.bot.structures.keyboards.buttons import invest_categories_kb, register_kb

start_router = Router(name = 'start')

START_IMG = 'AgACAgIAAxkBAAMuZjinXww9dNg1sh2Xk9RQ_JHyAAHGAAI72jEb4RTJSeF1rKGaBhShAQADAgADeQADNQQ'
START_IMG_2 = 'AgACAgIAAxkBAAMjZjilAvt8Q9RVTsGICrjeMBATgDkAAi7aMRvhFMlJnjBX8GYEmMsBAAMCAAN5AAM1BA'
START_IMG_3 = 'AgACAgIAAxkBAAIF02ZE2nonyFG5_QxhGhBLGtDMmNt_AAIm2jEbDo8hSsJBoF17oluTAQADAgADeQADNQQ'

referral_links = {
    "insta": "https://t.me/SITinvest_bot?start=insta",
    "football": "https://t.me/SITinvest_bot?start=football",
    "distribution": "https://t.me/SITinvest_bot?start=distribution",
    "dance": "https://t.me/SITinvest_bot?start=1234567",
    "friends": "https://t.me/SITinvest_bot?start=friends",
    "promo": "https://t.me/SITinvest_bot?start=promo",
    "biglini": "https://t.me/SITinvest_bot?start=biglini",
    "prosto_bot": "https://t.me/SITinvest_bot?start=start"
}


@start_router.message(CommandStart())
async def start_wo_register(message: Message, state: FSMContext) -> None:
    if message.text.startswith("/start"):
        link_name = message.text[7:]
        if link_name:
            await state.update_data(link_name=link_name)
        else:
            await state.update_data(link_name= "Перешел через поиск тг")
    text = (f'\nНиже представлено меню бота 💼\n'
            f'\nВыбери интересующую категорию 👇🏻\n')
    state_data = await state.get_data()
    user_id = state_data.get('user_id')
    if not user_id:
        await message.answer_photo(photo = START_IMG)
        await message.answer_photo(photo = START_IMG_2)
        await message.answer_photo(photo = START_IMG_3)
        await message.answer(
            text = f'\nПривет, {message.from_user.full_name} 👋!\n'
                   f'\nНа связи бот и команда SITinvest.\n'
                   f'\n🏘 Мы занимаемся инвестициями в сфере строительства.\n'
                   f'\n🤖 В этом боте ты получишь информацию, что такое инвестирование в недвижимость и сможешь '
                   f'\nначать зарабатывать уже сегодня\n'
                   f"\nНажимай на кнопку внизу 'регистрация', чтобы узнать подробнее о нашем проекте 😊\n",
            reply_markup = register_kb
        )
    else:
        await message.answer_photo(photo = START_IMG_3, caption = text,
                                   reply_markup = invest_categories_kb)


@start_router.message(F.photo)
async def start_photo(message: Message):
    photo_data = message.photo[-1].file_id
    await message.answer(f'{photo_data}')


@start_router.message(F.document)
async def start_document(message: Message):
    document_id = message.document.file_id
    await message.answer(f'{document_id}')
