from typing import Dict

from flask import Blueprint
from flask_jwt_extended import jwt_required, current_user

blueprint = Blueprint("event", __name__, url_prefix="/api/v1/events")


@blueprint.get("/")
@jwt_required()
def get_event() -> Dict[str, int]:
    user = current_user
    return {"userID": user.id}
