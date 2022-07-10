from __future__ import annotations

from datetime import timedelta
import os
from typing import Dict

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY: str = os.environ["SECRET_KEY"]
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES: timedelta = timedelta(days=30)
    SQLALCHEMY_DATABASE_URI: str = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    APISPEC_SPEC: APISpec = APISpec(
        title="It's party time API",
        version='v1',
        openapi_version="3.0.0",
        plugins=[MarshmallowPlugin()],
    )
    APISPEC_SWAGGER_URL: str = "/swagger/"


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass


class TestConfig(Config):
    TESTING: bool = True
    SQLALCHEMY_TEST_SCHEMA_NAME: str = "test"
    SQLALCHEMY_ENGINE_OPTIONS: Dict = {
        "execution_options": {"schema_translate_map": {None: SQLALCHEMY_TEST_SCHEMA_NAME}}}
