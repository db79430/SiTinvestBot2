from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, Message
from src.bot.structures.fsm.state import UserClickButton
from src.bot.structures.keyboards.invest_kb import invest_categories_kb

commands_router = Router(name = 'commands')


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command = 'start', description = "Запуск бота"),
        BotCommand(command = 'menu', description = "Меню бота"),
        BotCommand(command = 'help', description = "Поддержка")
    ]

    await bot.set_my_commands(commands = commands, scope = BotCommandScopeAllPrivateChats())


@commands_router.message(Command('menu'))
async def show_menu(message: Message, state: FSMContext):
    await message.answer(text = f'\n 🤝Взаимодейтсвие с компанией SiTInvest\n'
                                f'\n 💼 Ниже представлено меню бота',
                         reply_markup = invest_categories_kb)
    await state.set_state(UserClickButton.choice)


@commands_router.message(Command('help'))
async def show_menu(message: Message):
    await message.answer(text = '❓По всем вопросам, наша служба поддержки @SiT_investment, всегда на связи')
