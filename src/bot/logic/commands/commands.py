from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.bot.structures.keyboards.invest_kb import invest_categories_kb
from src.bot.structures.keyboards.menu_btn import menu_btn

commands_router = Router(name = 'commands')


@commands_router.message(Command('menu'))
async def show_menu(message: Message):
    await message.answer(text = 'Меню', reply_markup = invest_categories_kb)


@commands_router.message(Command('help'))
async def show_menu(message: Message):
    await message.answer(text = 'По всем вопросам, наша служба поддержки @SiT_investment, всегда на связи')


# async def show_help(message: Message):
#     await message.answer(
#         'По вопросам работы бота, обратитесь в службу поддержки @....'
#     )
