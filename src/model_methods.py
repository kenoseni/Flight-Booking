"""Module for model methods"""
from src import db

class ModelMethods:
    """Defines the methods for all models"""

    def save(self):
        """Persist data into the database
        Returns:
            instance(obj): model instance
        """
        db.session.add(self)
        db.session.commit
        return self

