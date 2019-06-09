"""Module to handle app errors"""

class ValidationError(Exception):
    """Base class for handling errors"""
    status_code = 400

    def __init__(self, payload=None, status_code=None):
        """Initialize error handler"""
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Return payload as dict"""
        return self.payload
