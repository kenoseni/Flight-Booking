from src import db
from .base import BaseModel


class Airplane(BaseModel):
    """Create airplane table"""
    __tablename__ = 'airplanes'

    model = db.Column(db.String(60), nullable=False)
    type = db.Column(db.String(60), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Airplane: {self.type}>'
