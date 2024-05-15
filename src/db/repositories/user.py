"""User repository file."""
from datetime import datetime
from typing import Union

from aiogram.types import Message
from redis.client import Redis
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute, selectinload, sessionmaker

from .abstract import Repository
from ..models.users import Users

referral_links = {
    "insta": "https://t.me/SITinvest_bot?start=insta",
    "football": "https://t.me/SITinvest_bot?start=football",
    "distribution": "https://t.me/SITinvest_bot?start=distribution",
    "dance": "https://t.me/SITinvest_bot?start=1234567",
    "friends": "https://t.me/SITinvest_bot?start=friends",
    "promo": "https://t.me/SITinvest_bot?start=promo",
    "biglini": "https://t.me/SITinvest_bot?start=biglini"
}


class UserRepo(Repository[Users]):
    """User repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(type_model = Users, session = session)

        self.session = session

    async def new(
            self,
            user_id: int,
            tg_id: Union[int, str],
            username: str = None,
            full_name: str = None,
            phone_number: str = None,
            reg_date: datetime = None
    ) -> Users:
        """Insert a new user into the database
        :param user_id: Telegram user id
        :param tg_id: Telegram user id
        :param username: Telegram username
        :param full_name: Telegram profile first name
        :param phone_number: Telegram phone
        :param reg_date: Date register

        """
        new_user = await self.session.merge(
            Users(
                user_id = user_id,
                tg_id = tg_id,
                username = username,
                full_name = full_name,
                phone_number = phone_number,
                reg_date = reg_date
            )
        )
        return new_user


async def get_user(user_id: int, session_maker: sessionmaker) -> Users:
    """
    Получить пользователя по его id
    :param user_id:
    :param session_maker:
    :return:
    """
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(Users)
                .filter(User.user_id == user_id)  # type: ignore
            )
            return result.scalars().one()


async def create_user(user_id: int, username: str, tg_id: int, full_name: str, phone_number: str, reg_date: datetime,
                      session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            user = Users(
                user_id = user_id,
                tg_id = tg_id,
                username = username,
                full_name = full_name,
                phone_number = phone_number,
                reg_date = reg_date
            )
            try:
                session.add(user)
            except ProgrammingError as e:
                # TODO: add log
                pass


async def save_referral_data(self, user_id: int, username: str, referral_source: str) -> None:
    """Save referral data to the database."""
    user = await self.get_user_by_id(user_id)

    if user:
        user.referral_source = referral_source
        await self.session.commit()

async def is_user_exists(user_id: int, session_maker: sessionmaker, redis: Redis) -> bool:
    res = await redis.get(name = 'is_user_exists:' + str(user_id))
    if not res:
        async with session_maker() as session:
            async with session.begin():
                sql_res = await session.execute(select(Users).where(Users.user_id == user_id))
                await redis.set(name = 'is_user_exists:' + str(user_id), value = 1 if sql_res else 0)
                return bool(sql_res)
    else:
        return bool(res)
