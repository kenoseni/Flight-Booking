"""Base schema module"""

from marshmallow import Schema, fields

class BaseSchema(Schema):
    """Base schema for all models"""
    id = fields.String(dump_only=True)
    created_at = fields.String(dump_only=True, dump_to='createdAt')
    updated_at = fields.String(dump_only=True, dump_to='updatedAt')
    created_by = fields.String(dump_only=True, dump_to='createdBy')
    updated_by = fields.String(dump_only=True, dump_to='updatedBy')
