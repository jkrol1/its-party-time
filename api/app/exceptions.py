from flask import Blueprint
from sqlalchemy.exc import IntegrityError

exceptions = Blueprint("exceptions", __name__)


@exceptions.app_errorhandler(IntegrityError)
def sqlalchemy_integrity_error(error):
    return {
               'code': 400,
               'message': 'Database integrity error',
               'description': str(error.orig),
           }, 400
