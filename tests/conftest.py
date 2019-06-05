"""Module for setting up fixtures for testing"""
from os import environ
import pytest
from main import create_app
from config import app_config
from src import db

environ['FLASK_ENV'] = 'testing'

pytest_plugins = [
    "tests.fixtures"
]

@pytest.yield_fixture(scope='session')
def app():
    """Setup our flask test app.
    Return: Flask app
    """

    _app = create_app(app_config)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture(scope='module')
def init_db(app):
    """Initialize database"""
    db.drop_all()
    db.create_all()
    yield db
    # clean database at end of test
    db.session.close()
    db.drop_all()
