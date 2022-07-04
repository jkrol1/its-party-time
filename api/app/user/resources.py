from typing import Tuple

from flask import jsonify, request, Response
from flask_restx import fields, Namespace, Resource

from app.extensions import db
from app.user.serializers import user_schema

users_ns = Namespace(name="users", description="Users")
user_model_doc = users_ns.model("User", {
    "username": fields.String,
    "password": fields.String,
    "email": fields.String
})


@users_ns.route("/")
class User(Resource):
    @users_ns.expect(user_model_doc)
    def post(self) -> Tuple[Response, int]:
        user = user_schema.load(request.get_json())
        db.session.add(user)
        db.session.commit()
        return jsonify(user_id=user.id), 201
