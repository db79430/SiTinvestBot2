"""User model file."""
from datetime import date

import sqlalchemy as sa
from sqlalchemy import BigInteger, Column, DATE, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


# class User(Base):
#     """User model."""
#
#     user_id: Mapped[int] = mapped_column(
#         sa.BigInteger, unique = True, nullable = False, primary_key = True
#     )
#     """ Telegram user id """
#     username: Mapped[str] = mapped_column(
#         sa.Text, unique = False, nullable = True
#     )
#     """ Telegram user name """
#     full_name: Mapped[str] = mapped_column(
#         sa.Text, unique = False, nullable = True
#     )
#     """ Telegram full name """
#     contact: Mapped[str] = mapped_column(
#         sa.Text, unique = False, nullable = True
#     )
#
#     phone_number: Mapped[str] = mapped_column(
#         sa.Text, unique = False, nullable = True
#     )
#
#     reg_date: Mapped[int] = mapped_column(DATE, default = date.today)
#
#     def __repr__(self) -> str:
#         return (f"<User {self.user_id}, {self.full_name}, {self.username}, {self.contact}, {self.phone_number}, "
#                 f"{self.reg_date}>")


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    tg_id = Column(BigInteger, unique = True)
    tg_name = Column(String, nullable = False)
    username = Column(String, nullable = False)
    full_name = Column(String, nullable = False)
    phone_number = Column(String, nullable = False)
    reg_date: Mapped[int] = mapped_column(DATE, default = date.today)


def __repr__(self) -> str:
    return (f"<Users{self.user_id}, {self.full_name}, {self.username}, {self.contact}, {self.phone_number}, "
            f"{self.reg_date}>")

