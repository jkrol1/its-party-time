from __future__ import annotations
from typing import List

from app.extensions import db
from app.event.roles import EventPermission, Role

event_participants = db.Table(
    "event_participants",
    db.Model.metadata,
    db.Column("id", db.Integer, primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("event_roles.id")),
)


class EventRole(db.Model):
    __tablename__ = "event_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Enum(Role), unique=True)
    permissions = db.Column(db.Integer, default=0)
    default = db.Column(db.Boolean, default=False, index=True)

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
    def create_roles() -> None:
        for role_to_create in Role:
            created_role = EventRole._create_role(role_to_create)
            db.session.add(created_role)
        db.session.commit()

    @staticmethod
    def _create_role(role_to_create: Role) -> EventRole:
        role = EventRole.query.filter_by(name=role_to_create).first()
        if not role:
            role = EventRole(name=role_to_create)
        role.reset_permissions()
        if role.name == Role.USER:
            role.default = True
        EventRole._add_permissions_to_role(role_to_create.value, role)
        return role

    @staticmethod
    def _add_permissions_to_role(permissions: List[EventPermission], role: EventRole) -> None:
        for permission in permissions:
            role.add_permission(permission)


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
