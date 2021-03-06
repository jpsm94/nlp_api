import logging
import json

from flask import request
from flask_restplus import Resource

from nlp_api.api import api
from nlp_api.api.models import text_summaries_model

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.text_rank import TextRankSummarizer

log = logging.getLogger('api')

ns = api.namespace('summaries', description='Extractive Text Summarization')

# defaults
LANGUAGE = 'english'
DEFAULT_NUM_SENTENCES = 3


@ns.route('/')
class Summaries(Resource):
    @ns.doc('post_summaries')
    @ns.expect(text_summaries_model)
    def post(self):
        """
        Extract summary (key sentences) from text
        """
        # data = api.payload
        data = request.json
        text = data['text']
        num_sentences = data['num_sentences']
        num_sentences = num_sentences if isinstance(num_sentences, int) else DEFAULT_NUM_SENTENCES
        log.debug('num_sentences={}'.format(num_sentences))

        # log.debug('text: {}'.format(text))

        # TODO: check for minimum number of sentences in text?

        summary_sentences = []
        if text:
            parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))

            stemmer = Stemmer(LANGUAGE)
            summarizer = TextRankSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary = summarizer(parser.document, num_sentences)
            # summary_text = ' '.join([sentence._text for sentence in summary])
            summary_sentences = [sentence._text for sentence in summary]

        log.debug('response body:\n{}'.format(summary_sentences))
        return summary_sentences, 200, {'Access-Control-Allow-Origin': '*'}
