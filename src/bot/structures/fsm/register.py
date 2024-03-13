from aiogram.fsm.state import StatesGroup, State


class RegisterGroup(StatesGroup):
    confirmation = State()
    regFullName = State()
    regContacts = State()
    regInfo = State()
    select = State()


class RegisterMessage(StatesGroup):
    message_id = State()
    text_message = State()


class RegisterImage(StatesGroup):
    img_path = State()


class RegisterChat(StatesGroup):
    chat_id = State()
    chat_name = State()


class RegisterButtonSelect(StatesGroup):
    button = State()
    button_id = State()
