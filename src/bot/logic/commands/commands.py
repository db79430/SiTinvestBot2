from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand, BotCommandScopeDefault, Message
from src.bot.structures.keyboards.buttons import invest_categories_kb, register_kb

commands_router = Router(name = 'commands')

TEAM_IMG = 'AgACAgIAAxkBAAIM3mYHFgVpkFftYQ52MnbrRYN5nk0wAAKc2TEb9jw4SOpRXpF4ZPHEAQADAgADeQADNAQ'
DOCUMENT_SIT = 'BQACAgIAAxkBAAIGLGZE4utiOQABm6iBgEoa8p4DJa6sfwAC208AAg6PIUoy4kDgh_VYzjUE'


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command = 'start', description = "Запуск бота"),
        BotCommand(command = 'menu', description = "Меню бота"),
        BotCommand(command = 'company', description = "О проекте"),
        BotCommand(command = 'help', description = "Поддержка")
    ]

    await bot.set_my_commands(commands = commands)


@commands_router.message(Command('menu'))
async def show_menu(message: Message, state: FSMContext) -> None:
    state = await state.get_data()
    user_id = state.get('user_id')
    if not user_id:
        await message.answer(text = 'Для работы с ботом, нужно сначала пройти регистрацию',
                             reply_markup = register_kb)
    else:
        await message.answer(text = f'\n 🤝Взаимодейтсвие с компанией SITinvest\n'
                                    f'\n 💼 Ниже представлено меню бота',
                             reply_markup = invest_categories_kb)


@commands_router.message(Command('company'))
async def show_companies(message: Message, state: FSMContext):
    state = await state.get_data()
    user_id = state.get('user_id')
    if not user_id:
        await message.answer(text = 'Для работы с ботом, нужно сначала пройти регистрацию',
                             reply_markup = register_kb)
    else:
        await message.answer_document(document = DOCUMENT_SIT, caption = "Презентация нашего проекта",
                                      reply_markup = invest_categories_kb)


@commands_router.message(Command('help'))
async def show_menu(message: Message):
    await message.answer(text = '❓По всем вопросам, наша служба поддержки @SiT_investment, всегда на связи')
