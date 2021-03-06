from typing import Type

from flask import Flask

from app.extensions import db, ma, migrate, api_spec, jwt
from config import Config

from app import token, user, event
from app.auth_callbacks import user_identity_loader_callback, user_lookup_callback, check_if_token_revoked_callback
from app.exceptions import exceptions


def create_app(config: Type[Config]) -> Flask:
    """
    Application factory

    :param Config config: App config
    :rtype: Flask
    :return: Flask app instance
    """

    app = Flask(__name__)
    app.config.from_object(config)

    _register_blueprints(app)
    _register_extensions(app)
    _register_shell_context(app)
    _register_callbacks()
    _register_apispec()

    return app


def _register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    api_spec.init_app(app)
    jwt.init_app(app)


def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(event.resources.blueprint)
    app.register_blueprint(user.resources.blueprint)
    app.register_blueprint(token.resources.blueprint)
    app.register_blueprint(exceptions)


def _register_callbacks() -> None:
    jwt.user_lookup_loader(user_lookup_callback)
    jwt.user_identity_loader(user_identity_loader_callback)
    jwt.token_in_blocklist_loader(check_if_token_revoked_callback)


def _register_apispec() -> None:
    api_spec.register(user.resources.register_user, blueprint=user.resources.blueprint.name)
    api_spec.register(event.resources.create_event, blueprint=event.resources.blueprint.name)
    api_spec.register(token.resources.create_tokens, blueprint=token.resources.blueprint.name)


def _register_shell_context(app):
    def shell_context():
        return {
            "db": db,
            "User": user.models.User,
            "Token": token.models.Token,
            "Event": event.models.Event,
            "EventRole": event.models.EventRole,
            "event_participants": event.models.event_participants
        }

    app.shell_context_processor(shell_context)
