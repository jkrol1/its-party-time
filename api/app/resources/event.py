from flask_restx import Namespace, Resource

ns = Namespace(name="events", description="Events")


@ns.route("/")
class Event(Resource):
    def get(self):
        return {}
