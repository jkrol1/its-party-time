from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.resources import blueprint as api

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api, url_prefix="/api/v1")

    return app
