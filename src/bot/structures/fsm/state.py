from aiogram.fsm.state import StatesGroup, State


class RegisterGroup(StatesGroup):
    confirmation = State()
    regFullName = State()
    regPhone = State()
    regTgName = State()
    regInfo = State()
    reg_source_key = State()
    question = State()


class UserSelect(StatesGroup):
    work = State()
    wo_money = State()
    w_money = State()
    buy_house = State()
    sale_house = State(),


class RegisterMessage(StatesGroup):
    message_id = State()
    text_message = State()


class RegisterChat(StatesGroup):
    chat_id = State()
    chat_name = State()


class UserClickButton(StatesGroup):
    choice = State()


class UserLink(StatesGroup):
    insta = State("https://t.me/SITinvest_bot?start=insta")
    promo = State("https://t.me/SITinvest_bot?start=promo")
    football = State("https://t.me/SITinvest_bot?start=football")
    dance = State("https://t.me/SITinvest_bot?start=1234567")
    friends = State("https://t.me/SITinvest_bot?start=friends")
    biglini = State("https://t.me/SITinvest_bot?start=biglini")
    distribution = State("https://t.me/SITinvest_bot?start=distribution")
