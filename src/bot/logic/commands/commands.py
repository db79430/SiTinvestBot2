from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, Message

from src.bot.logic.commands.start import start_wo_register
from src.bot.structures.fsm.state import UserClickButton
from src.bot.structures.keyboards.invest_kb import invest_categories_kb

commands_router = Router(name = 'commands')

TEAM_IMG = 'AgACAgIAAxkBAAIM3mYHFgVpkFftYQ52MnbrRYN5nk0wAAKc2TEb9jw4SOpRXpF4ZPHEAQADAgADeQADNAQ'


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command = 'start', description = "Запуск бота"),
        BotCommand(command = 'menu', description = "Меню бота"),
        BotCommand(command = 'company', description = "О компании"),
        BotCommand(command = 'help', description = "Поддержка")
    ]

    await bot.set_my_commands(commands = commands, scope = BotCommandScopeAllPrivateChats())


@commands_router.message(Command('menu'))
async def show_menu(message: Message, state: FSMContext):
    state = await state.get_data()
    user_id = state.get('user_id')
    if not user_id:
        await start_wo_register(message)
    else:
        await message.answer(text = f'\n 🤝Взаимодейтсвие с компанией SiTInvest\n'
                                    f'\n 💼 Ниже представлено меню бота',
                             reply_markup = invest_categories_kb)


@commands_router.message(Command('company'))
async def show_companies(message: Message, state: FSMContext):
    state = await state.get_data()
    user_id = state.get('user_id')
    if not user_id:
        await start_wo_register(message)
    else:
        await message.answer_photo(photo = TEAM_IMG)
        await message.answer(text = f'\n 🤝Взаимодейтсвие с компанией SiTInvest\n'
                                    f'\n 💼 Ниже представлено меню бота',
                             reply_markup = invest_categories_kb)


@commands_router.message(Command('help'))
async def show_menu(message: Message):
    await message.answer(text = '❓По всем вопросам, наша служба поддержки @SiT_investment, всегда на связи')
