from http import HTTPStatus
from typing import Dict, Tuple

from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import create_access_token, create_refresh_token

from app.user.models import User
from app.user.serializers import user_login_schema
from app.exceptions import InvalidCredentialsError
from app.token.models import Token
from app.token.serializers import token_response_schema

blueprint = Blueprint("token", __name__, url_prefix="/api/v1/tokens")


@blueprint.post("/")
@use_kwargs(user_login_schema)
@marshal_with(token_response_schema)
def create_tokens(email: str, password: str) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(email=email).scalar()
    if user is not None and user.verify_password(password):
        access_token = create_access_token(user)
        refresh_token = create_refresh_token(user)
        Token.register_tokens_for_user([access_token, refresh_token], user)
        return dict(access_token=access_token, refresh_token=refresh_token), HTTPStatus.CREATED
    else:
        raise InvalidCredentialsError
