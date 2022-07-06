from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_apispec import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api_spec = FlaskApiSpec()
ma = Marshmallow()
migrate = Migrate()
