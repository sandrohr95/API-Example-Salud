from typing import Optional

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError

from API.config import settings
from API.logger import logger

_connection: Optional[Database] = None


def get_connection() -> Database:
    """
        Returns -or creates- global database connection.
    """
    global _connection

    if not _connection:
        logger.debug("Connectiong to database for the first time")
        client = MongoClient(settings.MONGO_DNS)
        try:
            client.server_info()
        except ServerSelectionTimeoutError:
            raise ConnectionError(f"Could not connect to database with connection string {settings.MONGO_DNS}")
        _connection = client.API
    return _connection
