"""Module to create a user table"""
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.event import listens_for
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
from .base import BaseModel


class User(BaseModel):
    """Create a User table"""
    __tablename__ = 'users'

    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    image_url = db.Column(JSON)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'


@listens_for(User, 'before_insert')
def password_hash(mapper, connection, target):
    """Hash all passwords"""
    target.password = generate_password_hash(
        target.password, method='pbkdf2:sha256', salt_length=20)
