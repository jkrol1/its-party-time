from flask import Blueprint
from sqlalchemy.exc import IntegrityError

from app.types import EndpointResponse

exceptions = Blueprint("exceptions", __name__)


class InvalidCredentialsError(Exception):
    pass


@exceptions.app_errorhandler(InvalidCredentialsError)
def invalid_credentials_error(error: InvalidCredentialsError) -> EndpointResponse:
    return {
               "code": 401,
               "message": "Invalid email or password",
               "description": str(error),
           }, 401


@exceptions.app_errorhandler(IntegrityError)
def sqlalchemy_integrity_error(error: IntegrityError) -> EndpointResponse:
    return {
               "code": 400,
               "message": 'Database integrity error',
               "description": str(error.orig),
           }, 400
