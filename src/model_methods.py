"""Module for model methods"""
from werkzeug.security import check_password_hash
from sqlalchemy import or_
from src.database import db
from src.utilities.error_handler.request_error import request_error_message
from src.utilities.messages.error_messages import request_errors


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
            user = cls.query.filter(or_(
                cls.email == email, cls.username == username)).first()
            return user

    @classmethod
    def get_or_404_(cls, id):
        """Finds a model instance with an id
        Args:
            id(str): resource id
        """
        instance = cls.query.filter_by(id=id).first()
        if not instance:
            request_error_message(
                'error', request_errors['not_found'].format(cls.__name__), 404)
        return instance

    @classmethod
    def verify_password(cls, password_hash, password):
        """Verify if hash password matches plain password"""
        return check_password_hash(password_hash, password)
