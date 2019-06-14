"""Module for model methods"""
from werkzeug.security import check_password_hash
from sqlalchemy import or_
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
    def find_by_username_or_email(cls, data):
        """Find user by username or email
        Args:
            data(): user data
        """
        email = data.get('email')
        username = data.get('username')
        if email is not None or username is not None:
            user = cls.query.filter(or_(cls.email == email, cls.username == username)).first()
            return user

    @classmethod
    def verify_password(cls, password_hash, password):
        """Verify if hash password matches plain password"""
        return check_password_hash(password_hash, password)


    @classmethod
    def find_or_create(cls, data, **kwargs):
        """
        Finds a model instance or creates it
        """
        instance = cls.query.filter_by(**kwargs).first()
        if not instance:
            instance = cls(**data).save()
        return instance
