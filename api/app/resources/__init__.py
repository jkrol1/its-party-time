from flask import Blueprint
from flask_restx import Api

from app.resources.event import ns as ns_events

blueprint = Blueprint("api", __name__)

api = Api(blueprint,
          title="It's A Party Time API",
          version="1.0",
          description="It's A Party Time API")

api.add_namespace(ns_events)
