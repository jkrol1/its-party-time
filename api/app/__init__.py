from flask import Flask

from app.extensions import db, ma, migrate
from app.models import User
from app.resources import blueprint as api
from config import Config


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

    return app


def _register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(api, url_prefix="/api/v1")
