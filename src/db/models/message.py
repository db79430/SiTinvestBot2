"""Channel model file."""

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .chat import Chat
from .base import Base


class Message(Base):
    """Text model."""

    message_text: Mapped[str]
    message_id: Mapped[int]
    chat = relationship(
        Chat,
        uselist = False,
        back_populates = 'chat_messages',
        cascade = 'save-update,delete',
        lazy = 'joined',
    )
    message = relationship('Users', uselist = True)

    def __repr__(self):
        return f"<Message(message_id={self.message_id}, message_text={self.message_text})>"
