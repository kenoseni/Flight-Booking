"""Authorization fixtures module"""
import pytest
from src.utilities.constants import MIMETYPE, MIMETYPE_TEXT

@pytest.fixture(scope='module')
def auth_header():
    """Fixture that creates authorization header"""
    return {
        'Content-Type': MIMETYPE,
        'Accept': MIMETYPE
    }

@pytest.fixture(scope='module')
def auth_header_text():
    """Fixture that creates authorization header"""
    return {
        'Content-Type': MIMETYPE_TEXT,
        'Accept': MIMETYPE_TEXT
    }
