from flask_restx import Namespace, Resource

from app.user.serializers import UserSchema

users_ns = Namespace(name="users", description="Users")


@users_ns.route("/")
class User(Resource):
    def post(self):
        return {}
