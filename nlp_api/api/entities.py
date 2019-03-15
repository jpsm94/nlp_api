import logging
import spacy
import en_core_web_sm

from flask import request
from flask_restplus import Resource

from nlp_api.api import api
from nlp_api.api.models import text_model

log = logging.getLogger('api')

ns = api.namespace('entities', description='Named Entity Recognition')

# English model from spacy
# nlp = spacy.load('en')
nlp = en_core_web_sm.load()


@ns.route('/')
class Entities(Resource):
    @ns.doc('post_entities')
    @ns.expect(text_model)
    def post(self):
        """
        Get named entities from text
        """
        # data = api.payload
        data = request.json
        text = data['text']

        # log.debug('text: {}'.format(text))

        # TODO: select top N entities needed?

        entities = []
        if text:
            for ent in nlp(text).ents:
                entities.append({
                    'text': ent.text,
                    'label': ent.label_,
                    'start': ent.start_char,
                    'stop': ent.end_char
                })
                log.debug('found entity: {}'.format(ent.text))

        log.debug('response body:\n{}'.format(entities))
        return entities, 200, {'Access-Control-Allow-Origin': '*'}


@ns.route('/version')
class SpacyVersion(Resource):
    @ns.doc('get_spacy_version')
    def get(self):
        """
        Get spaCy version (library used for Named Entity Recognition)
        """
        version = {'spacy': spacy.about.__version__}
        return version, 200, {'Access-Control-Allow-Origin': '*'}