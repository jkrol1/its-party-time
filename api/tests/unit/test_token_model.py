from flask_jwt_extended import create_access_token, create_refresh_token

from app.user.models import User
from app.token.models import Token


def test_register_tokens_for_user(user: User) -> None:
    tokens = [create_access_token(user), create_refresh_token(user)]
    Token.register_tokens_for_user(tokens, user)

    for token_type in ["refresh", "access"]:
        assert Token.query.filter_by(user_id=user.id, token_type=token_type).with_entities(
            Token.token_type).scalar() is not None
