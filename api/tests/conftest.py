from typing import Generator

from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient
import pytest

from app import create_app
from app.extensions import db as db_fsa
from app.user import User
from config import TestConfig

from tests.fake import FakeInputData


@pytest.fixture()
def test_client() -> Generator[FlaskClient, None, None]:
    app = create_app(TestConfig)

    with app.app_context():
        with app.test_request_context():
            with app.test_client() as testing_client:
                _setup_db()
                yield testing_client
                _teardown_db()


@pytest.fixture()
def db(test_client) -> SQLAlchemy:
    return db_fsa


@pytest.fixture()
def fake_input_data() -> FakeInputData:
    return FakeInputData()


@pytest.fixture()
def user(db, fake_input_data) -> User:
    user = User(**fake_input_data.user.to_dict())
    db.session.add(user)
    db.session.commit()
    return user


def _setup_db() -> None:
    db_fsa.engine.execute(db_fsa.text(f"CREATE SCHEMA IF NOT EXISTS {TestConfig.SQLALCHEMY_TEST_SCHEMA_NAME}"))
    db_fsa.create_all()


def _teardown_db() -> None:
    db_fsa.session.close()
    db_fsa.drop_all()
