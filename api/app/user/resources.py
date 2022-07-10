from http import HTTPStatus

from flask import Blueprint
from flask_apispec import marshal_with, use_kwargs

from app.extensions import db
from app.user.serializers import user_schema
from app.user.models import User
from app.types import EndpointResponse

blueprint = Blueprint("user", __name__, url_prefix="/api/v1/users")


@blueprint.post("/")
@use_kwargs(user_schema)
@marshal_with(user_schema)
def register_user(**kwargs) -> EndpointResponse:
    new_user = User(**kwargs)
    db.session.add(new_user)
    db.session.commit()
    return new_user, HTTPStatus.CREATED
