from app.extensions import ma
from app.user.models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field()
    password = ma.String(required=True, load_only=True)
    email = ma.Email(required=True)
    first_seen = ma.auto_field(dump_only=True)
    last_seen = ma.auto_field(dump_only=True)


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
