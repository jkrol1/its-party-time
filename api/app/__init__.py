from flask import Flask

from app.api_blueprint import api_blueprint
from app.extensions import db, ma, migrate, api
from config import Config

from app.event import events_ns
from app.user import User, users_ns


def create_app(config: Config = Config) -> Flask:
    """
    Application factory

    :param Config config: App config
    :rtype: Flask
    :return: Flask app instance
    """

    app = Flask(__name__)
    app.config.from_object(config)
    _register_extensions(app)
    _register_blueprints(app)
    _register_api_namespaces()

    return app


def _register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(api_blueprint)


def _register_api_namespaces():
    api.add_namespace(events_ns)
    api.add_namespace(users_ns)
