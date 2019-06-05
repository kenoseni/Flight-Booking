"""Module to test unique Id generator"""
from src.helpers import unique_uuid_generator
from src.models import User
from tests.mocks.user import VALID_USER

class TestUniqueIdGenerator:
    """Test unique Id generator"""
    def test_unique_id_generator_succeeds(self):
        """should pass when a unique id is generated"""
        user = User(**VALID_USER)
        unique_uuid_generator(user)
        assert isinstance(user.id, str)
