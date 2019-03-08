import logging

from flask import request
from flask_restplus import Resource, Resource, fields

from nlp_api.api import api

log = logging.getLogger(__name__)

ns = api.namespace('conferences', description='Sample Conference API')

@ns.route('/')
class ConferenceList(Resource):
    def get(self):
        """
        returns a list of conferences
        """
    def post(self):
        """
        Adds a new conference to the list
        """
		
@ns.route("/<int:id>")
@ns.param('id', 'The id identifier')
@ns.response(404, 'id not found')
class Conference(Resource):
    def get(self, id):
        """
        Displays a conference's details
        """
    def put(self, id):
        """
        Edits a selected conference
        """		