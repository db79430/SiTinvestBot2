"""This file represents configurations from files and environment."""
import logging
from os import getenv
from dataclasses import dataclass
from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    """Database connection variables."""

    name: str | None = getenv('POSTGRES_DATABASE', 0)
    user: str | None = getenv('POSTGRES_USER')
    passwd: str | None = getenv('POSTGRES_PASSWORD', None)
    port: int = int(getenv('POSTGRES_PORT', 5432))
    host: str = getenv('POSTGRES_HOST')

    driver: str = 'asyncpg'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        """This function build a connection string."""
        return URL.create(
            drivername = f'{self.database_system}+{self.driver}',
            username = self.user,
            database = self.name,
            password = self.passwd,
            port = self.port,
            host = self.host,
        ).render_as_string(hide_password = True)


@dataclass
class RedisConfig:
    """Redis connection variables."""

    db: int = int(getenv('REDIS_DATABASE', 1))
    """ Redis Database ID """
    host: str = getenv('REDIS_HOST')
    port: int = int(getenv('REDIS_PORT', 6379))
    passwd: str | None = getenv('REDIS_PASSWORD', None)
    username: str | None = getenv('REDIS_USERNAME')
    state_ttl: int | None = getenv('REDIS_TTL_STATE', None)
    data_ttl: int | None = getenv('REDIS_TTL_DATA', None)


@dataclass
class BotConfig:
    """Bot configuration."""

    token: str | None = getenv('BOT_TOKEN')
    chat: str | None = getenv('CHAT_ID')
    print("Value of BOT_TOKEN:", token)
    print("Value of CHAT_ID:", chat)


@dataclass
class Configuration:
    """All in one configuration's class."""

    debug = bool(getenv('DEBUG'))
    logging_level = int(getenv('LOGGING_LEVEL', logging.INFO))

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()
    print(redis)


conf = Configuration()
