from typing import Dict, Union, Optional

from app.user.models import User
from app.token.models import Token


def user_identity_loader_callback(user: User) -> int:
    return user.id


def user_lookup_callback(_jwt_header: Dict[str, str], jwt_data: Dict[str, Union[str, int]]) -> Optional[User]:
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


def check_if_token_revoked_callback(jwt_header: Dict[str, str], jwt_payload: Dict[str, Union[str, int]]) -> bool:
    token_id = jwt_payload["jti"]
    token = Token.query.filter_by(token_id=token_id, is_revoked=True).scalar()
    return token is not None
