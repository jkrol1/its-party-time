from flask import Blueprint

blueprint = Blueprint("event", __name__, url_prefix="/api/v1/events")


@blueprint.get("/")
def get_event(*args, **kwargs):
    return {}
