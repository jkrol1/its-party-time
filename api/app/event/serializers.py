from app.extensions import ma
from app.event.models import Event


class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event


event_schema = EventSchema()
