import re
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from src.bot.structures.fsm.state import RegisterGroup
from .successfully_register import send_reg_data_tg_user_chat, send_reg_data_user_chat
from ...structures.keyboards.buttons import contacts_btn, invest_categories_kb, phone_numbers_btn
from .router import register_router

CATEGORIES_IMG = 'AgACAgIAAxkBAAM4Zjin3tSMuxVhd95CZFPBWsiXp3QAAh3aMRvhFMlJ96rmTrVRZHEBAAMCAAN5AAM1BA'
CATEGORIES_IMG_2 = 'AgACAgIAAxkBAAM6ZjioAAEROR02l8hLXuUI5vGMZaagAAI-2jEb4RTJSdEqQxQcuO-BAQADAgADeQADNQQ'


@register_router.message(F.text == '👩‍💻 Регистрация')
async def register_confirmation(message: Message, state: FSMContext):
    await state.set_state(RegisterGroup.regFullName)
    await message.answer(' 📝Введи имя на русском языке:')


@register_router.message(RegisterGroup.regFullName)
async def register_full_name(message: Message, state: FSMContext):
    if re.findall('^[а-яА-Я ]+$', message.text):
        await message.reply(
            'Супер 🙂! Имя я записал\n'
            '📱Теперь нужно нажать на кнопку внизу, чтобы подделиться контактом или никнеймом tg\n',
            reply_markup = contacts_btn
        )
        await state.update_data(regFullName = message.text)
        await state.set_state(RegisterGroup.regPhone)
    else:
        await message.reply('Неккоректное имя')
        return await message.answer(' 📝Введите имя на русском языке:')


@register_router.message(F.text == "🔔 Поделиться именем tg")
async def register_tg_name(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    await state.set_state(RegisterGroup.regTgName)
    reg_tg_name = reg_data.get('regTgName')
    msg = (
        f'\n✅ Твой никнейм: @{message.from_user.username}\n'
        f'\n✅ Твое имя: {reg_name}\n'
        f'\n🤗 Регистрация прошла успешно!\n'
        f'\n👇🏻 Ниже представлены категории инвестирования.\n'
    )
    if reg_tg_name is None:
        await message.answer(text = f"🥺 Упппс твой tg никнейм скрыт.\n "
                                    f"\n Нажми кнопку, пожалуйста, 📞 Поделиться контактом\n"
                                    f"\n Чтобы продолжить взаимодействие с ботом",
                             reply_markup = phone_numbers_btn)
    else:
        await message.answer(text = msg, reply_markup = ReplyKeyboardRemove())
        await send_reg_data_tg_user_chat(message, state)
        await send_sit_photo(message, state)


@register_router.message(F.contact)
async def register_phone(message: Message, state: FSMContext):
    await state.set_state(RegisterGroup.regPhone)
    reg_data = await state.get_data()
    reg_name = reg_data.get('regFullName')
    phone_number = str(message.contact.phone_number)
    start_param = reg_data.get('start_param')
    await state.update_data(start_param = start_param)
    await state.update_data(regTgName = message.from_user.username)
    msg = (
        f'\n✅ Твой телефон: {phone_number}\n'
        f'\n✅ Твое имя: {reg_name}\n'
        f'\n🤗 Регистрация прошла успешно!\n'
        f'\n👇🏻Ниже представлены категории инвестирования.\n'
    )
    await send_sit_photo(message, state)
    await send_reg_data_user_chat(message, state)
    await message.answer(text = msg, reply_markup = ReplyKeyboardRemove())


async def send_sit_photo(message: Message, state: FSMContext):
    await message.answer_photo(photo = CATEGORIES_IMG)
    await message.answer_photo(photo = CATEGORIES_IMG_2, reply_markup = invest_categories_kb)
