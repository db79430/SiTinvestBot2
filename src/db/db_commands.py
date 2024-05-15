from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, async_session
from sqlalchemy.orm import session

from src.db.models.message import Message
from src.db.models.users import Users


async def db_add_to_db(item, message: Message, session: AsyncSession):
    """Добавление сущности в бд"""

    session.add(item)
    try:

        await session.commit()
        await session.refresh(item)
        return item
    except IntegrityError as ex:
        await session.rollback()
        await message.answer('Произошла ошибка.')
        await message.answer(ex)


def check_user_exists(user_id):
    user = session.query(Users).filter_by(id = user_id).first()
    return user is not None


# регистрация юзера
async def db_register_user(message: Message, session: AsyncSession, username):
    tg_name = message.from_user.username if message.from_user.username else 'нет никнейма'
    full_name = message.from_user.full_name if message.from_user.full_name else ''
    phone = message.from_user.phone_number if message.from_user.phone else ''
    reg_date = message.from_user.reg_data if message.from_user.reg_data else ''

    user = Users(tg_id = int(message.from_user.id),
                 tg_name = tg_name,
                 full_name = full_name,
                 phone_number = phone,
                 reg_date = reg_date
                 )

    session.add(user)

    try:
        await session.commit()
        await session.refresh(user)
        return True
    except IntegrityError:
        await session.rollback()
        return False


async def is_registered_user(message: Message) -> bool:
    async with async_session() as session:
        result = await session.execute(
            select(Users).filter(Users.tg_id == message.from_user.id)
        )
        user = result.scalar_one_or_none()
        return user is not None


async def get_user_by_id(user_id: int, message: Message) -> Users:
    async with async_session() as session:
        result = await session.execute(
            select(Users).filter(Users.tg_id == user_id)
        )
        return result.scalar_one_or_none()


async def db_get_all_users(message: Message, session: AsyncSession):
    """ получение всех юзеров """

    sql = select(Users)
    users_sql = await session.execute(sql)
    users = users_sql.scalars()

    users_list = '\n'.join([f'{index + 1}. {item.tg_id}' for index, item in enumerate(users)])

    return users_list


# async def db_register_test(message: Message, session: AsyncSession, user_id: int):
#
#     message_title = message.text
#     message_text = MessageDB(message_title = message_title)
#
#     text = await db_add_to_db(message, message_text, session)
#     return text

# async def db_register_question(message: Message, session: AsyncSession, test: Test):
#     """Регистрация вопроса в базу данных"""
#
#     title = message.text
#     question = MessageDB()
#
#     question = await db_add_to_db(question, message, session)
#     return question
#
#
# """ удаление сущности из бд"""


async def db_delete_item(item, session: AsyncSession):
    try:
        await session.delete(item)
        await session.commit()
        # await session.refresh(item)
    except IntegrityError:
        await session.rollback()
