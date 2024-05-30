"""This file represent startup bot logic."""
import asyncio
import logging

from aiogram import Bot
from aiogram.filters import Command, CommandStart
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import engine

from src.bot.dispatcher import get_dispatcher, get_redis_storage
from src.bot.logic.commands import start
from src.bot.logic.commands.commands import set_commands, show_companies, show_help, show_menu
from src.bot.structures.data_structure import TransferData
from src.configuration import conf
from src.db.database import create_async_engine


async def start_bot():
    bot: Bot = Bot(token = conf.bot.token)
    await set_commands(bot)
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
