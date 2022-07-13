from http import HTTPStatus
from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, current_user

from app.event.serializers import event_schema
from app.types import EndpointResponse

blueprint = Blueprint("event", __name__, url_prefix="/api/v1/events")


@blueprint.get("/")
@jwt_required()
@use_kwargs(event_schema)
@marshal_with(event_schema)
def get_event() -> EndpointResponse:
    user = current_user
    return {"userId": user.id}, HTTPStatus.CREATED  # TBD
