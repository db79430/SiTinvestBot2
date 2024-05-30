from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

invest_categories_kb = ReplyKeyboardMarkup(
    keyboard = [
            [KeyboardButton(text='💸 Забрать 250 000 рублей')],
            [KeyboardButton(text='💵 Инвестирование собственных средств')],
            [KeyboardButton(text='🏡 Покупка дома для жилья')],
            [KeyboardButton(text='🏘 Покупка дома для дальнейшей перепродажи')],
            [KeyboardButton(text='👨🏻‍💻 Работать с нами')],
            [KeyboardButton(text='💬 Задать вопрос')]
    ],
    resize_keyboard=True
)

menu_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '💼 Меню')]
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)

contact_us = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '💬 Связаться со мной')],
        [KeyboardButton(text = '💼 Меню')]
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)

contact_us_wo_money = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '💬Заявка: Забрать 250 000 рублей')],
        [KeyboardButton(text = '💼 Меню')]
    ],
    resize_keyboard = True,
)

contact_us_w_money = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '💬Заявка: инвестирование средств')],
        [KeyboardButton(text = '💼 Меню')]
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)

contact_us_buy_home = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '💬Заявка: покупка дома для жилья')],
        [KeyboardButton(text = '💼 Меню')]
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)

contact_us_sale_home = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '💬Заявка: покупка дома для перепродажи')],
        [KeyboardButton(text = '💼 Меню')]
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)

contact_us_work = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '💬Заявка: работать с нами')],
        [KeyboardButton(text = '💼 Меню')]
    ],
    resize_keyboard = True,
    resize_horizontal = True,
)


register_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '👩‍💻 Регистрация')],
    ],
    resize_keyboard = True,

)

contacts_btn = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "📞 Поделиться контактом ", request_contact=True)],
        [KeyboardButton(text = "🔔 Поделиться именем tg")],
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