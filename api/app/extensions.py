from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_apispec import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy

basic_auth = HTTPBasicAuth()
db = SQLAlchemy()
api_spec = FlaskApiSpec()
ma = Marshmallow()
migrate = Migrate()
