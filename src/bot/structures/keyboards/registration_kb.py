from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from src.bot.structures.text.text import register_btn_text

register_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=register_btn_text, callback_data='register'
            )
        ]
    ]
)

contacts_btn = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Поделиться контактом ", callback_data = 'phone', request_contact = True)],
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)


application = ReplyKeyboardMarkup(keyboard = [
        [KeyboardButton(text = "Оставить заявку для сотрудничества 📝")],
    ],
    resize_keyboard = True,
    resize_horizontal = True,)
