"""Chat model file."""
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Chat(Base):
    """Chat model."""

    chat_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, nullable=False
    )
    """ Chat telegram id """
    chat_type: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=False
    )
    message = relationship('Massage', uselist=False)
    """ Foreign key to user (it can has effect only in private chats) """
