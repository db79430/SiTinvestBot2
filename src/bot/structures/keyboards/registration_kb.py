from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, KeyboardButtonRequestUser, \
    ReplyKeyboardMarkup
from src.bot.structures.text.text import register_btn_text

register_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = register_btn_text, callback_data = 'register'
            )
        ]
    ]
)

contacts_btn = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "📞 Поделиться контактом ", request_contact=True)],
        [KeyboardButton(text = "🔔 Поделиться именем тг")],
    ],
    resize_keyboard = True,

)

phone_numbers_btn = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "📞 Поделиться контактом ", request_contact=True)],
    ],
    resize_keyboard = True,
)

application = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Оставить заявку 📝")],
],
    resize_keyboard = True,
    resize_horizontal = True,
)
