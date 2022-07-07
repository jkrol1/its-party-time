from app.extensions import ma
from app.token.models import Token


class TokenSchema(ma.SQLAlchemyAutoSchema):
    model = Token


class TokenResponseSchema(ma.Schema):
    access_token = ma.String(required=True)
    refresh_token = ma.String(required=True)


token_response_schema = TokenResponseSchema()
