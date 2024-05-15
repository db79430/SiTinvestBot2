"""Message repository file."""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, selectinload

from src.bot.structures.category_invest import CLASS_INVEST
from src.db.models.message import Message
from src.db.models.users import Users
from src.db.repositories.abstract import Repository


class MessageRepo(Repository[Message]):
    """Message repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(type_model = Message, session = session)

    async def new(
            self,
            message_id: Mapped[int],
            message_text: int,
            role: Optional[CLASS_INVEST] = CLASS_INVEST,
            tg_user: Optional[Users] = None
    ) -> Message:
        """Insert a new user into the database
               :param message_id: Telegram message id,
               :param message_text: text of the message,
               :param role: category or invest,
               :param tg_user: telegram user

        """

        new_message = await self.session.merge(
            Message(
                message_id=message_id,
                message_text=message_text,
                role=role,
                tg_user=tg_user
            )
        )
        return new_message
