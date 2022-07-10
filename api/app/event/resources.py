from http import HTTPStatus
from flask import Blueprint
from flask_jwt_extended import jwt_required, current_user

from app.exceptions import EndpointResponse

blueprint = Blueprint("event", __name__, url_prefix="/api/v1/events")


@blueprint.get("/")
@jwt_required()
def get_event() -> EndpointResponse:
    user = current_user
    return {"userId": user.id}, HTTPStatus.CREATED.value
