from http import HTTPStatus
from typing import Dict

from flask import url_for
from flask.testing import FlaskClient

from app.event.models import EventRole
from app.event.roles import Role

from tests.fake import FakeInputData


def test_create_event(test_client: FlaskClient,
                      access_token: str,
                      fake_input_data: FakeInputData,
                      event_roles: Dict[Role, EventRole]) -> None:
    response = test_client.post(url_for("event.create_event"),
                                headers={"Authorization": f"Bearer {access_token}"},
                                json=fake_input_data.event.to_dict())

    assert response.status_code == HTTPStatus.CREATED
