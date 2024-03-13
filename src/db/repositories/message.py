"""Message repository file."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .abstract import Repository
from ..models.chat import Chat
from ..models.message import Message



class MessageRepo(Repository[Message]):
    """Message repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(type_model=Message, session=session)

    async def new(self, message_text: str, message_id: int) -> Message:
        """Insert a new user into the database.
        :param message_id: Telegram message id
        :param message_text: message text.
        """
        new_message = await self.session.merge(
            Message(message_text=message_text, message_id=message_id)
        )
        return new_message


