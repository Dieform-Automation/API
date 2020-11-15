from datetime import date
from .. import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ShippedPart(db.Model):
    """ Shipment model for storing Dieform shipment info """
    __tablename__ = "shipped_part"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_id = db.Column(db.Integer, ForeignKey('part.id'))
    shipment_id = db.Column(db.Integer, ForeignKey('shipment.id'))
    quantity = db.Column(db.Integer, nullable=False)
    bins = db.Column(db.Integer, nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Part number: '{}'>".format(self.id)