"""Creates a Flask app instance"""

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from src import api_blueprint, errors, api
from src import db
from config import config, app_config
from src.utilities.error_handler.handle_error import ValidationError

def _initialize_errorhandlers(application):
    """Error handler initialization"""
    application.register_blueprint(api_blueprint) 
    application.register_blueprint(errors)  

def create_app(app_config):
    """creates the flask application""" 
    app = Flask(__name__)
    app.config.from_object(app_config)

    # initialize flask-jwt
    jwt = JWTManager(app)

    _initialize_errorhandlers(app)

    # initialize db by binding app
    db.init_app(app)

    import src.models
    import src.views
    # initialize migration scripts
    migrate = Migrate(app, db)

    return app, jwt

@api.errorhandler(ValidationError)
@errors.app_errorhandler(ValidationError)
def error_handler(error):
    """Called when Exception is raised"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
