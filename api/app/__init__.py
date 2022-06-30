from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    @app.get("/")
    def main():
        return "<h1> Hello </h1>"

    return app
