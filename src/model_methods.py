"""Module for model methods"""
from src.database import db

class ModelMethods():
    """Defines the methods for all models"""

    def save(self):
        """Persist data into the database
        Returns:
            instance(obj): model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_or_create(cls, data, **kwargs):
        """
        Finds a model instance or creates it
        """
        instance = cls.query.filter_by(**kwargs).first()
        if not instance:
            instance = cls(**data).save()
        return instance
