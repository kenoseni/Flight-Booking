"""Module to create a user table"""
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import expression
from src import db
from .base import BaseModel

class User(BaseModel):
    """Create a User table"""
    __tablename__ = 'users'

    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    image_url = db.Column(JSON)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'
