from app.extensions import ma
from app.user.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    # password = ma.auto_field(load_only=True)
    email = ma.Email()
