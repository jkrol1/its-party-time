import os
from typing import Dict

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY: str = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI: str = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass


class TestConfig(Config):
    DEBUG: bool = False
    TESTING: bool = True
    SQLALCHEMY_TEST_SCHEMA_NAME: str = "test"
    SQLALCHEMY_ENGINE_OPTIONS: Dict = {
        "execution_options": {"schema_translate_map": {None: SQLALCHEMY_TEST_SCHEMA_NAME}}}
    PRESERVE_CONTEXT_ON_EXCEPTION = False
