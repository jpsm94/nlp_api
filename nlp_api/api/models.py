from flask_restplus import fields
from nlp_api.api import api

text_model = api.model("text model", {
    "text": fields.String("Input text")
})