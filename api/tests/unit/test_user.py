from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from tests.fake import FakeInputData


def test_create_user(test_client: FlaskClient, fake_input_data: FakeInputData) -> None:
    response = test_client.post(url_for("user.create_user"), json=fake_input_data.user.to_dict())

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["email"] == fake_input_data.user.email
    assert response.json["username"] == fake_input_data.user.username
