"""This file represents a start logic."""

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.bot.structures.fsm.state import RegisterGroup, UserClickButton
from src.bot.structures.keyboards.invest_kb import invest_categories_kb
from src.bot.structures.keyboards.registration_kb import register_kb
from src.configuration import conf
from src.db.db_commands import check_user_exists, is_registered_user

start_router = Router(name = 'start')

START_IMG = 'AgACAgIAAxkBAAIM0WYHELotGSRsX5XcN6RiD55xyd1TAAJF2TEb9jw4SMQGhbUeBqidAQADAgADeQADNAQ'
DOING_IMG = 'AgACAgIAAxkBAAIMz2YHEII3036FyBBhF28vb9UWqEX8AAJJ2TEb9jw4SPbiH30jRltwAQADAgADeQADNAQ'


@start_router.message(CommandStart())
async def start_wo_register(message: Message, state: FSMContext):
    await state.set_state(RegisterGroup.confirmation)
    state = await state.get_data()
    user_id = state.get('user_id')
    text = (f'\n Ниже представлено меню бота 💼\n'
            f'\n Выбери интересующую категорию 👇🏻\n')
    if not user_id:
        await message.answer_photo(photo = START_IMG)
        await message.answer(
            text = f'\nПривет, {message.from_user.full_name} 👋!\n'
                   f'\nНа связи бот и команда SiTInvest.\n'
                   f'\n🏘 Мы занимаемся инвестициями в сфере недвижимости.\n'
                   f'\n🤖 В этом боте ты получишь информацию, что такое инвестирование в недвижимость и сможешь '
                   f'\nначать зарабатывать уже сегодня\n'
                   f"\nНажимай на кнопку внизу 'регистрация', чтобы узнать подробнее о нашем проекте 😊\n",
            reply_markup = register_kb
        )
    else:
        await message.answer_photo(photo = DOING_IMG, caption = text,
                                   reply_markup = invest_categories_kb)


# @start_router.message(F.photo)
# async def start_photo(message: Message):
#     photo_data = message.photo[-1].file_id
#     await message.answer(f'{photo_data}')
