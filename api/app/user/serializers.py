from app.extensions import ma
from app.user.models import User
from app.token.serializers import TokenSchema


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field()
    password = ma.String(required=True, load_only=True)
    email = ma.Email(required=True)
    last_seen = ma.auto_field(dump_only=True)
    tokens = ma.Nested(TokenSchema, many=True)


class UserLoginSchema(UserSchema):
    class Meta:
        fields = ("email", "password")


user_schema = UserSchema()
user_login_schema = UserLoginSchema()
user_schemas = UserSchema(many=True)
