import logging
import json

from flask import request
from flask_restplus import Resource

from nlp_api.api import api
from nlp_api.api.models import text_model

log = logging.getLogger('api')

ns = api.namespace('topics', description='Topic Classification')


@ns.route('/')
class Topics(Resource):
    @ns.doc('post_topics')
    @ns.expect(text_model)
    def post(self):
        """
        Get topics from text (PLANNED)
        """
        # data = api.payload
        data = request.json
        text = data['text']

        log.debug('text: {}'.format(text))

        topics = ['Still', 'under', 'development']

        log.debug('response body:\n{}'.format(topics))
        return topics, 200, {'Access-Control-Allow-Origin': '*'}
