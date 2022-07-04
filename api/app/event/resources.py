from flask_restx import Namespace, Resource

events_ns = Namespace(name="events", description="Events")


@events_ns.route("/")
class Event(Resource):
    def get(self):
        return {}
