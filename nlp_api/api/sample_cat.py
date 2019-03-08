import logging

from flask import request
from flask_restplus import Resource, Resource, fields

from nlp_api.api import api

log = logging.getLogger(__name__)

ns = api.namespace('cats', description='Sample Cat APIs')

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'fel', 'name': 'Felix'},
    {'id': 'gar', 'name': 'Garfield'},
    {'id': 'pus', 'name': 'Puss in Boots'},
]

@ns.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        """List all cats"""
        return CATS

@ns.route('/<id>')
@ns.param('id', 'The cat identifier')
@ns.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        """Fetch a cat given its identifier"""
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)