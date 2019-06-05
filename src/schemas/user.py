"""User schema module"""

from marshmallow import fields
from .base import BaseSchema

class UserSchema(BaseSchema):
    """User schema"""
    first_name = fields.String(load_from='firstName', dump_to='firstName')
    last_name = fields.String(load_from='lastName', dump_to='lastName')
    username = fields.String()
    email = fields.String()
    password = fields.String()
    image_url = fields.String(load_from='imageUrl', dump_to='imageUrl')
    is_admin = fields.Boolean(dump_to="isAdmin", dump_only=True)
