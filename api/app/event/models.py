from app.extensions import db

event_participants = db.Table(
    "event_participants",
    db.Model.metadata,
    db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
)


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(124), nullable=False)
    description = db.Column(db.Text)
    participants = db.relationship("User", secondary=event_participants)
    address = db.Column(db.String(124), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    playlist_link = db.Column(db.Text)
    organizer_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)
    organizer = db.relationship("User", lazy="select")
