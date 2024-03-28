"""Channel model file."""

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class MessageDB(Base):
    """Text model."""

    message_text: Mapped[str]
    message_id: Mapped[int]
    # message = relationship('User', userlist = True)

    def __repr__(self):
        return f"<MessageDB(message_id={self.message_id}, message_text={self.message_text})>"
