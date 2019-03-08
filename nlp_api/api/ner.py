import logging
import json
import spacy
import en_core_web_sm

from flask import request
from flask_restplus import Resource, fields

from nlp_api.api import api

log = logging.getLogger(__name__)

ns = api.namespace('ner', description='Named Entity Recognition')

# nlp = spacy.load('en')
nlp = en_core_web_sm.load()

text_model = api.model("text model", {
    "text": fields.String("Input text")
})

@ns.route('/')
class Ner(Resource):
    @api.expect(text_model)
    def post(self):
        """
        Get named entities
        """
        # data = api.payload
        data = request.json
        text = data['text']

        log.debug('text: {}'.format(text))

        entities = []
        if text:
            for ent in nlp(text).ents:
                entities.append({
                    'text': ent.text,
                    'label': ent.label_,
                    'start': ent.start_char,
                    'stop': ent.end_char
                })
                log.debug('found {}'.format(ent.text))

        resp_body = json.dumps(entities)
        return resp_body, 200, {'Access-Control-Allow-Origin': '*'}

@ns.route('/version')
class SpacyVersion(Resource):
    def get(self):
        """
        Get spaCy version. This is the library used for NER.
        """
        resp_body = json.dumps({'spacy': spacy.about.__version__})
        return resp_body, 200, {'Access-Control-Allow-Origin': '*'}