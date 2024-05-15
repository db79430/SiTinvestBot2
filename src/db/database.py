""" Database class with all-in-one features """
from typing import Union

from aiogram import Dispatcher
from sqlalchemy import exc
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker

from src.configuration import conf
from src.db.repositories.message import MessageRepo
from src.db.repositories.user import UserRepo


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    """
    :param url:
    :return:
    """
    return _create_async_engine(
        url = url, echo = conf.debug, pool_pre_ping = True
    )


def proceed_schemas(session: AsyncSession, metadata) -> None:
    with session.begin():
        session.run_sync(metadata.create_all)


def create_session_maker(engine: AsyncEngine = None) -> sessionmaker:
    """
    :param engine:
    :return:
    """
    return sessionmaker(
        engine or create_async_engine(conf.db.build_connection_str()),
        class_ = AsyncSession,
        expire_on_commit = False,
    )


async def on_startup(dispatcher: Dispatcher):
    print('Подключение к базе данных')
    try:
        engine = create_async_engine(conf.db.build_connection_str())
        async_session = sessionmaker(
            engine,
            class_ = AsyncSession,
            expire_on_commit = False,
        )
        async with async_session() as session:
            async with session.begin():
                await session.connection()
    except exc.SQLAlchemyError as e:
        print(f"Ошибка при подключении к базе данных: {e}")


class Database:
    """
    Database class is the highest abstraction level of database and
    can be used in the handlers or any others bot-side functions
    """

    user: UserRepo
    """ User repository """
    message: MessageRepo
    """ Chat repository """

    session: AsyncSession

    def __init__(
            self, session: AsyncSession, user: UserRepo = None, chat: MessageRepo = None
    ):
        self.session = session
        self.user = user or UserRepo(session = session)
        self.chat = chat or MessageRepo(session = session)
