"""Base schema module"""

from marshmallow import Schema, fields
from ..utilities.error_handler.handle_error import ValidationError

class BaseSchema(Schema):
    """Base schema for all models"""
    id = fields.String(dump_only=True)
    created_at = fields.String(dump_only=True, dump_to='createdAt')
    updated_at = fields.String(dump_only=True, dump_to='updatedAt')
    created_by = fields.String(dump_only=True, dump_to='createdBy')
    updated_by = fields.String(dump_only=True, dump_to='updatedBy')

    def load_object_into_schema(self, data, partial=False):
        """Helper function to load python objects into schema"""
        data, errors = self.load(data, partial=partial)

        if errors:
            raise ValidationError(
                dict(errors=errors, message='An error occurred'), 400)

        return data
