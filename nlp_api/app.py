import os
import logging.config

from flask import Flask, Blueprint

from nlp_api import settings
from nlp_api.api import api
from nlp_api.api.entities import ns as entities_namespace
from nlp_api.api.topics import ns as topics_namespace
from nlp_api.api.summaries import ns as summaries_namespace

app = Flask(__name__)

logging.config.fileConfig('logging.conf')
log = logging.getLogger('api')


def config_app(flask_app):
    flask_app.config['SERVER_HOST'] = settings.FLASK_SERVER_HOST
    flask_app.config['SERVER_PORT'] = int(os.environ.get('PORT', settings.FLASK_SERVER_PORT))
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def init_app(flask_app):
    log.info('Initialising app...')
    config_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    # add namespaces that define routes
    api.add_namespace(entities_namespace)
    api.add_namespace(topics_namespace)
    api.add_namespace(summaries_namespace)
    flask_app.register_blueprint(blueprint)
    log.info('Initialisation done')


# initialization
init_app(app)

if __name__ == "__main__":
    server_port = int(os.environ.get('PORT', settings.FLASK_SERVER_PORT))
    log.info('Server started at http://%s:%d/api/', settings.FLASK_SERVER_HOST, server_port)
    app.run(host=settings.FLASK_SERVER_HOST, port=server_port, debug=settings.FLASK_DEBUG)
