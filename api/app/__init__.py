from typing import Type

from flask import Flask

from app.extensions import db, ma, migrate, api_spec
from config import Config

from app import event, token, user


def create_app(config: Type[Config]) -> Flask:
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
    _register_apispec()

    return app


def _register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    api_spec.init_app(app)


def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(event.resources.blueprint)
    app.register_blueprint(user.resources.blueprint)


def _register_apispec() -> None:
    api_spec.register(user.resources.create_user, blueprint=user.resources.blueprint.name)
    api_spec.register(event.resources.get_event, blueprint=event.resources.blueprint.name)
