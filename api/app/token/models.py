from __future__ import annotations
from datetime import datetime
from typing import List

from flask_jwt_extended import decode_token

from app.extensions import db
from app.user.models import User


class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True)
    token_id = db.Column(db.String(64), nullable=False, index=True)
    token_expiration = db.Column(db.DateTime, nullable=False)
    token_type = db.Column(db.String(10), nullable=False, index=True)
    is_revoked = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)

    user = db.relationship("User", back_populates="tokens")

    @classmethod
    def register_tokens_for_user(cls, tokens: List[str], user: User) -> None:
        for token in tokens:
            decoded_token = decode_token(token)
            db.session.add(cls(
                token_id=decoded_token["jti"],
                token_expiration=datetime.fromtimestamp(decoded_token["exp"]),
                token_type=decoded_token["type"],
                is_revoked=False,
                user_id=user.id
            ))
        db.session.commit()
