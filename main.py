"""Creates a Flask app instance"""

from flask import Flask
from flask_migrate import Migrate
from app import api_blueprint
from app.database import db
from config import config, app_config

def create_app(app_config):
    """creates the flask application"""
    
    app = Flask(__name__)
    app.config.from_object(app_config)

    app.register_blueprint(api_blueprint)
    
    # initialize db by binding app
    db.init_app(app)
    
    # initialize migration scripts
    migrate = Migrate(app, db)

    return app
