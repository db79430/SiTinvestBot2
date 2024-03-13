import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class Image(Base):
    __tablename__ = 'images'

    id = sa.Column(sa.Integer, primary_key = True)
    file_id = sa.Column(sa.BigInteger, unique = True, nullable = False)
    filename = sa.Column(sa.Text, nullable = True)

    def __repr__(self):
        return f"<Image(id={self.id}, file_id={self.file_id}, file_id={self.filename})>"
