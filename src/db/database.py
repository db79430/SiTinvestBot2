"""Database class with all-in-one features."""

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, engine
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker

from src.configuration import conf
from src.db.models.base import Base

from .models.users import Users
from .models.messagedb import MessageDB


def create_async_engine(url: URL | str) -> AsyncEngine:
    """Create async engine with given URL.

    :param url: URL to connect
    :return: AsyncEngine
    """
    return _create_async_engine(url = url, echo = conf.debug, pool_pre_ping = True)


def proceed_schemas(engine:AsyncEngine, metadata) -> None:
    with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all())

def get_session_maker(engine: AsyncSession) -> sessionmaker:
    return sessionmaker(engine = engine, class_ = AsyncSession)


class Database:
    """Database class.

    is the highest abstraction level of database and
    can be used in the handlers or any others bot-side functions.
    """

    user: Users
    message: MessageDB

    session: AsyncSession

    def __init__(
            self,
            session: AsyncSession,
            user: Users = None,
            message: MessageDB = None,
    ):
        """Initialize Database class.

        :param session: AsyncSession to use
        :param user: (Optional) User repository
        """
        self.session = session
        self.user = user or Users(session = session)
        self.message = message or MessageDB(session = session)
