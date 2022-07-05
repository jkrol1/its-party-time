from http import HTTPStatus

from flask import url_for

from tests.fake import get_fake_user_post_request_body


def test_create_user(test_client):
    post_request_body = get_fake_user_post_request_body()
    response = test_client.post(url_for("user.create_user"), json=post_request_body)

    assert response.status_code == HTTPStatus.CREATED.value
