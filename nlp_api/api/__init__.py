import logging
import traceback

from flask_restplus import Api
from flask_restplus import reqparse
from nlp_api import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='NLP Demo API',
          description='Experiments using open source NLP libraries')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
