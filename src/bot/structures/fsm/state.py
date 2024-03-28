from aiogram.fsm.state import StatesGroup, State


class RegisterGroup(StatesGroup):
    confirmation = State()
    regFullName = State()
    regPhone = State()
    regTgName = State()
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


class UserClickButton(StatesGroup):
    choice = State()
