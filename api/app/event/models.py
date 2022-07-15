from enum import Enum

from app.extensions import db

event_participants = db.Table(
    "event_participants",
    db.Model.metadata,
    db.Column("id", db.Integer, primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("event_roles.id")),
)


class EventPermission(Enum):
    CONTRIBUTE = 1
    MODERATE = 2
    DELETE_EVENT = 4


class EventRole:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer, default=0)
    event_participant_id = db.Column(db.Integer, db.ForeignKey("event_participants.id"), index=True)

    def add_permission(self, permission: int) -> None:
        if not self.has_permission(permission):
            self.permissions += permission

    def remove_permission(self, permission: int) -> None:
        if self.has_permission(permission):
            self.permissions -= permission

    def reset_permissions(self: int) -> None:
        self.permissions = 0

    def has_permission(self, permission: int) -> bool:
        return self.permissions & permission == permission

    @staticmethod
    def insert_roles():
        pass


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
    organizer = db.relationship("User")
