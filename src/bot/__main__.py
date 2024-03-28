"""This file represent startup bot logic."""
import asyncio
import logging

from aiogram import Bot
from redis.asyncio.client import Redis
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_session, async_sessionmaker, engine
from sqlalchemy.orm import Session

from src.bot.dispatcher import get_dispatcher, get_redis_storage
from src.bot.logic.commands.commands import set_commands
from src.bot.structures.data_structure import TransferData
from src.configuration import conf
from src.db.database import create_async_engine, get_session_maker, proceed_schemas
from src.db.models.users import Users


async def start_bot():
    """This function will start bot with polling mode."""
    async_engine = create_async_engine(url = conf.db.build_connection_str())
    session_maker = async_sessionmaker(async_engine, expire_on_commit = False)
    bot: Bot = Bot(token = conf.bot.token)
    chat: int = conf.chat.chat_id
    storage = get_redis_storage(
        redis = Redis(
            db = conf.redis.db,
            host = conf.redis.host,
            password = conf.redis.passwd,
            username = conf.redis.username,
            port = conf.redis.port,
        )
    )
    dp = get_dispatcher(storage = storage)
    await set_commands(bot)
    await dp.start_polling(
        bot,
        skip_updates = True,
        allowed_updates = dp.resolve_used_update_types(),
        **TransferData(
            engine = create_async_engine(url = conf.db.build_connection_str())
        )
    )

if __name__ == '__main__':
    logging.basicConfig(level = conf.logging_level)
    asyncio.run(start_bot())
