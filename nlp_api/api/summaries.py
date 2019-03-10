import logging
import json

from flask import request
from flask_restplus import Resource, fields

from nlp_api.api import api
from nlp_api.api.models import text_model

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.text_rank import TextRankSummarizer

log = logging.getLogger('api')

ns = api.namespace('summaries', description='Extractive Text Summarization')

LANGUAGE = 'english'
DEFAULT_NUM_SENTENCES = 4


@ns.route('/')
class Summaries(Resource):
    @ns.doc('pass_text')
    @ns.expect(text_model)
    def post(self):
        """
        Extract summary from text
        """
        # data = api.payload
        data = request.json
        text = data['text']

        # number of sentences param
        num_sentences = request.args.get("sentences")
        num_sentences = num_sentences if isinstance(num_sentences, int) else DEFAULT_NUM_SENTENCES

        # log.debug('text: {}'.format(text))

        # TODO: check for minimum number of sentences

        summary_sentences = []
        if text:
            parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))

            stemmer = Stemmer(LANGUAGE)
            summarizer = TextRankSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary = summarizer(parser.document, num_sentences)
            # summary_text = ' '.join([sentence._text for sentence in summary])
            summary_sentences = [sentence._text for sentence in summary]

        resp_body = json.dumps(summary_sentences)
        return resp_body, 200, {'Access-Control-Allow-Origin': '*'}
