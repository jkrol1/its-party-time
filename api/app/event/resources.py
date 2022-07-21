from http import HTTPStatus

from flask import Blueprint
from flask.typing import ResponseReturnValue
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, current_user

from app.extensions import db
from app.event.models import Event
from app.event.serializers import event_schema

blueprint = Blueprint("event", __name__, url_prefix="/api/v1/events")


@blueprint.post("/")
@jwt_required()
@use_kwargs(event_schema)
@marshal_with(event_schema)
def create_event(**kwargs) -> ResponseReturnValue:
    event = Event(**kwargs, organizer_id=current_user.id)
    db.session.add(event)
    db.session.commit()

    return event, HTTPStatus.CREATED
