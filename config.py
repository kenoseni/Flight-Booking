"""Application configuration module"""
import sys
from os import getenv
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

class Config:
    """Base configuration"""
    #  FLASK_ENV configuration
    FLASK_ENV = getenv('FLASK_ENV', 'development')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI', '')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    API_BASE_URL_V1 = getenv('API_BASE_URL_V1')


class ProductionConfig(Config):
    """Production configuration"""
    pass


class StagingingConfig(Config):
    """Staging configuration"""
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    FLASK_ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = getenv(
        'TEST_DATABASE_URI', default='postgresql://localhost/flights_test')

config = {
    'production': ProductionConfig,
    'staging': StagingingConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}

app_config = TestingConfig if 'pytest' in sys.modules else config.get(
    Config.FLASK_ENV, 'development')
