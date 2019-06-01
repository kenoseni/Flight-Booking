"""App Blueprint"""
from flask import Blueprint
from flask_restplus import Api


api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_blueprint, doc='/docs')
