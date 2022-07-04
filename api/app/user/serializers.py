from app.extensions import ma
from app.user.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    password = ma.String(required=True, load_only=True)
    email = ma.Email(required=True)


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
