from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from tests.fake import FakeInputData


def test_create_token(test_client: FlaskClient, fake_input_data: FakeInputData) -> None:
    fake_user_dict = fake_input_data.user.to_dict()
    test_client.post(url_for("user.register_user"), json=fake_user_dict)
    response = test_client.post(url_for("token.create_tokens"),
                                json={key: value for key, value in fake_user_dict.items() if
                                      key in ["email", "password"]})

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["access_token"] is not None
    assert response.json["refresh_token"] is not None
