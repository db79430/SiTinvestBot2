from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from src.bot.structures.text.text import (
    invest_with_text_btn,
    invest_without_text_btn,
    partner_text_btn,
)


invest_categories_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Инвестирование (ипотечное кредитование) 💸')],
        [KeyboardButton(text='Инвестирование собственных средств 💵')],
        [KeyboardButton(text='Стать нашим партнером 💼')],
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)


# invest_categories_kb = ReplyKeyboardMarkup(
#     keyboard = [
#         [KeyboardButton(text='Инвестирование (ипотечное кредитование) 💸')],
#         [KeyboardButton(text='Инвестирование собственных средств 💵')],
#         [KeyboardButton(text='Стать нашим партнером 💼')],
#     ],
#     resize_keyboard = True,
#     resize_horizontal = True,
# )

