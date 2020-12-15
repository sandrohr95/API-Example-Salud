from pathlib import Path

from pydantic import BaseSettings, AnyUrl

from API.logger import logger

class MongoDns(AnyUrl):
    allowed_schemes = {"mongodb"}
    user_required = True


class _Settings(BaseSettings):
    # api settings
    API_HOST: str = "localhost"
    API_PORT: str = 8080
    # for applications sub-mounted below a given path
    ROOT_PATH: str = ""
    # database connection
    MONGO_DNS: MongoDns = "mongodb://root:root@localhost:27017"

    class Config:
        if not Path(".env").is_file():
            logger.warning("⚠️ `.env` not found in current directory")
            logger.info("⚙️ Loading settings from environment")
        else:
            logger.info("⚙️ Loading settings from dotenv file")
        env_file = ".env"


settings = _Settings()
