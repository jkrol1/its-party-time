from typing import Tuple

from flask import Blueprint
from flask_apispec import marshal_with, use_kwargs

from app.extensions import db
from app.user.serializers import user_schema
from app.user import User

blueprint = Blueprint("user", __name__, url_prefix="/api/v1/users")


@blueprint.post("/")
@use_kwargs(user_schema)
@marshal_with(user_schema)
def create_user(user) -> Tuple[User, int]:
    db.session.add(user)
    db.session.commit()
    return user, 201
