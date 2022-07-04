from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from app.api_blueprint import api_blueprint

basic_auth = HTTPBasicAuth()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
api = Api(api_blueprint,
          title="It's A Party Time API",
          version="1.0",
          description="It's A Party Time API")
