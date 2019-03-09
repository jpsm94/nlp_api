import logging
import json

from flask import request
from flask_restplus import Resource, fields

from nlp_api.api import api
from nlp_api.api.models import text_model

log = logging.getLogger(__name__)

ns = api.namespace('topics', description='Topic Classification')


@ns.route('/')
class Topics(Resource):
    @ns.doc('pass_text')
    @ns.expect(text_model)
    def post(self):
        """
        Get topics from text (IN PROGRESS)
        """
        # data = api.payload
        data = request.json
        text = data['text']

        log.debug('text: {}'.format(text))

        topics = ['Still', 'under', 'development']

        resp_body = json.dumps(topics)
        return resp_body, 200, {'Access-Control-Allow-Origin': '*'}
