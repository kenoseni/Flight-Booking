"""Base model module"""
from datetime import datetime
from src import db
from src.model_methods import ModelMethods


class BaseModel(db.Model, ModelMethods):
    """Base model for all models"""

    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created_by = db.Column(db.String, nullable=True)
    updated_by = db.Column(db.String, nullable=True)
