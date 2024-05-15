"""Channel model file."""
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .users import Users
from ...bot.structures.category_invest import CLASS_INVEST


class Message(Base):
    """Text model."""

    message_text: Mapped[str]
    message_id: Mapped[int]
    role: Mapped[CLASS_INVEST] = mapped_column(sa.Enum(CLASS_INVEST), default=CLASS_INVEST)
    tg_user: Mapped[Users] = relationship(uselist=False, lazy='joined', cascade='save-update')

    def __repr__(self):
        return f"<MessageDB(message_id={self.message_id}, message_text={self.message_text})>"
