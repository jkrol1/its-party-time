from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    first_seen = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError("password attribute is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
