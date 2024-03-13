"""This file represents a start logic."""

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputFile, InputMediaPhoto, Message, PhotoSize
from src.bot.filters.register_filter import RegisterFilter
from src.bot.structures.fsm.register import RegisterGroup

from src.bot.structures.keyboards.menu_btn import menu_btn
from src.bot.structures.keyboards.registration_kb import register_kb

start_router = Router(name = 'start')

START_IMG = 'AgACAgIAAxkBAAIDY2XuDyW3T3ObPepm3go80JDJygweAAJy2TEbRVZwS9gHq-wc7N3_AQADAgADeQADNAQ'


@start_router.message(CommandStart(), RegisterFilter())
async def start_wo_register(message: Message, state: FSMContext):
    await state.set_state(RegisterGroup.confirmation)
    await message.answer_photo(photo = START_IMG)
    await message.answer(
        text = f'Привет, {message.from_user.full_name} 👋!'
               f'\n На связи бот и команда SiTInvest.'
               f'\n 🏘Мы занимаемся инвестициями в сфере недвижимости.\n'
               f'\n 🤖В этом боте ты получишь информацию, что такое инвестирование в недвижимость и сможешь '
               f'начать зарабатывать уже сегодня'
               f"\n Нажимай на кнопку внизу 'регистрация', чтобы узнать подробнее о нашем проекте 😊\n",
        reply_markup = register_kb
    )


@start_router.message(F.photo)
async def photo(message: Message):
    photo_data = message.photo[-1].file_id
    await message.answer(f'{photo_data}')


@start_router.message(CommandStart())
async def start_w_register(message: Message):
    markup = menu_btn()
    return await message.answer('Меню', reply_markup = markup)
