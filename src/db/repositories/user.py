"""User repository file."""
from aiogram.types import Message
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute

from ..models.users import Users
from .abstract import Repository

#
# class UserRepo(Repository[User]):
#     """User repository for CRUD and other SQL queries."""
#     def __init__(self, session: AsyncSession):
#         """Initialize user repository as for all users or only for one user."""
#         super().__init__(type_model = User, session = session)
#
#         self.session = session
#
#     async def new(
#             self,
#             user_id: int,
#             username: str = None,
#             full_name: str = None,
#             contact: str = None,
#             phone_number: str = None,
#     ) -> User:
#         """Insert a new user into the database
#         :param user_id: Telegram user id
#         :param username: Telegram username
#         :param full_name: Telegram profile first name
#         :param contact: Telegram phone user.
#         :param phone_number: Telegram phone
#
#         """
#         new_user = await self.session.merge(
#             User(
#                 user_id = user_id,
#                 username = username,
#                 full_name = full_name,
#                 contact = contact,
#                 phone_number = phone_number
#             )
#         )
#         return new_user
#
