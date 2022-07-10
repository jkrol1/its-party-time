from http import HTTPStatus
from typing import Optional

from flask import Blueprint, abort
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import create_access_token, create_refresh_token

from app.user.models import User
from app.user.serializers import user_login_schema
from app.token.models import Token
from app.token.serializers import token_response_schema
from app.types import EndpointResponse

blueprint = Blueprint("token", __name__, url_prefix="/api/v1/tokens")


@blueprint.post("/")
@use_kwargs(user_login_schema)
@marshal_with(token_response_schema)
def create_tokens(email: str, password: str) -> Optional[EndpointResponse]:
    user = User.query.filter_by(email=email).scalar()
    if user is not None and user.verify_password(password):
        access_token = create_access_token(user)
        refresh_token = create_refresh_token(user)
        Token.register_tokens_for_user([access_token, refresh_token], user)
        return {"access_token": access_token, "refresh_token": refresh_token}, HTTPStatus.CREATED
    else:
        abort(HTTPStatus.UNAUTHORIZED.value, description="Email and/or password are incorrect")
