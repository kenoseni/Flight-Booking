"""Module to test add function"""
import pytest
from app.add import add

class TestAddFunction:
    """Test add function"""

    def test_add_function_succeeds(self):
        """Test add function succeeds"""
        result = add(50, 100, 200)
        assert type(result) is int
        assert result == 350
