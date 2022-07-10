from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from tests.fake import FakeInputData


def test_register_user(test_client: FlaskClient, fake_input_data: FakeInputData) -> None:
    response = test_client.post(url_for("user.register_user"), json=fake_input_data.user.to_dict())

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["email"] == fake_input_data.user.email
    assert response.json["username"] == fake_input_data.user.username


def test_register_user_with_invalid_input(test_client: FlaskClient) -> None:
    response = test_client.post(url_for("user.register_user"), json={"email": ""})
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_user_already_signed_up(test_client: FlaskClient, fake_input_data) -> None:
    test_client.post(url_for("user.register_user"), json=fake_input_data.user.to_dict())
    response = test_client.post(url_for("user.register_user"), json=fake_input_data.user.to_dict())
    assert response.status_code == HTTPStatus.BAD_REQUEST
