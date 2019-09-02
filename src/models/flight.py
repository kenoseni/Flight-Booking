from src import db
from datetime import datetime
from .base import BaseModel
from ..utilities.enums import FlightStatusEnum


class Flight(BaseModel):
    """Create flight table"""
    __tablename__ = 'flights'

    flight = db.Column(db.String(60), nullable=False)
    check_in = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    departure = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    airplane_id = db.Column(
        db.String(60), db.ForeignKey('airplanes.id'), nullable=False)
    destination = db.Column(db.String(60), nullable=False)
    status = db.Column(
        db.Enum(FlightStatusEnum),
        nullable=False,
        server_default=FlightStatusEnum.scheduled.value)

    airplanes = db.relationship('Airplane', backref=db.backref(
        'flights', cascade='all, delete', lazy='dynamic'))

    @property
    def airplane(self):
        """Property method to return airplane details

        Returns:
            airplane (obj): The airplane details of the flight
        """
        from . import Airplane
        airplane = Airplane.get_or_404_(self.airplane_id)
        return airplane

    def __repr__(self):
        return f'<Flight: {self.flight}>'
