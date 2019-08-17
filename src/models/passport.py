from src import db
from .base import BaseModel
from ..utilities.enums import SexEnum


class Passport(BaseModel):
    """Create a Passport table"""
    __tablename__ = 'passports'

    user_id = user_id = db.Column(
        db.String(60), db.ForeignKey('users.id'), nullable=False)
    passport_type = db.Column(db.String(60), nullable=False)
    nationality = db.Column(db.String(60), nullable=False)
    passport_no = db.Column(db.String(60), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    sex = db.Column(db.Enum(SexEnum), nullable=False)
    date_of_issue = db.Column(db.DateTime, nullable=False)
    date_of_expiry = db.Column(db.DateTime, nullable=False)

    users = db.relationship(
        'User', backref=db.backref(
            'passports', cascade='all, delete', lazy='dynamic'))

    @property
    def user(self):
        """Property method to return passport user

        Returns:
            user (obj): The passport user details
        """
        from . import User
        user = User.get_or_404_(self.user_id)
        return user

    def __repr__(self):
        return f'<Passport: {self.user_id}>'
