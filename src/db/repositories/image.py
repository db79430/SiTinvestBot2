import asyncio
import os

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.testing.plugin.plugin_base import logging

from src.configuration import conf
from src.db.models.image import Image
from src.db.repositories import Repository


class ImageRepo(Repository[Image]):
    """Chat repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize chat repository as for all chats or only for one chat."""
        super().__init__(type_model = Image, session = session)

    async def new(
            self,
            file_id: int,
            file_name: str,
    ) -> Image:
        """Insert a new user into the database."""
        new_chat = await self.session.merge(
            Image(
                file_id = file_id,
                file_name = file_name
            )
        )
        return new_chat

