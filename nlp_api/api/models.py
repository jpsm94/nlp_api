from flask_restplus import fields
from nlp_api.api import api

text_model = api.model("text model", {
    "text": fields.String("Input text")
})

text_summaries_model = api.model("text summaries model", {
    "text": fields.String("Input text"),
    "num_sentences": fields.Integer("Number of summary sentences")
})
