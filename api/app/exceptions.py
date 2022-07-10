from http import HTTPStatus

from flask import Blueprint
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

from app.types import EndpointResponse

exceptions = Blueprint("exceptions", __name__)


@exceptions.app_errorhandler(HTTPException)
def http_error_as_json(error: HTTPException) -> EndpointResponse:
    return {
               'code': error.code,
               'message': error.name,
               'description': error.description,
           }, error.code


@exceptions.app_errorhandler(IntegrityError)
def sqlalchemy_integrity_error(error: IntegrityError) -> EndpointResponse:
    return {
               "code": HTTPStatus.BAD_REQUEST.value,
               "message": 'Database integrity error',
               "description": str(error.orig),
           }, HTTPStatus.BAD_REQUEST.value
