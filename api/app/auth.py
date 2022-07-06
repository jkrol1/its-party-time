from flask_httpauth import HTTPBasicAuth
from werkzeug.exceptions import Unauthorized, Forbidden

from extensions import db
from app.user import User

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(username, password):
    if username and password:
        user = db.session.scalar(User.select().filter_by(username=username))
        if user and user.verify_password(password):
            return user


@basic_auth.error_handler
def basic_auth_error(status=401):
    error = (Forbidden if status == 403 else Unauthorized)()
    return {
               'code': error.code,
               'message': error.name,
               'description': error.description,
           }, error.code, {'WWW-Authenticate': 'Form'}
