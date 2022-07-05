from typing import Generator

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient
import pytest

from app import create_app
from app.extensions import db as db_fsa
from app.user import User
from config import TestConfig

from tests.fake import get_fake_user_post_request_body


@pytest.fixture()
def app() -> Flask:
    app = create_app(TestConfig)
    return app


@pytest.fixture()
def test_client(app) -> Generator[FlaskClient, None, None]:
    with app.test_client() as testing_client:
        with app.app_context():
            with app.test_request_context():
                _setup_db()
                yield testing_client
                _teardown_db()


@pytest.fixture()
def db(test_client) -> Generator[SQLAlchemy, None, None]:
    return db_fsa


@pytest.fixture()
def user(db) -> User:
    user = User(**get_fake_user_post_request_body())
    db.session.add(user)
    db.session.commit()
    return user


def _setup_db():
    db_fsa.engine.execute(db_fsa.text(f"CREATE SCHEMA IF NOT EXISTS {TestConfig.SQLALCHEMY_TEST_SCHEMA_NAME}"))
    db_fsa.create_all()


def _teardown_db():
    db_fsa.session.close()
    db_fsa.drop_all()
